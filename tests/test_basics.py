import pytest

from src.basics import get_type_names, format_price, clean_text


def test_get_type_names() -> None:
    assert get_type_names(["a", 1, True, None]) == ["str", "int", "bool", "NoneType"]


def test_get_type_names_empty() -> None:
    assert get_type_names([]) == []


def test_get_type_names_none() -> None:
    assert get_type_names([None]) == ["NoneType"]


def test_format_price() -> None:
    assert format_price(12.3456) == "12.35"


def test_format_price_zero() -> None:
    assert format_price(0) == "0.00"


def test_format_price_negative() -> None:
    assert format_price(-5.678) == "-5.68"


def test_format_price_large() -> None:
    assert format_price(123456789.98765) == "123456789.99"


def test_format_price_small() -> None:
    assert format_price(0.0001) == "0.00"


def test_clean_text() -> None:
    assert clean_text("  Hello,   world!  ") == "hello, world!"


def test_clean_text_empty() -> None:
    assert clean_text("") == ""


def test_clean_text_whitespace() -> None:
    assert clean_text("     ") == ""


def test_clean_text_mixed_case() -> None:
    assert clean_text("  PyThOn  ") == "python"

    def test_clean_text_wrong_type() -> None:
        with pytest.raises(TypeError):
            clean_text(123)
