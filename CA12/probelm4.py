# Probelm4

# Write a program that adds up the sizes of all the files 
# in the current directory, and prints the result.

# from os.path import exists
# from os.path import isdir, isfile
from os.path import getsize
from os import getcwd, listdir

sizes = 0

directory = getcwd()

print(directory)

for file in listdir(directory):
    print(f"filename: {file}, filesize: {getsize(file)}")
    sizes += getsize(file)

print(f"Total size in {directory} in bytes is: {sizes}.")
