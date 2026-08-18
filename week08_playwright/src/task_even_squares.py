
def even_squares(n):
    return (x**2 for x in range(n+1) if x % 2 == 0)

if __name__ == '__main__':
    for x in even_squares(10):
        print(x, end=" ")
    # 0 4 16 36 64 100

    print()
    print(list(even_squares(6)))
    # [0, 4, 16, 36]

    print(list(even_squares(1)))
    # [0]  (только 0 чётное в диапазоне 0-1)

    print(list(even_squares(0)))
    # [0]

    print(list(even_squares(-1)))
    # []  (пустой диапазон)

    # Ручной вызов
    gen = even_squares(6)
    print(next(gen))  # 0
    print(next(gen))  # 4
    print(next(gen))  # 16
    print(next(gen))  # 36
    # next(gen) → StopIteration