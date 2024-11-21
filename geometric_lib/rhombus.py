def area(d1, d2):
    '''Takes d1 and d2 (int, float) - diagonals of the rhombus, returns its area - (d1 * d2) / 2 (int, float)'''
    if d1 > 0 and d2 > 0:
        return (d1 * d2) / 2
    else:
        return "Error"

def perimeter(a):
    '''Takes a (int, float) - side of the rhombus, returns its perimeter - 4 * a (int, float)'''
    if a > 0:
        return 4 * a
    else:
        return "Error"