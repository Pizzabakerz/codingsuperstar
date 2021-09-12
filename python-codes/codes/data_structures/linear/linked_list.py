# it stores data and address

# complexity is o(n)

# undo functions in softwares

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
        
        if self.head == None:
            self.head = node
        else:
            current = self.head                        

            while current.next:                                
                current = current.next                
            
            current.next = node
        
        self.size += 1
    
    def view_list(self):    
        # # Print the linked list item
        while self.head != None:
            print(self.head.item, end="->")
            self.head = self.head.next
    
    def get_list_size(self):
        print(self.size)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_item(1)
    linked_list.add_item(2)
    linked_list.add_item(3)
    linked_list.add_item(4)
    linked_list.add_item(5)
    linked_list.add_item(6)
    linked_list.add_item(7)
    linked_list.get_list_size()
    linked_list.view_list()

    # # Assign item values
    # linked_list.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # # Connect nodes
    # linked_list.head.next = second
    # second.next = third

    
    
    # print()