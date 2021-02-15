# Probelm7

# Modify the code in csv_file_io.py to do the following:

# Write more lines into the file based on user input.
# Add a Genre column into the CSV file an populate the list with the movie genres.

from csv import reader, writer

answer = 'Y'

fp = open("c:/Users/Reema Eilouti/Documents/Python/CA12/csv_file_io.csv", 'w' , newline="")

csv_writer = writer(fp)

csv_writer.writerow(["ID" , "Movie", "Rating","genre"])

while answer == 'Y' :
    id_1 = int(input("enter ID :"))

    movie_1 = input("enter your favorate movie :")

    rating_1 = float(input("enter your favorate movie rating :"))

    genre_1 = input("enter your favorate movie genre :")

    answer = input("do you want another movie ? Y/N").upper()

    csv_writer.writerow([id_1,movie_1, rating_1,genre_1]) 

fp.close()
