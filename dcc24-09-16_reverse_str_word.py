s = "word"
r = ""
l = s.split(" ")
s = " ".join(l[::-1])
for i in s:
    if i.isalnum():
        r += i
    elif r!="" and i == " " and r[-1].isalnum():
        r += " "
print(r.strip())

