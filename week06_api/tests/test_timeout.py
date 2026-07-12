from unittest.mock import Mock

import requests
from week06_api.src.timeout_practice import fetch_with_timeout


def test_success(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"data": "ok"}
    fake_response.status_code = 200

    mock_get = mocker.patch("week06_api.src.timeout_practice.requests.get")
    mock_get.return_value = fake_response

    result = fetch_with_timeout("https://api.com/data")
    expected = {"data": "ok"}

    assert result == expected, f'Expected {expected}, got {result}'

def test_connect_timeout(mocker):
    mock_get = mocker.patch("week06_api.src.timeout_practice.requests.get")
    mock_get.side_effect = requests.ConnectTimeout('"cannot connect"')

    result = fetch_with_timeout("https://api.com/data")

    assert result is None, f'Expected None, got {result}'

def test_read_timeout(mocker):
    mock_get = mocker.patch("week06_api.src.timeout_practice.requests.get")
    mock_get.side_effect = requests.ReadTimeout("server slow")

    result = fetch_with_timeout("https://api.com/data")

    assert result is None, f'Expected None, got {result}'

def test_http_error(mocker):
    fake_response = Mock()
    fake_response.status_code = 500
    fake_response.raise_for_status.side_effect = requests.HTTPError("500")

    mock_get = mocker.patch("week06_api.src.timeout_practice.requests.get")
    mock_get.return_value = fake_response

    result = fetch_with_timeout("https://api.com/data")

    assert result is None, f'Expected None, got {result}'
