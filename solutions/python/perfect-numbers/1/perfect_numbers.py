def get_divisors(n):
    divisors = set()
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.add(i)
    return divisors

def classify(number):
    """ A perfect number equals the sum of its positive divisors.
    
    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        divisors = get_divisors(number)
        if sum(divisors) == number:
            return "perfect"
        elif sum(divisors) > number:
            return "abundant"
        else:
            return "deficient"
