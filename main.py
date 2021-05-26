def isPalindrome(s):
    s = s.casefold()
    reversedS = reversed(s)

    return list(s) == list(reversedS)

print(isPalindrome("Mama"))
print(isPalindrome("Kajak"))
print(isPalindrome("kajak"))
print(isPalindrome("MaDAM"))
