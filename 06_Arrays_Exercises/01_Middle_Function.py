# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# Input = [1, 2, 3, 4]
# Output = [2, 3]

def middle(list):
    result = []
    for i in range(len(list)):
        if(i!=0 and i!=len(list)-1):
            result.append(list[i])
    return result

def middle_alternate(list):
    new = list[1:len(list)-1]
    new = list[1:]
    del new[-1]
    return new

myList = [1, 2, 3, 4]

print(middle(myList))
print(middle_alternate(myList))