a = [6, 6, 6, 6, 7, 7, 8, 8, 8]
s = set(a)
k = 3
for i in s:
    if a.count(i) == k:
        break
if a.count(i) == k:
    print(i)
else:
    print(-1)
