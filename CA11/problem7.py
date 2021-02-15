# Problem7

# Write a function generate_flat_dict(nested_dict) which flattens a nested dictionary by joining the keys with the . character. The function returns the flattened dictionary.
# Input: nested_dict = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4} and call generate_flat_dict(nested_dict)
# Output: {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

nested_dict = {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
output = {}
 
def generate_flat_dict(nested_dict):
 
    for item in nested_dict:
        if type(nested_dict[item]) == dict:
            generate_flat_dict(nested_dict[item])
        else:
            output[item] = nested_dict[item]
            
generate_flat_dict(nested_dict)
print(output)