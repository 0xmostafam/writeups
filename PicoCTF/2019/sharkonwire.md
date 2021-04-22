# Shark on Wire

---
## Description

We found this packet capture. Recover the flag.
Hint 1 : Try using a tool like Wireshark  
Hint 2 : What are streams?

---
## Solution

pcap files are opened in wireshark, when i opened it i decieded to scroll packet by packet first then i noticed there was some text in UDP packets
so i filtered by UDP and sorted by destination and followed every stream and in the second stream i found the flag.

---
## Flag

flag : picoCTF{StaT31355_636f6e6e}
