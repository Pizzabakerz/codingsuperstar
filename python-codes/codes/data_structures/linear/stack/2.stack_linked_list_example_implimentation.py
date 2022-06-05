class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None        
    
    def push(self,value):
        node = Node(value)
        current = None
        if self.head == None:
            self.head = node
        else:            
            current = node
            current.next = self.head
            self.head = current

    def pop(self):
        if self.head != None:
            temp = self.head
            self.head = temp.next
        else:
            print("stack empty")

    def peek(self):
        print(self.head.data)

    def printStack(self):

        current = self.head
        while current != None:
            print(current.data)
            current = current.next

stack = StackLinkedList()
stack.pop()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.printStack()
stack.pop()
print("after delete")
stack.printStack()

print("peek data")
stack.peek()