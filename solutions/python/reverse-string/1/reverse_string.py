def reverse(text):
    my_list = list(text)
    
    reversed_list = my_list[::-1]
    
    reversed_text = ''.join(str(x) for x in reversed_list)
    
    return reversed_text