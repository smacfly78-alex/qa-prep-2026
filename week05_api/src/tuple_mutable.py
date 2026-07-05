
def demonstrate_tuple_with_mutable() -> None:
    my_tuple = (1, "hello", [3, 4, 5])

    try:
        my_tuple[0] = 100
    except TypeError as e:
        print(f'{e}')
    print(my_tuple)

    my_tuple[2].append(6)
    print(my_tuple)

    try:
        hash(my_tuple)
    except TypeError as e:
        print(f'{e}')
    print(my_tuple)

if __name__ == '__main__':
    demonstrate_tuple_with_mutable()
