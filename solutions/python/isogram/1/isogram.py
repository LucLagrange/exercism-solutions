def is_isogram(string):
    # Clean string: convert to lowercase and remove spaces and hyphens
    cleaned = string.lower().replace(" ", "").replace("-", "")
    # Compare length of string with length of its unique characters
    return len(cleaned) == len(set(cleaned))