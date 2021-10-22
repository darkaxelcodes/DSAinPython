def max_min(lst):
    if len(lst)>1:
        for i in range(0,len(lst),2):
            print("before: ", lst)
            temp = lst[len(lst)-1]
            lst.remove(temp)
            lst.insert(i,temp)
            print("after ",lst)
    print("--------------")
    return lst