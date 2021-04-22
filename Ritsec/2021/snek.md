# Snek

---

## Description

No step on snek

---

## Solution

First things first i used `file` to know what type the file is

```bash
$ file snek
snek: python 3.7 byte-compiled
```

now that we know that type of file it is we can search for a python decompiler, after searching for a while i found this decompiler called [uncompyle6](https://pypi.org/project/uncompyle6/#description) and it only works with .pyc or .pyo files so we have to rename our files

```bash
$ un
unalias               unity-scope-loader    unrar
uname                 unix2dos              unrar-nonfree
uncompress            unix2mac              unset
uncompress.real       unix_chkpwd           unshare
uncompyle6            unix_update           unshield
unexpand              unlink                unsquashfs
unhex                 unlz4                 until
unicode_start         unlzma                unwrapdiff
unicode_stop          unmkinitramfs         unxz
uninstall_oh_my_bash  unopkg                unzip
uniq                  unpack200             unzipsfx
$ uncom
uncompress       uncompress.real  uncompyle6       
$ uncompyle6 snek

# file snek
# path snek must point to a Python source that can be compiled, or Python bytecode (.pyc, .pyo)

$ mv snek snek.pyc
renamed 'snek' -> 'snek.pyc'
$ uncompyle6 snek.pyc 
# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
# [GCC 9.3.0]
# Embedded file name: snek.py
# Compiled at: 2021-04-08 08:24:05
# Size of source mod 2**32: 834 bytes
"""
Written for RITSEC CTF 2021
Author: knif3
Flag: RITSEC{}

TODO: Finish this challenge
"""

class d(object):

    def __init__(self, password):
        self.password = password.encode()
        self.decrypt = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]

    def __eq__(self, other):
        if self.password == bytes(self.decrypt):
            print('!flag')
            return True
        return False


x = input('Enter my name: ')
a = d(x)
if a == x:
    print('IS_THIS_THE_FLAG??')
    print('NOPE')
else:
    print('WRONG')
# okay decompiling snek.pyc

```

After trying to reverse the script i found the flag

```bash
$ python3 
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> s = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 82, 83, 123, 97, 108, 108, 95, 104, 105, 36, 36, 95, 97, 110, 100, 95, 110, 48, 95, 98, 105, 116, 51, 125]
>>> bytes(s)
b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_RS{all_hi$$_and_n0_bit3}'
```

---

## Flag

RS{all_hi$$_and_n0_bits}