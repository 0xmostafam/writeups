# 							Inception CTF: Dream 1

---

## Description

The purpose of this CTF challenge is to  identify common methods of hiding malicious files and code. In most  cases adversaries will attempt to evade defenses in many cases by  masquerading, hiding files, and more. There are five directories like  the five levels in the movie Inception, Reality -> Van Chase ->  The Hotel -> Snow Fortress -> Limbo. You will find one flag in  each of the levels, that flag will also be the password to extract the  next directory. Requirements: • You must have 7zip installed • Drop the InceptionCTF.7z on the Desktop as “InceptionCTF” • Use the option “Extract to "<name of directory>\” for the CTF to function properly Missing either of the above may result in complications which may cause  issues when attempting to find flags. NOTE: These challenges have a flag format of RITSEC{} Dream 1: We have to get to their subconscious first, look for a hidden text file  within the directory “Reality” this flag will unlock the next directory.

---

## Solution

by extracting `InceptionCTFRITSEC.7z` we find that there is another file called `Reality.7z` by Extracting that also we find that there is a directory that have two files : 

- A zip file `VanChase.7z` that needs a password
- A text file `Subconscious.txt`

by opening the text file we have this

```
Wait a minute, whose subconscious are we going into, exactly? {dnalmaerD}CESTIR
```

using python to reverse the string we get the flag and the password for the next zip

```python
>>> print("{dnalmaerD}CESTIR"[::-1])
RITSEC}Dreamland{
```

---

## Flag

RITSEC{Dreamland}

