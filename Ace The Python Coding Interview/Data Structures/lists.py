#Removing even numbers from  a list of

def remove_even_numbers(alist):
    number = []
    return [number for number in alist if number % 2 != 0]

number=[1,2,4,5,10,6,3]
print(remove_even_numbers(number))
    