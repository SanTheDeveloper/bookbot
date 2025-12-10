from stats import get_word_count  # New Import


def get_book_text(path):
    # Use the with block to open and automatically close the file
    with open(path) as f:
        # Use .read() method to get the entire content as a single string
        return f.read()


def main():
    # Define the relative path to the book file
    book_path = "books/frankenstein.txt"

    # Get the text content
    text = get_book_text(book_path)

    # Calculate the word count
    num_words = get_word_count(text)

    # Print the required output message
    print(f"Found {num_words} total words")


# Call the main function to run the program
main()
