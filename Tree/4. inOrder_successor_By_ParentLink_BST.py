def min_bst(root):
  if root is None:
    return None
  while root.left is not None:
    root = root.left
  return root

def successor_by_parent(node):
  if node is None:
    return None
  if node.right is not None:
    return min_bst(node.right)
  while node.parent is not None:
    if node.parent.left == node:
      return node
    node = node.parent
  return None

def find_successor(root, d):
  successor = None
  if root is None:
    return None
  while root is not None:
    if root.data < d:
      root = root.right
    elif root.data > d:
      root = root.left
    else:
      return successor_by_parent(root)
  return None