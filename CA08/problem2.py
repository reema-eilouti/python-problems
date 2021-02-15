#CA07 Problem2

# Define a class called User.
class User:
# Define an attribute called login_attempts to your User class.
    login_attempts = 0

# Define two attributes called first_name and last_name. 
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
# Define and then create several other attributes that are typically stored in a user profile.
        self.password = None
        self.email = None

# Define a method called describe_user() that prints a summary of the user’s information.
    def describe_user(self):
        print(f"The first name {self.first_name}")
        print(f"The last name {self.last_name}")
        print(f"Email {self.email}")

# Define a another method called greet_user() that prints a personalized greeting to the user.
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} Welcome to my heart")

# Define a method called increment_login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        self.login_attempts += 1

# Define another method called reset_login_attempts() that resets the value of login_attempts to 0.
    def reset_login_attempts(self):
        self.login_attempts = 0

# Create several instances representing different users, and call both methods for each user.
user1=User('Ahmad' , 'Sami')    
user2=User('Sami' , 'Ahmad')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# Create an instance of the User class and call increment_login_attempts() several times.
user3=User("Hamza" , "Mohammad")
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
print(user1.login_attempts)
print(user3.login_attempts)

# Print login_attempts again to make sure it was reset to 0.
user3.reset_login_attempts()
print(user3.login_attempts)