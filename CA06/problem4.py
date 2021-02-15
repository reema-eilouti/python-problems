#CA05 Problem4

# Create a function last_two(astring) which returns the last two characters as a tuple. 
# If there are less than two characters, return the value "Error".

def last_two(astring):
    if len(astring) < 2 :
        return "Error"
    else :
        return tuple(astring[-2:])

print(last_two("hi how's it going"))