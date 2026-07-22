import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from src.oauth_practice import refresh_access_token, TokenExpired


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type((requests.ConnectionError, requests.Timeout)),
    reraise=True
)
def get_secured_data(url: str, access_token: str, refresh_token: str) -> dict | None:
    try:
        response = requests.get(url, headers={'Authorization': f'Bearer {access_token}'}, timeout=(3, 10))
        if response.status_code == 401:
            try:
                new_access_token = refresh_access_token(refresh_token)

                response = requests.get(url, headers={'Authorization': f'Bearer {new_access_token}'}, timeout=(3, 10))
                response.raise_for_status()
                return  response.json()
            except TokenExpired:
             return None
        response.raise_for_status()
        return response.json()
    except requests.HTTPError:
        return None
