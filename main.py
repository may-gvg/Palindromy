

def isPalindrome(s):
    return s == s[::-1]


s = input ('wpisz wyraz i sprawdż czy  jest palidromem:')
ans = isPalindrome(s)

if ans:
    print("Tak")
else:
    print("Nie")
