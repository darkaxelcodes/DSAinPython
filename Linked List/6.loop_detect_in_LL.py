from LinkedList import LinkedList
from Node import Node

#FLoyd's circle detection algorithm
def detect_loop(lst):
    p = q = lst.get_head()
    while p and q and q.next_element:
        p = p.next_element
        q = q.next_element.next_element
        if p == q:
            return True
    return False