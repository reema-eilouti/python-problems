# CA04 Problem6

# Given a string, get the length of the string without using the len() function.

string = input("Please enter a string: ")

num = 0

for char in string :
    num += 1

print(f"The length of your string '{string}' is: {num} characters.")



