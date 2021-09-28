# stack follows method of LIFO

# complexity is o(1)

# example back button in browsers


class Stack:
    def __init__(self):
        self.__stack = []

    def insert(self,value):
        self.__stack.append(value)
        return True

    def isempty(self):
        return True if not self.__stack else False
        
    def pop(self):
        if self.isempty():
            return False
        else:
            self.__stack.pop()
    
    def view(self):
        print(self.__stack)

if __name__ == '__main__':
    stack = Stack()
    stack.pop()
    stack.view()
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)
    stack.insert(4)

    stack.view()

    stack.pop()

    stack.view()
        