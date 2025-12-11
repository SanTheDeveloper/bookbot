from stats import get_word_count, get_char_count, get_sorted_char_list


def get_book_text(path):
    # Use the with block to open and automatically close the file
    with open(path) as f:
        # Use .read() method to get the entire content as a single string
        return f.read()


def main():
    # Define the relative path to the book file
    file_path = "books/frankenstein.txt"

    # Get the file content
    file_contents = get_book_text(file_path)

    # Get the word count
    word_count = get_word_count(file_contents)

    # Get the character count dictionary
    char_count = get_char_count(file_contents)

    # Get the sorted list of character dictionaries
    sorted_list = get_sorted_char_list(char_count)

    # --- Print the Report ---

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Print the sorted character counts
    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")


# Call the main function to run the program
if __name__ == "__main__":
    main()
