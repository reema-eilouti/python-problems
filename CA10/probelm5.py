# Probelm5

# You are given a binary string (001011001011) as input, return a list of all substrings which start and end with a 1.

# Input: 001011001011
# Return: ['101', '1011', '1011001', '101100101', '1011001011', '']


binary_string = "001011001011"
result = []

for i in range(len(binary_string)):
    if binary_string[i] == '1':
        for j in range(i+1, len(binary_string)):
            if binary_string[j] == '1':
                result.append(binary_string[i:j+1])
print(result)
