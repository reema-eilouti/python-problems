# Probelm2

# Adapt the code above to count how often the word flatland (with any capitalization) occurs 
# in the first 5 lines. Print only the number of occurrences of that word. 
# Once it works, remove the count so that you count the number of occurrences of the word 
# in the text as a whole.

filename = "c:/Users/Reema Eilouti/Documents/Python/CA12/flatland.txt"

my_file = open(filename, "r")

my_word = "flatland"

# for line in my_file:
#     if my_word in line.lower():
#         print(line)

for i,line in enumerate(my_file):
    if i < 6:
        if my_word in line.lower():
            print(line)

my_file.close()

