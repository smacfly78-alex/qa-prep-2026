
items = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]

new_items = [item for item in items if item % 2 == 0]
print(new_items)


phrase = "hello world"

new_phrase = set(phrase.replace(" ", ""))
print(new_phrase)

cort = (1, 2, 3)

try:
    cort[0] = 5
except TypeError as e:
    print(f'{e} - некорректный тип')


def bytearray_demo() -> None:
    b_ar = bytearray("QA Test", "utf-8")

    b_ar[0] = ord('B')

    result = b_ar.decode("utf-8")
    print(result)


