# Probelm3

# You are given a sentence as input. Return a list of all words of even length.

# Input: Print every word in this sentence that has an even number of letters.
# Return: ['word', 'in', 'this', 'sentence', 'that', 'an', 'even', 'number', 'of']

string = input("enter the sentence here :").split(' ')
print(string)
sentence = []
 
for word in string:
    if len(word) % 2 == 0:
        sentence.append(word)
        
print(sentence)