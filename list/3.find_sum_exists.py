def find_sum(lst, k):
    for number in lst:
        if k-number in lst:
            return ([number,k-number])
    else:
        return None