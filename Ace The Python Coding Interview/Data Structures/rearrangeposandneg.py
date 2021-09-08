"""
Given a list, can you rearrange its elements in
such a way that the negative elements appear at one end
and positive elements appear at the other. 

A list with negative elements at the left and 
positive elements at the right
e.g
[10,-1,20,4,5,-9,-6]
output:
[-1,-9,-6,10,20,4,5]
"""
#sol 1 
def rearrange(lst):
    neg_items = [ ]
    pos_items = [ ]
    for i in lst:
       if i < 0:
           neg_items.append(i)
       else:
           pos_items.append(i)
            
    lst = neg_items + pos_items
    return lst

print(rearrange([10,-1,20,4,5,-9,-6]))

def rearrange(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]
print(rearrange([10,-1,20,4,5,-9,-6]))