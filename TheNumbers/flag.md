# Description

The numbers... what do they mean?
Hint 1 : The flag is in the format PICOCTF{}

# Solution

we now that the beginning of the flag is PICOCTF so the first 7 numbers stand for PICOCTF and we can also observe that each number represent its counter in the alphapet so we can just continue manually or in my case to practise more on python i made a simple script (it is bad i know)

```python
val = input("Enter your value : ")
li = val.split(" ")
s = ""
for i in li:
    if i.isnumeric():
        s += chr(int(i) + 64)
    else:
        s += i
print(s)
```

when i run it

```bash
python3 script.py
Enter your value : 16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
PICOCTF{THENUMBERSMASON}
```

# Flag

flag : PICOCTF{THENUMBERSMASON}
