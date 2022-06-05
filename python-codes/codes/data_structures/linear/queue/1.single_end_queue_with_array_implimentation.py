# queue follows method FIFO

# complexity is o(1)

# example ticket booking systems

class Queue:
    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        return True if not self.__queue else False

    def enqueue(self,value):
        # insert element into last postion of queue
        self.__queue.append(value)
        return True

    def dequeue(self):
        # remove element in first position
        if self.isEmpty():
            print("empty")
        else:
            self.__queue.remove(self.peek())

    def peek(self):
        # get first value of queue
        if self.isEmpty():
            return False
        else:
            value = self.__queue[0]
            return value

    def view(self):
        print(self.__queue)


if __name__ == '__main__':
    queue = Queue()
    
    queue.peek()
    queue.dequeue()
    print(queue.isEmpty())
    queue.view()

    queue.enqueue(0)
    queue.enqueue(2)
    print(queue.isEmpty())
    queue.peek()
    
    queue.enqueue(3)
    queue.view()
    queue.peek()
    queue.dequeue()
    queue.view()
    
    queue.enqueue(4)
    queue.view()