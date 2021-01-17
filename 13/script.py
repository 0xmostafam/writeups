cleartxt = input("Enter you text : ")
abc = "abcdefghijklmnopqrstuvwxyz"
secret = "".join([abc[(abc.find(c)+13)%26] for c in cleartxt])
print(secret)