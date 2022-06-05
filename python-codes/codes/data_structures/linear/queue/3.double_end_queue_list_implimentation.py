class DoubleEndQueue:
    def __init__(self):
        self.data = []
    
    def enqueue_front(self,data):
        self.data.insert(0,data)        

    def enqueue_rear(self,data):
        self.data.append(data)

    def dequeue_front(self):
        if self.data == []: return 
        del self.data[0]

    def dequeue_rear(self):
        if self.data == []: return 
        del self.data[-1]
    
queue = DoubleEndQueue()
queue.dequeue_front()
queue.dequeue_rear()
queue.enqueue_front(2)
queue.enqueue_front(3)
queue.enqueue_front(4)
print(queue.data)
queue.enqueue_rear(11)
queue.enqueue_rear(12)
queue.enqueue_rear(13)
print(queue.data)
queue.dequeue_rear()
print(queue.data)
queue.dequeue_front()
print(queue.data)