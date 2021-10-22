# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

from Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        self.main_stack = MyStack()
        self.min_stack = MyStack()

    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty():
            self.min_stack.push(value)
        elif value < self.min_stack.peek():
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    def min(self):
        return self.min_stack.peek()

