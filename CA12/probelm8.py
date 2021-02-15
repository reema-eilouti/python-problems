# Probelm8

# Write a program to check if a given path exists in the current working directory. 
# If it is found, then print the details of the path.

# Type (directory / file).
# Size in kilobytes, or megabytes.
# Creation time / access time / modification time.

from os.path import exists
from os.path import isdir, isfile
from os.path import getsize
from os import getcwd
from datetime import time
import os.path, time

my_path = "csv_file_io.csv"

# > Checking if a path exists

if exists(my_path):
    print(f"Found the path '{my_path}'.")

    csv_file = getsize(my_path)                                     #get the size of the file
    
    print(f"The size of the path '{my_path}' is {csv_file} bytes.") #print the path and size 

    if isdir(my_path):
        print(f"'{my_path}' is a directory.")                        #check if a file is directory
    else:
        print(f"'{my_path}' is a file.")                             #check if a file is file
        print("Last modified: %s" % time.ctime(os.path.getmtime("csv_file_io.csv")))# Creation time 
        print("Created: %s" % time.ctime(os.path.getctime("csv_file_io.csv")))      # modification time
        print("Accessed: %s" % time.ctime(os.path.getatime("csv_file_io.csv")))     # access time
        # print(os.path.getatime("csv_file_io.csv"))                                                    
else:
    print(f"The path '{my_path}' was not found.")
