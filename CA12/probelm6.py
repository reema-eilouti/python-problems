# Probelm6

# Which exceptions can the code below raise? 
# Extend the code to handle all of them in a reasonable manner.

number_list = [ 100, 101, 0, "103", 104 ]

try:
    i = int(input( "Give an index: " ))
    print(f"100 / {number_list[i]} = {100 / number_list[i]}")  

except TypeError:
    print("You cant divide another type by int")

except ZeroDivisionError :
    print("You cant divide by zero")

except ValueError:
    print( "invalid input." )

except IndexError:
    print("index out of range")