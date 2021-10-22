from Node import Node
from LinkedList import LinkedList

def length(lst):
    if lst.is_empty():
        return 0
    cur_node = lst.get_head()
    count = 1
    while cur_node.next_element is not None:
        count += 1
        cur_node = cur_node.next_element
    return count
