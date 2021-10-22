class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
    # used in some questions
    self.next = None
    self.parent = None
    self.count = None