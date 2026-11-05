"""Open API 공통 HTTP. 인증키가 포함된 URL·응답 원문은 예외 메시지에 넣지 않는다."""
import json
import time
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = 'FoodValue-collector/1.0'
TIMEOUT_SECONDS = 20
RETRIES = 3


class CollectorError(Exception):
    """수집 실패. code는 external_collection_run.error_code에 그대로 저장한다."""
    status = 'FAILED'

    def __init__(self, code: str):
        super().__init__(code)
        self.code = code[:120]


class AuthError(CollectorError):
    status = 'AUTH_ERROR'


class NetworkError(CollectorError):
    status = 'NETWORK_ERROR'


def service_key(value: str) -> str:
    # 공공데이터포털은 인코딩/디코딩 키를 모두 발급한다. 인코딩 키를 넣어도 이중 인코딩되지 않게 한다.
    return urllib.parse.unquote(value) if '%' in value else value


def fetch_json(url: str, params: dict, *, timeout: float = TIMEOUT_SECONDS, retries: int = RETRIES, sleep=time.sleep):
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    # 파라미터가 없으면 '?'를 붙이지 않는다. ECOS는 경로형 URL 끝의 '?' 때문에 무자료(INFO-200)를 돌려준다.
    request = urllib.request.Request(f'{url}?{query}' if query else url,
                                     headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    last = 'UNKNOWN'
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read()
            break
        except urllib.error.HTTPError as error:
            if error.code in (401, 403):
                raise AuthError(f'HTTP_{error.code}') from None
            if error.code != 429 and error.code < 500:
                raise CollectorError(f'HTTP_{error.code}') from None
            last = f'HTTP_{error.code}'
        except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
            last = type(error).__name__
        if attempt + 1 < retries:
            sleep(2 ** attempt)
    else:
        raise NetworkError(last)
    return decode(body)


def decode(body: bytes):
    text = body.decode('utf-8', errors='replace').strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # 공공데이터포털은 키 오류를 JSON 요청에도 XML로 응답한다.
        if 'SERVICE_KEY' in text or 'returnAuthMsg' in text or 'SERVICE ERROR' in text:
            raise AuthError('SERVICE_KEY_ERROR') from None
        raise CollectorError('NON_JSON_RESPONSE') from None


def text_value(value):
    # KAMIS는 빈 필드를 []로 보낸다. 목록·객체는 문자열 값으로 보지 않는다.
    if value is None or isinstance(value, (list, dict)):
        return None
    value = str(value).strip()
    return value or None


def number(value):
    """'1,234' → 1234.0. 빈 값·'-'는 None."""
    value = text_value(value)
    if value is None or value == '-':
        return None
    try:
        return float(value.replace(',', ''))
    except ValueError:
        return None


def as_list(value):
    if value is None or value == '':
        return []
    return value if isinstance(value, list) else [value]
