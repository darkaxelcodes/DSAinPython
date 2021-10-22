import math
def find_second_maximum(lst):
    max1 = lst[0]
    max2 = -math.inf
    for i in range(1,len(lst)):
        if lst[i] > max1:
            max2 = max1
            max1 = lst[i]
        elif lst[i] > max2 and lst[i] != max1:
            max2 = lst[i]
    return max2

        

