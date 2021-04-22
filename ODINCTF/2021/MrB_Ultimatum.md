# Mr.B Ultimatum / OSINT / Hard

## Description

Someone claims they knew a programmer named Mr.B, who liked to share  his projects with other programmers in order for them to use and even  build upon them, find out if you can get more information out of this. All we know about him besides his alias is a strange name known to be  used by him (THE4llANDP0werfu1MrB).

---

## Solution

since it mentioned open source i searched for the username in github and found a user with only one [repo](https://github.com/THE4llANDP0werfu1MrB/THE4llANDP0werfu1MrB) that has this text

```
Hi, I’m Mr.B I’m currently working on a great project and wanted to share it with fellow programmers, but anyone with access to internet could see it here, i will throw the code in my "bin" wink so only programmers can see it. here's the address: "/2yxugDsw", and the password: "37r4QwoeMCZR8k8I"
```

at first i didn't release what bin is, but then i realized that it probably means pastebin, entering this URL `https://pastebin.com/2yxugDsw` i found this

![img](https://i.imgur.com/xMjmzWF.png)

entering the password we get the paste , searching in it we find two folders secret and source code opening the secret file we get the flag. 

---

## Flag

SBCTF{DoNotUseTheSamePasswordForEverything}

1. 