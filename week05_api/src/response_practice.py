
import requests
from requests import Session


def get_response_metadata(post_id: int) -> dict:
    response = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)

    result = {
        "status_code": response.status_code,
        "content_type": response.headers.get("Content-Type", None),
        "content_length": int(response.headers.get("Content-Length", 0)),
        "elapsed_seconds": response.elapsed.total_seconds()
    }

    return result

def get_post_with_token(post_id: int, token: str) -> dict:
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', headers=headers, timeout=5)

    if not response.ok:
        raise Exception(f'Error! Status code: {response.status_code}')
    return response.json()


def get_multiple_posts(post_ids: list[int]) -> list[dict]:
    result = []
    with Session() as session:
        session.headers.update({"User-Agent": "MyTestClient/1.0"})
        for post_id in post_ids:
            response = session.get(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)
            if response.ok:
                result.append(response.json())
    return result
