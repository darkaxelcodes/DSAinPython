# using recursion
def find_minimum_depth(root):
  global min_depth
  if root is None:
    return -1
  l_depth = find_minimum_depth(root.left)
  r_depth = find_minimum_depth(root.right)
  if root:
    if l_depth == -1 and r_depth == -1:
      return min(l_depth,r_depth) + 2
    elif l_depth == -1 and r_depth > -1:
      return r_depth + 1
    else:
      return l_depth + 1
      
# using level order traversal

def find_minimum_depth(root):
  if root is None:
    return 0
  q = []
  min_depth = 0
  q.append(root)
  while q:
    min_depth += 1
    for _ in range(len(q)):
      cur = q.pop(0)
      if not cur.left and not cur.right:
        return min_depth
      if cur.left:
        q.append(cur.left)
      if cur.right:
        q.append(cur.right)