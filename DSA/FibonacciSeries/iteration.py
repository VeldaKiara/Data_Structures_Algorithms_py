#defines fibonacci_of(), which takes a positive integer, n, as an argument.
def fibonacci_of(n):
    # Validate the value of n
    #perform the usual validation of n.
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    # Handle the base cases
    if n in {0, 1}:
        return n

    #defines two local variables, previous and fib_number, and initializes them with the first two numbers in the Fibonacci sequence.
    previous, fib_number = 0, 1
    #starts a for loop that iterates from 2 to n + 1. The loop uses an underscore (_) for the loop variable because it’s a throwaway variable and you won’t be using this value in the code.
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number
    
    
print(fibonacci_of(5))