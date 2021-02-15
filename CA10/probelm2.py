# Probelm2

# Use list comprehensions in Python to return a new list ages using the list of birth years as input.

# Input: years_of_birth = [1991, 1990, 1990, 1988, 1992, 1990]
# Return: ages = [29, 30, 30, 32, 28, 30]

years_of_birth = [int(input("Enter a year: ")) for year in range(5)]
ages = []
ages = [2020 - year for year in years_of_birth]
# for year in years_of_birth:
#     ages.append(2020 - year)
print(ages)