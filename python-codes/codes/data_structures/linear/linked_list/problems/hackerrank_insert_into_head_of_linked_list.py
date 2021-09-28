class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self,item):
        node = Node(item)
        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.next = current   

    def print(self):
        while self.head != None:
            print(self.head.item)
            self.head = self.head.next


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(0,100,5):
        ll.insert_head(i)
    ll.print()