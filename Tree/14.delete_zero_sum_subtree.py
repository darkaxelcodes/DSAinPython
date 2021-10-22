def delete_zero_sum_subtree_rec(root):
  if root is None:
    return 0
  l_sum = delete_zero_sum_subtree_rec(root.left)
  if l_sum == 0:
    root.left = None
  r_sum = delete_zero_sum_subtree_rec(root.right)
  if r_sum == 0:
    root.right = None
  return (root.data + l_sum + r_sum)

def delete_zero_sum_subtree(root):
  if root is not None:
    sum = delete_zero_sum_subtree_rec(root)
    if sum == 0:
      root = None