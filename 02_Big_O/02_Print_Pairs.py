def printPairs(array):
    for i in array:                     # O(N^2)
        for j in array:                 # O(N)
            print(str(i)+","+str(j))    # O(1)

    # Time Complexity : O(N^2)