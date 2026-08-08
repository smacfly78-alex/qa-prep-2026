
class Fibonacci:
    def __init__(self, n: int) -> None:
        self.limit = n
        self.start = 0
        self.a = 0
        self.b = 1

    def __iter__(self) -> 'Fibonacci':
        return self

    def __next__(self) -> int:
        if self.start >= self.limit:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.start += 1
        return result

if __name__ == '__main__':
    fib = Fibonacci(10)
    for num in fib:
        print(num, end=" ")
    # 0 1 1 2 3 5 8 13 21 34

    print()
    print(list(Fibonacci(5)))
    # [0, 1, 1, 2, 3]

    print(list(Fibonacci(1)))
    # [0]

    print(list(Fibonacci(0)))
    # []

    # Ручной вызов
    it = iter(Fibonacci(3))
    print(next(it))  # 0
    print(next(it))  # 1
    print(next(it))  # 1
    # next(it) — StopIteration!