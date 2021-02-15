# CA04 Problem7

# Write a program which reads the age of 3 different people. 
# Then print the oldest, and youngest between them.

a1, a2, a3 = [int(a) for a in input("Enter three ages").split()]

ages_list = a1, a2, a3

print(min(ages_list))
print(max(ages_list))