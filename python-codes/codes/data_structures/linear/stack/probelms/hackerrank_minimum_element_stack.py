# https://www.hackerrank.com/challenges/maximum-element/problem

# 1 x  -Push the element x into the stack.
# 2    -Delete the element present at the top of the stack.
# 3    -Print the maximum element in the stack.


import pdb
import numpy as np

class Stack:
    def __init__(self):
        self.stack = np.array([])

    def insert(self,data):
        self.stack.append(int(data))
    
    def delete(self):        
        if self.stack != []: 
            self.stack.pop()
            
            
def getMax(list_of_operations):
    # Write your code here
    stack_object  = Stack()    
    get_max = [] 
    for operation in list_of_operations:
        ops = operation[0]
        if ops == "1":
            # Push the element x into the stack.
            stack_object.insert(operation[1::])
        elif ops == "2":
            # Delete the element present at the top of the stack.
            stack_object.delete()
        elif ops == "3":
            highest = None
            last = len(stack_object.stack)-1
            first = 0
            
            for value in stack_object.stack:
                if highest == None:
                    highest = value
                else:
                    if highest < value: highest = value                            
            get_max.append(highest)
            
    return get_max


if __name__ == "__main__":
    stack  = Stack()
    # stack.delete()
    # stack.insert(1)
    # stack.insert(2)
    # stack.insert(3)
    # stack.insert(4)
    # stack.delete()
    # stack.insert(10)
    # stack.print_stack()
    # print(stack.size)
    list_operation = ['1 97','2','1 20','2','1 26','1 20','2','3','1 91','3']
    print(getMax(list_operation))