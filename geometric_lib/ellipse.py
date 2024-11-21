import math

def area(a, b):
    '''Takes a and b (int, float) - semi-major and semi-minor axes of the ellipse, returns its area - pi * a * b (int, float)'''
    return math.pi * a * b

def perimeter(a, b):
    '''Approximate perimeter of an ellipse using Ramanujan's formula'''
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))