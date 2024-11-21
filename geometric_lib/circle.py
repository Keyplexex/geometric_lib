import math


def area(r):
    '''Takes r (int, float) - radius of the circle, returns its area - pi * r ** 2 (int, float)''' 
    if r > 0:
        return math.pi * r * r
    else:
        return "Error"


def perimeter(r):
    '''Takes r (int, float) - radius of the circle, returns its perimeter - 2 * pi * r (int, float)'''
    if r > 0: 
        return 2 * math.pi * r
    else:
        return "Error"