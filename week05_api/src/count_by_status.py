
def count_by_status(responses: list[dict]) -> dict[int, int]:
    result = {}
    for response in responses:
        if response['status'] in result:
            result[response['status']] += 1
        else:
            result[response['status']] = 1
    return result

if __name__ == '__main__':
    responses = [
        {"status": 200, "data": "ok"},
        {"status": 200, "data": "ok"},
        {"status": 404, "error": "not found"},
        {"status": 500, "error": "server error"},
        {"status": 200, "data": "ok"},
        {"status": 404, "error": "not found"},
    ]

    print(count_by_status(responses))
    # {200: 3, 404: 2, 500: 1}

    print(count_by_status([]))
    # {}

    print(count_by_status([{"status": 200, "data": "ok"}]))
    # {200: 1}