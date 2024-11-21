def area(b, h):
    '''Takes b (int, float) - base and h (int, float) - height of the parallelogram, returns its area - b * h (int, float)'''
    if b > 0 and h > 0:
        return b * h
    else:
        return "Error"

def perimeter(a, b):
    '''Takes a and b (int, float) - sides of the parallelogram, returns its perimeter - 2 * (a + b) (int, float)'''
    if a > 0 and b > 0:
        return 2 * (a + b)
    else:
        return "Error"