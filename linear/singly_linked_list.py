class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # The linked list is empty initially, so head is None.
    def __init__(self):
        self.head = None

    # Add node from the start
    def add_to_first(self, data):
        # This method creates new node, focus on the arguments passed. 
        # data refers to whichever value this new node has.
        # self.head refers to the next value in the linked list. 
        # As we are adding new value to the beginning of the linked list, current head will be the next node, and the newly created node will become the head.
        new_node = Node(data, self.head)
        self.head = new_node

    # Add node from the end
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

    # Add node from specific position
    def add_node_pos(self, data, position):
        # Get current head in the node
        current = self.head 
        
        # Get current length of linked list
        curr_length = self.length()

        # If user enters 1, this is the same as adding to beginning (continue below...)
        if position == 1:
            # Create new node which points to the current head of the list
            node = Node(data, current)
            # After creating the new node, we change the value of current head to the newly created node
            self.head = node
            return
        # If position entered is bigger than actual length of list, will raise an error
        elif position > curr_length:
            raise ValueError(f"Position cannot be larger than the total length of the linked list. Current length: [{curr_length}].")
        else:
            # Underscore variable as we don't care about it, the loop is purely so we can traverse through the list.
            for _ in range(1, position - 1):
                current = current.next
            
            node = Node(data, current.next)
            current.next = node
            return
        
    # Delete node from certain position
    def delete_node(self, position):
        # Get current head of node and assign to variable
        current = self.head
        length = self.length()

        # Check if linked list is empty
        if current is None:
            raise ValueError("List is empty. No nodes to delete!")
        
        # If position is 1, we can assign the next node in the list as head. Python's GC will handle the deleted node as it is no longer referenced
        if position == 1:
            self.head = current.next
        # For position != 1 and lesser than total length, we can loop just before the node we wish to remove. 
        # Reference the next node of 'current' to next.next, imagine if we skip referencing the deleted node, and instead reference the one node after.
        elif position > 1 and position <= length:
            for _ in range(1, position - 1):
                current = current.next
            current.next = current.next.next

    # Delete the whole linked list
    def delete_list(self):
        if self.head is None:
            raise  ValueError("List is empty. Nothing to delete!")
        else:
            self.head = None
                    
    def length(self):
        if self.head is None:
            raise ValueError("List is empty. Please add new node to the linked list!")
        
        current = self.head
        length = 1
        # As long as the while loop returns true, it will keep traversing to next node and add to the length. 
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
                print(f"({current.data}: [{current}], {current.next})", end=' --> ')
            else:
                print(f"({current.data}: [{current}], {current.next})")
            # The next node memory allocation, we assign to current so we can print it while looping.
            current = current.next

if __name__ == '__main__':
    pass