#CA07 Problem1

# Define a class called Restaurant.

class Restaurant:
    # The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    # Add an attribute called number_served with a default value of 0.   
        self.number_served = 0        

# Define a method called describe_restaurant() that prints these two pieces of information.
    def describe_restaurant(self):
        print(f"The restaurant name {self.restaurant_name} and the cuisine is {self.cuisine_type}")

# Define a method called open_restaurant() that prints a message indicating that the restaurant is open.
    def open_restaurant(self):
        print(f"The  Restaurant {self.restaurant_name} is open")

# Define a method called set_number_served() that lets you set the number of customers that have been served.
    def set_number_served(self, number):
        self.number_served = number

#Define a method called increment_number_served() that lets you increment the number of customers who’ve been served.
    def increment_number_served(self, n):
        self.number_served += n

# Create an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
restaurant1=Restaurant("Manchester" , "french")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print("*" * 10)

# Create three different instances from the class, and call describe_restaurant() for each instance.
restaurant2=Restaurant("Hesham" , "French")
restaurant3=Restaurant("Hashem" , "Burger")
restaurant4=Restaurant("Hesham Hashem" , "Shawarma")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

print("*" * 10)

# Create an instance called restaurant from this class.
restaurant5=Restaurant("Reema" , "Pizza")

#Print the number of customers the restaurant has served, and then change this value and print it again.
print(restaurant5.number_served)
restaurant5.number_served=5
print(restaurant5.number_served)

#Call this method with a new number and print the value again.
restaurant5.set_number_served(6)
print(restaurant5.number_served)

#Call this method with any number you like that could represent how many customers were served in, say, a day of business.
restaurant5.increment_number_served(20)
print(restaurant5.number_served)