# Euclidean algorithm
# gcd(a, 0) = a
# gcd(a, b) = gcd(b, a mod b)

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The number must be integer only!'
    if a < 0:
        a = -1 * a;
    if b < 0:
        b = -1 * b;
    if b==0:
        return a
    return gcd(b, a%b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"The GCD of {a} and {b} is {gcd(a,b)}")