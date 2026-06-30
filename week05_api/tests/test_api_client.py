def test_get_post_returns_dict(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
    )

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_post_has_required_fields(api_session):
    response = api_session.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
    )

    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "userId" in data