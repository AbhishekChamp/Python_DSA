# How to check if an array contains a number in python

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def findNumber(array, number):
    for i in range(len(myArray)):
        if array[i] == number:
            print(i)


findNumber(myArray, 8)