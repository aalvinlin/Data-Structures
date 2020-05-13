"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __str__(self):
        return str(self.value)


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):

        output = []
        current_node = self.head
        
        while current_node:
            output.append(f"prev: {current_node.prev} <- {current_node.value} -> next: {current_node.next}")
            current_node = current_node.next
        
        return "\n".join(output)


    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        # wrap given value in a ListNode
        new_head = ListNode(value)

        # if current DLL is empty, set head and tail to the new value
        if not self.head:
            self.head = new_head
            self.tail = new_head
            return

        # point new ListNode to existing head
        new_head.next = self.head

        # reassign the prev pointer of the old head
        new_head.next.prev = self.head

        # reassign pointer to new head
        self.head = new_head

        # increment length by 1
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):

        # prevent trying to remove from an empty DLL
        if not self.head:
            return None

        # store current head value
        removed_value = self.head

        # move the current head pointer
        self.head = self.head.next

        # set the second element's prev pointer to None
        self.head.prev = None

        # decrease length of list by one
        self.length -= 1

        return removed_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        
        # wrap given value in a ListNode
        new_tail = ListNode(value)

        # if current DLL is empty, set head and tail to the new value
        if not self.head:
            self.head = new_tail
            self.tail = new_tail
            return

        # find current tail
        current_node = self.head

        while current_node.next:
            current_node = current_node.next

        # add pointer to new ListNode
        current_node.next = new_tail

        # set prev pointer to old tail
        current_node.next.prev = current_node
        self.tail = current_node

        # increment length by 1
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        
        # prevent trying to remove from an empty DLL
        if not self.head or not self.tail:
            return

        # store current tail value
        removed_value = self.tail

        # move the current tail pointer
        self.tail = self.tail.prev

        # set the second element's prev pointer to None
        self.tail.next = None

        # decrease length of list by one
        self.length -= 1

        return removed_value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        
        # store a reference to this node
        node_to_move = node

        # delete and rewire prev and next pointers
        node.delete()

        # add as new head
        self.add_to_head(node_to_move)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):

        # store a reference to this node
        node_to_move = node

        # delete and rewire prev and next pointers
        node.delete()

        # add as new tail
        self.add_to_tail(node_to_move)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):

        if not node.prev:
            self.remove_from_head(node)
        elif not node.tail:
            self.remove_from_tail(node)
        else:
            node.delete()
            self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):

        current_node = self.head
        current_max = self.head.value

        while current_node.next:
            current_node = current_node.next

            if current_node.value > current_max:
                current_max = current_node.value

        return current_max

test = DoublyLinkedList()
test.remove_from_head()
test.remove_from_tail()

test.add_to_tail(1)
test.add_to_tail(2)
test.add_to_tail(3)
test.add_to_tail(4)
test.add_to_tail(5)
print(test)

print("======================")

print("where is the head?", str(test), print(test.head))
print("where is the tail?", test.tail)


test.add_to_head(10)
test.add_to_head(9)
test.add_to_head(8)
test.add_to_head(7)
test.add_to_head(6)
test.add_to_tail(500)
test.add_to_head(200)

test.remove_from_tail()

print("===========")
print(test)