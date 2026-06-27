class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

class SingleLinkedList():

    def __init__(self, head = None):
        self.head = head

    def new_node(self, value):
        return Node(value)

    # Add new value at end
    def append(self, value):
        new_node = self.new_node(value)
        
        if self.head is None:
            self.head = self.new_node
            return

        current = self.head
        
        while current.next:
            current = current.next
        
        current.next = new_node
    # Add value at beginning
    def insert_at_beginning(self, value):
        new_node = self.new_node(value)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        return

    # Insert at position 
    def insert_at_position(self, pos, value):

        if pos == 0:
            self.insert_at_beginning(value)
            return
    
        new_node = Node(value)
        current = self.head
        
        for _ in range(pos-1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
             
   
    # Traversal -> Visit every node once
    def traversal(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
    
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
        
    def delete_end(self):
        
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
        
        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
    
    def search(self, key):

        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def length(self):

        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

list1 = SingleLinkedList(Node(1))
list1.append(2)
list1.append(3)
list1.traversal()          # 1->2->3->None        O(n)

list1.insert_at_beginning(0)
list1.traversal()          # 0->1->2->3->None     O(1)

list1.insert_at_position(2, 2)
list1.traversal()          # 0->1->2->2->3->None  O(n)

list1.delete_beginning()
list1.traversal()          # 1->2->2->3->None     O(1)

list1.delete_end()
list1.traversal()          # 1->2->2->None        O(n)

print(list1.search(2))     # True                 O(n)

print(list1.length())      # 3                    O(n)
