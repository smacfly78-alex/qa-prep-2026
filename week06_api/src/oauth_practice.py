import requests


class TokenExpired(Exception):
    """Raised when refresh token is also expired."""
    pass


def refresh_access_token(refresh_token: str) -> str:
    """
    Exchanges refresh token for a new access token.
    Raises TokenExpired if refresh token is invalid.
    """
    response = requests.post(
        "https://api.example.com/oauth/token",
        json={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        timeout=5
    )

    if response.status_code == 401:
        raise TokenExpired("Refresh token expired, user must re-login")

    response.raise_for_status()
    return response.json()["access_token"]


def get_user_data(access_token: str, refresh_token: str) -> dict | None:
    """
    Fetches user data. If access_token expired (401), refreshes and retries.
    Returns None on network errors or if refresh_token also expired.
    """

    def _make_request(token: str):
        return requests.get(
            "https://api.example.com/users/me",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )

    try:
        response = _make_request(access_token)

        if response.status_code == 401:
            try:
                new_token = refresh_access_token(refresh_token)
            except TokenExpired:
                return None

            response = _make_request(new_token)

        response.raise_for_status()
        return response.json()

    except requests.RequestException:
        return None