
import requests


def get_user_posts(user_id: int, limit: int = 10) -> list[dict]:
    response = requests.get(url='https://jsonplaceholder.typicode.com/posts', params={'userId': user_id, '_limit': limit}, timeout=5 )

    if not response.ok:
        raise Exception(f"Request failed with status {response.status_code}")

    return response.json()

def get_post_or_none(post_id: int) -> dict | None:
    response = requests.get(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)

    if response.ok:
        return response.json()
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"Unexpected status {response.status_code}")

if __name__ == '__main__':
    post = get_post_or_none(1)
    print(post["title"])  # успешно

    missing = get_post_or_none(99999)
    print(missing)  # None


    # posts = get_user_posts(user_id=1, limit=3)
    # print(len(posts))  # 3
    # for post in posts:
    #     print(post["title"])
