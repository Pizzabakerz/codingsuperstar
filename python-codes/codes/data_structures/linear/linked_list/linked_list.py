# it stores data and address

# complexity is o(n)

# undo functions in softwares
import pdb

class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_item(self,item):
        node = Node(item)
        current = None
        # this if the node is null the the current element is place where the value to be inserted
        if self.head == None:
            self.head = node
        else:
            # if there is a head node we are moving from the first node to insert at the last
            # in order to do that we take current node as head node and move from left to right
            # and then once we are at the last node then we insert it to the last
            current = self.head                        
            
            # pdb.set_trace()
            while current.next:                                
                current = current.next                
            
            current.next = node
        
        self.size += 1
    
    def add_item_prefix(self,value):
        node = Node(value)
        # pdb.set_trace()
        current = self.head

        if self.head == None:
            self.head = node
        else:
            self.head = node
            self.head.next = current
        self.size += 1

    def add_item_mid(self,value,after):        
        node = Node(value)
        current = None
        if self.head == None:
            self.head = node
        elif self.head.item == after:
            node.next = self.head.next
            self.head.next = node            
        else:
            current = self.head
            while current.next:                     
                current = current.next
                # pdb.set_trace()
                if current.item == after:                    
                    node.next = current.next
                    current.next = node
                    break
        
        self.size += 1                                    

    def view_list(self):    
        # # Print the linked list item
        while self.head != None:
            print(self.head.item, end="->")
            self.head = self.head.next
    
    def get_list_size(self):
        print("\n",self.size)


if __name__ == '__main__':
    linked_list = LinkedList()
    
    linked_list.add_item(1)
    linked_list.add_item(2)
    linked_list.add_item(3)        
    linked_list.add_item_mid(11,3)
    # linked_list.add_item(4)
    # linked_list.add_item(5)
    # linked_list.add_item(6)
    # linked_list.add_item(7)
    
    linked_list.view_list()
    # linked_list.add_item_prefix(1)
    # linked_list.add_item_prefix(2)
    # linked_list.add_item_prefix(3)    
    linked_list.add_item_prefix(5)    
    linked_list.add_item_prefix(6)
    linked_list.add_item_mid(10,6)    
    linked_list.add_item_prefix(7)    
    linked_list.add_item_prefix(8)
    linked_list.view_list()

    linked_list.get_list_size()
    