# Welcome to the challenge / Forensics

---

## Description

Welcome to the RCTS Challenge!

Can you find the flag?

Flag format: flag{string}

---

## Solution

After downloading the image, i tried strings but didn't got anything.
So lets analyze the image, using "binwalk" i noticed that there is another image with our image as a png,
lets extract it with "foremost"

![img](https://i.imgur.com/X6hiuog.png)

opened the png image and got the flag :D

![img](https://i.imgur.com/oOmC3jG.png)

---

## Flag

flag{0n3_1m4g3_1s_n0t_3n0ugh}