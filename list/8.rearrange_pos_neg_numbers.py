def rearrange(lst):
    rearranged = ([number for number in lst if number < 0] +
    [number for number in lst if number >= 0])
    return rearranged

'''
we can also do :
lst.sort()
return lst
'''