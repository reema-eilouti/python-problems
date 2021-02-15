# Probelm6

# Ask the user for a lowercase string (s) as input. 
# Create a function called check_palindrome(s) which returns the longest substring which is palindrome.

# Input: "I love python.nohtyp evol I Python is never odd or even"
# Return: "never odd or even"

def check_palindrome(s1):
    p_list=[]
    max=0
    for i in range(0,len(s1)):                        

            for j in range(0,len(s1)-i):
                x=s1[i:len(s1)-j]                       #sub string
                y=x[::-1]

                if x.replace(' ','')== y.replace(' ',''):        #string = reverse of it without spaces
                    if len(x)>max:                           
                        max=len(x)
                        p_list.append(x)
    return p_list[-1]

s1=' never odd or even I love python.nohtyp evol I Python is'
print(check_palindrome(s1))
s2='heloo python nohtyp iam esraa etoom mooteaarse'
print(check_palindrome(s2))





# lower_case = input("please enter a lower case string : ").lower()

# list_lower = list(lower_case)
 
# reversed_list = list_lower[:] #remember that y = x only copies the pointer, y = x[:] makes a new list

# reversed_list.reverse()

# print(list_lower)

# print(reversed_list)

# result = []
 

# def check_palindrome():
#     for i in range(len(list_lower)+1):
#         for j in range(len(reversed_list)+1):
#             if list_lower[i:j-1] == reversed_list[i:j-1]:
#                 result.append(list_lower[i:j+1])


# check_palindrome()

# print(result)

# longest_string = max(result, key=len)

# print(longest_string)