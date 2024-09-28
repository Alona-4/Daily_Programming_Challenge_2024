def isort(s, e):
    if len(s) == 0 or s[-1] <= e:
        s.append(e)
    else:
        t = s.pop()
        isort(s, e)
        s.append(t)
def sorts(s):
    if len(s) == 0:
        return
    t = s.pop()
    sorts(s)
    isort(s, t)

s = [3, 3, 3]
print("Original stack:", s)

sorts(s)
print("Sorted stack:", s)
