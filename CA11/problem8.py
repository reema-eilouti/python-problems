# Problem8

# Write a function find_max_sublist(numbers) which returns the sum of maximum sub-list in a list of integers.
# Input: numbers = [-8, -2, -3]
# Return: 27

def find_max_sublist(numbers):

    sum = 0
    for number in numbers:
        if number > 0:
            sum = sum + number
    return sum

numbers = [-8, -2, 4, 6, 8, 4, 5, -3]
print(find_max_sublist(numbers))