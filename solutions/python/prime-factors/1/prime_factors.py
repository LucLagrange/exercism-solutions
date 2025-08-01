def factors(value):
    # 1. Divide by 2 until there is a rest
        # If there is a least one loop with no rest -> add 2 to a set
    # 2. Divide by 3 until there is a rest
    # 3. ...
    # 5. Stop when the division result is one
    # 6. Return the list of divisors

    # Initialize an empty set
    divisors = []

    for divisor in range (2, int(value ** 0.5) + 1):
        while value % divisor == 0:
            print(f"Initial value is: {value}")
            print(f"Divisor is: {divisor}")

            divisors.append(divisor)
            value = value // divisor
    if value > 1:
        divisors.append(value)  # Append the remaining prime (if any)

    print(divisors)
    return divisors