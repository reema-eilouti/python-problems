# CA04 Problem5

# Given a list of numbers, reverse the list without using the reverse() method.

list_of_nums = [5, 3, 7, 2]
reverse_list = []

for i in list_of_nums:
    reverse_list.insert(0,i)

print(reverse_list)