"""
arrange elements in such a way that the maximum element 
appears at first position, then minimum at second, 
then second maximum at third and second minimum at fourth and so on.
 In other words, all the even-numbered indices 
 will have the largest numbers in the list in 
 descending order and the odd-numbered indices will have 
 the smallest numbers in ascending order.
e.g
lst = [1,2,3,4,5]
Output
lst = [5,1,4,2,3]
"""
#sol 1
def max_min(lst):
    new_list = [ ]
    for i in range(len(lst)//2):
        new_list.append(lst[-(i+1)])
        new_list.append(lst[i])
    if len(lst) % 2:
        new_list.append(lst[len(lst)//2])
    return new_list
print(max_min([1, 2, 3, 4, 5, 6]))

"""
In this solution, we 
we first create a new empty list,
that we will append the appropriate elements to and return. 
Then iterate through the list starting from the 0th index till the middle 
of the list indexed as lst[length(list)/2]. So if the length of the given
list is 10, the iterator variable i on line 4 in our solution would 
start from 0 and end at 10/2 = 510/2=5. 
Note that the starting index 0 in the example is inclusive, 
and the ending index 5 is exclusive. 
At each iteration, we first append the largest unappended
element and then the smallest.
So in the first iteration, i = 0 and lst[-(0+1)] = lst[-1] 
corresponds to the last element of the list, which is also the largest. 
So the largest element in the list is 
appended to result first, and then the
current or element indexed by i is appended. Next, the second largest
and the second smallest are appended and so on until the end of the list.
"""
#sol 2
def max_min(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
This solution exploits the properties of the modulus operator to store two 
elements at one index. Let’s take an example list [1, 2, 3, 4, 5, 6]. The 
maximum element is 6, and if we increment it by 1, we get 7. 
If we were to apply the modulus 7 to, let’s say, the element at index 0, 
we would get the same element back, i.e., 1.
The other important characteristic is that we can add multiples of 7 to 
the elements, and we will still get back the original values by 
applying the modulus operator.
Let’s consider lst[0] as an example. 
In the max/min ordering, we need to store 6 at index 0 in the list, 
since that is the maximum value in the list. 
Multiply 6 with 7 and add lst[0] to it, we get 7 * 6 + 1 = 43 7∗6+1=43. 
For our last trick, when we apply 43 modulo\ 7, we get back the original 1.
At the same time, if we divide 43 by 7, we get back 6.
We achieve this behavior with the following line of code,
lst[i] += (lst[maxIdx] % maxElem) * maxElem
lst[maxIdx] is stored as a multiplier and lst[i]
is stored as remainder. Taking the same example from above, 
in the list, [1, 2, 3, 4, 5, 6], the maxElem is 6 + 1 = 7  and 43 is 
stored at index 0. Once we have 43, we can get the new element 6 using 43/7.
Also, we can go back to the original element, 1, using the expression 43%7.
Similarly, we use the following line of code for odd indexes,
lst[i] += (lst[minIdx] % maxElem) * maxElem
This allows us to swap the numbers in place without using any extra space.
To get the final list, we simply divide each element by maxElem
as done in the last for loop.
Note: This approach only works for non-negative numbers!

"""



