
def multiply_all(*args: float) -> float:
    result = 1
    for i in args:
        result *= i
    return result

if __name__ == '__main__':
    print(multiply_all(2, 3, 4))  # 24
    print(multiply_all(5))  # 5
    print(multiply_all(1.5, 2, 4))  # 12.0
    print(multiply_all())  # 1 (пустое произведение)