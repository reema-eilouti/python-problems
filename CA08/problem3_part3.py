#CA07 Problem3 Part3

# Class Triangle

class Triangle():
    
    # TODO: Implement __init__ for this class use a,b,c and for the length of the sides
    def __init__(self , a , b , c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        tri =  """
*
**
***
****
        """
        values = f"The lenghts os the sides are {self.a},{self.b},{self.c}"
        sentence = f"The area is {self.find_area()} and the perimeter is {self.find_perimeter()}."
        return sentence + tri + values

    # TODO: Implement find_area() for this class
    def find_area(self):
        # height = ((self.c * 0.5)**2 - self.a**2)**0.5
        # area= 0.5 * self.c * height
        # per = self.a + self.b + self.c
        s = self.find_perimeter() / 2
        area = abs((s*(s-self.a)*(s-self.b)*(s-self.c))) ** 0.5
        return  area     

    # TODO: Implement find_perimeter() for this class
    def find_perimeter(self):    
        return self.a + self.b + self.c

    # TODO: Implement a print_triangle_type() method which prints 
    # the type of the triangle based on the length of the sides.
    # Hint: You can use the Pythagorean Theorum to find the type of triangle.
    # Hint: Read more https://www.geeksforgeeks.org/find-the-type-of-triangle-from-the-given-sides/
    def print_triangle_type(self):
        if self.a == self.b == self.c :
            print("Equilateral Triangle") 
        elif self.a == self.b or self.a == self.c or self.b == self.c :
            print("Isosceles Triangle")
        else : 
            print("Scalene Triangle")    


how_many = int(input("please enter how many triangles: "))
triangles = []
print(f"Now I'll ask for the lenght of the {how_many} triangles.")

for i in range(1, how_many+1):
    #ternery operator
    a, b, c = [ int(x) for x in input("please enter three lengths for triangle {i} like (1,2,3): ").split(',') ]

    triangles.append(Triangle(a,b,c))

for triangle in triangles:
    print(triangle)



# print
# t1=Triangle(4,4,4)
# print(t1.find_area())
# t1.print_triangle_type()