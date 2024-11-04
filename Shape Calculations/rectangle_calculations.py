class Area:
    def getArea(self, length, breadth):
        return length * breadth

class Perimeter:
    def getPerimeter(self, length, breadth):
        return 2 * (length + breadth)

class Rectangle(Area, Perimeter):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.getArea(self.length, self.breadth)

    def perimeter(self):
        return self.getPerimeter(self.length, self.breadth)

# Create a Rectangle object
rect = Rectangle(10, 5)

# Print area and perimeter of the rectangle
print("Area of Rectangle:", rect.area())
print("Perimeter of Rectangle:", rect.perimeter())
