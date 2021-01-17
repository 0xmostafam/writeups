val = input("Enter your value : ")
li = val.split(" ")
s = ""
for i in li:
    if i.isnumeric():
        s += chr(int(i) + 64)
    else:
        s += i
print(s)