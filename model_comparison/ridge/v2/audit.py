"""Exclusive artifacts, durable events, snapshot verification and process locking."""
from contextlib import contextmanager
from datetime import datetime, timezone
from importlib import metadata
import csv
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback
from uuid import uuid4

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPERIMENTS = HERE / 'experiments'
EXTRA_ID = 'fv-v2-extra-20261031-r2'
EXTRA_SHA = 'b23ca4844be2ad3167c2001dd69de276b7f9300aa81c5fc51f78c4d37c7b6acc'
BASE_SHA = '3297209f59afbe96faa1e93d22f267fcc653d107cf42082f10018dee4eb81aa0'


def now():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def sha(path):
    with Path(path).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def object_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False, separators=(',', ':')).encode('utf-8')).hexdigest()


def exclusive_json(path, value):
    with Path(path).open('x', encoding='utf-8', newline='\n') as f:
        json.dump(value, f, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())


def append(path, text):
    with Path(path).open('a', encoding='utf-8', newline='\n') as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode('utf-8').strip()


def environment():
    return {'python': sys.version, 'executable': sys.executable, 'os': platform.platform(),
            'processor': platform.processor(), 'cpu_count': os.cpu_count(),
            'libraries': {d.metadata['Name']: d.version for d in metadata.distributions()},
            'thread_env': {k: os.environ.get(k) for k in
                           ('TZ', 'OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'PYTHONHASHSEED')}}


def peak_memory_mb():
    """Measured process peak; unknown is null, never a synthetic zero."""
    if sys.platform != 'win32':
        try:
            import resource
            peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            return peak/(1024*1024 if sys.platform=='darwin' else 1024)
        except (ImportError,OSError):
            return None
    try:
        import ctypes
        from ctypes import wintypes
        class Counters(ctypes.Structure):
            _fields_=[('cb',wintypes.DWORD),('PageFaultCount',wintypes.DWORD)]+[
                (name,ctypes.c_size_t) for name in ('PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage',
                'QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage')]
        kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        psapi=ctypes.WinDLL('psapi',use_last_error=True)
        kernel.GetCurrentProcess.restype=wintypes.HANDLE
        psapi.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.POINTER(Counters),wintypes.DWORD]
        psapi.GetProcessMemoryInfo.restype=wintypes.BOOL
        counters=Counters(); counters.cb=ctypes.sizeof(counters)
        if not psapi.GetProcessMemoryInfo(kernel.GetCurrentProcess(),ctypes.byref(counters),counters.cb):
            return None
        return counters.PeakWorkingSetSize/1024/1024 or None
    except (OSError,AttributeError):
        return None


@contextmanager
def lock(root):
    """One writer for aggregate documents; OS releases lock on kill/crash."""
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    with (root / 'execution.lock').open('a+b') as f:
        if f.tell() == 0:
            f.write(b'0')
            f.flush()
        f.seek(0)
        try:
            if sys.platform == 'win32':
                import msvcrt
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as e:
            raise RuntimeError('Another Ridge v2 process holds the audit lock') from e
        try:
            yield
        finally:
            f.seek(0)
            if sys.platform == 'win32':
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(f, fcntl.LOCK_UN)


class Attempt:
    """Allocate before argparse, config parsing, imports or snapshot validation."""
    def __init__(self, root=EXPERIMENTS, command=None):
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        self.folder = root / ('ridge-v2-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ-') + uuid4().hex)
        self.folder.mkdir(exist_ok=False)
        self.started, self.cpu = time.perf_counter(), time.process_time()
        self.context = {}
        self.event('STARTED', command=command or [], pid=os.getpid())
        exclusive_json(self.folder / 'invocation.json', {'at': now(), 'argv': command or [],
                       'command': subprocess.list2cmdline([sys.executable, '-m', 'model_comparison.ridge.v2.run', *(command or [])]),
                       'cwd': str(Path.cwd()), 'pid': os.getpid()})
        # Even argparse/config/import failures retain Python, OS and installed versions.
        info=environment()
        try:
            info.update(git_sha=git('rev-parse','HEAD'),branch=git('branch','--show-current'),
                        worktree=git('status','--porcelain=v1','--untracked-files=all'))
        except (OSError,subprocess.CalledProcessError) as e:
            info['git_capture_error']=str(e)
        exclusive_json(self.folder/'bootstrap.json',info)

    def event(self, event, **fields):
        record = {'at': now(), 'run_id': self.folder.name, **self.context, 'event': event, **fields}
        append(self.folder / 'events.jsonl', json.dumps(record, ensure_ascii=False, allow_nan=False) + '\n')
        append(self.folder / 'run.log', json.dumps(record, ensure_ascii=False, allow_nan=False) + '\n')

    def capture(self):
        info = environment()
        info.update(git_sha=git('rev-parse', 'HEAD'), branch=git('branch', '--show-current'),
                    worktree=git('status', '--porcelain=v1', '--untracked-files=all'))
        exclusive_json(self.folder / 'environment.json', info)
        with (self.folder / 'environment.txt').open('x', encoding='utf-8') as f:
            f.write(json.dumps(info, ensure_ascii=False, indent=2) + '\n')
        # Archive only implementation/config/evaluation sources, never secrets/data.
        paths = list(HERE.glob('*.py')) + list(HERE.glob('*.json')) + list((HERE/'configs').glob('*.json'))
        paths += list((ROOT/'model_comparison/v2').glob('*.py')) + list((ROOT/'tools').glob('*.py'))
        paths += [ROOT/'pyproject.toml', ROOT/'uv.lock']
        hashes = {}
        for p in sorted(paths):
            rel = p.relative_to(ROOT)
            dst = self.folder / 'sources' / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            with dst.open('xb') as f:
                f.write(p.read_bytes())
            hashes[rel.as_posix()] = sha(dst)
        exclusive_json(self.folder / 'sources_sha256.json', hashes)

    def error(self, error, stage):
        self.event('ERROR', stage=stage, error_type=type(error).__name__, message=str(error),
                   traceback=''.join(traceback.format_exception(error)), retry=False)

    def finish(self, status, **fields):
        if (self.folder/'outcome.json').exists() or (self.folder/'artifacts_sha256.json').exists():
            raise FileExistsError('Terminal record already exists; refusing to mutate/reseal run')
        peak = peak_memory_mb()
        resources = {'wall_seconds': time.perf_counter()-self.started,
                     'cpu_seconds': time.process_time()-self.cpu, 'peak_process_memory_mb': peak}
        self.event(status, resources=resources, **fields)
        exclusive_json(self.folder / 'outcome.json', {'status': status, 'at': now(), 'run_id': self.folder.name,
                                                     'resources': resources, **fields})
        hashes = {p.relative_to(self.folder).as_posix(): sha(p) for p in self.folder.rglob('*')
                  if p.is_file() and p.name != 'artifacts_sha256.json'}
        exclusive_json(self.folder / 'artifacts_sha256.json', hashes)


def verify_seal(folder):
    folder = Path(folder)
    hashes = read(folder/'artifacts_sha256.json')
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()
              and p.name != 'artifacts_sha256.json'}
    if set(hashes) != actual or any(sha(folder/n) != h for n,h in hashes.items()):
        raise ValueError('Artifact seal mismatch')
    return hashes


