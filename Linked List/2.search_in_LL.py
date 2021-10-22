from Node import Node
from LinkedList import LinkedList

def search(lst, value):
    cur_node = lst.get_head()
    if cur_node.data == value:
        return True
    while cur_node.next_element:
        if cur_node.data == value:
            return True
        else:
            cur_node = cur_node.next_element
    return False
    
