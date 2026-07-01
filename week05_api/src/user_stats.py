
def merge_user_stats(previous: dict, updates: list[dict]) -> dict:
    result = previous.copy()
    for update in updates:
        user_id = update['user_id']
        delta = update['delta']
        if user_id in result:
            result[user_id] += delta
        else:
            result[user_id] = delta
    return result

if __name__ == '__main__':
    previous = {1: 100, 2: 250, 3: 50}
    updates = [
        {"user_id": 1, "delta": 50},
        {"user_id": 2, "delta": -30},
        {"user_id": 4, "delta": 200},
        {"user_id": 1, "delta": 20},
    ]

    result = merge_user_stats(previous, updates)
    print(result)
    # {1: 170, 2: 220, 3: 50, 4: 200}

    # Важно: previous не изменился
    print(previous)
    # {1: 100, 2: 250, 3: 50}