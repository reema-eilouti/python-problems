# Problem6

# Write a function generate_flat_list(nested_list) which flattens a nested list. 
# The function returns the flattened list.
# Input: nested_list = [[1, 2, [3, 4]], [5, 6], 7] and call generate_flat_list(nested_list)
# Output: [1, 2, 3, 4, 5, 6, 7]

nested_list = [[1, 2, [3, 4]], [5, 6], 7]
output = []

def generate_flat_list(nested_list):

    for i in range(len(nested_list)):
        if type(nested_list[i]) == int:
            output.append(nested_list[i])
        else:
            generate_flat_list(nested_list[i])

generate_flat_list(nested_list)
print(output)



