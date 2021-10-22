from LinkedList import LinkedList
from Node import Node
def insert_at_tail(lst, value):
    new_node = Node(value)
    if lst.get_head() is None:
        lst.head_node = new_node
        return
    cur_node = lst.get_head()
    while cur_node.next_element:
        cur_node = cur_node.next_element
    cur_node.next_element = new_node
    return

    
    