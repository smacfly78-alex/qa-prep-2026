
def greet(name: str, greeting: str = "Hello") -> str:
    return f'{greeting} {name}!'

def create_user(name: str, age: int, city: str = "Москва", is_active: bool = True) -> dict:
    return {'name': name, 'age': age, 'city': city, 'is_active': is_active}

def sum_all(*numbers: int) -> int:
    total = 0
    for n in numbers:
        total += n
    return total

def describe(**fields) -> str:
    lines = []
    for key, value in fields.items():
        line = f'{key}={value}'
        lines.append(line)
    return ", ".join(lines)

def safe_append(item: object, target: list | None = None) -> list:
    if target is None:
        target = []
    target.append(item)
    return target

if __name__ == '__main__':
    print(greet('Игорь'))
    print(greet('Игорь', 'Привет'))
    print(sum_all(1, 2, 3))
    print(safe_append('яблоко'))
    print(safe_append('яблоко', ['груша', 'дыня']))