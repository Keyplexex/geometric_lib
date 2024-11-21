def area(a, b):
    '''Takes a and b (int, float) - sides of a rectangle, returns its area - a * b (int, float)''' 
    if a > 0 and b > 0:
        return a * b 
    else:
        return "Error"

def perimeter(a, b):
    '''Takes a and b (int, float) - sides of a rectangle, returns its perimeter - 2 * (a + b) (int, float)'''
    if a > 0 and b > 0: 
        return 2*(a + b)
    else:
        return "Error"
