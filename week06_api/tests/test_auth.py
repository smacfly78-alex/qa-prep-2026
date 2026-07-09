from unittest.mock import Mock
import requests

from src.auth_practice import get_user_profile, fetch_stripe_customers


def test_get_user_profile_success(mocker):
    fake_response = Mock()
    fake_response.json.return_value = {"id": 1, "name": "Igor"}
    fake_response.status_code = 200

    mock_get = mocker.patch("src.auth_practice.requests.get")
    mock_get.return_value = fake_response

    result = get_user_profile('test_token_123')

    expected_result = {"id": 1, "name": "Igor"}
    assert result == expected_result, f'Expected {expected_result}, got {result}'

    mock_get.assert_called_once_with("https://api.example.com/users/me",
    headers={"Authorization": "Bearer test_token_123"},
    timeout=5)


def test_get_user_profile_returns_none_on_401(mocker):
    fake_response = Mock()
    fake_response.status_code = 401

    mock_get = mocker.patch("src.auth_practice.requests.get")
    mock_get.return_value = fake_response

    result = get_user_profile('test_token_123')

    assert result is None, f'Expected None, got {result}'

def test_get_user_profile_returns_none_on_network_error(mocker):
    mock_get = mocker.patch('src.auth_practice.requests.get')
    mock_get.side_effect = requests.ConnectionError

    result = get_user_profile('test_token_123')

    assert result is None, f'Expected None, got {result}'


def test_fetch_stripe_customers_success(mocker):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"data": [{"id": "cus_1"}, {"id": "cus_2"}], "has_more": False}

    mock_get = mocker.patch("src.auth_practice.requests.get")
    mock_get.return_value = fake_response

    result = fetch_stripe_customers("sk_test_abc123")

    expected = [{"id": "cus_1"}, {"id": "cus_2"}]
    assert result == expected, f'Expected {expected}, got {result}'

    mock_get.assert_called_once_with(url='https://api.stripe.com/v1/customers',
                                     headers={'Authorization': 'Bearer sk_test_abc123'}, timeout=5)