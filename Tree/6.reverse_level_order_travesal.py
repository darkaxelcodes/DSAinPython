def level_order_traversal(root):
  result = ""
  if root is None:
    return None
  # we use a list and treat it as queue. Enque() -> append() | Dequeue() -> q.pop(0)
  q = [root]
  while len(q) > 0:
    if q[0].left is not None:
      q.append(q[0].left)
    if q[0].right is not None:
      q.append(q[0].right)
    result = str(q.pop(0).data) + " " + result
  return result
  
# To print each level in different line  
def level_order_traversal(root):
  result = ""
  if root is None:
    return None
  # we use a list and treat it as queue. Enque() -> append() | Dequeue() -> q.pop(0)
  q = []
  q.append(root)
  q.append(None)
  while len(q) > 0:
    if q[0] == None:
      q.pop(0)
      print()
      if len(q) > 0:
        q.append(None)
    else:
      if q[0].left is not None:
        q.append(q[0].left)
      if q[0].right is not None:
        q.append(q[0].right)
      result = str(q.pop(0).data) + " " + result
  return result