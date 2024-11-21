def area(a, h):
    '''Takes a, h (int, float) - side and height of a triangle, returns its area - a * h / 2 (int, float)''' 
    if a > 0 and h > 0:
        return a * h / 2 
    else:
        return "Error"

def perimeter(a, b, c):
    '''Takes a, b, and c (int, float) - sides of a triangle, returns its perimeter - a + b + c (int, float)''' 
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        return "Error"