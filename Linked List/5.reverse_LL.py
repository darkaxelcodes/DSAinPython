from Node import Node
from LinkedList import LinkedList

def reverse(lst):
  prev = None
  cur = lst.get_head()
  next = None
  while cur:
    next = cur.next_element
    cur.next_element = prev
    prev = cur
    cur = next
  lst.head_node = prev
  return lst  