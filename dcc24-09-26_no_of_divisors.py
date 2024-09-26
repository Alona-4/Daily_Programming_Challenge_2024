import math
n=997
s = set()
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        s.add(i)
        s.add(n//i)
print(len(s))