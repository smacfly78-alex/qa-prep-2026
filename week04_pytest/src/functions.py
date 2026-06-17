from curses.ascii import isalpha
from typing import Iterator


def word_frequency(line: str) -> dict[str, int]:
    result = {}
    items = line.lower().split()
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def countdown(n: int) -> Iterator[int]:
    for current_value in range(n, 0, -1):
        yield current_value


def calculate_score(correct: int, total: int) -> float:
    if total <= 0:
        raise ValueError("Total must be positive")
    if correct < 0:
        raise ValueError("Correct count cannot be negative")
    if correct > total:
        raise ValueError("Correct cannot exceed total")
    return (correct / total) * 100

def is_palindrome(text: str) -> bool:
    line = text.lower()
    items = []
    for char in line:
        if char.isalpha():
            items.append(char)
    clear_line = ''.join(items)
    reverse_clear_line = clear_line[::-1]
    return clear_line == reverse_clear_line