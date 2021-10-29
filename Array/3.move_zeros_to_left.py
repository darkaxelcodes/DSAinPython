def move_zeros_to_left(A):
  read = len(A)-1
  write = len(A)-1
  while read >= 0:
    if A[read] != 0:
      A[write] = A[read]
      write -= 1
    read -= 1
  
  for i in range(write+1):
    A[i] = 0
  return A