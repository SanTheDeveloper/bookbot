def get_word_count(text):
    """
    Calculates the total number of words in the given text string.
    """
    # .split() without arguments splits the string into a list of words,
    # using any sequence of whitespace (spaces, tabs, newlines) as a delimiter.
    words = text.split()

    # The number of words is simply the number of elements in the resulting list.
    return len(words)


def get_char_count(text):
    """
    Counts the frequency of every character (including spaces and symbols)
    in the text. All characters are converted to lowercase to avoid duplicates
    (e.g., 'A' and 'a' are counted together).
    """
    # Initialize an empty dictionary to store character -> count mappings.
    counts = {}

    # Iterate through the text, processing one character at a time.
    for char in text:
        # Ensures case-insensitivity by treating 'A' and 'a' as the same key ('a').
        lowered_char = char.lower()

        # Efficiently update the count in the dictionary:
        # counts.get(key, default) retrieves the current count or returns
        # the 'default' value (0) if the key is not found (first time seeing the char).
        counts[lowered_char] = counts.get(lowered_char, 0) + 1

    return counts


# --- Helper Function for Sorting ---


def sort_on(d):
    """
    This is a 'key' function used by the .sort() method.
    It tells Python to sort the list of dictionaries based on the value
    associated with the 'num' key in each dictionary.
    """
    return d["num"]


def get_sorted_char_list(char_count_dict):
    """
    Converts a raw character count dictionary into a sorted list of dictionaries.
    It only includes characters that are part of the alphabet (a-z).
    """
    sorted_list = []

    # Iterate through the key-value pairs (character and its count) of the dictionary.
    for char, count in char_count_dict.items():
        # .isalpha() returns True if the string contains only alphabet characters (a-z, A-Z).
        # We skip spaces, punctuation, and other symbols by checking this.
        if not char.isalpha():
            continue

        # Create the required dictionary format: {"char": 'a', "num": 12345}
        sorted_list.append({"char": char, "num": count})

    # Sort the list:
    # 1. reverse=True: Sorts in descending order (highest count first).
    # 2. key=sort_on: Uses the sort_on function to extract the 'num' value for comparison.
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
