import pytest

from src.calculator import calculate


def test_calculate_basic():
    assert calculate(5, 3, "add") == 8
    assert calculate(5, 3, "subtract") == 2
    assert calculate(5, 3, "multiply") == 15
    assert calculate(6, 2, "divide") == 3


def test_calculate_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        calculate(5, 0, "divide")


def test_calculate_unknown_operation():
    with pytest.raises(
        ValueError,
        match="Invalid operation 'mod'. Supported operations are: add, subtract, multiply, divide.",
    ):
        calculate(5, 3, "mod")


def test_calculate_negative_numbers():
    assert calculate(-5, -3, "add") == -8
    assert calculate(-5, -3, "subtract") == -2
    assert calculate(-5, -3, "multiply") == 15
    assert calculate(-6, -2, "divide") == 3


def test_calculate_floats():
    assert calculate(5.5, 2.2, "add") == pytest.approx(7.7)
    assert calculate(5.5, 2.2, "subtract") == pytest.approx(3.3)
    assert calculate(5.5, 2.2, "multiply") == pytest.approx(12.1)
    assert calculate(5.5, 2.2, "divide") == pytest.approx(2.5)
