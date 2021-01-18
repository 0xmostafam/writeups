text = list(input("Enter Text : "))
secret = list(input("Enter Secret : "))
length = len(text)
for i in range(length):
    newChar = int(ord(text[i]) - ord(secret[i]))
    if newChar <= 0:
        text[i] = chr(newChar + 91)
    else:
        text[i] = chr(newChar + 65)

print("picoCTF{" + ''.join(i for i in text) + "}")
