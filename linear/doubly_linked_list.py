class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev= prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add node from the start
    def add_to_first(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        elif self.head:
            # This method creates new node, focus on the arguments passed. 
            # data refers to whichever value this new node has.
            # self.head refers to the next value in the linked list. 
            # As we are adding new value to the beginning of the linked list, current head will be the next node, and the newly created node will become the head.
            node = Node(data, None, self.head)
            # Assign the new node to as the head
            self.head = node
            # Assign prev to next node (previously head)
            node.next.prev = node

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
        current.next = Node(data, current, None)

    # Add node from specific position
    def add_node_pos(self, data, position):
        current = self.head
        length = self.length()

        if current is None:
            raise ValueError('List is empty. Please add new node to the linked list!')
        
        if position == 1:
            node = Node(data, None, self.head)
            # Assign the new node to as the head
            self.head = node
            # Assign prev to next node (previously head)
            node.next.prev = node
        elif position > 1 and position <= length:
            for _ in range(1, position - 1):
                # Remember to iterate always!
                current = current.next
            node = Node(data, current, current.next)
            current.next = node
            node.next.prev = node
            return
        elif position > length: 
            raise ValueError(f"Position cannot be larger than the total length of the linked list. Current length: [{length}].")
        elif position == position < 0:
            raise ValueError("Position entered cannot be negative!")
    
    # Delete node from specific position
    def delete_node(self, position):
        current = self.head
        length = self.length()

        if current is None:
            raise ValueError("List is empty. No nodes to delete!")
        
        if position == 1:
            self.head = current.next
            self.head.prev = None
        elif position > 1 and position <= length:
            for _ in range(1, position - 1):
                current = current.next
            current.next = current.next.next
            current.next.prev = current
            return

    # Delete whole list
    def delete_list(self):
        if self.head is None:
            print('List is empty!')
        self.head = None

    # Get certain node
    def get_node(self, position):
        current = self.head
        length = self.length()

        if current is None:
            raise ValueError('Empty linked list, cannot get any node')
        
        if position == 1:
            print(f"[prev: {current.prev} | data: {current.data} | next: {current.next}]")
        if position > 1 and position <= length:
            for _ in range(1, position):
                current = current.next
            print(f"[prev: {current.prev} | data: {current.data} | next: {current.next}]")

    # Print linked list method
    def print(self):
        length = self.length()
        if not self.head:
            return
        
        # Getting the head of the current node
        current = self.head

        while current:
            # Adding if-else condition so the last node will not have the arror at the end as it's not pointing to any node
            if current.next is not None:
            # Loop through the linked list, current.data is the current.head data, and the current.next holds the next node's memory allocation
                print(f"[prev: {current.prev} | {current.data}: {current} | next: {current.next}]", end=' <--> ')
            else:
                print(f"[prev: {current.prev} | {current.data}: {current} | next: {current.next}]")
            # The next node memory allocation, we assign to current so we can print it while looping.
            current = current.next
        print(f'Current length: {length}')
        
    # Get current length
    def length(self):
        if self.head is None:
            print('List is empty, length is 0!')
            return
        
        current = self.head
        length = 1
        # As long as the while loop returns true, it will keep traversing to next node and add to the length. 
        while current.next:
            current = current.next
            length += 1
        
        return length

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.add_to_first(4)
    ll.add_node(8)
    ll.add_node(-10)
    ll.add_to_first(2)
    ll.add_node_pos(998, 2)
    ll.add_node_pos(11, 4)
    ll.delete_node(2)
    ll.get_node(1)
    # ll.delete_list()
    # ll.print()