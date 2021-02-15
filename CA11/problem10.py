# Define a class for the linked list
from node import Node
 
# Class for a simple Linked List
 
class LinkedList:
    def __init__(self, data):
        self.start_node = Node(data)
 
    def traverse_list(self):
        pointer_node = self.start_node
        while pointer_node is not None:
            print(pointer_node.data)
            pointer_node = pointer_node.next
 
    def insert_at_start(self, data):
        new_node = Node(data)        
        pointer_node = new_node
        pointer_node.next = self.start_node
        self.start_node = new_node
 
    def insert_at_end(self, data):
        new_node = Node(data)
        pointer_node = self.start_node
        while pointer_node.next is not None:
            pointer_node = pointer_node.next
        pointer_node.next = new_node
 
    def insert_after(self, x, data):
        new_node = Node(data)
        pointer_node = self.start_node
        for point in range(x):
            pointer_node = pointer_node.next
        new_node.next = pointer_node.next
        pointer_node.next = new_node
        
    def insert_before_item(self, x, data):
        new_node = Node(data)
        pointer_node = self.start_node
        while pointer_node.next.data != x:
            pointer_node = pointer_node.next
        else:
            new_node.next = pointer_node.next
            pointer_node.next = new_node
        
    def insert_at_index (self, index, data):
        new_node = Node(data)
        pointer_node = self.start_node
        for point in range(index-1):
            pointer_node = pointer_node.next
        new_node.next = pointer_node.next
        pointer_node.next = new_node
 
    def get_count(self):
        counter = 0
        pointer_node = self.start_node
        while pointer_node is not None:
            pointer_node = pointer_node.next
            counter += 1
        print(counter)
 
    def search_item(self, x):
        pointer_node = self.start_node
        while pointer_node.data != x : 
            if pointer_node.next == None:
                break           
            pointer_node = pointer_node.next
            
            
        if pointer_node.next == None:
            print("the item you are looking for does not exist")
        else:
            print(f"the item you are looking for exists ")
 
 
    def make_new_list(self):
        
        node_bravo = Node(2)
        node_charlie = Node(3)
        node_delta = Node(4)
        node_echo = Node(5)
        node_fox = Node(6)
 
        node_alpha.start_node.next = node_bravo
        node_bravo.next = node_charlie
        node_charlie.next = node_delta 
        node_delta.next = node_echo
        node_echo.next = node_fox
 
    def delete_at_start(self):
        pointer_node = self.start_node
        self.start_node = pointer_node.next
 
    def delete_at_end(self):
        pointer_node = self.start_node
        while pointer_node.next.next != None:
            pointer_node = pointer_node.next
            
        pointer_node.next = None
            
 
    def reverse_linkedlist(self):
        my_list = []
        pointer_node = self.start_node
        while pointer_node is not None:
            my_list.append(pointer_node.data)
            pointer_node = pointer_node.next

        my_list.reverse()
        print(my_list)
        
 
# Our linked list like this now
#   (40)->(10)->(5)->(3)->(15)->(20)-> None
 
# node_1 = LinkedList(40)
# node_2 = Node(10)
# node_3 = Node(5)
# node_4 = Node(3)
# node_5 = Node(15)
# node_6 = Node(20)
 
# node_1.start_node.next = node_2
# node_2.next = node_3
# node_3.next = node_4 
# node_4.next = node_5
# node_5.next = node_6
 
# node_1.insert_at_start(12) 
# node_1.insert_at_end(88)
# node_1.insert_after
# node_1.insert_before_item(15,55)
# node_1.insert_at_index(2,66)
# node_1.get_count()
 
# node_1.traverse_list()
# node_1.search_item(40)
 
node_alpha = LinkedList(1)
node_alpha.make_new_list()
# node_alpha.delete_at_start()
# node_alpha.delete_at_end()
node_alpha.reverse_linkedlist()
# node_alpha.traverse_list()