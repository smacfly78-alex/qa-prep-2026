# src/user_repo.py
import requests


def get_active_users_count() -> int:
    """
    Fetches list of users, returns count of active ones.
    Returns 0 on network errors.
    """
    try:
        response = requests.get("https://api.com/users", timeout=5)
        response.raise_for_status()
        users = response.json()
        return sum(1 for user in users if user.get("is_active"))
    except (requests.ConnectionError, requests.Timeout, requests.HTTPError):
        return 0
