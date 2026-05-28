from typing import Callable

def double_all(items: list) -> list:
    new_items = []
    for item in items:
        item = item * 2
        new_items.append(item)
    return new_items

def keep_positive(items: list[int]) -> list[int]:
    new_items = []
    for item in items:
        if item > 0:
            new_items.append(item)
    return new_items

def list_to_dict(items: list[str]) -> dict:
    count = {}
    for item in items:
        count[item] = len(item)
    return count

def count_chars(phrase: str) -> dict:
    count = {}
    for char in phrase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def unique_items(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def capitalize_words(phrase: str) -> str:
    new_phrase = []
    for word in phrase.split(' '):
        new_phrase.append(word.capitalize())
    return ' '.join(new_phrase)

def transform_list(items: list[int], func: Callable[[int], int]) -> list[int]:
    new_items=[]
    for item in items:
        new_items.append(func(item))
    return new_items

def make_multiplier(n: int) -> Callable[[int], int]:
    def multiply(x: int) -> int:
        return x * n
    return multiply

def make_running_sum() -> Callable[[int], int]:
    result = 0
    def summator(x: int) -> int:
        nonlocal result
        result = result + x
        return result
    return summator

def make_logger_with_filter(prefix: str, condition: Callable[[str], bool]) -> Callable[[str], str | None]:
    count = 0
    def log_long(phrase:str) -> str|None:
        nonlocal count
        if condition(phrase):
            count += 1
            return f'[{prefix}] ({count}) {phrase}'
        return None
    return log_long



if __name__ == '__main__':
    # Фильтр: логировать только сообщения длиннее 5 символов
    log_long = make_logger_with_filter("API", lambda msg: len(msg) > 5)

    print(log_long("OK"))  # None  (короткое — не логируем)
    print(log_long("Request started"))  # [API] (1) Request started
    print(log_long("hi"))  # None
    print(log_long("Response 200"))  # [API] (2) Response 200
    print(log_long("Done"))  # None
    print(log_long("Connection closed"))  # [API] (3) Connection closed

    # Другой фильтр: логировать только сообщения с восклицательным знаком
    log_alerts = make_logger_with_filter("ALERT", lambda msg: "!" in msg)

    print(log_alerts("everything fine"))  # None
    print(log_alerts("danger!"))  # [ALERT] (1) danger!
    print(log_alerts("ok"))  # None
    print(log_alerts("attack!"))  # [ALERT] (2) attack!


    # total = make_running_sum()
    #
    # print(total(5))  # 5    (5)
    # print(total(3))  # 8    (5 + 3)
    # print(total(10))  # 18   (5 + 3 + 10)
    # print(total(-2))  # 16   (5 + 3 + 10 - 2)
    #
    # total2 = make_running_sum()
    # print(total2(100))  # 100
    # print(total2(50))  # 150
    # print(total(7))  # 23  (старый продолжает считать своё: 16 + 7)


    # double = make_multiplier(2)
    # triple = make_multiplier(3)
    #
    # print(double(5))  # 10
    # print(double(10))  # 20
    # print(triple(5))  # 15
    # print(triple(10))  # 30


    # print(unique_items([1, 2, 2, 3, 3, 3])) # [1, 2, 3]
    # print(unique_items(["a", "b", "a", "c"]))  # ['a', 'b', 'c']
    # print(unique_items([]))  # []

    # print(capitalize_words("hello world"))

    # print(transform_list([1, 2, 3], lambda x: x * 10))     # [10, 20, 30])
    #
    # def square(n):
    #     return n * n
    #
    # print(transform_list([1, 2, 3, 4], square))  # [1, 4, 9, 16]