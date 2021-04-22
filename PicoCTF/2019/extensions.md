# Extensions

---
## Description

This is a really weird text file TXT? Can you find the flag?  
Hint 1 : How do operating systems know what kind of file it is? (It's not just the ending!  
Hint 2 : Make sure to submit the flag as picoCTF{XXXXX}

---
## Solution

the operating system know what type of file it is from the starting bytes and by using the command file it reads those bytes and outputs the type accordingly

```bash
$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
$ mv flag.txt flag.png
$ eog flag.png
```

---
## Flag

flag : picoCTF{now_you_know_abount_extensions}
