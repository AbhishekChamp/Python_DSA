def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):                            # O(A)
        for j in range(len(arrayB)):                        # O(B)
            if arrayA[i] < arrayB[j]:                       
                print(str(arrayA[i])+","+str(arrayB[j]))    # O(1)

# Time Complexity: O(AB)