from stats import *
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    """
    Main function to execute the script.
    
    Returns:
        None
    """
    # Check if the command was input correctly
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Define the path to the book file
    path = sys.argv[1]

    # Get the content of the book
    file_contents = get_book_text(path)

    # Count the number of words, and instances of characters, in the book
    num_words = count_words(file_contents)

    num_chars = count_chars(file_contents)

    # Sort the counted characters from most to least
    ordered_chars = sorted_chars(num_chars)

    # Remove non-letters
    alpha_cars = []
    for a in ordered_chars:
        if a["char"].isalpha():
            alpha_cars.append(a)
    
    # Print a report on the number of characters in the text
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")  
    for r in alpha_cars:
        print(f"{r["char"]}: {r["num"]}")
    print("============= END ===============")

main()
