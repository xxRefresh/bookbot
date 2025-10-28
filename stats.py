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

def count_characters(text: str) -> int:
    ## counts the number of times each character appears in a string including symbols and spaces. converts all characters to lowercase to ensure case insensitivity. use as dictionary to store counts.

    """Counts the number of characters in a given text.
    Args:
        text (str): The text to count characters in.
    Returns:
        int: The number of characters in the text.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

