import requests


def fetch_data(url: str) -> dict:
    """Fetch data from URL. Retries up to 3 times on 500 status."""
    for attempt in range(3):
        response = requests.get(url, timeout=5)
        if response.status_code == 500:
            continue   # повтор
        response.raise_for_status()
        return response.json()
    raise RuntimeError("All retries failed with 500")