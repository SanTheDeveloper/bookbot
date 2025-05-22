def get_num_words(text):
    return len(text.split())  # Returns the number of words

def count_characters(text):
    char_counts = {}  # Dictionary to store character counts
    for char in text.lower():  # Convert all characters to lowercase
        if char.isalpha():  # Check if it's a letter (a-z)
            if char in char_counts:
                char_counts[char] += 1  # Increment count if already in dict
            else:
                char_counts[char] = 1  # Initialize count if new
    return char_counts

def sort_characters(char_counts):
    sorted_list = [] # list to store character-count dictionaries
    for char in char_counts:
        # Create a new dictionary for this character with its count, and add it to list
        sorted_list.append({"char": char, "count": char_counts[char]})
    # Sort by count in descending order
    sorted_list.sort(reverse=True, key=lambda item: item["count"])
    return sorted_list
