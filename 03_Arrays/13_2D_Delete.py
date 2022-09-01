import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

newCol2DArray = np.delete(twoDArray, 0, axis=0)
print(newCol2DArray)

newRow2DArray = np.delete(twoDArray, 0, axis=1)
print(newRow2DArray)

# Time Complexity : O(N^2)
# Space Complexity : O(1)