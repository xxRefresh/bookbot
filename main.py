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

def main(get_book_text): 
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_words(book_text)

main(get_book_text)
