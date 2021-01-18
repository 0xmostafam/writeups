text = input("Enter Your Text : ")
text = list(text)

for i in range(len(text)):
    if(text[i].isalpha()):
            if(text[i].isupper()):
                text[i] = chr(((ord(text[i]) - 65 + 13 ) % 26 ) + 65)
            else:
                text[i] = chr(((ord(text[i]) - 97 + 13 ) % 26 ) + 97)
print(''.join(i for i in text))