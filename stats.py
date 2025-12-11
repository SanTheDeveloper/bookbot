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


# --- New Code for Sorting ---


def sort_on(d):
    """
    Helper function to return the value of the "num" key for sorting.
    """
    return d["num"]


def get_sorted_char_list(char_count_dict):
    """
    Takes a dictionary of character counts, filters for alphabetical characters,
    converts to a list of dictionaries, and sorts them by count.
    """
    sorted_list = []

    # Iterate through the character count dictionary
    for char, count in char_count_dict.items():
        # Skip the character if it is NOT an alphabetical character
        if not char.isalpha():
            continue

        # Create the required dictionary structure and append it to the list
        sorted_list.append({"char": char, "num": count})

    # Sort the list: reverse=True for descending order, key=sort_on for sorting by "num"
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
