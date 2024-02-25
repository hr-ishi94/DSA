def palendrome(s):
    s=s.lower()
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and palendrome(s[1:-1])

print(palendrome('Malayalam'))
print(palendrome('English'))