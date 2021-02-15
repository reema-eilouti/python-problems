# CA04 Problem1

# Write a program which reads a number (n) from the user and the print the sum of all numbers between 1 and n.

upper_bound = int(input("Please enter a number: "))

print(sum(range(1, upper_bound+1)))