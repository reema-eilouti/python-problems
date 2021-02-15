# CA04 Problem2

# Write a program which prints the following pattern for any given number, n = 5, for example.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

number = input("enter number")
my_string = ""
for i in range(1, int(number)+1):
    my_string += str(i) + " "
    print(my_string)
