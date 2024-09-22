s = "pqpqs"
k = 2
c = 0
for i in range(len(s)):
    se = set()
    for j in range(i,len(s)):
        se.add(s[j])
        if len(se) == k:
            c += 1
print(c)