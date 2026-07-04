
def unique_chars(text: str) -> set[str]:
    return set(text.replace(" ", ""))

if __name__ == '__main__':
    print(unique_chars("hello world"))
    # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

    print(unique_chars("qa test"))
    # {'q', 'a', 't', 'e', 's'}

    print(unique_chars(""))
    # set()

    print(unique_chars("   "))
    # set()  ← только пробелы, всё убирается


schema = {
    "type": "object",
    "properties": {
        "user_id": {"type": "integer"},
        "email" : {"type": "string"},
        "is_active": {"type": "boolean"}
    },
    "required": ["user_id", "email", 'is_active']
}