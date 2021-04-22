# Glory of The Garden

---
## Description

This garden contains more than it seems.  
Hint 1 : What is a hex editor?

---
## Solution

you can use the following command to get the flag where strings gets all the readable strings in a file and grep gets only the matching strings with the given string

```bash
strings garden.jpg | grep pico
```

or you can open a hexeditor and search for the word "pico" by hitting Ctrl + W

---
## Flag

flag : picoCTF{more_than_m33ts_the_3y3eBdBd2cc}
