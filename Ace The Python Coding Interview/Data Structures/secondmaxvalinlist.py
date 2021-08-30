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



