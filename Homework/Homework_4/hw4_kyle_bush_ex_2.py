'''
Homework 4, Exercise 2
Kyle Bush
10/7/2020
Program defines classes for a Circle, Rectangle, and Square.
Each class has methods to calculate the area, diagonal, and perimeter of the shape.
The main program prints the perimeter of a circle defined with a radius  
that is equal to the diagonal of a rectangle with a width of 20 and length of 10.
'''

import math

# Circle defined by a radius. Calculates the area, diagonal, and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def diagonal(self):
        return self.radius * 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Rectangle defined by length and width. Calculates the area, diagonal, and perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def diagonal(self):
        return math.sqrt(self.length**2 + self.width**2)

    def perimeter(self):
        return 2 * (self.length + self.width)

# Square inherits from Rectangle since a Square is a Rectangle.
# Uses Rectangle's methods to calculate the area, diagonal, and perimeter.
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)



def main():
    # Create a rectangle with length 20 and width 10. 
    rectangle = Rectangle(20, 10)
    radius = rectangle.diagonal() / 2
    
    # Create a circle with a radius equal to the diagonal of the rectangle
    circle = Circle(radius)
    print(circle.perimeter())


if __name__ == '__main__':
    main()