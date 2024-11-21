def area(a):
    '''Takes a (int, float) - side of the square, returns its area - a ** 2 (int, float)''' 
    if a > 0:
        return a * a
    else:
        return "Error"


def perimeter(a):
    '''Takes a (int, float) - side of the square, returns its perimeter - 4 * a (int, float)'''
    if a > 0:
        return 4 * a
    else:
        return "Error"