def effective_outcome(folder):
    """A terminal claim is authoritative only after sealing and recovery checks."""
    folder = Path(folder)
    original = read(folder/'outcome.json') if (folder/'outcome.json').exists() else None
    if not (folder/'artifacts_sha256.json').exists():
        return {'status': 'INCOMPLETE', 'recorded_outcome': original}
    verify_seal(folder)
    if (folder/'recovery.json').exists():
        return {'status': 'ABANDONED', 'recorded_outcome': original,
                'recovery': read(folder/'recovery.json')}
    return original or {'status': 'INCOMPLETE', 'recorded_outcome': None}


def recover_incomplete(root):
    """Call only under the global writer lock, before allocating this invocation."""
    for folder in Path(root).glob('ridge-v2-*'):
        if folder.is_dir() and (folder/'invocation.json').exists() and not (folder/'artifacts_sha256.json').exists():
            original = read(folder/'outcome.json') if (folder/'outcome.json').exists() else None
            record = {'at': now(), 'event': 'RECOVERED_INCOMPLETE', 'status': 'ABANDONED',
                      'run_id': folder.name, 'recorded_status': original.get('status') if original else None,
                      'reason': 'Previous writer exited before artifact sealing; recorded outcome is uncommitted',
                      'normal_completion': False, 'retry': False}
            # Idempotent even if a second interruption follows recovery.json creation.
            if not (folder/'recovery.json').exists():
                exclusive_json(folder/'recovery.json', record)
                append(folder/'events.jsonl', json.dumps(record)+'\n')
            if not (folder/'outcome.json').exists():
                exclusive_json(folder/'outcome.json', {'status': 'ABANDONED', **record})
            hashes = {p.relative_to(folder).as_posix(): sha(p) for p in folder.rglob('*') if p.is_file()
                      and p.name != 'artifacts_sha256.json'}
            exclusive_json(folder/'artifacts_sha256.json', hashes)


def verify_manifest(folder, expected_sha):
    folder = Path(folder).resolve()
    if sha(folder/'manifest.json') != expected_sha:
        raise ValueError(f'Manifest SHA-256 mismatch: {folder}')
    manifest = read(folder/'manifest.json')
    if not manifest.get('files'):
        raise ValueError('Manifest has no files')
    for name, info in manifest['files'].items():
        p = (folder/name).resolve()
        if not p.is_relative_to(folder) or p == folder or sha(p) != info['sha256']:
            raise ValueError(f'Snapshot file SHA-256 mismatch: {name}')
        with p.open(encoding='utf-8', newline='') as f:
            count = sum(1 for _ in csv.reader(f))-1
        if count != info['rows']:
            raise ValueError(f'Snapshot row count mismatch: {name}')
    return manifest


def verify_data(base, extra):
    from tools import check_snapshot, standard
    from model_comparison.v2 import snapshot
    v1 = verify_manifest(base, BASE_SHA)
    v2 = verify_manifest(extra, EXTRA_SHA)
    if (v1.get('snapshot_id') != standard.DATA_VERSION or v2.get('extra_id') != EXTRA_ID
            or v2.get('base_manifest_sha256') != BASE_SHA
            or v2.get('base_snapshot_id') != v1['snapshot_id']):
        raise ValueError('Snapshot identity or lineage mismatch')
    errors, _ = check_snapshot.check(Path(base))
    errors += snapshot.check(Path(extra), Path(base))
    if errors:
        raise ValueError(f'Snapshot verification failed: {errors}')
    return {'v1': {'id': v1['snapshot_id'], 'manifest_sha256': BASE_SHA, 'manifest': v1},
            'v2': {'id': v2['extra_id'], 'manifest_sha256': EXTRA_SHA, 'manifest': v2}}
