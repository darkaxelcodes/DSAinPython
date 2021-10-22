from Stack import MyStack
class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()

    def enqueue(self, value):
        self.main_stack.push(value)        

    def dequeue(self):
        self.aux_stack = MyStack()
        while not self.main_stack.is_empty():
            self.aux_stack.push(self.main_stack.pop())
        front = self.aux_stack.peek()
        self.aux_stack.pop()
        while not self.aux_stack.is_empty():
            self.main_stack.push(self.aux_stack.pop())
        return front