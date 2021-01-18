# Description

Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}  
Hint 1 : This can be solved online if you don't want to do it by hand!

# Solution

ROT13 is a specfic case of ceaser cipher where it switches the letters 13 times.  
you can search for a online tool for solving like : https://rot13.com/ but i made a python script for it

```python
text = input("Enter Your Text : ")
text = list(text)

for i in range(len(text)):
    if(text[i].isalpha()):
            if(text[i].isupper()):
                text[i] = chr(((ord(text[i]) - 65 + 13 ) % 26 ) + 65)
            else:
                text[i] = chr(((ord(text[i]) - 97 + 13 ) % 26 ) + 97)
print(''.join(i for i in text))
```

when i run it

```bash
$ python3 script.py
Enter Your Text : cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
picoCTF{not_too_bad_of_a_problem}
```

# Flag

flag = picoCTF{not_too_bad_of_a_problem}
