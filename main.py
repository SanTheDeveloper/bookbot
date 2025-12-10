from stats import get_word_count, get_char_count


def get_book_text(path):
    # Use the with block to open and automatically close the file
    with open(path) as f:
        # Use .read() method to get the entire content as a single string
        return f.read()


def main():
    # Define the relative path to the book file
    book_path = "books/frankenstein.txt"

    # Get the file content
    file_contents = get_book_text(book_path)

    # Get the word count
    word_count = get_word_count(file_contents)

    # Print the word count
    print(f"The book has {word_count} words.")

    # Get the character count dictionary
    char_count = get_char_count(file_contents)

    # Print the character count dictionary
    print(char_count)


# Call the main function to run the program
if __name__ == "__main__":
    main()
