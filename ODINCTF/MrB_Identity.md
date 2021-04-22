# Mr.B Identity / OSINT / Easy

## Description

"A person known as Mr.B claims that he has discovered information about a secret project that affects people all around the world, we couldn't  find a way to talk to him yet, but some say he shared his email address  on the internet for people to contact him. All we know about him besides his alias is a strange name known to be  used by him (THE4llANDP0werfu1MrB). Find his email address and submit the flag like below: Email: exampleMailTest@test.com, Flag: SBCTF{exampleMailTest}"

---

## Solution

Searching for the user name `THE4llANDP0werfu1MrB` on google i found three results

![img](https://i.imgur.com/awdYrvA.png)

opening the reddit account i found this base64 encoded

![img](https://i.imgur.com/eF30w1K.png)

decoding it we get this

```
Here's my email address: privateMailOfMrB@protonmail.com, but I will NOT reply in any way or form, so don't bother.
```

---

## Flag

SBCTF{privateMailOfMrB}