prev = -1
def is_bst(root):
  # in a BST, IN order travesrsal is always sorted.
  # So we keep a track of prev and currenct, if cur >= prev its fine
  if root is None: 
    return True
  global prev
  if root:
    if is_bst(root.left) == False:
      return False
    
    if prev > root.data and prev != -1:
      return False
    prev = root.data
    
    if is_bst(root.right) == False:
      return False

  return True