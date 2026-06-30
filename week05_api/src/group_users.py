
def group_users_by_status(responses: list[dict]) -> dict[str, list[int]]:
    result = {}
    for response in responses:
        if response['status'] in result:
            result[response['status']].append(response['id'])
        else:
            result[response['status']] = [response['id']]
    return result

if __name__ == '__main__':
    responses = [
        {"id": 1, "status": "active", "name": "Igor"},
        {"id": 2, "status": "active", "name": "Anna"},
        {"id": 3, "status": "pending", "name": "Dmitry"},
        {"id": 4, "status": "inactive", "name": "Sasha"},
        {"id": 5, "status": "active", "name": "Maria"},
        {"id": 6, "status": "pending", "name": "Pavel"},
    ]

    print(group_users_by_status(responses))
    # {
    #   'active': [1, 2, 5],
    #   'pending': [3, 6],
    #   'inactive': [4]
    # }

    print(group_users_by_status([]))
    # {}

    print(group_users_by_status([{"id": 1, "status": "active"}]))
    # {'active': [1]}