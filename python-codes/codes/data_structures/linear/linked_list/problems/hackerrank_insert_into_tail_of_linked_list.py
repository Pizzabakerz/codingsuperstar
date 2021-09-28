class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,item):
        node = Node(item)

        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def print(self):
        while self.head != None:
            print(self.head.item)            
            self.head = self.head.next

if __name__ == "__main__":
    ll = LinkedList()
    for i in range(0,100,5):
        ll.insert(i)
    ll.print()
        
        