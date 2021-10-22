def find_product(lst):
    # if we have non zero list, we can multiply all the elements
    # store result in a variable. 
    # then divide the variable by each element iteratively,
    left = 1
    product = []
    for number in lst:
        product.append(left)
        left = left * number
    right = 1
    for i in range(len(lst)-1,-1,-1):
        product[i] *= right
        right *= lst[i]
    return product