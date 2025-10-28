def count_words(text: str) -> int:
    """Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    num_words = len(words)
    return print(f"Found {num_words} total words")
