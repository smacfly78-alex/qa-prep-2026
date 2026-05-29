from itertools import count
from typing import Callable

def most_frequent(phrase: str) -> str:
    counter = {}
    best_char = ''
    best_count = 0
    for char in phrase:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    for char, count in counter.items():
        if count > best_count:
            best_char = char
            best_count = count
    return best_char

def group_by_length(items: list[str]) -> dict:
    result = {}
    for word in items:
        key = len(word)
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return result

def make_validator(min_len: int, max_len: int) -> Callable[[str], bool]:
    def username_validator(phrase: str) -> bool:
        return min_len <= len(phrase) <= max_len
    return username_validator

def make_attempt_tracker() -> Callable[[bool], dict]:
    counter_all = 0
    counter_true = 0
    counter_false = 0
    def tracker(flag: bool) -> dict:
        nonlocal counter_all
        nonlocal counter_true
        nonlocal counter_false
        counter_all += 1
        if flag:
            counter_true += 1
        else:
            counter_false += 1
        return {'total': counter_all, 'success': counter_true, 'failed': counter_false}
    return tracker

def make_request_tracker(prefix: str) -> Callable[[int], str | None]:
    success, failed = 0, 0
    def api_tracker(status: int) -> str | None:
        nonlocal success, failed
        if 200 <= status <= 299:
            success += 1
            return f'[{prefix}] (success #{success}) status={status}'
        else:
            failed += 1
            return None
    return api_tracker




if __name__ == '__main__':
    api_tracker = make_request_tracker("API")

    print(api_tracker(200))  # [API] (success #1) status=200
    print(api_tracker(404))  # None
    print(api_tracker(201))  # [API] (success #2) status=201
    print(api_tracker(500))  # None
    print(api_tracker(204))  # [API] (success #3) status=204

    # Независимый трекер
    db_tracker = make_request_tracker("DB")
    print(db_tracker(200))  # [DB] (success #1) status=200
    print(api_tracker(200))  # [API] (success #4) status=200  ← старый продолжает счёт

    # tracker = make_attempt_tracker()
    #
    # print(tracker(True))  # {'total': 1, 'success': 1, 'failed': 0}
    # print(tracker(False))  # {'total': 2, 'success': 1, 'failed': 1}
    # print(tracker(True))  # {'total': 3, 'success': 2, 'failed': 1}
    # print(tracker(False))  # {'total': 4, 'success': 2, 'failed': 2}
    # print(tracker(True))  # {'total': 5, 'success': 3, 'failed': 2}
    #
    # # Независимый трекер
    # tracker2 = make_attempt_tracker()
    # print(tracker2(True))  # {'total': 1, 'success': 1, 'failed': 0}
    # print(tracker(False))  # {'total': 6, 'success': 3, 'failed': 3} — старый продолжает


    # print(most_frequent("hello")) # "l"
    # print(most_frequent("aabbbcc"))  # "b"
    # print(most_frequent("python"))  # "p"   (или любая буква — все по 1, но первая встретилась 'p')

    # print(group_by_length(["cat", "dog", "hello", "hi", "world", "ok"]))
    # {3: ['cat', 'dog'], 5: ['hello', 'world'], 2: ['hi', 'ok']}