## Gallery


1. Enumerate with nmap, ports 80 and 8080 are open
```
root@ip-10-10-199-150:~# nmap -sS -sV 10.10.187.97

Starting Nmap 7.60 ( https://nmap.org ) at 2022-03-22 16:51 GMT
Nmap scan report for ip-10-10-187-97.eu-west-1.compute.internal (10.10.187.97)
Host is up (0.0012s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
8080/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
MAC Address: 02:C9:D8:1F:EB:1F (Unknown)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.40 seconds
```

2. Run gobuster
```
root@ip-10-10-199-150:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.187.97
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.187.97
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/03/22 16:53:09 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/gallery (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2022/03/22 16:53:12 Finished
===============================================================
```
