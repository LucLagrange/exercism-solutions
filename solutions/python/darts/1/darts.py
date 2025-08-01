import math

def score(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)

    if distance <= 1:
        points = 10
    elif distance > 1 and distance <= 5:
        points = 5
    elif distance > 5 and distance <= 10:
        points = 1
    else:
        points = 0
    return points