import pytest


# Напишите ДВЕ фикстуры:
# 1. fresh_dict — scope="function" — возвращает новый {"count": 0}
# 2. shared_list — scope="module" — возвращает новый []

@pytest.fixture(scope="function")
def fresh_dict() -> dict[str, int]:
    return {"count": 0}

@pytest.fixture(scope="module")
def shared_list() -> list[int]:
    return []

# И ТРИ теста:
# test_a: добавляет элемент в shared_list, увеличивает fresh_dict["count"]
# test_b: добавляет элемент в shared_list, увеличивает fresh_dict["count"]
# test_c: проверяет, что в shared_list ДВА элемента, и fresh_dict["count"] == 1

def test_a(shared_list, fresh_dict) -> None:
    shared_list.append(1)
    fresh_dict['count'] += 1

def test_b(shared_list, fresh_dict) -> None:
    shared_list.append(1)
    fresh_dict['count'] += 1

def test_c(shared_list, fresh_dict) -> None:
    assert len(shared_list) == 2 and fresh_dict["count"] == 1