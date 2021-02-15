# Probelm5

# The code below can generate several exceptions. 
# These are now handled by a single try ... except clause. 
# Extend this code by handling all exceptions that may occur explicitly 
# (there are at least three different kinds of exceptions that can be raised). 


fruit_list = ["apple", "banana", "cherry"]

try:
    num = input("Please enter a number: ") 
    if "." in num:
        num = float(num)
    num = int(num) 
    print(fruit_list[num])
except IndexError:
    print("You enetered an invalid index!")
except ValueError:
    print("You entered a non integer value!")

    #problem with else and TypeError 


