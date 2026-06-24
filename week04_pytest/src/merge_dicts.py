
def merge_dicts(dicts: list[dict[str, int]]) -> dict[str, int]:
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result