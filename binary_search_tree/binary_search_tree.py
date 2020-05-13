from queue import QueueFromLinkedList as Queue
from stack import StackFromLinkedList as Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # determine which way to branch to find the node that will serve as the parent
        if value < self.value:

            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
            
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        
        else:
            if self.right:
                return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):

        current_node = self

        while current_node.right:
            current_node = current_node.right
        
        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        fn(self.value)
                
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if self.left:
            self.left.in_order_print(self.left)
        
        print(node.value)

        if self.right:
            self.right.in_order_print(self.right)
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        # hold all nodes in order
        queue = Queue()

        # add current node
        queue.enqueue(node)

        while len(queue) > 0:

            next_in_line = queue.dequeue()
            print(next_in_line.value)

            if next_in_line.left:
                queue.enqueue(next_in_line.left)
            
            if next_in_line.right:
                queue.enqueue(next_in_line.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        
        # hold all nodes in the order they were accessed
        stack = Stack()

        # add curren tnode
        stack.push(node)

        while len(stack) > 0:

            last_added = stack.pop()
            print(last_added.value)

            # go in ascending order by pushing the right branch first
            if last_added.right:
                stack.push(last_added.right)
              
            if last_added.left:
                stack.push(last_added.left)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

tree = BinarySearchTree(15)
tree.insert(10)
tree.insert(12)
tree.insert(22)
tree.insert(19)
tree.insert(55)

# print("contains 18?", tree.contains(18))
# print("contains 19?", tree.contains(19))
# print("max is", tree.get_max())
# tree.for_each(print)

# tree.in_order_print(tree)t
# tree.bft_print(tree)
tree.dft_print(tree)