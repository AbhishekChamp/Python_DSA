import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

addColTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1)
print(addColTwoDArray)

addRowTwoDArray = np.insert(twoDArray, 0, [[5, 6, 7, 8]], axis=0)
print(addRowTwoDArray)