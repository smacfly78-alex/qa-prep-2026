import requests

def safe_get_post(post_id: int) -> dict | None:
    try:
        response = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)
    except requests.Timeout:
        print('Request timed out')
        return None
    except requests.ConnectionError:
        print('Connection error')
        return None
    except requests.RequestException as e:
        print(f'Request error: {e}')
        return None
    else:
        if response.status_code == 404:
            return None
        elif response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Unexpected status: {response.status_code}")


class APIError(Exception):
    def __init__(self, message: str, status_code: int, endpoint: str) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.endpoint = endpoint


def fetch_with_api_error(endpoint: str) -> dict:
    response = requests.get(url=f'https://jsonplaceholder.typicode.com{endpoint}', timeout=5)

    if response.status_code in (200, 201):
        return response.json()
    else:
        raise APIError("Request failed", status_code=response.status_code, endpoint=endpoint)