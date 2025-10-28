from stats import count_words, count_characters

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

# def main(get_book_text):
#     book_path = "books/frankenstein.txt"
#     book_text = get_book_text(book_path)
#     print(book_text)



def main(get_book_text): 
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_words(book_text)
    char_counts = count_characters(book_text)
    print(char_counts)
    print_report(book_path, char_counts, num_words)


def print_report(book_path: str, char_counts: dict, num_words: int) -> None:
    """Prints a report of character counts.

    Args:
        char_counts (dict): A dictionary with characters as keys and their counts as values.
    """
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for char, count in sorted(char_counts.items()):
        print(f"'{char}': {count}")



main(get_book_text)
