# Find the maximum product of two integers in the array where all elements are positive

import numpy as np

myArray = np.array([1, 2, 30, 4, 33, 23, 12, 38, 32, 18])


def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxProduct)


findMaxProduct(myArray)