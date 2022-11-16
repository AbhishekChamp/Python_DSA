# Write a function to remove duplicates in an array

# Input : [1, 1, 2, 2, 3, 4, 5]
# Output : [1, 2, 3, 4, 5]

def removeDuplicates(myList):
    result = []
    for i in range(len(myList)):
        if myList[i] not in result:
            result.append(myList[i])
    return result


myList = [1, 1, 2, 2, 3, 4, 5]
print(removeDuplicates(myList))