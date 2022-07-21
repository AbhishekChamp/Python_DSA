def foo(array):
    sum = 0                                                 # O(1)
    product = 1                                             # O(1)

    for i in array:                                         # O(N)
        sum += i                                            # O(1)

    for i in array:                                         # O(N)
        product *= 1                                        # O(1)

    print("Sum = "+str(sum)+", Product = "+str(product))    # O(1)

    # Time Complexity: O(N)