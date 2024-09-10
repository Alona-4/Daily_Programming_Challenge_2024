arr = [i for i in range(1,1000000)]
s = sum(arr)
n = len(arr)+1
ns = (n*(n+1))//2
print(ns-s)
