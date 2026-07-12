import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception_type, wait_exponential,
)
from urllib3.contrib.emscripten import response


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(0),   # ← 0 для тестов, чтобы не ждать реально
    retry=retry_if_exception_type(requests.ConnectionError),
    reraise=True
)
def fetch_data_with_retry(url: str) -> dict:
    """
    Fetches data with retry on ConnectionError.
    Retries up to 3 times, no wait between (for tests).
    """
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=16),
    retry=retry_if_exception_type((requests.ConnectionError, requests.Timeout)),
    reraise=True
)
def fetch_orders(order_id: int) -> dict:
    response = requests.get(f'https://api.example.com/orders/{order_id}', timeout=5)
    response.raise_for_status()
    return response.json()