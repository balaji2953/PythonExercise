class Node:
    
    def __init__(self, value, next=None, prev=None):
        self.value = value 
        self.next = next
        self.prev = prev
    

class DoublyLinkedList:

    def __init__(self, value):
       self.head = Node(value) if value is not None else None
    
    def display(self):
        if self.head is None:
            print("Empty List")
            return
    
        current = self.head
        while current.next:
            print(current.value, end=" <-> ")
            current = current.next
        print(current.value)
    

    def insert_at_beginning(self, value):

        if self.head is None:
            self.head = Node(value)
            return
        
        new_node = Node(value)
        new_node.next = self.head
        new_node.next.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        current = self.head
        
        while current.next:
            current = current.next
        
        new_node = Node(value)
        new_node.prev = current
        current.next = new_node

list1 = DoublyLinkedList(1)
list1.display()

list1.insert_at_beginning(0)
list1.display()
list1.insert_at_beginning(2)
list1.display()
list1.insert_at_beginning(5)
list1.display()


list1.insert_at_end(10)
list1.display()