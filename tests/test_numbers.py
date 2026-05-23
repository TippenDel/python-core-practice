import pytest

from src.numbers import (
    sum_numbers,
    average,
    max_number,
    get_even_numbers,
    normalize_scores,
)


def test_sum_numbers_integers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15


def test_sum_numbers_floats():
    assert sum_numbers([1.5, 2.5, 3.0]) == 7.0


def test_sum_numbers_mixed():
    assert sum_numbers([1, 2.5, 3]) == 6.5


def test_sum_numbers_empty():
    assert sum_numbers([]) == 0


def test_sum_numbers_negative():
    assert sum_numbers([-1, -2, -3]) == -6


def test_sum_numbers_single():
    assert sum_numbers([42]) == 42


def test_sum_numbers_non_numeric():
    with pytest.raises(TypeError):
        sum_numbers([1, "two", 3])


def test_sum_numbers_none():
    with pytest.raises(TypeError):
        sum_numbers([1, None, 3])


def test_average_integers():
    assert average([1, 2, 3, 4, 5]) == 3.0


def test_average_floats():
    assert average([1.5, 2.5, 3.0]) == pytest.approx(2.3333333333333335)


def test_average_mixed():
    assert average([1, 2.5, 3]) == pytest.approx(2.1666666666666665)


def test_average_empty():
    with pytest.raises(ValueError):
        average([])


def test_average_negative():
    assert average([-1, -2, -3]) == -2.0


def test_average_single():
    assert average([42]) == 42.0


def test_average_non_numeric():
    with pytest.raises(TypeError):
        average([1, "two", 3])


def test_average_none():
    with pytest.raises(TypeError):
        average([1, None, 3])


def test_max_number_integers():
    assert max_number([1, 2, 5, 4, 3]) == 5


def test_max_number_floats():
    assert max_number([1.5, 2.5, 3.0]) == 3.0


def test_max_number_mixed():
    assert max_number([1, 5.5, 3]) == 5.5


def test_max_number_empty():
    with pytest.raises(ValueError):
        max_number([])


def test_max_number_negative():
    assert max_number([-1, -2, -3]) == -1


def test_max_number_single():
    assert max_number([42]) == 42


def test_max_number_non_numeric():
    with pytest.raises(TypeError):
        max_number([1, "two", 3])


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_even_numbers_empty():
    assert get_even_numbers([]) == []


def test_get_even_numbers_no_evens():
    assert get_even_numbers([1, 3, 5]) == []


def test_get_even_numbers_all_evens():
    assert get_even_numbers([2, 4, 6]) == [2, 4, 6]


def test_get_even_numbers_negative():
    assert get_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]


def test_get_even_numbers_zero():
    assert get_even_numbers([0]) == [0]


def test_normalize_scores():
    assert normalize_scores([50, 75, 100]) == [0.5, 0.75, 1.0]


def test_normalize_scores_empty():
    assert normalize_scores([]) == []


def test_normalize_scores_all_zero():
    assert normalize_scores([0, 0, 0]) == [0.0, 0.0, 0.0]


def test_normalize_scores_mixed():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]


def test_normalize_scores_non_numeric():
    with pytest.raises(TypeError):
        normalize_scores([50, "seventy-five", 100])


def test_normalize_scores_negative():
    assert normalize_scores([-50, 0, 50]) == [-1.0, 0.0, 1.0]


def test_normalize_scores_floats():
    assert normalize_scores([0.5, 1.0, 1.5]) == pytest.approx(
        [0.3333333333333333, 0.6666666666666666, 1.0]
    )
