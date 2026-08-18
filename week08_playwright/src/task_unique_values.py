
def unique_values(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    for x in result:
        yield x


if __name__ == '__main__':
    result = list(unique_values([1, 2, 2, 3, 1, 4, 3, 5]))
    print(result)
    # [1, 2, 3, 4, 5]

    result = list(unique_values("hello"))
    print(result)
    # ['h', 'e', 'l', 'o']  ← вторая 'l' пропущена

    result = list(unique_values([]))
    print(result)
    # []

    result = list(unique_values(["apple", "banana", "apple", "cherry", "banana"]))
    print(result)
    # ['apple', 'banana', 'cherry']

    # Ручной вызов
    gen = unique_values([1, 1, 2, 3, 2])
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    # next(gen) → StopIteration
