# CA04 Problem9

# Given two lists, create a third list by picking an even-index element from the first list 
# and odd-index element from second.

first_list = [3, 6, 9, 12, 15, 18, 21]
second_list = [4, 8, 12, 16, 20, 24, 28]
#result_list = [3, 8, 9, 16, 15, 24, 21]

result_list = []

for i in range(len(first_list)):
    if i % 2 == 0 :
        result_list.append(first_list[i])
    else:
        result_list.append(second_list[i])

print(result_list)



