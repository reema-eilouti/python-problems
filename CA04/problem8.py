# CA04 Problem8

# Write a program which prints the absolute value of any given number n without using the abs() function .

number = int(input("Please enter a number: "))

if number > 0 :
    print(f"The absolute value of {number} is {number}")
else :
    print(f"The absolute value of {number} is {-1 * number}")
