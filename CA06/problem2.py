#CA05 Problem2

#Create a function sum_ten(n1, n2) which returns a Boolean True if the sum of the numbers is 10. 
# Otherwise, return the actual sum value.

def sum_ten(n1, n2):
    if n1 + n2 == 10:
        return True
    else:
        return n1 + n2

print(sum_ten(4,6))