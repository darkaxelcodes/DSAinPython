def find_max_sum_sublist(lst): 
  if len(lst)<1:
    return 0
  else:
    prev_max = lst[0]
    curr_max = lst[0]
    length = len(lst)
    for i in range(1, length):
      if prev_max < 0:
        prev_max = lst[i]
      else:
        prev_max += lst[i]
      if curr_max < prev_max:
        curr_max = prev_max
  return curr_max