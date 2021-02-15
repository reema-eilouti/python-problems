#CA05 Problem5

# Create a function seq_check(numbers) 
# which when given a list of integers, returns True if the sequence [1,2,3] appears somewhere in that list.

def seq_check(numbers):
    if  "1, 2, 3" in str(numbers) :
        return True 
print(seq_check([7,1,2,3,6]))

# def seq_check(numbers):
#     for n in range(0 , len(numbers)):
#         if numbers[n:n+3]==[1,2,3]:
#             return True
#         else : pass