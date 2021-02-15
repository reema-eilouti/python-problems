#CA05 Problem10

# Create a function which take a string as an argument, 
# then prints a string where for every character in the original there are three characters.

def my_function (my_string):
    repeated_string = ""
    for char in my_string:
        repeated_string += char * 3
    print(repeated_string)

my_function("abc")