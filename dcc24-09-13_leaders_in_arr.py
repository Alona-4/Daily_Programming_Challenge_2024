arr = [i for i in range(1,1000001)]
if arr == sorted(arr):
    print(arr[-1])
elif arr == sorted(arr,reverse=True):
    print(arr)
r = []
for i in range(len(arr)-1):
    if arr[i]>=max(arr[i+1:]) and arr[i] not in r:
        r.append(arr[i])
r.append(arr[-1])
print(r)