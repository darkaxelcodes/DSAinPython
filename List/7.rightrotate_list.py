def right_rotate(lst, k):
    if len(lst) > 0:
        k = k % len(lst)
        for i in range(k):
            temp = lst[-1]
            lst.remove(lst[-1])
            lst.insert(0,temp)
    return lst
'''
rotate in 1 line
return (lst[-k:]+lst[:-k]) 
'''
    