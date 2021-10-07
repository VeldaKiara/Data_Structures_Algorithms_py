"""
In this problem, you have to implement the find_sum(lst,k) 
function which will take a number k as input and 
return two numbers that add up to k.
Sample Input
lst = [1,21,3,14,5,60,7,6]
k = 81
Sample Output
lst = [21,60]
"""

#Brute force
def find_sum(lst, k):
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if(lst[i]+lst[j] is k and i is not j):
                return [lst[i], lst[j]]


print(find_sum([1, 2, 3, 4], 5))
"""
This is the most time intensive but intuitive solution. 
Traverse the whole list of size, say s,
for each element in the list and check if any of the two 
elements add up to the given number k. So, using two nested 
for-loops each iterating over the entire list will serve the purpose.

"""

#Sorting the list 
def binary_search(a, item):
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


def find_sum(lst, k):
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return the only if we find an index
        index = binary_search(lst, k -lst[j])
        if index is not -1 and index is not j:
            return [lst[j], k -lst[j]]
"""
While solution #1 is very intuitive, it is not very time efficient.
A better way to solve this challenge is by first sorting the list.
Then for each element in the list, use a binary search to look 
for the difference between that element and the intended sum. 
In other words, if the intended sum is k and the first element 
of the sorted list is a0, then we will do a binary search for k-a0. 
The search is repeated for every ai up to an until one is found.” 
You can implement the binary_search() function however you like, 
recursively or iteratively.
Time Complexity
Since most optimal comparison-based sorting functions take O(nlogn)O(nlogn),
let’s assume that the Python .sort() function takes the same. 
Moreover, since binary search takes O(logn)O(logn) time for a 
finding a single element, therefore a binary search for all n 
elements will take O(nlogn)O(nlogn) time.”
"""

#Moving Indices 
def find_sum(lst, k):
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while (index1 != index2):
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))

"""
The linear scan takes O(n)O(n) and 
sort takes O(n log n)O(nlogn). The time complexity 
becomes O(n log n) + O(n)O(nlogn)+O(n) because the 
sort and the linear scan are done one after the other. 
The overall would be O(n log n)O(nlogn) in the worst case.
"""




