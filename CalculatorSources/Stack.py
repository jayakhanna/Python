from collections import deque;
import LookupError


# Stack class that will help in implementing Calculator.
class Stack:
    def __init__(self):
        self.stack = deque()

    # Check whether the stack instance is empty.
    def  isEmpty(self):
        if (len(self.stack) < 1):
            return True
        else:
            return False

    # Return the total elements in the stack instance.
    def getlength(self):
        return len(self.stack)

    # Push an element in the stack instance.
    def push(self, item):
        self.stack.append(item)

    # Check the top element in the stack without pop.
    def peek(self):
        length = len(self.stack)
        if (self.isEmpty() is False):
            return self.stack[length -1];
        else:
            return None

    # Remove the element from the stack and return it.
    def pop(self):
        if(self.isEmpty() is False):
            return self.stack.pop()
        else:
            return LookupError.CalcLookupError['EmptyStack']

