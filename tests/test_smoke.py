from src.smoke import add


def test_add() -> None:
    assert add(2, 3) == 5


def test_add_negative() -> None:
    assert add(-1, -1) == -2


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_add_large_numbers() -> None:
    assert add(1000000, 2000000) == 3000000


def test_add_mixed() -> None:
    assert add(-5, 5) == 0


def test_add_floats() -> None:
    assert add(2.5, 3.5) == 6.0
