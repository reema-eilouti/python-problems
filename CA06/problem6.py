#CA05 Problem6

# Create a function compare_length(s1, s2) which returns the difference in length between the strings.

def compare_length(s1, s2):
    return abs(len(s1) - len(s2))

print(compare_length("Hey","Hello"))