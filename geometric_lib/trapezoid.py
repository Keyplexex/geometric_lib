def area(a, b, h):
    '''Takes a and b (int, float) - bases of the trapezoid, h (int, float) - height, returns its area - ((a + b) / 2) * h (int, float)'''
    if a > 0 and b > 0 and h > 0:
        return ((a + b) / 2) * h
    else:
        return "Error"

def perimeter(a, b, c, d):
    '''Takes a, b, c, and d (int, float) - sides of the trapezoid, returns its perimeter - a + b + c + d (int, float)'''
    if a > 0 and b > 0 and c > 0 and d > 0:
        return a + b + c + d
    else:
        return "Error"