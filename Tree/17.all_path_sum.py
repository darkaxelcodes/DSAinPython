def find_paths(root, sum):
  allPaths = []
  find_paths_rec(root, sum, [], allPaths)
  return allPaths

def find_paths_rec(current_node, required_sum, current_path, allPaths):
  if current_node is None:
    return None
  
  current_path.append(current_node.data)

  if current_node.data == required_sum and not current_node.left and not current_node.right:
    print(current_path)
    allPaths.append(list(current_path))
  else:
    find_paths_rec(current_node.left, required_sum - current_node.data, current_path, allPaths)
    find_paths_rec(current_node.right, required_sum - current_node.data, current_path, allPaths)
  
  current_path.pop()