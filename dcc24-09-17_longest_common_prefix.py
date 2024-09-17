arr =  ["alone"]
arr = sorted(arr,key = len)
i = arr[0]
r = arr[0]
for j in arr[1:]:
    if i[0]!= j[0]:
        r = ""
        break
    else:
        t = ""
        for k in range(len(i)):
            if i[k] == j[k]:
                t += i[k]
            else:
                break
        r = min(r,t)
print(r)
