import pytest

from src.basics import get_type_names, format_price, clean_text


def test_get_type_names():
    assert get_type_names(["a", 1, 2.5, True, None]) == [
        "str",
        "int",
        "float",
        "bool",
        "NoneType",
    ]


def test_get_type_names_empty():
    assert get_type_names([]) == []


def test_get_type_names_string():
    assert get_type_names(["a", "b", "c"]) == ["str", "str", "str"]


def test_get_type_names_bools():
    assert get_type_names([True, False]) == ["bool", "bool"]


def test_format_price():
    assert format_price(3.14159) == "3.14"


def test_format_price_empty():
    assert format_price(0.0) == "0.00"


def test_format_price_negative():
    assert format_price(-5.678) == "-5.68"


def test_format_price_large():
    assert format_price(123456.789) == "123456.79"


def test_format_price_small():
    assert format_price(0.0001) == "0.00"


def test_format_price_exact():
    assert format_price(2.5) == "2.50"


def test_format_price_string():
    with pytest.raises(ValueError):
        format_price("not a number")


def test_clean_text():
    assert clean_text("  Hello World!  ") == "hello world!"


def test_clean_text_empty():
    assert clean_text("   ") == ""


def test_clean_text_no_whitespace():
    assert clean_text("Hello") == "hello"


def test_clean_text_mixed_case():
    assert clean_text("PyThOn") == "python"


def test_clean_text_extra_spaces():
    assert clean_text("  Hello   World  ") == "hello world"
