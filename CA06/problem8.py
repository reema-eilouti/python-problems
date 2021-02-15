#CA05 Problem8

# Create a function which returns a list of all numbers between 1 and 50 that are divisible by 3.

def three_dividends (x,y):
    three_dividends_list = []
    for i in range(x,y):
        if i % 3 == 0:
            three_dividends_list += [i]
    return three_dividends_list

print(three_dividends(1,50))

# def divisible_fun ():
#     list_1 = []
#     for i in range(1,50):
#         if i % 3 == 0:
#             list_1 += [i]
 
#     return list_1
 
# print(divisible_fun())