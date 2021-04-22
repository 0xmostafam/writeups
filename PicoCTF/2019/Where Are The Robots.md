# Where Are The Robots

---
## Description

Can you find the robots? https://jupiter.challenges.picoctf.org/problem/60915/ (link) or http://jupiter.challenges.picoctf.org:60915  
Hint 1 : What part of the website could tell you where the creator doesn't want you to look?

---
## Solution

when a developer wants to tell a search engine crawler not to search a endpoint they put it in the robots.txt  
so if we go to http://jupiter.challenges.picoctf.org:60915/robots.txt

```
User-agent: *
Disallow: /8028f.html
```

so we now that 8028f.html is a forbidden endpoint so when we open http://jupiter.challenges.picoctf.org:60915/8028f.html 

---
## Flag

flag : picoCTF{ca1cu1at1ng_Mach1n3s_8028f}
