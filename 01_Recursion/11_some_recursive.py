# some_recursive([1, 2, 3, 4], isOdd)     # True
# some_recursive([4, 6, 8, 9], isOdd)     # True
# some_recursive([4, 6, 8], isOdd)     # False


def is_odd(num):
    if num%2==0:
        return False
    else:
        return True


def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1:], cb)
    return True