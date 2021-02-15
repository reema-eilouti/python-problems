# Probelm1

# Ask the user for two integers (x, y) as input. 
# Create a range using the range(x,y) then only print the positive numbers.

x , y = input("Please enter two numbers seperated by a space: ").split()

for num in range(int(x) , int(y)):
    if num > 0:
        print(f"a positive number between them => {num}")