from array import *

arr = array('i', [1, 2, 3, 4, 5, 6, 7])
index = int(input("Enter the index you want to know the value of "))


def access_element(array, index):
    if index >= len(array):
        print("This index value is more than the length of the array")
    else:
        print(array[index])


access_element(arr, index)