def min_bst(root):
  if root is None:
    return None
  while root.left is not None:
    root = root.left
  return root

def inorder_successor_bst(root, d):
  successor = None
  if root is None:
    return None
  while root is not None:
    if root.data < d:
      root = root.right
    elif root.data > d:
      successor = root
      root = root.left
    else:
      if root.right is not None:
        successor = min_bst(root.right)
      break
  return successor