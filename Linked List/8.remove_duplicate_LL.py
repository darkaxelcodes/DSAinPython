'''
Remove Duplicates from LL
We can pick each node and compare it with rest of the elements of the list and remove duplicates
this will take O(n^2)

Or we can use hashing.

Below method uses a list to remove duplicates
'''
from LinkedList import LinkedList
from Node import Node

def remove_duplicates(lst):
    existing = []
    cur = lst.get_head()
    if cur.next_element is None:
        return lst
    prev = cur
    existing.append(cur.data)
    cur = cur.next_element
    while cur:
        if cur.data in existing:
            prev.next_element = cur.next_element
            cur = cur.next_element            
        else:
            existing.append(cur.data)
            prev = cur
            cur = cur.next_element
    return lst


