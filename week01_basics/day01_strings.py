
def split_full_name(full_name):
    split_name = tuple(full_name.split())
    return split_name

split_name = split_full_name("Иван Петров Сергеевич")
print(split_name)

def make_initials(first, last):
    a = first[0]+'.'
    full = f'{a} {last}'
    return full

print(make_initials('Иван', 'Петров'))

gl = 'уеыаоэяиюeuioaqwy'
def count_vowels(text):
    count = 0
    string = text.lower()
    for chat in string:
        if chat in gl:
            count += 1
    return count

print(count_vowels('Доброго вечера my little friends'))


def reverse_words(sentence):
    a = sentence.split()
    a.reverse()
    return ' '.join(a)

print(reverse_words('Доброго вечера друзья'))

def is_palindrome(text):
    a = (text.replace(" ", "")).lower()
    b = a[::-1]
    if a == b:
        return True

print(is_palindrome('А роза упала на лапу Азора'))