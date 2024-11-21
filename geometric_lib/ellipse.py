import math

def area(a, b):
    '''Takes a and b (int, float) - semi-major and semi-minor axes of the ellipse, returns its area - pi * a * b (int, float)'''
    if a > 0 and b > 0:
        return math.pi * a * b
    else:
        return "Error"

def perimeter(a, b):
    '''Approximate perimeter of an ellipse using Ramanujan's formula'''
    if a > 0 and b > 0:
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))
    else:
        return "Error"