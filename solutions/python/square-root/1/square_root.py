def square_root(number):
    result = 1
    for i in range(1, number):
        if i * i == number:
            result = i
            break
    print(result)
    return result
square_root(1)