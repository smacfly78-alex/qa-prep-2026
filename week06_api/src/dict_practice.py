from unittest import result


def average_age(users: dict[str, int]) -> float:
    ages = 0
    names = 0
    if users == {}:
        raise ValueError("Cannot calculate average of empty dict")
    for key in users:
        ages += users[key]
        names += 1
    return round(ages/names, 2)

def analyze_users(users: dict[str, dict]) -> dict:
    result = {}
    result['all_emails'] = list(users.keys())
    result['all_names'] = []
    for user in users.values():
        result['all_names'].append(user["name"])
    result['total_orders'] = sum(user["orders"] for user in users.values())
    result['top_customer_email'] = max(
        users.items(),
        key=lambda item: item[1]["orders"]
    )[0]
    return result






if __name__ == '__main__':
    users = {
        "Igor": 30,
        "Anna": 25,
        "Bob": 40
    }

    print(average_age(users))  # 31.67

    # Один пользователь
    print(average_age({"Igor": 30}))  # 30.0

    # Пустой словарь
    try:
        average_age({})
    except ValueError as e:
        print(f"Error: {e}")
    # Error: Cannot calculate average of empty dict