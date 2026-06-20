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


def test_users_list_has_three_items(users_list: list[User]) -> None:
    assert len(users_list) == 3

def test_two_users_are_adults(users_list: list[User]) -> None:
    adults_count = sum(1 for user in users_list if user.is_adult())
    assert adults_count == 2


def test_all_users_have_valid_emails(users_list: list[User]) -> None:
    assert all(user.is_valid_email() for user in users_list)


def test_default_user_is_adult(default_user: User) -> None:
    assert default_user.is_adult()

def test_default_user_has_valid_email(default_user: User) -> None:
    assert default_user.is_valid_email()

def test_default_user_has_correct_name(default_user: User) -> None:
    assert default_user.name == "Igor"