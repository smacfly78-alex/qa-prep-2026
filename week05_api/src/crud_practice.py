import requests

def create_post(title: str, body: str, user_id: int) -> dict:
    BODY = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(url='https://jsonplaceholder.typicode.com/posts', json=BODY, timeout=5)

    if response.status_code != 201:
        raise Exception(f"Failed to create post: status {response.status_code}")
    return response.json()

def update_post(post_id: int, title: str, body: str, user_id: int) -> dict:
    BODY = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.put(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=BODY, timeout=5)

    if response.status_code != 200:
        raise Exception(f'Failed to create post: status {response.status_code}')
    return response.json()

def delete_post(post_id: int) -> bool:
    response = requests.delete(url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)

    if response.status_code in (200, 204):
        return True
    elif response.status_code == 404:
        return False
    else:
        raise Exception(f'Failed to create post: status {response.status_code}')

if __name__ == '__main__':
    result = delete_post(1)
    print(result)
    # True

    result = delete_post(99999)
    print(result)
    # False (поста с таким id нет)

    # updated = update_post(1, "New Title", "New body", user_id=1)
    # print(updated)

    # {'id': 1, 'title': 'New Title', 'body': 'New body', 'userId': 1}
    # new_post = create_post("My Title", "Post body content", user_id=1)
    # print(new_post)
    # # {'title': 'My Title', 'body': 'Post body content', 'userId': 1, 'id': 101}
    #
    # print(new_post["id"])  # 101