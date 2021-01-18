# Description

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](table.txt) to solve it?.

# Solution

this is called vigenere cipher where they pick each character in the secret and the original text and the find the intersecting letter between them in the [table](table.txt)  
Hint 1 : Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.  
Hint 2 : Please use all caps for the message.
so i made a simple script to reverse it

```python
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
```

the output is :

```bash
$ python3 script.py
Enter Text : UFJKXQZQUNB
Enter Secret : SOLVECRYPTO
picoCTF{CRYPTOISFUN}
```

# Flag

flag picoCTF{CRYPTOISFUN}
