# Description

Decrypt this [message](ciphertext).

# Solution

ceaser cipher is a cipher where every letter is shifted by a certian number of times and it can be easily brute forced so i made a script for it

```python
text = input("Enter the cipher : ")
text = list(text)
length = len(text)
for i in range(25):
	for j in range(length):
		text[j] = chr(((ord(text[j]) + 1 ) % 26 ) + 97)
	print("picoCTF{" + ''.join(i for i in text)+ "}")
```

the output :

```
$ python3 script.py
Enter the cipher : ynkooejcpdanqxeykjrbdofgkq
picoCTF{sheiiydwjxuhkrysedlvxizaek}
picoCTF{mbyccsxqdrobelsmyxfprctuye}
picoCTF{gvswwmrkxlivyfmgsrzjlwnosy}
picoCTF{apmqqglerfcpszgamltdfqhims}
picoCTF{ujgkkafylzwjmtaugfnxzkbcgm}
picoCTF{odaeeuzsftqdgnuoazhrtevwag}
picoCTF{ixuyyotmznkxahoiutblnypqua}
picoCTF{crossingtherubiconvfhsjkou}
picoCTF{wlimmchanbylovcwihpzbmdeio}
picoCTF{qfcggwbuhvsfipwqcbjtvgxyci}
picoCTF{kzwaaqvobpmzcjqkwvdnparswc}
picoCTF{etquukpivjgtwdkeqpxhjulmqw}
picoCTF{ynkooejcpdanqxeykjrbdofgkq}
picoCTF{sheiiydwjxuhkrysedlvxizaek}
picoCTF{mbyccsxqdrobelsmyxfprctuye}
picoCTF{gvswwmrkxlivyfmgsrzjlwnosy}
picoCTF{apmqqglerfcpszgamltdfqhims}
picoCTF{ujgkkafylzwjmtaugfnxzkbcgm}
picoCTF{odaeeuzsftqdgnuoazhrtevwag}
picoCTF{ixuyyotmznkxahoiutblnypqua}
picoCTF{crossingtherubiconvfhsjkou}
picoCTF{wlimmchanbylovcwihpzbmdeio}
picoCTF{qfcggwbuhvsfipwqcbjtvgxyci}
picoCTF{kzwaaqvobpmzcjqkwvdnparswc}
picoCTF{etquukpivjgtwdkeqpxhjulmqw}
```

the only one that makes sense is the flag

# Flag

flag : picoCTF{crossingtherubiconvfhsjkou}
