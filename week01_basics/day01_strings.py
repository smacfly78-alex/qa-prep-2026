
def split_full_name(full_name: str) -> tuple[str, ...]:
    return tuple(full_name.split())

def make_initials(first: str, last: str) -> str:
    return f'{first[0]}. {last}'

def count_vowels(text:str) -> int:
    VOWELS = 'aeiouуеыаоэяиюё'
    return sum(1 for char in text.lower() if char in VOWELS)

def reverse_words(sentence: str) -> str:
    return ' '.join(sentence.split()[::-1])

def is_palindrome(text:str) -> bool:
    phrase = text.lower().replace(" ", "")
    return phrase == phrase[::-1]


if __name__ == '__main__':
    print(split_full_name("Иван Петров Сергеевич"))
    print(make_initials("Иван", "Петров"))
    print(count_vowels("Доброго вечера my little friends"))
    print(reverse_words('hello world python'))
    print(is_palindrome('А роза упала на лапу Азора'))