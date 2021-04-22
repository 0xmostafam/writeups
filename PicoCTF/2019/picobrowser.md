# picobrowser

---
## Description

This website can be rendered only by picobrowser, go and catch the flag! https://jupiter.challenges.picoctf.org/problem/50522/  or http://jupiter.challenges.picoctf.org:50522  
Hint 1 : You don't need to download a new web browser

---
## Solution

this is the first challenge to require us to open burpsuite there is an obvious hint when you press flag in the beginning that you need to change
the user-agent tag in the request in burpsuite so change your User-Agent to

```
User-Agent : picobrowser
```

---
## Flag

flag : picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}
