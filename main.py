import sys  # Essential for accessing system-specific parameters and functions, including command-line arguments.
from stats import get_word_count, get_char_count, get_sorted_char_list


def get_book_text(file_path):
    """
    Reads the content of the file at the given path and returns it as a string.
    """
    # The 'with open(...)' structure (context manager) is best practice.
    # It ensures the file is automatically closed, even if errors occur.
    with open(file_path) as f:
        # The .read() method pulls the entire file content into a single string.
        return f.read()


def main():
    # --- Command-Line Argument Handling ---

    # sys.argv is a list of strings passed on the command line.
    # sys.argv[0] is the script name ('main.py').
    # We expect sys.argv[1] to be the book path, so the list length should be 2.
    if len(sys.argv) != 2:
        # If the user didn't provide a path, print a helpful message.
        print("Usage: python3 main.py <path_to_book>")
        # sys.exit(1) exits the program immediately and returns a status code of 1.
        # Status code 1 conventionally signals an error/failure.
        sys.exit(1)

    # If validation passes, the file path is the second element in the list.
    file_path = sys.argv[1]

    # --- Main Logic with Error Handling ---

    # The try...except block catches potential issues during file operations.
    try:
        # 1. Get the file content
        file_contents = get_book_text(file_path)

        # 2. Process the data using functions from stats.py
        word_count = get_word_count(file_contents)

        # char_count is a dictionary like {'a': 1000, 'b': 500, ...}
        char_count = get_char_count(file_contents)

        # sorted_list is a list of dictionaries like [{'char': 'e', 'num': 44538}, ...]
        sorted_list = get_sorted_char_list(char_count)

        # --- Print the Final Report (UI/Output) ---

        print("============ BOOKBOT ============")
        # Use an f-string for easy insertion of variables into the output.
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        # Iterate through the pre-sorted list and print each character's count.
        for item in sorted_list:
            char = item["char"]
            count = item["num"]
            print(f"{char}: {count}")

        print("============= END ===============")

    # Catch a specific error if the file path is valid but the file doesn't exist.
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    # Catch any other unexpected errors during execution (e.g., permission issues).
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


# This standard Python construct ensures 'main()' only runs when the script
# is executed directly (not when it is imported as a module by another script).
if __name__ == "__main__":
    main()
