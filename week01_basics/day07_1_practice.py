from typing import Callable


def sum_of_evens(items: list[int]) -> int:
    result = 0
    for item in items:
        if item % 2 == 0:
            result += item
    return result

def find_first_negative(items: list[int]) -> int | None:
    result = None
    for item in items:
        if item < 0:
            result = item
            break
    return result

def clean_strings(items: list[str| None]) -> list[str]:
    new_items = []
    for item in items:
        if item is None:
            continue
        cleaned = item.strip().lower()
        if cleaned == "":
            continue
        new_items.append(cleaned)
    return new_items

def keep_doubling_until(start: int, limit: int) -> int:
    counter = 0
    while start < limit:
        counter += 1
        start = start * 2
    return counter

def pair_with_position_enumerate(names: list[str], values: list[int]) -> list[str]:
    items = []
    for i, (name, value) in enumerate(zip(names, values), start=1):
        items.append(f'{i}. {name}: {value}')
    return items

def pair_with_position(names: list[str], values: list[int]) -> list[str]:
    items = []
    i = 1
    for name, value in zip(names, values):
        items.append(f'{i}. {name}: {value}')
        i +=1
    return items






if __name__ == '__main__':
    print(pair_with_position(["Igor", "Anna", "Dmitry"], [85, 92, 78]))
    # ['1. Igor: 85', '2. Anna: 92', '3. Dmitry: 78']

    print(pair_with_position(["Alex"], [100]))
    # ['1. Alex: 100']

    print(pair_with_position([], []))
    # []


    # print(keep_doubling_until(1, 100))  # 7   (1→2→4→8→16→32→64→128, 7 удвоений)
    # print(keep_doubling_until(1, 10))  # 4   (1→2→4→8→16, 4 удвоения)
    # print(keep_doubling_until(50, 100))  # 1   (50→100, ровно 1 удвоение, 100 не меньше предела)
    # print(keep_doubling_until(100, 50))  # 0   (уже больше предела, ни одного удвоения)


    # print(clean_strings(["Hello", "  WORLD  ", "", "Python", None, "  GO"]))
    # # ['hello', 'world', 'python', 'go']


    # print(find_first_negative([1, 2, -3, 4, -5]))  # -3   (первое отрицательное, дальше не ищем)
    # print(find_first_negative([1, 2, 3]))  # None (нет отрицательных)
    # print(find_first_negative([-1, -2, -3]))  # -1   (первое же)
    # print(find_first_negative([]))  # None


    # print(sum_of_evens([1, 2, 3, 4, 5, 6]))  # 12   (2 + 4 + 6)
    # print(sum_of_evens([1, 3, 5]))  # 0
    # print(sum_of_evens([])) # 0
    # print(sum_of_evens([10, 20, 30]))  # 60