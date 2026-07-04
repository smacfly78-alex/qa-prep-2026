import requests


def fetch_user_name(user_id: int) -> str:
    """Fetches user by id and returns their name."""
    response = requests.get(
        f"https://api.example.com/users/{user_id}",
        timeout=5
    )
    response.raise_for_status()
    return response.json()["name"]


def fetch_user_name_safe(user_id: int) -> str | None:
    """Same as fetch_user_name, but returns None on network errors."""
    try:
        response = requests.get(
            f"https://api.example.com/users/{user_id}",
            timeout=5
        )
        response.raise_for_status()
        return response.json()["name"]
    except requests.ConnectionError:
        return None
    except requests.Timeout:
        return None


def fetch_and_notify(user_id: int, phone: str) -> bool:
    """Fetches user data and sends SMS notification. Returns success bool."""
    try:
        response = requests.get(
            f"https://api.example.com/users/{user_id}",
            timeout=5
        )
        response.raise_for_status()
        user_name = response.json()["name"]
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError):
        return False

    # Отправляем SMS
    from week05_api.src.sms_client import send_sms
    send_sms(phone, f"Hello, {user_name}!")
    return True