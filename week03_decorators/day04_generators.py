from typing import Generator, Iterator


def countdown(n: int) -> Generator[int, None, None]:
    for current_value in range(n, 0, -1):
        yield current_value


def read_csv_lines(csv_text:str) -> Iterator[dict[str, str]]:
    lines  = csv_text.strip().split("\n")
    headers = lines[0].split(",")
    data_lines = lines[1:]

    for line in data_lines:
        values = line.split(",")
        row = dict(zip(headers, values))
        yield row

if __name__ == "__main__":
    # Через for
    for num in countdown(5):
        print(num)
    # 5
    # 4
    # 3
    # 2
    # 1

    # Через next()
    gen = countdown(3)
    print(next(gen))  # 3
    print(next(gen))  # 2
    print(next(gen))  # 1
    # print(next(gen)) # StopIteration!