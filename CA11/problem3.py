# Problem 3
# You are given a list of words. Write a function called find_frequencies(words) which returns a dictionary of the words along with their frequency.
 
#   Input: find_frequencies(['cat', 'bat', 'cat'])
#   Return: {'cat': 2, 'bat': 1}
 
my_dict={}
my_list=['cat' , 'cat' , 'dog' , 'bat' ,'bat']

def find_frequencies(words):
    
    for i in range(len(words)):
 
        number = words.count(words[i])
        my_dict[words[i]] = number
    
find_frequencies(my_list)    
print(my_dict)