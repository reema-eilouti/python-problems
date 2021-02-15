# Probelm1

# Write a program that reads the lines from flatland.txt and displays only those lines 
# that contain the word Triangles, Squares, Pentagons, Hexagons. Ignore the cases of the words.

filename = "c:/Users/Reema Eilouti/Documents/Python/CA12/flatland.txt"

my_file = open(filename, "r")

my_words = ['triangles', 'squares', 'pentagons', 'hexagons']

for line in my_file:
    for word in my_words:
        if word in line.lower():
            print(line)
            break

my_file.close()
        
    
    