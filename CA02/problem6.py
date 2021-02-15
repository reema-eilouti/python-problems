#CA02 Problem6

#Given a list, add the item 7000 after the item 6000 in the list.
list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list[2][2].insert(2, 7000)

print(list)