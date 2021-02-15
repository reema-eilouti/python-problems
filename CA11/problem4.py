# Problem4 

# You are given a list of integers. 
# Write a function cumulative_sum(numbers) which calculates the cumulative sum of the list. 
# The cumulative sum of a list numbers = [a, b, c, ...] can be defined as [a, a+b, a+b+c, ...].
# Input: numbers = [1, 2, 3, 4]
# Return: cumulative_sum_list = [1, 3, 6, 10]


my_list = [10,20,30,40,50]
new_list = [] 
j = 0

def cumulative_sum(my_list):
    global j
    for i in range(len(my_list)):
        j += my_list[i]
        new_list.append(j)
 
cumulative_sum(my_list)     
print(new_list)