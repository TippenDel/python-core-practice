def merge_dicts(left: dict, right: dict) -> dict:

    merged = left.copy()
    merged.update(right)

    return merged


def invert_dict(data: dict[str, str]) -> dict[str, str]:
    inverted = {}
    for key, value in data.items():
        inverted[value] = key
    return inverted


def group_by_age(users: list[dict]) -> dict[int, list[dict]]:
    grouped = {}

    for user in users:
        age = user.get("age")

        if age is None:
            continue

        if age not in grouped:
            grouped[age] = []

        grouped[age].append(user)

    return grouped


def filter_by_age(users: list[dict], min_age: int) -> list[dict]:
    filtered = []

    for user in users:
        age = user.get("age")

        if age is not None and age >= min_age:
            filtered.append(user)

    return filtered


def count_by_status(items: list[dict]) -> dict[str, int]:
    counts = {}

    for item in items:
        status = item.get("status")

        if status is None:
            continue

        if status not in counts:
            counts[status] = 0

        counts[status] += 1

    return counts


print(
    count_by_status(
        [
            {"title": "Task 1", "status": "done"},
            {"title": "Task 2", "status": "pending"},
            {"title": "Task 3", "status": "done"},
            {"title": "Task 4"},
        ]
    )
)

"""
def merge_dicts(left: dict, right: dict) -> dict:
    merged = {}

    for key, value in left.items():
        merged[key] = value

    for key, value in right.items():
        merged[key] = value

    return merged  


def merge_dicts(left: dict, right: dict) -> dict:
    return left | right


def merge_dicts(left: dict, right: dict) -> dict:
    return {**left, **right}     

    
def invert_dict(data: dict[str, str]) -> dict[str, str]:
    return {value: key for key, value in data.items()}
"""
