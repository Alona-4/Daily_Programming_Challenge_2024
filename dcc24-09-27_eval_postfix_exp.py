p = "5".split(" ")
s = []
for i in p:
    if i.isdigit() or (i[0]=="-" and len(i)>1):
        s.append(int(i))
    elif i == "+":
        s[-2] += s[-1]
        s.pop()
    elif i == "-":
        s[-2] -= s[-1]
        s.pop()
    elif i == "*":
        s[-2] *= s[-1]
        s.pop()
    elif i == "/":
        s[-2] /= s[-1]
        s.pop()
    elif i == "^":
        s[-2] **= s[-1]
        s.pop()

print(int(s[0]))

    