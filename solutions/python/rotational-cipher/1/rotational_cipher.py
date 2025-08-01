def rotate(text, key):

    words = []

    alphabet_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    reverse_dict = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }

    for letter in text:
        if letter.lower() in alphabet_dict:
            print(f"Index before rotation: {alphabet_dict[letter.lower()]}")
            index = alphabet_dict[letter.lower()] + key

            if index > 26:
                index = index - 26

            print(f"Index after rotation: {index}")

            if letter.isupper():
                words.append(reverse_dict[index].upper())
            else:
                words.append(reverse_dict[index])
                print(reverse_dict[index])
        else:
            words.append(letter)
    
    
        word = ''.join(words)

    print(word)
    return word