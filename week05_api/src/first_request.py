import requests


def get_first_post() -> dict:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()


if __name__ == '__main__':
    post = get_first_post()
    print(post)