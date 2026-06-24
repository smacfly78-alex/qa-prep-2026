
def count_words_by_length(text: str) -> dict[int, int]:
    result = {}
    for item in text.split():
        if len(item) in result:
            result[len(item)] += 1
        else:
            result[len(item)] = 1
    return result

if __name__ == '__main__':
    text = "hi hello ok world fox by"

    print(count_words_by_length(text))
    # {2: 3, 5: 2, 3: 1}
    # длина 2: "hi", "ok", "by" — 3 слова
    # длина 5: "hello", "world" — 2 слова
    # длина 3: "fox" — 1 слово

    print(count_words_by_length(""))
    # {}