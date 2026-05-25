
def increment_counter(counter: dict, key: str) -> None:
    if key in counter:
        counter[key] += 1
    else:
        counter[key] = 1

def try_replace_list(items: list, new_items: list) -> None:
    items[:] = new_items


def safe_modify(items: list) -> list:
    new_items = []
    for number in items:
        new_items.append(number * 2)
    return new_items


if __name__ == '__main__':
    fruits = {"яблоко": 3, "груша": 1}
    print("До:", fruits)

    increment_counter(fruits, "яблоко")
    print("После 'яблоко':", fruits)

    increment_counter(fruits, "слива")
    print("После 'слива':", fruits)

    a = [1, 2, 3]
    b = [10, 20, 30]
    try_replace_list(a, b)
    print(a)

    a = [1, 2, 3]
    b = safe_modify(a)
    print(a)  # [1, 2, 3] — не изменился
    print(b)  # [2, 4, 6] — новый список