from LinkedList import LinkedList
from Node import Node

def find_nth(lst, n):
    l = lst.length()
    cur = lst.get_head()
    if n < l:
        for i in range(l-n):
            cur = cur.next_element
        return cur.data
    return -1

'''
We can also use two pointers
get the idea
implement corner cases as well
'''
'''
def find_nth(lst,n):
    end = lst.get_head()
    nth = lst.get_head()
    for i in range(n):
        end = end.next_element
    while end.next_element:
        end = end.next_element
        nth = nth.next_element
    if nth:
        return nth.data
    return -1
'''