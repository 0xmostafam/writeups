#							Inception CTF: Dream 3 					

---

## Description

Note: This challenge builds on Inception CTF: Dream 2. While the first two steps were easy it’s all hard from here on out,  ThePointMan is the most crucial role of the mission he has to be  presentable but without giving away our intentions. Use Alternate Dream  State to find the flag before the kick. Author: Brandon Martin

Zip file password : WaterUnderTheBridge

---

## Solution

After the Extraction we can find three files 

- a zip files that need a password called `SnowFortress.7z`
- two txt files one has an empty name and the second is called `ThePointMan.txt`

viewing the empty txt file we find this

```
You mean, a dream within a dream? NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q=
```

this looks like a base64 lets decode it

```bash
$ echo "NTIgNDkgNTQgNTMgNDUgNDMgN2IgNDYgNDAgMjEgMjEgNjkgNmUgNjcgNDUgNmMgNjUgNzYgNDAgNzQgNmYgNzIgN2Q=" | base64 -d
52 49 54 53 45 43 7b 46 40 21 21 69 6e 67 45 6c 65 76 40 74 6f 72 7d
```

this look like hexdecimal characters like the previous challenge lets decode them the same way

```python
>>> s = "52 49 54 53 45 43 7b 46 40 21 21 69 6e 67 45 6c 65 76 40 74 6f 72 7d"
>>> bytes.fromhex(s).decode('utf-8')
'RITSEC{F@!!ingElev@tor}'
```

---

## Flag

RITSEC{F@!!ingElev@tor}