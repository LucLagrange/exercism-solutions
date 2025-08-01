def is_pangram(sentence):
    alphabet_list = [chr(i) for i in range(97, 123)]
    characters = [char.lower() for char in sentence if char.isalpha()]
    
    alphabet_set = set(alphabet_list)
    character_set = set(characters)
    
    return alphabet_set.issubset(character_set)
