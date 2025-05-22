import sys  # Import sys module for command-line arguments
from stats import get_num_words, count_characters, sort_characters

def get_book_text(filepath):
    """Reads and returns the text content from a file."""
    with open(filepath) as f:
        return f.read()

def main():
    # Check if correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1 for incorrect usage

    # Get the book path from command-line arguments
    book_path = sys.argv[1]

    try:
        # Read and analyze the book
        text = get_book_text(book_path)
        word_count = get_num_words(text)
        char_counts = count_characters(text)
        sorted_chars = sort_characters(char_counts)

        # Print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['count']}")
        print("============= END ===============")

    except FileNotFoundError:
        print(f"Error: File not found at path '{book_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
