def mirror_tree(root):
  if root is None:
    return None
  
  temp_left = root.left
  root.left = root.right
  root.right = temp_left
  mirror_tree(root.left)
  mirror_tree(root.right)

  return root