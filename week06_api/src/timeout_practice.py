import requests


def fetch_with_timeout(
        url: str,
        connect_timeout: float = 3.0,
        read_timeout: float = 10.0,
) -> dict | None:

    try:
        response = requests.get(url, timeout=(connect_timeout, read_timeout))
        response.raise_for_status()
        return response.json()
    except requests.ConnectTimeout:
        return None
    except requests.ReadTimeout:
        return None
    except requests.HTTPError:
        return None
    except requests.RequestException:
        return None

