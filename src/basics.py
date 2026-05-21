def get_type_names(values: list[object]) -> list[str]:
    return [type(value).__name__ for value in values]


def format_price(value: float) -> str:
    return f"{value:.2f}"


def clean_text(text: str) -> str:
    words = text.strip().split()
    return " ".join(words).lower()
