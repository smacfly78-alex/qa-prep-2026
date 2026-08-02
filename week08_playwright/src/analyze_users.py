
def analyze_users(users: list[dict]) -> dict:
    result = {
        "total_users": 0,
        "active_users": 0,
        "unique_roles": set(),
        "by_role": {},
    }

    result['total_users'] = len(users)
    for user in users:
        if user['is_active'] == True:
            result['active_users'] += 1
        if user['role'] not in result['unique_roles']:
            result['unique_roles'].add(user['role'])
        if user['role'] in result['by_role']:
            result['by_role'][user['role']] += 1
        else:
            result['by_role'][user['role']] = 1
    return result


if __name__ == '__main__':
    users = [
        {"name": "Igor", "role": "admin", "is_active": True},
        {"name": "Anna", "role": "user", "is_active": True},
        {"name": "Sam", "role": "user", "is_active": False},
        {"name": "Kate", "role": "admin", "is_active": True},
        {"name": "John", "role": "guest", "is_active": False},
    ]

    result = analyze_users(users)
    print(result["total_users"])  # 5
    print(result["active_users"])  # 3
    print(result["unique_roles"])  # {'admin', 'user', 'guest'}
    print(result["by_role"])  # {'admin': 2, 'user': 2, 'guest': 1}

    # Пустой список — краевой случай
    empty_result = analyze_users([])
    print(empty_result)
    # {'total_users': 0, 'active_users': 0, 'unique_roles': set(), 'by_role': {}}