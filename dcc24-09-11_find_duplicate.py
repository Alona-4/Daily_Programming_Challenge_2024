arr = [i for i in range(1,100000)] + [50000]
arr.sort()
for i in range(len(arr)):
    if arr[i] == arr[i+1]:
        print(arr[i])
        break