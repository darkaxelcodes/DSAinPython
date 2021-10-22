def find_level_averages(root):
  result = []
  average = []
  if root is None:
    return None

  q = []
  q.append(root)
  q.append(None)

  while len(q) > 0:
    if q[0] == None:
      q.pop(0)
      sum = 0
      for i in result:
        sum += i
      average.append(sum/len(result))
      result = []
      if len(q) > 0:
        q.append(None)
    else:
      if q[0].left is not None:
        q.append(q[0].left)
      if q[0].right is not None:
        q.append(q[0].right)
      result.append(q.pop(0).data)
  return average