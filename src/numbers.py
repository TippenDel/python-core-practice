def sum_numbers(numbers: list[int | float]) -> int | float:
    total = 0
    for number in numbers:
        total += number
    return total


def average(numbers: list[int | float]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum_numbers(numbers) / len(numbers)


def max_number(numbers: list[int | float]) -> int | float:
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    max_val = numbers[0]
    for number in numbers:
        if number > max_val:
            max_val = number
    return max_val


def get_even_numbers(numbers: list[int]) -> list[int]:
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def normalize_scores(scores: list[int | float]) -> list[float]:
    if not scores:
        return []
    max_score = max_number(scores)
    if max_score == 0:
        raise ValueError("Cannot normalize scores when the maximum score is zero.")
    normalized_scores = []
    for score in scores:
        normalized_scores.append(score / max_score)
    return normalized_scores


if __name__ == "__main__":
    print(sum_numbers([1, 2, 3, 4, 5]))
    print(average([10, 20, 30]))
    print(max_number([3, 7, 1, 9, 4]))
    print(get_even_numbers([1, 2, 3, 4, 5, 6]))
    print(normalize_scores([50, 75, 100]))
