import requests


class APIClient:
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def __enter__(self) -> "APIClient":
        self.session = requests.Session()
        headers = {f'Authorization': f'Bearer {self.token}'}
        self.session.headers.update(headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def get(self, endpoint) -> dict:
        response = self.session.get(url=f'{self.base_url}{endpoint}', timeout=5)
        if response.status_code != 200:
            raise Exception(f"Response status {response.status_code}")
        return response.json()

if __name__ == '__main__':
    with APIClient("https://jsonplaceholder.typicode.com", "fake_token") as client:
        post = client.get("/posts/1")
        print(post["title"])

        user = client.get("/users/1")
        print(user["name"])

    # Сессия закрылась автоматически