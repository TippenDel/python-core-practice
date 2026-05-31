from src.calculator import calculate


def test_calculate():
    assert calculate(2, 3, "add") == 5
    assert calculate(2, 3, "subtract") == -1
    assert calculate(2, 3, "multiply") == 6
    assert calculate(6, 3, "divide") == 2


def test_calculate_division_by_zero():
    try:
        calculate(2, 0, "divide")
    except ZeroDivisionError as e:
        assert str(e) == "Division by zero is impossible"


def test_calculate_unknown_operation():
    try:
        calculate(2, 3, "addtt")
    except ValueError as e:
        assert str(e) == "Invalid operation: addtt"


def test_calculate_negative_operation():
    assert calculate(-2, -3, "add") == -5
    assert calculate(-2, -3, "subtract") == 1
    assert calculate(-2, -3, "multiply") == 6
    assert calculate(-6, -3, "divide") == 2


def test_calculate_float_numbers():
    assert calculate(2.5, 3.5, "add") == 6.0
    assert calculate(2.5, 3.5, "subtract") == -1.0
    assert calculate(2.5, 3.5, "multiply") == 8.75
    assert calculate(7.0, 3.5, "divide") == 2.0
