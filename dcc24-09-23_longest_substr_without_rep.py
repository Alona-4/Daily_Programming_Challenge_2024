s =  "a"
l,j,le =[],0,1

while j < len(s):
    while s[j] in l:
        l.pop(0)
    l.append(s[j])
    j += 1
    le = max(len(l),le)
print(le)