"""
Given an array, find the contiguous sublist with the largest sum.
Given an integer list, return the maximum sublist sum. 
The list may contain both positive and 
negative integers and is unsorted.

e.g  lst = [ -4, 2, -5, 1, 2, 3, 6, -5, 1]
output: 12
"""
#Kadane's algorithm
def find_max_sum_sublist(lst): 
  if (len(lst) < 0):
    return 0
  current_max = lst[0]
  global_max = lst[0]
  len_array = len(lst)
  for i in range(1, len_array):
    if current_max < 0:
      current_max = lst[i]
    else:
      current_max += lst[i]
    if global_max < current_max:
      global_max = current_max
  return global_max
print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))

"""The basic idea of Kadane’s algorithm is to scan the entire
list and at each position find the maximum sum of the sublist
ending there.
This is achieved by keeping a current_max for the current
list index and a global_max. The algorithm is as follows:

current_max = A[0]
global_max = A[0]
for i = 1 -> size of A
    if current_max is less than 0
        then current_max = A[i]
    otherwise 
        current_max = current_max + A[i]
    if global_max is less than current_max 
        then global_max = current_max
The solution above only finds the maximum contiguous 
sum in the list; however, it can easily be modified 
to track the starting and ending indexes of this sublist.

Let’s run through an example to understand how it works. Initially, 
the current_max and global_max are both set to the value at A[0], 
that is, -4:
"""
