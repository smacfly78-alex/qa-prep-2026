from typing import Callable


def make_logger(prefix: str) -> Callable[[str], str]:
    count = 0
    def logger(message: str) -> str:
        nonlocal count
        count += 1
        return f'[{prefix}] ({count}) {message}'
    return logger

def make_filter(condition: Callable[[int], bool]) -> Callable[[list[int]], list[int]]:
    def apply_filter(items: list[int]) -> list[int]:
        result = []
        for item in items:
            if condition(item):
                result.append(item)
        return result
    return apply_filter

def make_safe_appender(initial: list[int]) -> Callable[[int], list[int]]:
    result = initial.copy()
    def appender(value: int) -> list[int]:
        result.append(value)
        return result
    return appender



if __name__ == '__main__':
    api_log = make_logger("API")
    db_log = make_logger("DB")

    print(api_log("Request started"))  # [API] (1) Request started
    print(api_log("Response 200"))  # [API] (2) Response 200
    print(db_log("Connect"))  # [DB] (1) Connect          ← независимый счётчик
    print(api_log("Request ended"))  # [API] (3) Request ended
    print(db_log("Query"))  # [DB] (2) Query

    filter_positive = make_filter(lambda x: x > 0)
    filter_even = make_filter(lambda x: x % 2 == 0)

    print(filter_positive([-2, -1, 0, 1, 2, 3]))  # [1, 2, 3]
    print(filter_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
    print(filter_positive([10, -10, 20, -20]))  # [10, 20]

    my_list = [1, 2, 3]
    append_to_list = make_safe_appender(my_list)

    print(append_to_list(4))  # [1, 2, 3, 4]
    print(append_to_list(5))  # [1, 2, 3, 4, 5]
    print(append_to_list(6))  # [1, 2, 3, 4, 5, 6]

    print(my_list)  # [1, 2, 3]  ← оригинал не изменился!