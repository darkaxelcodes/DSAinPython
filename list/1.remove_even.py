def remove_even(lst):
    for item in lst:
        if item%2 == 0:
            lst.remove(item)
    return lst