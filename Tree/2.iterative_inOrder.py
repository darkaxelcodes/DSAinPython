def inorder_iterative(root):
  result = ""
  # we will use a list and treat it a s stack using append() and pop()
  # in-order : Left -> Root -> Right
  stack = []
  node = root
  while (len(stack) != 0 or node is not None) :
    if node is not None:
      stack.append(node)
      node = node.left
    else:
      node = stack.pop()
      result += str(node.data) + " "
      node = node.right

  return result