h = [2, 0, 2]
t = 0
for i in range(len(h)):
    if h[:i] == []:
        ml = 0
    else:
        ml = max(h[:i])
    if h[i+1:] == []:
        mr = 0
    else:
        mr = max(h[i+1:])
    m = min(ml, mr)
    if m > h[i]:
        t += m - h[i]
print(t)
