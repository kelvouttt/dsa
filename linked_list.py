from exception import *

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # The linked list is empty initially, so head is None.
    def __init__(self):
        self.head = None

    def add_to_first(self, data):
        # This method creates new node, focus on the arguments passed. 
        # data refers to whichever value this new node has.
        # self.head refers to the next value in the linked list. 
        # As we are adding new value to the beginning of the linked list, current head will be the next node, and the newly created node will become the head.
        new_node = Node(data, self.head)
        self.head = new_node

    # We assume add_node method is just to add node from the last of the node
    def add_node(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # Get the existing head as the current node
        current = self.head

        # This while loop checks if there is next node, if there is --> loop to the next node
        while current.next:
            current = current.next
        # If there is no next node, set the next node as Node(data, None), focus on how we create new node with pointer 'None' as the newly created node will be at the last. 
        current.next = Node(data, None)

    def add_specific_position(self, data, position):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        # Get current head in the node
        current = self.head 
        curr_length = self.length()
        
        if position == 1:
            node = Node(data, current)
            self.head = node
            return
        elif position > curr_length:
            raise ValueError(f"Position cannot be larger than the total length of the linked list. Current length: [{curr_length}].")
        else:
            for _ in range(1, position - 1):
                current = current.next
                break
            
            node = Node(data, current.next)
            current.next = node
            node.next = current.next.next
            return
        
    def length(self):
        if self.head is None:
            raise EmptyNode("List is empty. Please add new node to the linked list!")
        
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        return length
        
    def print(self):
        if not self.head:
            print("Linked list is empty")
            return
        
        # Getting the head of the current node
        current = self.head

        while current:
            # Adding if-else condition so the last node will not have the arror at the end as it's not pointing to any node
            if current.next is not None:
            # Loop through the linked list, current.data is the current.head data, and the current.next holds the next node's memory allocation
                print(f"({current.data}, {current.next})", end=' --> ')
            else:
                print(f"({current.data}, {current.next})")
            # The next node memory allocation, we assign to current so we can print it while looping.
            current = current.next

                     
if __name__ == '__main__':
    ll = LinkedList()
    ll.add_to_first(2)
    ll.add_node(-10)
    ll.add_specific_position(8, 2)
    ll.add_specific_position(10,3)
    ll.print()