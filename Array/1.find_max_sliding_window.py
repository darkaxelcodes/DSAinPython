def find_max_sliding_window(arr, window_size):
  result = []
  if len(arr) == 0:
    return result
  
  if window_size > len(arr):
    return result
    
  q = []
  for i in range(window_size):
    q.append(arr[i])
  result.append(max(q))
  q.pop(0)
  cur_pos = window_size
  while cur_pos < len(arr):
    q.append(arr[cur_pos])
    result.append(max(q))
    q.pop(0)
    cur_pos += 1
  return result