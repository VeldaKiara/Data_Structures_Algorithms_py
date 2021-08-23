# Given two sorted lists, merge them into one list which 
# should also be sorted.

def merge_lists(lst1, lst2):
    #initializing two variables to track the current index of each list
    index1 = 0
    index2 = 0
    #while both indeces are less than the length of the list
    while (index1 < len(lst1) and index2 < len(lst2)):
        #if current element in list 1 is greater than current element in list 2
        if (lst1[index1] > lst2[index2]):
            #insert lists 2 current index to list 1
            lst1.insert(index1, lst2[index2])
            #increment indeces
            index1 += 1
            index2 += 1
        else:
            index1 += 1
    if (index2 < len(lst2)):
        #Append whatever is left of list2 to list1
        lst1.extend(lst2[index2:])
    return lst1
    
lst1 = [1,2,3]
lst2 = [4,5,6]
print(merge_lists(lst1,lst2))

lst1 = [1,3,5]
lst2 = [2,4,6]
print(merge_lists(lst1,lst2))

lst1 = [2,3,5]
lst2 = [1,4,6]
print(merge_lists(lst1,lst2))

#algorithm test case fails because it uses stacks 
# lst1 = [5,3,1]
# lst2 = [6,4,2]
# print(merge_lists(lst1,lst2))

''' output 
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[5, 3, 1, 6, 4, 2]

'''

"""

This solution merges the two lists in place, 
no new list is created. First, initialize two new 
variables to track the ‘current index’ of both the 
lists to zero. Then, compare the current elements of both.
 
If the current element of the first list is greater than the current 
element of the second list, insert the current element of the 
second list in place of the current element of the first list and 
increment both index variables by 1. 

However, if the current element of the first list is smaller than the current 
element of the second list, then only increment the index variable of 
the first list by 1.

Continue this until the end of one of the lists is reached, i.e., 
until one of the index variables is greater than or equal to the 
length of its respective list. 

After that, if the index of the second 
list is smaller than the length of the list, extend the first list 
by the second one from that index until the end.
"""
