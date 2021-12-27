''' 
Inside fibonacci_of(), you first check the base case. 
You then return the sum of the values that results from calling 
the function with the two preceding values of n. 
The list comprehension at the end of the example generates a 
Fibonacci sequence with the first fifteen numbers.

This function quickly falls into the repetition issue 
you saw in the above section. The computation gets more and
 more expensive as n gets bigger. The required time grows 
 exponentially because the function calculates many identical 
 subproblems over and over again.


'''

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
        
print([fibonacci_of(n) for n in range(15)])