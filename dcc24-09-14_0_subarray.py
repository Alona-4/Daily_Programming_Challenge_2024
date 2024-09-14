arr = [1, -1, 2, -2, 3, -3] * 10000
r = []
ps = 0
s = {}

for i in range(len(arr)):
    ps += arr[i]
    if ps == 0:
        r.append((0, i))
    if ps in s:
        for start_index in s[ps]:
            r.append((start_index + 1, i))
    if ps in s:
        s[ps].append(i)
    else:
        s[ps] = [i]

print(r)
