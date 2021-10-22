def populate_sibling_pointers(root):
  if root is None:
    return None
  q = [root]
  while q:
    cur_node = q.pop(0)
    if cur_node.left:
      q.append(cur_node.left)
    if cur_node.right:
      q.append(cur_node.right)
    if q:
      cur_node.next = q[0]
    else:
      cur_node.next = None
  return root