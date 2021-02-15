#CA07 Problem3 Part2

# Class Square
class Square:

    def __init__(self, length, width):
        # TODO: Define the instance attributes
        self.length = length
        self.width = width
        self.color = None

    # TODO: Define the string representation method and print the details of your square
    def __str__(self):
        return f"length = {self.length} width = {self.width}"
        

    # TODO: Define a find_area() method and return the area
    def find_area(self):
        return self.length * self.width

    # TODO: Define a find_perimeter() method and return the perimeter
    def find_perimeter(self):
        return 2 * self.length + 2 * self.width
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
        
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two squares
square_1 = Square(10 , 20)
square_2 = Square(6 , 4)

# TODO: Set the colors of your squares using the setter method
square_1.set_color("pink")
square_2.set_color("white")

# TODO: Print the colors of your squares using the getter method
print(square_1.get_color())
print(square_2.get_color())

# TODO: Print your squares. How does this work?
print(square_1)
print(square_2)

# TODO: Print the length, width, and area of your squares
print(f"the area of square 1 is :{square_1.find_area()}")
print(f"the area of square 2 is :{square_2.find_area()}")

print(square_1.length)
print(square_1.width)

print(square_2.length)
print(square_2.width)

# TODO: Print the perimeter of your square using the find_perimeter() method
print(f"the perimeter of square 1 is {square_1.find_perimeter()}")
print(f"the perimeter of square 2 is {square_2.find_perimeter()}")