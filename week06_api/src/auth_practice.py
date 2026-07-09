
import requests


def check_basic_auth(url: str, username: str, password: str) -> bool:
    try:
        response = requests.get(url=url, auth=(username, password), timeout=5)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return False

    return response.status_code == 200


def get_user_profile(token: str) -> dict | None:
    """
    Fetches user profile using Bearer token.
    Returns dict on success, None on 401 or network errors.
    """
    try:
        response = requests.get(
            "https://api.example.com/users/me",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )
    except requests.RequestException:
        return None

    if response.status_code == 401:
        return None

    response.raise_for_status()
    return response.json()

def fetch_stripe_customers(api_key: str) -> list | None:
    try:
        headers = {'Authorization': f'Bearer {api_key}'}
        response = requests.get(url='https://api.stripe.com/v1/customers', headers=headers, timeout=5)

    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    return response.json()['data']


if __name__ == '__main__':
    # Правильные credentials
    result = check_basic_auth(
        "https://httpbin.org/basic-auth/user/passwd",
        "user",
        "passwd"
    )
    print(result)  # True

    # Неправильные credentials
    result = check_basic_auth(
        "https://httpbin.org/basic-auth/user/passwd",
        "wrong",
        "wrong"
    )
    print(result)  # False

    # Неверный URL
    result = check_basic_auth(
        "https://nonexistent.example.com/",
        "user",
        "passwd"
    )
    print(result)  # False (network error)