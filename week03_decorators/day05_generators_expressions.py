
def sum_of_even_squares(numbers: list[int]) -> int:
    return sum(x ** 2 for x in numbers if x % 2 == 0)



if __name__ == '__main__':
    print(sum_of_even_squares([1, 2, 3, 4, 5]))  # 20 (2² + 4² = 4 + 16)
    print(sum_of_even_squares([1, 3, 5]))  # 0 (нет чётных)
    print(sum_of_even_squares([2, 4, 6]))  # 56 (4 + 16 + 36)
    print(sum_of_even_squares([]))  # 0 (пустой список)