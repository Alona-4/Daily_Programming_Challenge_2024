s = "{[}"
l = []
for i in s:
    if i in "({[":
        l.append(i)
    elif i == "}":
        if l[-1] != "{":
            break    
        l.pop()
    elif i == "]":
        if l[-1] != "[":
            break
        l.pop()
    elif i == ")":
        if l[-1] != "(":
            break
        l.pop()
if l != []:
    print("False")
else:
    print("True")
