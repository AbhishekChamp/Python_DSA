# words = ['i', 'am', 'learning recursion']
# capitalize_words(words)     # ['I', 'AM', 'LEARNING', 'RECURSION']

def capitalize_words(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_words(arr[1:])