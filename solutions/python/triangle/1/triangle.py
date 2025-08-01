def equilateral(sides):
    return 0 not in sides and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    a, b, c = sorted(sides)
    return  0 not in sides and a + b > c and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    a, b, c = sorted(sides)
    return 0 not in sides and len(set(sides)) == 3 and a + b > c
