"""
Given a list, can you rotate its elements by one index from right to left

Implement a function right_rotate(lst, k) 
which will rotate the given list by k. 
This means that the right-most elements will appear 
at the left-most position in the list and so on. 
You only have to rotate the list by one element at a time.

e.g lst = [10,20,30,40,50]
n = 3
output
lst = [30,40,50,10,20]
"""
# abs takes single argument and returns absolute value of it
#sol1
def right_rotate(lst, k): 
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotatedList = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotatedList.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotatedList.append(lst[item])
    return rotatedList


print(right_rotate([10, 20, 30, 40, 50], abs(3)))


#sol2
#list slicing elements and adding the first element to the end
def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(right_rotate([10,20,30,40,50],3))
