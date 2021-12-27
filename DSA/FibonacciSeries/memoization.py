''' 
Memoization speeds up the execution of expensive recursive functions by 
storing previously calculated results in a cache. 
This way, when the same input occurs again, the function just has 
to look up the corresponding result and return it without having to
 run the computation again. You can refer to these results as cached or 
 memoized

''' 
def fibonacci_of(n):
    cache = {0: 0, 1: 1}
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]
print([fibonacci_of(n) for n in range(15)])
