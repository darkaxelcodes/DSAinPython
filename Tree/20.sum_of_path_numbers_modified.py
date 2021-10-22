def find_sum_of_path_numbers(root):
  all_path_sum = 0
  return find_sum_of_path_numbers_helper(root, all_path_sum)
  

def find_sum_of_path_numbers_helper(node, all_path_sum):
  if node is None:
    return 0
  all_path_sum = all_path_sum * 10 + node.val
  if node.left is None and node.right is None:
    return all_path_sum
  return find_sum_of_path_numbers_helper(node.left, all_path_sum) + find_sum_of_path_numbers_helper(node.right, all_path_sum)
    