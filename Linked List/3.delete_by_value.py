from LinkedList import LinkedList
from Node import Node

def delete(lst, value):
    cur_node = lst.get_head()
    prev_node = cur_node
    deleted = False
    if cur_node is not None:
        if cur_node.data is value:
            lst.head_node = cur_node.next_element
            cur_node.next_element = None
            cur_node.data = None
            deleted = True
            return deleted

    while cur_node is not None:
        if cur_node.data is value:
            prev_node.next_element = cur_node.next_element
            cur_node.next_element = None
            cur_node.data = None
            deleted = True
            break
        cur_node = cur_node.next_element
        prev_node = cur_node
    else:
        deleted = False
    return deleted      