def get_word_count(text):
    # .split() splits the string into a list of words based on whitespace
    words = text.split()
    # The number of words is the length of the list
    return len(words)
