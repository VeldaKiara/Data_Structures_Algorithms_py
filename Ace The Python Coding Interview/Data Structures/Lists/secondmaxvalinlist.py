"""
Implement a function find_second_maximum(lst) which
returns the second largest element in the list.
e.g [9,2,3,6]
output is 6
"""
# def find_second_maximum(lst):
#     max = float('-inf')
#     secondmax = float('-inf')
#     for number in lst:
#         if number > max:
#             secondmax = max
#             max = number
#         elif number > secondmax:
#             secondmax = number
#     return secondmax
            
#sorting and index sol, remember to take care of edge 
# cases like duplicate values
def find_second_maximum(lst):
    alst = []
    [alst.append(i)for i in lst if i not in alst]
    alst.sort()
    if len(alst) >= 2:
        return alst[-2]
    else:
        return None
print(find_second_maximum([9, 2, 3, 6,7,5]))
print(find_second_maximum([2,4,1,2,3,4])) 

#traversing the list of elements twice
#The time complexity of the solution is O(n)
# since the list is traversed twice.
def find_second_maximum(lst):
    first_max_value = float('-inf')
    second_max_value = float('-inf')
    # find first max
    for number in lst:
        if number > first_max_value:
            first_max_value = number
    # find max relative to first max
    for number in lst:
        if number != first_max_value and number > second_max_value:
            second_max_value = number
    return second_max_value


print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([9, 2, 3, 6,5,5]))
print(find_second_maximum([2,4,4]))

#traversing once
def find_second_maximum(lst):
    if (len(lst) < 2):
        return
    # initialize the two to infinity
    max_number = second_max_number = float('-inf')
    for i in range(len(lst)):
        # update the max_number if max_number value found
        if (lst[i] > max_number):
            second_max_number = max_number
            max_number = lst[i]
        # check if it is the second_max_number and not equal to max_number
        elif (lst[i] > second_max_number and lst[i] != max_number):
            second_max_number = lst[i]
    if (second_max_number == float('-inf')):
        return
    else:
        return second_max_number

print(find_second_maximum([9, 2, 3, 6]))
print(find_second_maximum([9, 2, 3, 6,5,5]))
print(find_second_maximum([2,4,4]))      
"""
We initialize two variables max_number and secondmax
to -inf. We then traverse the list, and if the current element 
in the list is greater than the maximum value, 
then set secondmax to max_no and max_no to the current element. 
If the current element is greater than the second maximum
number and not equal to maximum number, then update secondmax 
to store the value of the current variable. Finally,
return the value stored in secondmax.
Time complexity: O(n) since the list is traversed once only.
"""
     
   
   
   
       
       
           
           
       
       
           
   
       
   
       








