def printUnorderedPairs(array):
    for i in range(0, len(array)):          # O(N^2)
        for j in range(i+1, len(array)):    # O(N)
            print(array[i]+","+array[j])    # O(1)

# Time Complexity: O(N^2)