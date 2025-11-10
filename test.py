# full script to test outputs


def get_book_text(path_to_file: str) -> str:
    """Reads the content of a book from a text file.

    Args:
        path_to_file (str): The path to the text file containing the book.
    Returns:
        str: The content of the book as a string.
    """
    with open(path_to_file) as f:
        #f is a file object
        book_contents = f.read()
    return book_contents

def count_words(file_text: str) -> int:
    """Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    words = file_text.split()
    num_words = len(words)
    return num_words

print(count_words(get_book_text("books/frankenstein.txt")))

def count_characters(book_content: str) -> dict[str, int]:
    """Counts the number of characters in a given text.
    Args:
        text (str): The text to count characters in.
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_dict: dict[str, int] = {}

    for text in book_content.split():
        lower_text = text.lower()
        for char in lower_text:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
    return char_dict

print(count_characters(get_book_text("books/frankenstein.txt")))


def print_report(book_path: str, char_dict: dict, num_words: int) -> None:
    char = []

    for letter, num in char_dict.items():
        per_dict = {}
        per_dict["character"] = letter
        per_dict["num"] = num
        char.append(per_dict)

    # Sort the characters by their count
    
    char.sort(reverse=True, key=sort_on)

    for content in char:
        character = content["character"]
        value = content["num"]
        print(f"The {character} character was found {value} times")
        
    print("--- End report ---")

def sort_on(item: dict) -> int:
    return item["num"]

print_report("books/frankenstein.txt", count_characters(get_book_text("books/frankenstein.txt")), count_words(get_book_text("books/frankenstein.txt")))

def main(get_book_text): 
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    print_report(book_path, char_counts, num_words)


