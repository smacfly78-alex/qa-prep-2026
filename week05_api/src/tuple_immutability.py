
def demonstrate_tuple_immutability() -> None:
    my_tuple = (1, "hello", [5, 1, 4])

    print(f"First: {my_tuple[0]}")
    print(f"Second: {my_tuple[1]}")
    print(f"Third: {my_tuple[2]}")

    try:
        my_tuple[0] = 5
    except TypeError as e:
        print(f"Cannot modify tuple: {e}")


if __name__ == '__main__':
    demonstrate_tuple_immutability()