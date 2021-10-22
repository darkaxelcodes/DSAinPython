def are_identical(root1, root2):
  identity = False
  identitiy_left = False
  identity_right = False
  if root1 == None and root2 == None:
    return True
  if root1 is not None and root2 is not None:
    if root1.data == root2.data:
      identity = True
      identity_left = are_identical(root1.left, root2.left)
      identity_right = are_identical(root1.right, root2.right)
  identity = identity and identity_left and identity_right
  return identity