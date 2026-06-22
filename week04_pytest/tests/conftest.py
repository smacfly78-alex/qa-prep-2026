import pytest
from src.user import User

@pytest.fixture
def default_user() -> User:
    return User(name="Igor", email="igor@example.com", age=30)

@pytest.fixture
def users_list() -> list[User]:
    user_1 = User("Igor", "igor@example.com", 30)
    user_2 = User("Anna", "anna@example.com", 17)
    user_3 = User("Dmitry", "dmitry@example.com", 45)
    return [user_1, user_2, user_3]