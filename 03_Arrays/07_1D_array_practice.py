from array import *

# 1. Create an array and traverse

my_array = array('i', [1, 2, 3, 4, 5])

print("Step 1")
for i in my_array:
    print(i)


# 2. Access individual elements through indexes

print("Step 2")
print(my_array[0])


# 3. Append any value to the array using append() method

print("Step 3")
my_array.append(6)
print(my_array)


# 4. Insert value in an array using insert() method

print("Step 4")
my_array.insert(3, 8)
print(my_array)

# 5. Extend python array using extend() method

print("Step 5")
my_array_new = array('i', [10, 11, 12, 13])
my_array.extend(my_array_new)
print(my_array)


# 6. Add items from list into array using fromlist() method

print("Step 6")
temp = [20, 21, 22, 23]
my_array.fromlist(temp)
print(my_array)


# 7. Remove any array element using remove() method

print("Step 7")
my_array.remove(8)
print(my_array)


# 8. Remove last array element using pop() method

print("Step 8")
my_array.pop()
print(my_array)


# 9. Fetch any element through its index using index() method

print("Step 9")
print(my_array.index(21))


# 10. Reverse a python array using reverse() method

print("Step 10")
my_array.reverse()
print(my_array)


# 11. Get array buffer information through buffer_info() method

print("Step 11")
print(my_array.buffer_info())


# 12. Check for number of occurance of an element using count() method

print("Step 12")
my_array.append(12)
print(my_array.count(12))


# 13. Convert array to a python list with same elements using tolist() method

print("Step 13")
print(my_array.tolist())


# 14. Slice Elements from an array

print("Step 14")
print(my_array[3:8])