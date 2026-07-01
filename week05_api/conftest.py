
import pytest
from requests import Session


@pytest.fixture
def api_session():
    with Session() as session:
        session.headers.update({'Authorization': 'Bearer test_token'})
        yield session


@pytest.fixture
def new_post_data() -> dict:
    """Standard test data for creating a new post."""
    return {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }


# В conftest.py
@pytest.fixture
def created_post(api_session, new_post_data) -> dict:
    """Creates a post for the test, yields it, then deletes after."""
    response = api_session.post('https://jsonplaceholder.typicode.com/posts', json=new_post_data, timeout=5)
    post = response.json()
    try:
        yield post
    finally:
        api_session.delete(f'https://jsonplaceholder.typicode.com/posts/{post['id']}', timeout=5)