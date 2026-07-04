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