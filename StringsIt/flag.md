# Description

Can you find the flag in file without running it?  
Hint 1 : [strings](https://linux.die.net/man/1/strings)

# Solution

you can use the following command to get the flag where strings gets all the readable strings in a file and grep gets only the matching strings with the given string

```bash
strings garden.jpg | grep pico
```

# Flag

flag = picoCTF{5tRIng5_1T_d66c7bb7}
