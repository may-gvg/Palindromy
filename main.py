

def isPalindrome(s):
    return s == s[::-1]


s = input ('wpisz wyraz i sprawdż czy  jest palidromem:')
s = s.lower()

ans = isPalindrome(s)

if ans:
    print("Tak")
else:
    print("Nie")
