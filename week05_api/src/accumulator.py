from collections.abc import Callable


def make_accumulator(start: int = 0) -> Callable:
    total = start
    def add(step: int = 1) -> int:
        nonlocal total
        total += step
        return total
    return add

if __name__ == '__main__':
    acc = make_accumulator()
    print(acc())  # 1
    print(acc())  # 2
    print(acc(step=5))  # 7
    print(acc(10))  # 17

    acc2 = make_accumulator(start=100)
    print(acc2())  # 101   ← НЕ 100!
    print(acc2(step=50))  # 151
    print(acc())  # 18    ← первый acc не затронут