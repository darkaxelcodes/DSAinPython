left = ""
leaf = ""
right = ""

def left_side(root):
  global left
  if root:
    if root.left:
      left += str(root.data) + " "
      left_side(root.left)
    elif root.right:
      left += str(root.data) + " "
      left_Side(root.right)

def right_side(root):
  global right
  if root:
    if root.right:
      right_side(root.right)
      right += str(root.data) + " "
    elif root.left:
      right_side(root.left)
      right += str(root.data) + " "

def leaf_side(root):
  global leaf
  if root:
    leaf_side(root.left)
    if root.left is None and root.right is None:
      leaf += str(root.data)  + " "
    leaf_side(root.right)

def display_tree_perimeter(root):
  global left
  global leaf
  global right
  if root:
    left_side(root.left)
    leaf_side(root.left)
    leaf_side(root.right)
    right_side(root.right)
  return (str(root.data) + " " + left + leaf + right)
  
  
  
'''
# Iterative Method
def left_side(root, result):
  while root:
    cur_value = root.data
    if root.left:
      root = root.left
    elif root.right:
      root = root.right
    else:
      break
    result += str(cur_value) + ' '

def right_side(root, result):
  stack = []
  while root:
    cur_value = root.data
    if root.right:
      root = root.right
    elif root.left:
      root = root.left
    else:
      break
    stack.append(cur_value)
  while stack:
    result += str(stack.pop()) + ' '

def leaf_side(root):
  if root:
    leaf_side(root.left,result)
    if root.left is None and root.right is None:
      result += root.data + ' '
    leaf_side(root.right,result)

    
def display_tree_perimeter(root):

'''