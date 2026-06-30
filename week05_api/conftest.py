
import pytest
from requests import Session


@pytest.fixture
def api_session():
    with Session() as session:
        session.headers.update({'Authorization': 'Bearer test_token'})
        yield session
