def find_minimum_depth(root):
  if root is None:
    return 0
  l_depth = find_minimum_depth(root.left)
  r_depth = find_minimum_depth(root.right)
  if root:
    return max(l_depth,r_depth)+1


def find_minimum_depth(root):
  if root is None:
    return 0
  q = []
  max_depth = 0
  q.append(root)
  while q:
    max_depth += 1
    for _ in range(len(q)):
      cur = q.pop(0)
      if cur.left:
        q.append(cur.left)
      if cur.right:
        q.append(cur.right)
  return max_depth