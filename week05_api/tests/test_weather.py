from unittest.mock import Mock

import pytest
import requests

from src.weather import get_temperature


def test_get_temperature_returns_value_on_success(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"temperature": 22.5}

    mock_get = mocker.patch('src.weather.requests.get')
    mock_get.return_value = fake_response

    result = get_temperature('Moscow')

    assert result == 22.5, f'Expected 22.5, got {result}'

    mock_get.assert_called_once_with('https://api.weather.com/current?city=Moscow', timeout=5)

def test_get_temperature_raises_on_connection_error(mocker):
    mock_get = mocker.patch('src.weather.requests.get')
    mock_get.side_effect = requests.ConnectionError('Bad connect')

    with pytest.raises(requests.ConnectionError):
        get_temperature("Moscow")

def test_get_temperature_calls_correct_city(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"temperature": 20.0}

    mock_get = mocker.patch('src.weather.requests.get')
    mock_get.return_value = fake_response

    get_temperature("Berlin")

    mock_get.assert_called_once_with('https://api.weather.com/current?city=Berlin', timeout=5)