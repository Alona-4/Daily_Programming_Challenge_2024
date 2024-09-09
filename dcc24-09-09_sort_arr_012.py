a = [0, 1, 2, 1, 0, 2, 1, 0]
i = 0 
b,c = 0,len(a)-1
while i<=c:
    if a[i] == 0:
        a[b],a[i] = a[i],a[b]
        b += 1
    elif a[i] == 2:
        a[c],a[i] = a[i], a[c]
        c -= 1
    i += 1
print(a)

