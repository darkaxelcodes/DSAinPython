'''
For each element ii in a list, the function finds the first element to its right 
which is greater than element ii. 
If for any element such a value does not exist, the answer is -1.
'''
from Stack import MyStack

def next_greater_element(lst):
    aux_stack = MyStack()
    aux_stack.push(-1)
    res = []
    for i in range(len(lst)-1,-1,-1):
        if lst[i] < aux_stack.peek():
            res.insert(0,aux_stack.peek())
        else:
            while aux_stack.size() > 1 and lst[i] > aux_stack.peek():
               aux_stack.pop()
            res.insert(0,aux_stack.peek())
        aux_stack.push(lst[i]) 
    return res
