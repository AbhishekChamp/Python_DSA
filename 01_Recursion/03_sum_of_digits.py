def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'The number has to be a positive integer only'
    if (n==0):
        return 0
    else:
        return int(n % 10) + sum_of_digits(n // 10)

number = int(input("Enter the number: "))
print(f"The sum of digits of the number {number} is {sum_of_digits(number)}")