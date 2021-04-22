# Don't Use Client Side

---
## Description

Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/29835/ or http://jupiter.challenges.picoctf.org:29835  
Hint 1 : Never trust the client

---
## Solution

right click -> view page source  
all we care about is this if condition

```javascript
split = 4;
if (checkpass.substring(0, split) == "pico") {
  if (checkpass.substring(split * 6, split * 7) == "723c") {
    if (checkpass.substring(split, split * 2) == "CTF{") {
      if (checkpass.substring(split * 4, split * 5) == "ts_p") {
        if (checkpass.substring(split * 3, split * 4) == "lien") {
          if (checkpass.substring(split * 5, split * 6) == "lz_7") {
            if (checkpass.substring(split * 2, split * 3) == "no_c") {
              if (checkpass.substring(split * 7, split * 8) == "e}") {
                alert("Password Verified");
              }
            }
          }
        }
      }
    }
  }
}
```

by arranging them manually we get the flag.

---
## Flag

flag : picoCTF{no_clients_plz_7723ce}
