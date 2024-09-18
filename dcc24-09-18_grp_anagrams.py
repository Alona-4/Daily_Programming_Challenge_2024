arr = ["abc", "def", "ghi"]
d = {}
for i in arr:
    l = list(i)
    l.sort()
    s = "".join(l)
    if s not in d:
        d[s] = [i]
    else:
        d[s].append(i)
r = []
for i in d:
    r.append(d[i])
print(r)
