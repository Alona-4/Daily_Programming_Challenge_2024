s = "abc"
rl = 0
r = ""
for i in range(len(s)):
    a, b =i,i
    while a>=0 and b<len(s) and s[a] == s[b]:
        if len(s[a:b+1])>rl:
            rl = len(s[a:b+1])
            r = s[a:b+1]
        a -= 1
        b += 1
    a,b = i, i+1
    while a>=0 and b<len(s) and s[a] == s[b]:
        if len(s[a:b+1])>rl:
            rl = len(s[a:b+1])
            r = s[a:b+1]
        a -= 1
        b += 1
print(r)