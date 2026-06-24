from typing import Iterator


def even_numbers(limit: int) -> Iterator[int]:
    for number in range(limit):
        yield number*2


if __name__ == "__main__":
    for n in even_numbers(5):
        print(n)
    # 0
    # 2
    # 4
    # 6
    # 8

    print(list(even_numbers(3)))
    # [0, 2, 4]

    print(list(even_numbers(0)))
    # []