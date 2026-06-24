from typing import Iterator


class RangeReversed:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "RangeReversed":
        return self

    def __next__(self) -> int:
        if self.current == 0:
            raise StopIteration
        result = self.current
        self.current -= 1
        return result


if __name__ == '__main__':
    for n in RangeReversed(5):
        print(n)
    # 5
    # 4
    # 3
    # 2
    # 1

    print(list(RangeReversed(3)))
    # [3, 2, 1]

    print(list(RangeReversed(0)))
    # []