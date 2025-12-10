def get_word_count(text):
    # .split() splits the string into a list of words based on whitespace
    words = text.split()
    # The number of words is the length of the list
    return len(words)


def get_char_count(text):
    """
    Counts the number of times each character (including symbols and spaces)
    appears in the text, converting all characters to lowercase.
    """
    counts = {}

    # Iterate through the text, character by character
    for char in text:
        # Convert the character to lowercase
        lowered_char = char.lower()

        # Update the count in the dictionary
        # Use .get() to handle new characters easily: if the key doesn't exist,
        # it defaults to 0 before we add 1.
        counts[lowered_char] = counts.get(lowered_char, 0) + 1

    return counts
