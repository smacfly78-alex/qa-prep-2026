from typing import Generator


def read_lines(text) -> Generator[str, None, None]:
    items = []
    for item in text.split('\n'):
        items.append(item.strip())
    for item in items:
        if item != '':
            yield item


if __name__ == '__main__':
    text = """Line 1
    Line 2

    Line 3

    Line 4"""

    for line in read_lines(text):
        print(line)
    # Line 1
    # Line 2
    # Line 3
    # Line 4

    print(list(read_lines("hello\nworld")))
    # ['hello', 'world']

    print(list(read_lines("")))
    # []

    print(list(read_lines("   \n\n   ")))
    # []  (только пустые строки — пропускаются)