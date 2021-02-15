#CA05 Problem9

# Create a function which returns a list of all even number between x and y. Use the range() function.

def even_numbers (x,y):
    even_list = []
    for i in range(x,y):
        if i % 2 == 0:
            even_list += [i]
    return even_list

print(even_numbers(1,10))
