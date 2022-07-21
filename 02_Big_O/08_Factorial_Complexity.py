def factorial(n):                       # M(N)
    if n < 0:                           # O(1)
        return -1                       # O(1)
    elif n == 0:                        # O(1)
        return 1                        # O(1)
    else:                               # O(1)
        return n * factorial(n-1)       # O(N-1)
    
# Time Complexity: O(N)