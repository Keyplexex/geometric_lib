import math


def area(r):
    '''Takes r (int, float) - radius of the circle, returns its area - pi * r ** 2 (int, float)''' 
    return math.pi * r * r


def perimeter(r):
    '''Takes r (int, float) - radius of the circle, returns its perimeter - 2 * pi * r (int, float)''' 
    return 2 * math.pi * r