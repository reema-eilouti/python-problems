# Probelm3

# Write a program that reads the contents of sentences.txt and writes exactly 
# the same contents to the file sentences.tmp. 
# Then open the file sentences.tmp and display the contents.

filename = "c:/Users/Reema Eilouti/Documents/Python/CA12/sentences.txt"

filename2 = "c:/Users/Reema Eilouti/Documents/Python/CA12/sentences.tmp"


my_file = open(filename, 'r')
another_file = open(filename2, 'w')

for line in my_file:
    another_file.write(line)
    