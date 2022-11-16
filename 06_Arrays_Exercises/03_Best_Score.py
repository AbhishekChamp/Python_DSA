# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.

# Input: [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# Output: 90, 87

def firstSecond(myList):
    max1, max2 = 0, 0
    for i in range(len(myList)):
        if(myList[i] > max2 and max1 != myList[i]):
            max2 = myList[i]
            if(max2 > max1):
                max1, max2 = max2, max1
    return max1,max2

def firstScoreAlternate(given_list):
    a = given_list   #make a copy
    a.sort(reverse=True)
    print(a) 
    first = a[0]
    second = None
    for element in given_list:
        if element != first:
            second = element
            return first, second


myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0,90]
print(firstSecond(myList))
