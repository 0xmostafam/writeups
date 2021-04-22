# Inception CTF: Dream 2

---

## Description

Note: This challenge builds off Inception CTF: Dream 1, Unfortunately, the subconscious isn’t enough for this mission, we  have to kidnap Fischer we need to go further into the system of the  mind. Use the flag found to edit the PowerShell script, entering the  Flag in line three in-between the single quotes. Run the PowerShell  script and wait for it to complete its actions. Thanks to SRA for providing this challenge!

Zip file password : Dreamland

---

## Solution

there is three files after extracting

- A zip file called `TheHotel.7z` that needs a password
- one txt file called `kidnap.txt`
- a powershell file called `kick.ps1`

first lets see the content of `kidnap.txt`

```
An idea is like a virus, resilient, highly contagious. 
52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d
```

these look like hexdecimal characters we can use python to decode it

```python
>>> s = "52 49 54 53 45 43 7b 57 61 74 65 72 55 6e 64 65 72 54 68 65 42 72 69 64 67 65 7d"
>>> bytes.fromhex(s).decode('utf-8')
'RITSEC{WaterUnderTheBridge}'
```

---

## Flag

RITSEC{WaterUnderTheBridge}