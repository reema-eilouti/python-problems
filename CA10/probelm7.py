# Probelm7

# Ask the user for two lowercase words (w1, w2) as input. 
# Create a function called create_anagram(w1, w2). 
# The only allowed operation is to remove a character from any string. 
# Find minimum number of characters to be deleted to make both the strings anagram?

# Input: art rat   hey hello
# Output:  0           4

w1 = input("please enter the first word: ").lower()
w2 = input("please enter the second word: ").lower()

def create_anagram(w1, w2):
    for letter1 in w1:
        for letter2 in w2:
            if letter1 == letter2:
                w1 = w1.replace(letter1, '')
                w2 = w2.replace(letter2, '')
    print(f"The minimum number of characters to be deleted to make both the strings anagram: {len(w1) + len(w2)}")

create_anagram(w1, w2)



