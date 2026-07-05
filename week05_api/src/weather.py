# week05_api/src/weather.py
import requests


def get_temperature(city: str) -> float:
    """Fetches current temperature for city. Returns Celsius."""
    response = requests.get(
        f"https://api.weather.com/current?city={city}",
        timeout=5
    )
    response.raise_for_status()
    return response.json()["temperature"]
