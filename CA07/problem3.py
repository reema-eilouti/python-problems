#CA06 Problem3

# Shopping List

# Your shopping list should keep asking for new items until nothing is entered 
# (no input followed by enter/return key).
# The program should then print a menu for the user to choose one of the following options:
# (A)dd - To add a new item to the list.
# (F)ind - To search for an item in the list.
# (P)rint - To pretty print the list.
# (S)ort - To sort the list.
# (C)lear - To clear all items in the list.
# (Q)uit - To exit your program.

# TODO: Define a data structure to keep track of your shopping list.
shopping_list = []

# TODO: Implement a function to show the menu to the user, then wait for a valid user choice.
def show_menu():
    print("""
    (A)dd - To add a new item to the list.
    (F)ind - To search for an item in the list.
    (P)rint - To pretty print the list.
    (S)ort - To sort the list.
    (C)lear - To clear all items in the list.
    (Q)uit - To exit your program.""")
  
    
# TODO: Implement a function to add an item to your shopping list.
def add_item():
    item = the_item()
    shopping_list.append(item)
    print(shopping_list)

# TODO: Implement a function to find an item in your shopping list.
def find_item():
    item = the_item()
    return str(shopping_list).find(item)

# TODO: Implement a function to pretty print your tabbed list.
def print_list():
    tabbed = "\n \t * ".join(shopping_list)
    print(tabbed) 

# TODO: Implement a function to pretty print your tabbed lits.
def sort_list():
    shopping_list.sort()

# TODO: Implement a function to pretty print your tabbed lits.
def clear_list():
    shopping_list.clear()

# TODO: Implement a function which calls the exit() function.
def quit():
    print("Goodbye! Hope to see you again soon :).")
    exit()

def the_item():
    return input("enter the item: ")
    

def ask_input():
    #while input("Enjoying the course? (y/n) ") not in ('y', 'n'):
        #print("Sorry, I didn't catch that. Enter again:")
    options = {'A':add_item, 'F':find_item, 'P':print_list, 'S':sort_list, 'C':clear_list, 'Q':quit}
    choice =  input("Please enter a valid letter: ").upper()
    options[choice]()

while True:
    show_menu()
    ask_input()

