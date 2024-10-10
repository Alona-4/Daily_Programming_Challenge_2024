Edges = [[0, 1], [1, 2]]
start = 2
end = 3
d = {}
for i in Edges:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])
    if i[1] not in d:
        d[i[1]] = [i[0]]
    else:
        d[i[1]].append(i[0])
def find(n,di,v):
    if end == n:
        return di
    else:
        di += 1
        mi = float('inf')
        v.append(n)
        for i in d[n]:
            if i not in v:
                m = find(i,di,v)
                di = min(m,mi)      
    return di
if end not in d:
    print(-1)
else:
    print(find(start,0,[]))

