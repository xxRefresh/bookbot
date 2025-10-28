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

main(get_book_text)
