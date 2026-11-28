#!/usr/bin/env sh
# 공유 DB(Supabase)에 Flyway를 실행한다. 접속 정보는 .env의 SUPABASE_DATABASE_URL에서 읽고 화면에 출력하지 않는다.
# 사용: scripts/flyway_shared.sh info      # 적용 상태 확인(기본)
#       scripts/flyway_shared.sh migrate   # 새 V 파일 적용(PR 머지 후 담당자 1명만)
set -e
cd "$(dirname "$0")/.."
eval "$(uv run python - <<'PY'
import os, shlex
from urllib.parse import unquote, urlsplit
from dotenv import load_dotenv
load_dotenv('.env')
url = os.environ.get('SUPABASE_DATABASE_URL')
if not url:
    raise SystemExit('.env에 SUPABASE_DATABASE_URL이 없습니다')
u = urlsplit(url)
print(f"FLYWAY_URL={shlex.quote(f'jdbc:postgresql://{u.hostname}:{u.port or 5432}{u.path}')}")
print(f"FLYWAY_USER={shlex.quote(unquote(u.username))}")
print(f"FLYWAY_PASSWORD={shlex.quote(unquote(u.password))}")
PY
)"
export FLYWAY_URL FLYWAY_USER FLYWAY_PASSWORD
docker run --rm -e FLYWAY_URL -e FLYWAY_USER -e FLYWAY_PASSWORD -v "$PWD/db/migration:/flyway/sql:ro" \
  flyway/flyway:12-alpine -outOfOrder=true "${1:-info}"
