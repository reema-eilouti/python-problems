# Probelm10

sum = 0
my_list = []

# Define a class for the tree node.
class Node:

    # Define your __init__() method.
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def insert(self, value):
    #     number_of_levels = self.get_height()

    #     jumping_variable = [[None, None], [self, self], [self.left, self.right]]
        

    #     for level in range(2, number_of_levels + 5):

    #         number_of_empty_slots = 2**(level-1)

    #         # for slot in range(1, number_of_empty_slots + 1):

    #         if level == 2:

    #             if self.left == None:
    #                 self.left = value

    #             elif self.right == None:
    #                 self.right = value

            

    #         if level == 3:

    #             if self.left.left == None:
    #                 self.left.left = value
                    

    #             elif self.left.right == None:
    #                 self.left.right = value
                    

    #             elif self.right.left == None:
    #                 self.right.left = value
                    

    #             elif self.right.right == None:
    #                 self.right.right = value

    #         # if level == 4

    #             # if self.left.left.left == None:

                    

    

    def insert(self, value):
        if self.data:
        
            if self.left is None:
                self.left = value

            elif self.right is None:
                self.right = value

            elif self.left.left is None: 
                self.left.insert(value)

            elif self.left.right is None:
                self.left.insert(value)

            elif self.right.left is None:
                self.right.insert(value)
            
            elif self.right.right is None:
                self.right.insert(value)

        else:
            self.data = value.data

                
            
        
            

        
        
        


    def insert_at(self, value, node):
        pass

    def get_height(self):              
        if self.left == None:
            return 1            
        else:          
            return 1 + self.left.get_height()

    def print_given_level(self, root, level):
        pass
    
    # Traversals


    

    def print_inorder(self): #LPR
        if self.left != None:
            self.left.print_inorder()
        print(self.data)
        if self.right != None:
            self.right.print_inorder()

    def print_preorder(self): #PLR
        print(self.data)
        if self.left != None:
            self.left.print_inorder()
        if self.right != None:
            self.right.print_inorder() 

    def print_postorder(self): #LRP
        if self.left != None:
            self.left.print_postorder() 
        if self.right != None:
            self.right.print_postorder()
        print(self.data)
    
    def sum_root_to_leaf(self, root):
        global sum
        
        if self.left != None:
            self.left.sum_root_to_leaf(self)

        sum += self.data

        if self.right != None:
            self.right.sum_root_to_leaf(self)
        # if self.left == None:
        #     return sum += self.data            
        # else:          
        #     return 1 + self.left.get_height()


    # Symmetric Trees
    def is_tree_symmetric(self, root):
        pass
    
    # Find Largest and Second Largest

    def find_largest(self, root):
        global my_list
        
        if self.left != None:
            self.left.find_largest(self)        
        
        if self.right != None:
            self.right.find_largest(self)
            
        my_list.append(self.data)

        if len(my_list) == self.number_of_items(): 
            print(max(my_list))

    def number_of_items(self):
        number = 0
        number_of_levels = self.get_height()

        for i in range(number_of_levels):
            number += 2**(number_of_levels - i)

        return number

    def find_second_largest(self, root):
        pass

# Instantiating a tree with the root node with value (10)
root = Node(10)

# Our tree look like this now
#        10
#      /    \
#    None   None

# Adding the left child of the root to 34
root.left = Node(24)

# Setting the right child of the root to 89
root.right = Node(42)

# Our tree look like this now
#          10        1
#        /    \
#      24      42     3
#     /   \  /   \
#    7    8   9   11    7
#  
#  7 24 8 10 9 42 11

root.insert(Node(7))
root.insert(Node(8))
# root.insert(Node(9))
# root.insert(Node(11))
# root.insert(Node(12))
root.print_inorder()
# print(root.get_height())

# root.sum_root_to_leaf(root)
# print(sum)

# root.find_largest(root)
