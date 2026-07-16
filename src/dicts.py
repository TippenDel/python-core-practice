def merge_dicts(left: dict, right: dict) -> dict:
    return left | right


def invert_dict(data: dict[str, str]) -> dict[str, str]:
    result = {}
    for key, value in data.items():
        result[value] = key
    return result


def group_by_age(users: list[dict]) -> dict[int, list[dict]]:

    result = {}
    for user in users:
        age = user.get("age")
        if age is not None:
            if age not in result:
                result[age] = []
            result[age].append(user)
    return result


def filter_by_age(users: list[dict], min_age: int) -> list[dict]:
    result = []
    for user in users:
        age = user.get("age")
        if age is not None and age >= min_age:
            result.append(user)
    return result


def count_by_status(items: list[dict]) -> dict[str, int]:
    result = {}
    for item in items:
        status = item.get("status")
        if status is not None:
            if status not in result:
                result[status] = 0
            result[status] += 1
    return result
