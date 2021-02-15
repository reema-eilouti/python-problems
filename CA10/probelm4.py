# Probelm4

# Iterate over the range(1, 100) and print the numbers. 
# However, if the number is a multiple of 3, print Fizz instead. 
# If the number is a multiple of 5, print Buzz. If the number is a multiple of both 3 and 5, print FizzBuzz.

# Input: None
# Print: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz 10 ...

for number in range(1,100):
    if number % 3 == 0 and number % 5 ==0 : 
        print('FizzBuzz')
        
    elif number % 3 == 0 :
        print('Fizz')
 
    elif number % 5 == 0:
        print('Buzz')
    
    else:    
        print(number)