# Is unique: Implement an algorithm to determine if a list has all unique characters, using python list

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]


def isUnique(list):
    empty_list = []
    for i in list:
        if i in empty_list:
            print(i)
            return False
        else:
            empty_list.append(i)
    print('Unique')
    return True

isUnique(myList)