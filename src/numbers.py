def sum_numbers(numbers: list[int | float]) -> int | float:

    total = 0

    for number in numbers:
        total += number

    return total


def average(numbers: list[int | float]) -> float:

    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    total = 0.0

    for number in numbers:
        total += number

    return total / len(numbers)


def max_number(numbers: list[int | float]) -> int | float:

    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    max_num = numbers[0]

    for number in numbers:
        if number > max_num:
            max_num = number

    return max_num


def get_even_numbers(numbers: list[int]) -> list[int]:

    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


def normalize_scores(scores: list[float]) -> list[float]:

    if not scores:
        return []

    max_score = max_number(scores)

    if max_score == 0:
        return [0.0 for _ in scores]

    normalized = []

    for score in scores:
        normalized.append(score / max_score)

    return normalized
