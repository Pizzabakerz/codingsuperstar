class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self,data):
        node = Node(data)
        
        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node    
        
def insertNodeAtPosition(llist, data, position):
    # Write your code here
    node = Node(data)        
    i = 0

    while llist.next:        
        if position == i:                        
            node.next = llist.next 
            llist.next = node
            break
        llist = llist.next
        i = i+1    


    
if __name__ == "__main__":

    llist = SinglyLinkedList()

    for i in range(0,10):        
        llist.insert_node(i)
    
    llist_head = insertNodeAtPosition(llist.head, 11, 6)

    