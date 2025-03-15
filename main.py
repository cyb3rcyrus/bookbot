import sys
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
#takes in a filepath and then returns the contents of the text file as a string
from stats import num_words
from stats import num_letters
from stats import dictionary
def main():
    try:
        print(f"Found {num_words(get_book_text(sys.argv[1]))} total words")
        dictionary(num_letters(get_book_text(sys.argv[1])))
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
