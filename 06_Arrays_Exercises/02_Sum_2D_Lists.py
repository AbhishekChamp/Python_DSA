# Given 2D list calculate the sum of diagonal elements.

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 15

def sumDiagonal(twoDlist):
    sum = 0
    for i in range(len(twoDlist)):
        sum += twoDlist[i][i]
    return sum

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(sumDiagonal(myList2D))
