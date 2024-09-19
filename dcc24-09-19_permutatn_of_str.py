s = "abcd"
def perm(s,r,l):
    if r == "":
        if s not in l:
            l.append(s)
        return l
    for i in range(len(r)):
        perm(s+r[i],r[:i]+r[i+1:],l)
    return l
print(perm("",s,[]))