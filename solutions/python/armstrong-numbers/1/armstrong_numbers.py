def is_armstrong_number(number):
    digits = [digit for digit in str(number)]
    number_of_digits = len(digits)
    
    sum_of_digits = 0
    
    for digit in digits:
        sum_of_digits += int(digit)**number_of_digits
    
    return number == sum_of_digits