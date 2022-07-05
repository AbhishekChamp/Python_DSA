def recursive_range(n):
    if n <= 0:
        return 0
    return n + recursive_range(n-1)