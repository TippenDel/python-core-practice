def flatten(items: list) -> list:
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


def unique_preserve_order(items: list) -> list:
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


def chunk_list(items: list, chunk_size: int) -> list[list]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    result = []

    for i in range(0, len(items), chunk_size):
        result.append(items[i : i + chunk_size])

    return result
