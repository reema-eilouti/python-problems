#CA02 Problem1

#Given an input list remove the element at index 2 and add it at index 4 and also at the end of the list.
list = [54, 44, 27, 79, 91, 41]
results_list = [54, 44, 79, 27, 91, 41, 27]

element = list[2]

list.remove(element)

list.insert(4, element)

list.insert(len(list), element)

print(list)