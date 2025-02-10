class Node:
    # Given a circular linked list, we can initially set the 'next' value as None. 
    # We can point to the next value to the self.head after the creation of Node object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_to_first(self, data):
        # Here we instantiate a Node object by only passing data as arguments, this means that the next is None.
        node = Node(data)
        if self.head is None:
            # First step we check if the linked list is empty, we will set the new node created as the head.
            self.head = node
            # Remember that the Node object we create still has the next value of None. 
            # Here, after setting the new Node object as the head of the linked list, we set the next value to point to itself. 
            node.next = node
        else:
            current = self.head
            # If the linked list is not empty, we traverse until the end of the linked list. 
            # If the last Node object has its next value pointing to head, it means we have traversed until the end of linked list, assigning to current below. 
            while current.next != self.head:
                current = current.next

            # Here, we instantiate new Node object, but this time, we set the 'next' value as the current head in the linked list. 
            new_node = Node(data, self.head)
            # Set the new node as the head of the linked list.
            self.head = new_node
            # As we have 'current' at end of the linked list, we can set its 'next' value to the new node we instantiate above so it forms a circular linked list.
            current.next = new_node

    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = node

        current = self.head
        while current.next != self.head:
            current = current.next
        
        current.next = node
        node.next = self.head

    def add_node_pos(self, data, position):
        length = self.length()

        if self.head is None:
            raise ValueError('Linked list is empty, position not found. Use add_node() or add_to_first() for an empty list.')
        
        current = self.head
        while current.next != self.head:
            current = current.next
        if position > 1 and position <= length:
            for _ in range(1, position - 1):
                current = current.next
            print(current.data)

            node = Node(data, current.next)
            current.next = node
            return

    def length(self):
        if self.head is None:
            raise ValueError("List is empty!")
        
        current = self.head
        length = 1

        while True:
            current = current.next
            length += 1
            if current == self.head:
                break

        return length

    def print(self):
        if not self.head:
            print("Linked list is empty")
            return
        
        # Getting the head of the current node
        current = self.head
        
        # We create an infinity loop here so we can traverse to the end of list.
        while True:
            print(f"({current.data}: [{current}], {current.next})", end=' --> ')
            # This is where the traversing occurs.
            current = current.next
            # Once we evaluate that the 'next' value of the node refers to head.
            # We break out of the loop as it means we have reached the end of list. 
            if current == self.head:
                # Once we evaluate that the last node points to self.head
                # Print the head at the most back of the linked list.
                print(f"(HEAD >> {current.data}: [{current}])")
                break
            
if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.add_to_first(10)
    cll.add_node(-9)
    cll.add_node_pos(-51, 2)
    cll.print()
    print(f"Length is: {cll.length()}")
