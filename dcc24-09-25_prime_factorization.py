l = []
n = 123456
i = 2
p = [2,3,5,7,11,13,17,19,23,29,31]
if i>32:
    for i in range(32,n):
        for j in p:
            if i%p == 0:
                break
        if j == p[-1]:
            p.append(i)
while n > 1:
    while n%i == 0 and n>1:
        l.append(i)
        n = n/i
    i += 1
print(l)