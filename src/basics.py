def get_type_names(values: list[object]) -> list[str]:

    return [type(value).__name__ for value in values]


def format_price(value: float) -> str:

    return f"{value:.2f}"


def clean_text(text: str) -> str:

    return " ".join(text.split()).lower()


if __name__ == "__main__":
    print(get_type_names(["a", 1, True, None]))
    print(format_price(12.3456))
    print(clean_text("  Hello,   world!  "))
