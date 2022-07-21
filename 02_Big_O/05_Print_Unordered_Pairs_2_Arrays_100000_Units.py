def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                        # O(A)
        for j in range(len(arrayB)):                    # O(B)
            for k in range(0, 100000):                  # O(1)  
                print(str(arrayA[i]+','+arrayB[j]))     # O(1)

# Time Complexity: O(AB)