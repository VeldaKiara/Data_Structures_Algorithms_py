"""
problem statement
Given a list, modify it so that each index stores the product
all  the indices of all elements in the list except the
element at the index itself.

 e.g arr = [1,2,3,4]
 output = [24,12,8,6]
"""

# nested loops
def find_product(lst):
    result = []
    # stores product of all previous values from currentIndex
    left = 1
    for i in range(len(lst)):
        # store current product for index i
        current_product = 1
        # compute product of values to the right of i index of list
        for item in lst[i+1:]:
            current_product = current_product * item
            # currentproduct * product of all values to the left of i index
        result.append(current_product * left)
        # Updating `left`
        left = left * lst[i]
    return result

print(find_product([1,2,3,4]))
print(find_product([2, 5, 9, 3, 6]))
print(find_product([0, 1, 10, 100]))
print(find_product([0, 2, 9, 0, 12, 25]))
# output
# [24, 12, 8, 6]
# [810, 324, 180, 540, 270]
# [1000, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]

#time complexity is O(n​2) 
# because the list is iterated over n(n-1)/2n(n−1)/2 times
#this solution iterates  over the list and calculates the product 
# of all the numbers to the right of the current element as on lines 16 and 18.
#Then it calculates the product of all the elements to the left of the current element 
# line 23. It then multiplies the two products and returns the result line 26.


def find_product(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele

    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]

    return product
print(find_product([1,2,3,4]))
print(find_product([2, 5, 9, 3, 6]))
print(find_product([0, 1, 10, 100]))
print(find_product([0, 2, 9, 0, 12, 25]))
 
# Since this algorithm only traverses over the list twice,
# it’s in linear time, O(n).
#The algorithm for this solution is to first create a new
# list with products of all elements to the left of each element
# as done on lines 48-51. Then multiply each element in that list
# to the product of all the elements to the right of the list by 
# traversing it in reverse as done on lines 53-56
