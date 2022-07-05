def power(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exponent must be positive integer only!'
    if (exp==0):
        return 1
    if (exp==1):
        return base
    return base * power(base, exp-1)

base_number = int(input("Enter the base number: "))
exp_number = int(input("Enter the power value: "))
print(f"The value of {base_number} power {exp_number} is {power(base_number, exp_number)}")