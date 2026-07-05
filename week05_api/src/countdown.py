from typing import Iterator


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start
        self.current = self.start

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.current >= 1:
            result = self.current
            self.current -= 1
            return result
        else:
            raise StopIteration

if __name__ == '__main__':
    cd = Countdown(5)
    for n in cd:
        print(n)
    # 5
    # 4
    # 3
    # 2
    # 1

    # List
    print(list(Countdown(3)))
    # [3, 2, 1]

    # Пустой countdown
    print(list(Countdown(0)))
    # []