# f(n) = n mod 2 + 10 * f(n/2)

def decimal_to_binary(n):
    assert int(n) == n, 'The parameter must be an integer only!'
    if n==0:
        return 0
    return (n % 2) + (10 * decimal_to_binary(int(n/2)))


decimal_number = int(input("Enter the decimal number: "))
print(f"The binary equivalent of the decimal number {decimal_number} is {decimal_to_binary(decimal_number)}")