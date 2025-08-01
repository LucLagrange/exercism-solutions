def is_valid(isbn):
    print(f"Original ISBN: {isbn}")
    
    # Remove hyphens
    clean_isbn = isbn.replace('-', '')
    print(f"Cleaned ISBN: {clean_isbn}")
    
    # X should only appear at the end of the string
    for i, char in enumerate(clean_isbn[:-1]):
        print(char)
        if char == "X":
            return False
    
    # ISBN should not be empty 
    if clean_isbn == '':
        return False
    
    # Generate a list of multipliers
    multipliers = [i for i in range(10, 0, -1)]
    
    # Convert to list of digits, properly handling 'X'
    digit_list = []
    for d in clean_isbn:
        if d == 'X':
            digit_list.append(10)
        elif d.isdigit():
            digit_list.append(int(d))
        else:
            return False
    print(digit_list)

    # ISBN should always consists of 10 digits    
    if len(digit_list) != 10:
        return False
    
    # Multiply digits and multipliers, then sum the result
    res = []
    for i in range(len(multipliers)):
        if i < len(digit_list):  # Prevent index errors
            res.append(multipliers[i] * digit_list[i])
    
    
    
    valid = sum(res) % 11 == 0
    print(f"ISBN is valid: {valid}")
    return valid