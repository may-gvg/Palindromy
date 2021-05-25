def isPalindrome(s):
    s = s.casefold()
    reversedS = reversed(s)

    if (list(s) == list(reversedS)):
        return True
    else:
        return False

print(isPalindrome("Mama"))
print(isPalindrome("Kajak"))
print(isPalindrome("kajak"))
print(isPalindrome("MaDAM"))
