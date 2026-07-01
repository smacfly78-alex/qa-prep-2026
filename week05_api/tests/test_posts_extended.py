import pytest
import requests


def test_create_post_returns_201(api_session, new_post_data):
    response = api_session.post('https://jsonplaceholder.typicode.com/posts', json=new_post_data, timeout=5)

    assert response.status_code == 201, f'Error: {response.status_code}'



def test_create_post_response_has_id(api_session, new_post_data):
    response = api_session.post('https://jsonplaceholder.typicode.com/posts', json=new_post_data, timeout=5)

    data = response.json()
    assert "id" in data, f"Response missing 'id' field: {data}"


def test_create_post_preserves_title(api_session, new_post_data):
    response = api_session.post('https://jsonplaceholder.typicode.com/posts', json=new_post_data, timeout=5)

    data = response.json()
    assert data['title'] == new_post_data['title'], f"Expected '{new_post_data['title']}', got '{data['title']}'"


@pytest.mark.parametrize("post_id,expected_status", [
    (1, 200),
    (50, 200),
    (100, 200),
    (101, 404),
    (99999, 404),
])
def test_get_post_status(api_session, post_id: int, expected_status: int) -> None:
    response = api_session.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}', timeout=5)

    assert response.status_code == expected_status, f"For post_id={post_id}: expected {expected_status}, got {response.status_code}"


def test_created_post_has_correct_userId(api_session, created_post) -> None:
    """A post created via fixture should have userId from new_post_data."""
    assert created_post["userId"] == 1