
def count_paths(root, S):  
  current_path = []  
  return (count_paths_helper(root, S,  current_path))  

def count_paths_helper(root, S, current_path):
  if root is None:
    return 0

  path_count = 0
  sums = 0
  current_path.append(root.val)  
  for i in range(len(current_path)-1, -1, -1):
    sums += current_path[i]
    if sums == S:
      path_count += 1  
  path_count += count_paths_helper(root.left, S,  current_path)   
  path_count += count_paths_helper(root.right, S,  current_path)
  current_path.pop()
  return path_count