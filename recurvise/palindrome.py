def palindrome(s, i):
    if len(s) == 1:
        return True
    else:
        if s[0] == s[len(s) - 1]:
            return True
        else:
            palindrome(s[i+1:len(s)-2])

res = palindrome('alddola', 0)
print(res)
