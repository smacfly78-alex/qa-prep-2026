import requests


def authenticated_session(base_url: str, username: str, password: str,) -> requests.Session:
    body = {
        'username': username,
        'password': password
    }
    response = requests.post(f'{base_url}/login', json=body, timeout=(3, 10))
    response.raise_for_status()
    token = response.json()['access_token']

    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {token}'})

    return session