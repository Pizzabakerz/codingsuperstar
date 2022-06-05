class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class QueueLinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue(self,data):
        node = Node(data)
        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head            
            while current.next != None:                
                current = current.next
            current.next = node

    def dequeue(self):
        if self.head != None:
            temp = self.head 
            self.head = temp.next
        else:
            print("queue empty")
    
    def printQueue(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

queue = QueueLinkedList()
queue.dequeue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.printQueue()
queue.dequeue()
queue.dequeue()
print("after dequeue")
queue.printQueue()