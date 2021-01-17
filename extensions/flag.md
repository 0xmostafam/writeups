This is a really weird text file TXT? Can you find the flag?

you can search for the file command before reading

the operating system know what type of file it is from the starting bytes and by using file it reads those files and outputs the real type

```bash
$ file flag.txt 
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
$ mv flag.txt flag.png
```
flag : picoCTF{now_you_know_abount_extensions}


