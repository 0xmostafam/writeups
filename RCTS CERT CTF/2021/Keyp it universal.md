# Keyp it universal / Forensics

---

## Description

We intercepted a strange communication which we believe has important information inside.

Can you retrieve the information from it?

Flag format: flag{string}

Regex: flag{[0-9a-z_]+}

---

## Solution

this challenge was about analyzing a pcap file.
opend the file with wireshark.

![img](https://i.imgur.com/AtVXE7z.png)

noticed the used protocol is USB,
after searching and understanding the frame and few details of data input abd ouput in USB protocol

[https://wiki.wireshark.org/USB](https://wiki.wireshark.org/USB)

and noticed the communication between 'host' and '1.41.0' only with 8 bytes difference

![img](https://i.imgur.com/1JPhQXQ.png)

also noticed there is a value is keeping changing, it's the HID Data and its equivalent to letters.

so lets list all interrupt communication with 8 bytes since its our attention only with

((usb.transfer_type == 0x01) && (frame.len == 72)) && !(usb.capdata == 00:00:00:00:00:00:00:00)

![img](https://i.imgur.com/69GGFgA.png)

so lets save those letters in a txt file to deal with them with python script to get the flag

![img](https://i.imgur.com/Y2BysKS.png)

with this script

coding: utf-8
newmap={
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "del",
43: "tab",
44: "space",
45: "-",
47: "[",
48: "]",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}
myKeys = open('capture.txt')
i = 1
keyVal = int(00000000)
for line in myKeys:
	bytesArray = bytearray.fromhex(line.strip())
	#print "Line Number: " + str(i)
	for byte in bytesArray:
		if byte != 0:
			keyVal = int(byte)
	if keyVal in newmap:
		#print "Value map : " + str(keyVal) + " — -> " + newmap[keyVal]
		print newmap[keyVal]
	else:
		print "No map found for this value: " + str(keyVal)
#print format(byte, ‘02X’)
	i+=1


running the script on our file, we got the flag :"D

![img](https://i.imgur.com/pgsGn6k.png)

---

## Flag

flag{usb-p4ck3t-c4ptur3-1s-fun}
