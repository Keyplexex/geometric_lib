# geometric_lib

This library provides functions to calculate the area and perimeter of various geometric shapes.

## Available Shapes

### Circle

- **Area**: 
    - Formula: ```S = pi R^2```
    - Function: circle.area(r)
    - Parameters: 
        - r (int, float): The radius of the circle.
    - Returns: The area of the circle.

- **Perimeter**: 
    - Formula: ```P = 2pi R```
    - Function: circle.perimeter(r)
    - Parameters: 
        - r (int, float): The radius of the circle.
    - Returns: The perimeter of the circle.

### Rectangle

- **Area**: 
    - Formula: ```S = ab```
    - Function: rectangle.area(a, b)
    - Parameters: 
        - a (int, float): One side of the rectangle.
        - b (int, float): The other side of the rectangle.
    - Returns: The area of the rectangle.

- **Perimeter**: 
    - Formula: ```P = 2a + 2b```
    - Function: rectangle.perimeter(a, b)
    - Parameters: 
        - a (int, float): One side of the rectangle.
        - b (int, float): The other side of the rectangle.
    - Returns: The perimeter of the rectangle.

### Square

- **Area**: 
    - Formula: ```S = a^2```
    - Function: square.area(a)
    - Parameters: 
        - a (int, float): The side of the square.
    - Returns: The area of the square.

- **Perimeter**: 
    - Formula: ```P = 4a```
    - Function: square.perimeter(a)
    - Parameters: 
        - a (int, float): The side of the square.
    - Returns: The perimeter of the square.

### Triangle

- **Area**: 
    - Formula: ```S = ah/2```
    - Function: triangle.area(a, h)
    - Parameters: 
        - a (int, float): The base of the triangle.
        - h (int, float): The height of the triangle.
    - Returns: The area of the triangle.

- **Perimeter**: 
    - Formula: ```P = a + b + c```
    - Function: triangle.perimeter(a, b, c)
    - Parameters: 
        - a, b, c (int, float): The lengths of the sides of the triangle.
    - Returns: The perimeter of the triangle.

### Trapezoid

- **Area**:
    - Formula: ```S = (a + b)h/2```
    - Function: trapezoid.area(a, b, h)
        - Parameters:
        - a, b (int, float): The lengths of the two bases.
        - h (int, float): The height of the trapezoid.
    - Returns: The area of the trapezoid.

- **Perimeter**:
    - Formula: ```P = a + b + c + d```
    - Function: trapezoid.perimeter(a, b, c, d)
    - Parameters:
        - a, b, c, d (int, float): The lengths of all four sides.
    - Returns: The perimeter of the trapezoid.

### Rhombus

- **Area**:
    - Formula: ```S = d_1 * d_2/2```
    - Function: rhombus.area(d1, d2)
    - Parameters:
        - d1, d2 (int, float): The lengths of the diagonals.
    - Returns: The area of the rhombus.

- **Perimeter**:
    - Formula: ```P = 4a```
    - Function: rhombus.perimeter(a)
    - Parameters:
        - a (int, float): The length of a side.
    - Returns: The perimeter of the rhombus.

### Parallelogram

- **Area**:
    - Formula: ```S = a * h```
    - Function: parallelogram.area(a, h)
    - Parameters:
        - a (int, float): The length of a base.
        - h (int, float): The height.
    - Returns: The area of the parallelogram.

- **Perimeter**:
    - Formula: ```P = 2(a + b)```
    - Function: parallelogram.perimeter(a, b)
    - Parameters:
        - a, b (int, float): The lengths of the sides.
    - Returns: The perimeter of the parallelogram.

### Ellipse

- **Area**:
    - Formula: ```S = pi a b```
    - Function: ellipse.area(a, b)
    - Parameters:
        - a, b (int, float): The semi-major and semi-minor axes.
    - Returns: The area of the ellipse.

- **Perimeter**:
    - Approximate formula using Ramanujan's approximation:
      ```P  =  approx pi [3(a + b) - sqrt{(3a + b)(a + 3b)}]```
    - Function: ellipse.perimeter(a, b)
    - Parameters:
        - a, b (int, float): The semi-major and semi-minor axes.
    - Returns: The approximate perimeter of the ellipse.

## Running Tests

To run tests for this library:

1. Make sure you have Python installed on your machine.
2. Navigate to the directory containing your tests.
3. Run the following command: ```python3 -m unittest discover -s tests```

   