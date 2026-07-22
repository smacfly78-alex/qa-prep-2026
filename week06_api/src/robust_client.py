import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type((requests.ConnectionError, requests.Timeout)),
    reraise=True,
)
def robust_fetch(url: str, token: str) -> dict | None:
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token}'})

    try:
        response = session.get(url, timeout=(3, 10))
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        return None