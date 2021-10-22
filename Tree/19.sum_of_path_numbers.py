def find_sum_of_path_numbers(root):
  all_path_sum = 0
  all_paths = []
  current_path = ""
  find_sum_of_path_numbers_helper(root, current_path, all_paths)
  for path in all_paths:
    all_path_sum += path
  return all_path_sum

def find_sum_of_path_numbers_helper(node, current_path, all_paths):
  if node is None:
    return None
  if node:
    current_path += str(node.val)
    if node.left:
      find_sum_of_path_numbers_helper(node.left, current_path, all_paths)
    if node.right:
      find_sum_of_path_numbers_helper(node.right, current_path, all_paths)

    if int(current_path) not in all_paths and not node.left and not node.right:
      all_paths.append(int(current_path))
    current_path = current_path[:-1]