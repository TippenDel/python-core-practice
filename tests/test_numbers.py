import pytest

from src.numbers import (
    sum_numbers,
    average,
    max_number,
    get_even_numbers,
    normalize_scores,
)


def test_sum_numbers_basic() -> None:
    assert sum_numbers([1, 2, 3, 4, 5]) == 15


def test_sum_numbers_float() -> None:
    assert sum_numbers([1.5, 2.5, 3.0]) == 7.0


def test_sum_numbers_negative() -> None:
    assert sum_numbers([-1, -2, -3]) == -6


def test_sum_numbers_empty() -> None:
    assert sum_numbers([]) == 0


def test_sum_numbers_zero() -> None:
    assert sum_numbers([0]) == 0


def test_sum_numbers_mixed_types() -> None:
    assert sum_numbers([1, 2.5, 3]) == 6.5


def test_average_basic() -> None:
    assert average([10, 20, 30]) == 20.0


def test_average_float() -> None:
    assert average([1.5, 2.5, 3.0]) == 2.3333333333333335


def test_average_negative() -> None:
    assert average([-1, -2, -3]) == -2.0


def test_average_mixed_types() -> None:
    assert average([1, 2.5, 3]) == 2.1666666666666665


def test_average_empty() -> None:
    with pytest.raises(ValueError):
        average([])


def test_max_number_basic() -> None:
    assert max_number([3, 7, 1, 9, 4]) == 9


def test_max_number_negative() -> None:
    assert max_number([-1, -2, -3]) == -1


def test_max_number_mixed() -> None:
    assert max_number([1, -2, 3]) == 3


def test_max_number_single_element() -> None:
    assert max_number([17]) == 17


def test_max_number_empty() -> None:
    with pytest.raises(ValueError):
        max_number([])


def test_max_number_with_floats() -> None:
    assert max_number([1.5, 2.5, 3.0]) == 3.0


def test_max_number_with_mixed_types() -> None:
    assert max_number([1, 2.5, 3]) == 3


def test_get_even_numbers_basic() -> None:
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_even_numbers_empty() -> None:
    assert get_even_numbers([]) == []


def test_get_even_numbers_no_evens() -> None:
    assert get_even_numbers([1, 3, 5]) == []


def test_get_even_numbers_all_evens() -> None:
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]


def test_get_even_numbers_negative() -> None:
    assert get_even_numbers([-2, -3, -4, -5]) == [-2, -4]


def test_normalize_scores_basic() -> None:
    assert normalize_scores([50, 75, 100]) == [0.5, 0.75, 1.0]


def test_normalize_scores_empty() -> None:
    assert normalize_scores([]) == []


def test_normalize_scores_single_element() -> None:
    assert normalize_scores([50]) == [1.0]


def test_normalize_scores_zero_max() -> None:
    with pytest.raises(ValueError):
        normalize_scores([0, 0, 0])


def test_normalize_scores_negative() -> None:
    assert normalize_scores([-50, -25, -100]) == [2.0, 1.0, 4.0]


def test_normalize_scores_mixed() -> None:
    assert normalize_scores([-50, 0, 50]) == [-1.0, 0.0, 1.0]


def test_normalize_scores_with_floats() -> None:
    assert normalize_scores([0.5, 1.0, 1.5]) == [
        0.3333333333333333,
        0.6666666666666666,
        1.0,
    ]


def test_normalize_scores_all_same() -> None:
    assert normalize_scores([50, 50, 50]) == [1.0, 1.0, 1.0]
