#CA07 Problem3 Part1

# Class Circle

class Circle:

    # TODO: Define an instance attribute for PI
    PI = 3.14

    def __init__(self, radius=1.0):

        # TODO: Define an instance attribute for the radius
        self.radius = radius
        self.color = None

    # TODO: Define the string representation method and print
    # r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}
    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    # TODO: Define a get_area() method and return the area
    def get_area(self):
        return self.radius ** 2 * Circle.PI

    # TODO: Define a get_circumference() method and return the circumference
    def get_circumference(self):
        return self.radius * 2 * self.PI
    
    # TODO: Define a set_color(color) method which sets the object attribute
    def set_color(self, color):
        self.color = color
    
    # TODO: Define a get_color() method which returns the object attribute
    def get_color(self):
        return self.color

# Playground

# TODO: Create two circles one with radius 3, and one with the default radius
circle1 = Circle(3)
circle2 = Circle()

# TODO: Set the colors of your circles using the setter method
circle1.set_color("Yellow")
circle2.set_color("Red")

# TODO: Print the colors of your circles using the getter method
circle1.get_color()
circle2.get_color()

# TODO: Print your circles. How does this work?
print(circle1)
print(circle2)

# TODO: Print the radius and areas of your cricles
print(f"Circle 1 radius is {circle1.radius} and its area is {circle1.get_area()}")
print(f"Circle 2 radius is {circle2.radius} and its area is {circle2.get_area()}")

# TODO: Print the circumference of your circles using the getter methods
print(f"Circle 1 circumference is {circle1.get_circumference()}")
print(f"Circle 2 circumference is {circle2.get_circumference()}")