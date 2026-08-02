
class EvenNumbers:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self) -> 'EvenNumbers':
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        result = self.current
        self.current += 2
        return result


if __name__ == '__main__':
    even = EvenNumbers(10)
    for n in even:
        print(n, end=" ")
    # 0 2 4 6 8 10

    print()
    print(list(EvenNumbers(6)))
    # [0, 2, 4, 6]

    print(list(EvenNumbers(1)))
    # [0]

    print(list(EvenNumbers(0)))
    # [0]

    # Ручной вызов
    it = iter(EvenNumbers(4))
    print(next(it))  # 0
    print(next(it))  # 2
    print(next(it))  # 4
    # next(it) — StopIteration!