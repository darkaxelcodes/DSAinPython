def find_path(root, sequence):
  path = []
  value = find_path_helper(root, sequence, path)
  if value:
    return True
  else:
    return False
    

def find_path_helper(root, sequence, path):
  if root is None:
    return None
  path.append(root.val)
  if root.left is None and root.right is None:
    if path == sequence:
      return True
  find_path_helper(root.left, sequence, path)
  find_path_helper(root.right,sequence, path)
  path.pop()  
  return path