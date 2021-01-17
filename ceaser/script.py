text = input("Enter the cipher : ")
text = list(text)
length = len(text)
for i in range(25):
	for j in range(length):
		text[j] = chr(((ord(text[j]) + 1 ) % 26 ) + 97)
	print("picoCTF{" + ''.join(i for i in text)+ "}")