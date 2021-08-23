"""
problem statement
Implement a function findMinimum(lst) which finds the smallest number in the given list
e.g 
arr = [9,2,3,6]
output = 2
"""
def find_minimum(arr):
    # arr[0] is the element in the first index 
    v = arr[0]
    for item in arr:
        if item < v:
            v = item
    return v
            
print(find_minimum([100, 12, 34, 40]))
print(find_minimum([4, 5, 0, 3, 6]))

"""
In this solution we Keep Track of currentMinimum while 
traversing each index of array 
and compare currentMinimum with each index of array.
Since the entire list is iterated over once,this algorithm is in linear time, O(n).
The above solution is not optimal since it does not account if the list is empty
"""

def find_minimum(arr):
    if (len(arr) <= 0):
        return None
    v = arr[0]
    for i in arr:
        # update if found a smaller element
        if i < v:
            v = i
    return v
print(find_minimum([9, 2, 3, 6]))
print(find_minimum([100, 12, 34, 40]))
print(find_minimum([4, 5, 0, 3, 6]))
print(find_minimum([]))

"""
output
2
12
0
None
"""
