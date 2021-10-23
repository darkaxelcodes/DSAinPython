def find_least_common_number(a, b, c):
   i, j, k = 0, 0, 0
   while i < len(a) and j < len(b) and k < len(c):
      if a[i] == b[j] and b[j] == c[k]:
         return a[i]
      if a[i] <= b[j] and a[i] <= c[k]:
         i += 1
      elif b[j] <= a[i] and b[j] <= c[k]:
         j += 1
      elif c[k] <= a[i] and c[k] <= b[j]:
         k += 1
   
   return -1