def find_successor(root, key):
  if root is None:
    return None
  # we use a list and treat it as queue. Enque() -> append() | Dequeue() -> q.pop(0)
  q = [root]
  while len(q) > 0:
    if q[0].left is not None:
      q.append(q[0].left)
    if q[0].right is not None:
      q.append(q[0].right)
    if q[0].val == key:
      return q[1]
    q.pop(0).val
  return None