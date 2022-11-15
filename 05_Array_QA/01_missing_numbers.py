# Question - How to find the missing number in an integer array of 1 to n

# Hint - 1 + 2 + 3 + ... + n = n(n+1) / 2


mylist = [1, 2, 3, 4, 5, 6, 7, 9, 10]

def findMissing(list, n):
    sum1 = n * (n+1) / 2
    sum2 = sum(list)
    print(sum1-sum2)
    return sum1-sum2

findMissing(mylist, 10)