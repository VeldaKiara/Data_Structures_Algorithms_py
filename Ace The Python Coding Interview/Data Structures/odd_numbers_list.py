#Removing even numbers from  a list of integers
# creates an empty list iterates through the list and skips all the evens but adds 
#all the odds and returns the odds list
def remove_even_numbers1(alist):
    empty_list = []
    for number in alist:
        if number % 2 != 0:
            empty_list.append(number)
    return empty_list

print(remove_even_numbers1([1,2,4,5,10,6,3]))

#second iteration using list comprehensions
#list comprehensions are economical since they iterate, checking 
# a condition and appending and code only uses one line

def remove_even_numbers(alist):
    number = []
    return [number for number in alist if number % 2 != 0]
print(remove_even_numbers([1,2,4,5,10,6,3]))