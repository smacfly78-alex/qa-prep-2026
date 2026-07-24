def analyze_users(users: list[dict]) -> dict:
    if not users:
        return {
            "total": 0,
            "avg_age": 0,
            "by_role": {},
            "oldest": None
        }

    result = {}
    result['total'] = len(users)
    result['avg_age'] = sum(user['age'] for user in users) / len(users)
    oldest_user = max(users, key=lambda user: user['age'])
    result['oldest'] = oldest_user['name']
    by_role = {}
    for user in users:
        role = user["role"]
        by_role[role] = by_role.get(role, 0) + 1
    result['by_role'] = by_role
    return result

if __name__ == '__main__':
    users = [
        {"name": "Igor", "age": 30, "role": "admin"},
        {"name": "Anna", "age": 25, "role": "user"},
        {"name": "Petr", "age": 35, "role": "user"},
        {"name": "Maria", "age": 28, "role": "admin"},
    ]

    result = analyze_users(users)
    print(result)
    # {
    #   "total": 4,
    #   "avg_age": 29.5,
    #   "by_role": {"admin": 2, "user": 2},
    #   "oldest": "Petr"
    # }


