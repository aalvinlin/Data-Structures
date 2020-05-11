# copy of Node, LinkedList classes to use with Queue class

class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:

    def __init__(self):
        self.head = None

    def add_to_end(self, value):

        new_node = Node(value)

        # list is empty: start a new list
        if not self.head:
            self.head = new_node

        else:
            current_node = self.head

            while current_node.next_node:
                current_node = current_node.get_next()

            current_node.set_next(new_node)

    def remove_from_head(self):

        # list is empty: return None
        if not self.head:
            return None

        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            return head_value