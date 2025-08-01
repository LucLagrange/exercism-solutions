def square_of_sum(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    print(f"The square of sums is: {result ** 2}")
    return result ** 2


def sum_of_squares(number):
    result = 0
    for i in range(1, number + 1):
        result += i **2

    print(f"The sum of squares is: {result}")
    return result


def difference_of_squares(number):
    if number == 0:
        return False 
    result = square_of_sum(number) - sum_of_squares(number)
    
    return result