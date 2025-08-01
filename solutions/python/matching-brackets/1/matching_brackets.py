def is_paired(input_string):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in input_string:
        # If we find an opening bracket, add it to the stack
        if char in '({[':
            stack.append(char)
            
        # If we find a closing bracket
        elif char in ')}]':
            # If stack is empty but we found closing bracket, it's invalid
            if not stack:
                return False
                
            # Pop the last opening bracket and check if it matches
            last_opening = stack.pop()
            if last_opening != brackets[char]:
                return False
    
    # At the end, stack should be empty if all brackets were properly closed
    return len(stack) == 0