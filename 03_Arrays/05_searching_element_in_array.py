from array import *

arr = array('i', [1, 2, 3, 4, 5, 6])


def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"


print(searchInArray(arr, 5))


# Time Complexity : O(n)
# Space Complexity : O(1)