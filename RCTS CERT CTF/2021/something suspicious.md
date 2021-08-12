# Something Suspicious

![](https://i.imgur.com/oXJ6Jhq.png)

- we are presented with two files `ftp.log` and `ssh.log` they both have logs of a bruteforce attack happening on the machine

- carefully checking every line I found these two base64 encoded strings in the files
- `Fri Jun 25 03:52:03 2021 [pid 1] [ftp] OK LOGIN: Client "192.168.1.23", anon password "ZmxhZ3tzMG0zdGgxbmc="` in the ftp.log file
- `Jun 25 00:49:14 lockedout auth.info sshd[3029]: Invalid user X3N1c3AxYzEwdXN9 from 192.168.1.23 port 53522` in the ssh.log file
- decode them and we have the flag

- Flag: flag{s0m3th1ng_susp1c10us}