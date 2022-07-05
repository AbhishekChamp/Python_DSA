def palindrome(word):
    if len(word) == 0:
        return True
    if word[0] != word[len(word)-1]:
        return False
    return palindrome(word[1:-1])