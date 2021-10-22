from LinkedList import LinkedList

# We can either find length of LL in one iteration, then do len/2 or len+1/2
# based on even/odd length and traverse the LL again to that element.

# Or we an use the slow and fast pointer method. One jumps 2 at a time other 1 at a time.
# by the time the fast pointer reaches end
# the slow one is in mid

def find_mid(lst):
    fast = lst.get_head()
    if fast.next_element is None:
        return fast.data
    slow = fast
    fast = fast.next_element.next_element
    while fast:
        slow = slow.next_element
        fast = fast.next_element
        if fast:
            fast = fast.next_element
    if slow:
        return slow.data
