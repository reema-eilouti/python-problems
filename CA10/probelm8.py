# Probelm8

# Given two lists (a and b) of any size as input, 
# return a list that contains only the elements that are common between the lists (without duplicates).

# Input: a = [20, 11, 23, 1, 26, 5, 22, 9, 19, 29, 8, 18] 
# and b = [20, 25, 11, 26, 4, 14, 19, 27, 5, 18, 15, 6, 10, 22, 9, 21].
# Return: [5, 9, 11, 18, 19, 20, 22, 26]

list_a = [20, 11, 23, 1, 26, 5, 22, 9, 19, 29, 8, 18]
list_b = [20, 25, 11, 26, 4, 14, 19, 27, 5, 18, 15, 6, 10, 22, 9, 21]
 
x=set(list_a) - set(list_b)
print(set(list_a) - x )