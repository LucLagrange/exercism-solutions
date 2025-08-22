

def encode(plain_text):

    alphabet_dict = {
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
        'n': 'm',
        'o': 'l',
        'p': 'k',
        'q': 'j',
        'r': 'i',
        's': 'h',
        't': 'g',
        'u': 'f',
        'v': 'e',
        'w': 'd',
        'x': 'c',
        'y': 'b',
        'z': 'a',
    }

    # Encode in groups of 5 letters
    # Ignore spaces
    # Keep numbers as is



    new_characters = []

    for character in plain_text:
        if character.lower() in alphabet_dict:
            new_character = alphabet_dict[character.lower()]
            new_characters.append(new_character)
        elif character.isdigit():
            new_characters.append(character)

    new_string = ''.join(new_characters)
    new_string_sliced = ' '.join(new_string[i:i+5] for i in range(0, len(new_string), 5))

    print(new_string_sliced)
    return new_string_sliced

def decode(ciphered_text):

    alphabet_dict = {
        'a': 'z',
        'b': 'y',
        'c': 'x',
        'd': 'w',
        'e': 'v',
        'f': 'u',
        'g': 't',
        'h': 's',
        'i': 'r',
        'j': 'q',
        'k': 'p',
        'l': 'o',
        'm': 'n',
        'n': 'm',
        'o': 'l',
        'p': 'k',
        'q': 'j',
        'r': 'i',
        's': 'h',
        't': 'g',
        'u': 'f',
        'v': 'e',
        'w': 'd',
        'x': 'c',
        'y': 'b',
        'z': 'a',
    }

    inverted_alphabet_dict = {v: k for k, v in alphabet_dict.items()}

    original_characters = []

    for character in ciphered_text:
        if character in inverted_alphabet_dict:
            original_characters.append(inverted_alphabet_dict[character.lower()])
        elif character.isdigit():
            original_characters.append(character)

    original_string = ''.join(original_characters)

    print(original_string)
    return original_string
