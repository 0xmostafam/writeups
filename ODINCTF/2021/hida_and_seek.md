# Hida And Seek / Forensics / Easy

## Description

we are playing a game can you be the winner

---

## Solution

Lets unzip that we downloaded

```bash
┌─[mostafa][mostafa-MS-7816][~/.../ODINCTF/hide]
└─▪ unzip Hide\&seek.zip 
Archive:  Hide&seek.zip
  inflating: 1.rar                   
  inflating: 2.rar                   
  inflating: 3.rar                   
  inflating: 4.rar                   
  inflating: 5.rar                   
  inflating: 6.rar                   
  inflating: 7.rar                   
  inflating: 8.rar                   
  inflating: 9.rar                   
  .
  .
  .
  inflating: 99.rar                  
  inflating: 100.rar       
```

looks like there is alot of files each one of them have 1000 txt files so lets try to grep recursively in all the files

```bash
┌─[mostafa][mostafa-MS-7816][~/.../ODINCTF/hide]
└─▪ grep -r -i "ctf"
Binary file 81.rar matches
```

looks like we found the rar lets extract it and grep again

```bash
┌─[mostafa][mostafa-MS-7816][~/.../ODINCTF/hide]
└─▪ grep -r -i "ctf"
367.txt:SBCTF{Y0U_H4VE_PL4Y3D_1T_W3LL}
```

---

## Flag

SBCTF{Y0U_H4VE_PL4Y3D_1T_W3LL} 