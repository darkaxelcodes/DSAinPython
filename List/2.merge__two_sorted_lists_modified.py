def merge_lists(lst1, lst2):
    in_lst1 = 0
    in_lst2 = 0
    while in_lst1 < len(lst1) and in_lst2 < len(lst2):    
        if lst1[in_lst1] > lst2[in_lst2]:
            lst1.insert(in_lst1,lst2[in_lst2])
            in_lst1 += 1
            in_lst2 += 1
        else:
            in_lst1 += 1
    if in_lst2 < len(lst2):
        lst1.extend(lst2[in_lst2:])
    return lst1  