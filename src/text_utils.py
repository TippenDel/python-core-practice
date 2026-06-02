def is_palindrome(text: str) -> bool:
    cleaned_text = ""

    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()

    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[-(i + 1)]:
            return False

    return True


def count_words(text: str) -> dict[str, int]:
    counts = {}

    for word in text.lower().split():
        word = word.strip(".,!?\"'()[]{}:;")

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def truncate_text(text: str, max_length: int) -> str:
    if max_length <= 0:
        return ""

    if len(text) <= max_length:
        return text

    return text[:max_length]
