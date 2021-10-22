count = 0
result = None
def find_nth_highest_in_bst(node, n ):
  if node is None or count >= n:
    return None
  else:
    global count
    global result
    res = find_nth_highest_in_bst(node.right, n)
    count += 1
    if count == n:
      result = node    
    res = find_nth_highest_in_bst(node.left, n)
  return result