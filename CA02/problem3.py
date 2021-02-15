#CA02 Problem3

#Given a list slice it into a three equal slices and then print each slice reversed.

list = [1,2,3,4,5,6,7,8,9]

step = int(len(list) / 3)

first_third = list[:step]
second_third = list[step:step*2]
third_third = list[step*2:]

print(first_third.reverse())
print(second_third.reverse())
print(third_third.reverse())