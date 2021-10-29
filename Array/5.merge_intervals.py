'''
Given an array (list) of interval pairs as input where each interval has a start and end timestamp.
The input array is sorted by starting timestamps. 
You are required to merge overlapping intervals and return a new output array.
Consider the input array below. 
Intervals (1, 5), (3, 7), (4, 6), (6, 8) are overlapping so they should be merged to one big interval (1, 8). 
Similarly, intervals (10, 12) and (12, 15) are also overlapping and should be merged to (10, 15).

'''


class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

def merge_intervals(v):
  result = []
  #new_start,new_end = v[0].first, v[0].second
  #new_element = Pair(new_start,new_end)
  result.append(v[0])
  for i in range(1, len(v)):
    if v[i].first <= result[-1].second:
      result[-1].second = v[i].second
    else:
      result.append(v[i])  
  return result