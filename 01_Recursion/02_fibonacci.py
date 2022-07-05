def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number cannot be negative or non integer."
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
print(f"The Fibonacci number of parameter {number} is {fibonacci(number)}")