import pytest
from jsonschema import validate
from week05_api.src.schemas import POST_SCHEMA


def test_post_matches_schema(api_session):
    """Post response should match POST_SCHEMA."""
    response = api_session.get(url="https://jsonplaceholder.typicode.com/posts/1", timeout=5)

    assert response.status_code == 200, f'Expected status code: 200, got {response.status_code}'

    validate(instance=response.json(), schema=POST_SCHEMA)


@pytest.mark.parametrize("post_id", [1, 5, 50, 100])
def test_posts_match_schema(api_session, post_id: int) -> None:
    response = api_session.get(url=f"https://jsonplaceholder.typicode.com/posts/{post_id}", timeout=5)

    assert response.status_code == 200, f"For post_id={post_id}: expected 200, got {response.status_code}"

    validate(instance=response.json(), schema=POST_SCHEMA)