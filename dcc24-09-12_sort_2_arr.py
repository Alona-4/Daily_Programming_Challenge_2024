import math
arr1 = [i for i in range(1,100001)]
arr2 = [i for i in range(50001,100001)]
l1 = len(arr1)
l2 = len(arr2)
c = math.ceil((l1+l2)/2)
while c>0:
    a = 0
    while (a+c) < l1:
        if arr1[a]>arr1[a+c]:
            arr1[a], arr1[a+c] = arr1[a+c], arr1[a]
        a += 1
    b = c - l1 if c > l1 else 0
    while b<l2 and a<l1:
        if arr1[a]>arr2[b]:
            arr1[a], arr2[b] = arr2[b],arr1[a]
        a += 1
        b += 1
    
    if b<l2:
        b = 0
        while b+c<l2:
            if arr2[b]>arr2[b+c]:
                arr2[b],arr2[b+c] = arr2[b+c], arr2[b]
            b += 1
    if c == 1:
        c =0
    c = math.ceil(c/2)
print(arr1)
print(arr2)
    
        