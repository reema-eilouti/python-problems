# Problem9

# Write a function recursive_sum(numbers) which returns the sum of the list.
# Input: numbers = [1, 2, 3, 4, 5]
# Return: 15

numbers = [1, 2, 3, 4, 5 , 6]

def recursive_sum(numbers):

    if len(numbers) == 0 :
        return 0
    else:
        number = numbers.pop()
        return number + recursive_sum(numbers)

print(recursive_sum(numbers)) 