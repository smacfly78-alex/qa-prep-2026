from typing import Iterator
from unittest import result


def enumerate_words(text: str) -> Iterator[tuple[int, str]]:
    items = text.split()
    for index in range(len(items)):
        yield (index, items[index])

if __name__ == '__main__':
    for index, word in enumerate_words("hello world python"):
        print(f"{index}: {word}")
    # 0: hello
    # 1: world
    # 2: python

    print(list(enumerate_words("one two")))
    # [(0, 'one'), (1, 'two')]

    print(list(enumerate_words("")))
    # []