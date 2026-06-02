from src.text_utils import is_palindrome, count_words, truncate_text


def test_is_palindrome():
    assert is_palindrome("level")
    assert is_palindrome("Noon ")
    assert not is_palindrome("race a car")
    assert is_palindrome("A man, a plan, a canal, Panama")
    assert is_palindrome("Madam, I'm Adam!")
    assert is_palindrome("")
    assert is_palindrome(" ")
    assert is_palindrome("12321")
    assert not is_palindrome("12345")
    assert is_palindrome("a")
    assert not is_palindrome("ab")
    assert is_palindrome("Aa")
    assert is_palindrome(".,!?")
    assert is_palindrome("123@321")


def test_count_words():
    assert count_words("Hello world! Hello everyone.") == {
        "hello": 2,
        "world": 1,
        "everyone": 1,
    }
    assert count_words("This is a test. This test is only a test.") == {
        "this": 2,
        "is": 2,
        "a": 2,
        "test": 3,
        "only": 1,
    }
    assert count_words("") == {}
    assert count_words("   ") == {}
    assert count_words("Word") == {"word": 1}
    assert count_words("Punctuation! Should be stripped? Yes.") == {
        "punctuation": 1,
        "should": 1,
        "be": 1,
        "stripped": 1,
        "yes": 1,
    }


def test_truncate_text():
    assert truncate_text("Hello, world!", 5) == "Hello"
    assert truncate_text("Short text", 20) == "Short text"
    assert truncate_text("Exact length", 12) == "Exact length"
    assert truncate_text("Negative length", -1) == ""
    assert truncate_text("Zero length", 0) == ""
    assert truncate_text("", 10) == ""
    assert truncate_text("   ", 2) == "  "
    assert truncate_text("Truncate me", 4) == "Trun"
    assert truncate_text("Truncate me", 10) == "Truncate m"
