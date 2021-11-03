import pdb  

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None        
            
    def insert_node(self,value):
        node = Node(value)
        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current =  current.next
            current.next = node           
    
    def print_list(self,head):
        while head != None:
            print(head.value,end="->")
            head = head.next
        print("\n")
                    
def deleteNode(llist, position):
    # Write your code here    
    current = llist 
    prev = None
    counter = 0
    
    if current == None:
        return None    
    else:
        while current != None:
            if counter == position: break
            prev = current 
            current = current.next
            counter = counter+1    

        if current != None and prev: 
            prev.next = current.next
        else:            
            # this is how it should be removed 
            # but for some reasons the object don't get manupulated while removing head
            # insted should return the head completely and print
            current = current.next
            
           
    
        
    

if __name__ == '__main__':
    
    llist = SinglyLinkedList()

    for i in [20,6,2,19,7,4,15,9,3]:        
        llist.insert_node(i)

    position = 0
    # llist.print_list()
    llist1 = deleteNode(llist.head, position)
    llist.print_list(llist.head)
    
