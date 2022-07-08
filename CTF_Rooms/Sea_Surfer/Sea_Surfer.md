# Sea Surfer


1. Scan ports with rustscan.
```
root@ip-10-10-17-14:~# rustscan -r 1-65535 -a 10.10.235.8
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 10.10.235.8:22
Open 10.10.235.8:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2022-07-08 18:06 UTC
Initiating Ping Scan at 18:06
Scanning 10.10.235.8 [2 ports]
Completed Ping Scan at 18:06, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:06
Completed Parallel DNS resolution of 1 host. at 18:06, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:06
Scanning ip-10-10-235-8.eu-west-1.compute.internal (10.10.235.8) [2 ports]
Discovered open port 22/tcp on 10.10.235.8
Discovered open port 80/tcp on 10.10.235.8
Completed Connect Scan at 18:06, 0.00s elapsed (2 total ports)
Nmap scan report for ip-10-10-235-8.eu-west-1.compute.internal (10.10.235.8)
Host is up, received syn-ack (0.00056s latency).
Scanned at 2022-07-08 18:06:14 UTC for 0s

PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.22 seconds
```

2. Run gobuster on port 80.
```
root@ip-10-10-17-14:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.235.8/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.235.8/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/08 19:07:25 Starting gobuster
===============================================================
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/.hta (Status: 403)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2022/07/08 19:07:27 Finished
===============================================================
```

3. Check the response headers with either Inspect Element or Burp Suite. The `X-Backend-Server` is `seasurfer.thm`.
```
HTTP/1.1 200 OK
Date: Fri, 08 Jul 2022 18:08:02 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Sun, 17 Apr 2022 18:54:09 GMT
ETag: "2aa6-5dcde2b3f2ff9-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
X-Backend-Server: seasurfer.thm
Content-Length: 3138
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html
```

4. Add `10.10.235.8     seasurfer.thm` to `/etc/hosts` and then navigate to `http://seasurfer.thm/`.

5. Run gobuster on the domain. An interesting subdirectory found was `/adminer`, which contains a DBMS called [Adminer](https://www.adminer.org/) running version `4.8.1`.
```
root@ip-10-10-17-14:~# gobuster dir -w /usr/share/wordlists/dirb/big.txt -u http://seasurfer.thm/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://seasurfer.thm/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/big.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/08 19:12:44 Starting gobuster
===============================================================
/! (Status: 301)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/0 (Status: 301)
/0000 (Status: 301)
/A (Status: 301)
/About (Status: 301)
/B (Status: 301)
/Blog (Status: 301)
/C (Status: 301)
/Contact (Status: 301)
/H (Status: 301)
/Home (Status: 301)
/N (Status: 301)
/News (Status: 301)
/S (Status: 301)
/a (Status: 301)
/ab (Status: 301)
/abo (Status: 301)
/about (Status: 301)
/admin (Status: 302)
/adminer (Status: 301)
/asdfjkl; (Status: 301)
/atom (Status: 301)
/b (Status: 301)
/bl (Status: 301)
/blog (Status: 301)
/c (Status: 301)
/co (Status: 301)
/coffee (Status: 301)
/comment-page-1 (Status: 301)
/comment-page-2 (Status: 301)
/comment-page-3 (Status: 301)
/comment-page-4 (Status: 301)
/comment-page-6 (Status: 301)
/comment-page-5 (Status: 301)
/con (Status: 301)
/cont (Status: 301)
/contact (Status: 301)
/conta (Status: 301)
/dashboard (Status: 302)
/embed (Status: 301)
/favicon.ico (Status: 200)
/feed (Status: 301)
/fixed! (Status: 301)
/h (Status: 301)
/home (Status: 301)
/login (Status: 302)
/n (Status: 301)
/ne (Status: 301)
/new (Status: 301)
/news (Status: 301)
/page1 (Status: 301)
/page2 (Status: 301)
/rdf (Status: 301)
/robots.txt (Status: 200)
/rss (Status: 301)
/rss2 (Status: 301)
/s (Status: 301)
/sa (Status: 301)
/sal (Status: 301)
/sale (Status: 301)
/sam (Status: 301)
/sample-page (Status: 301)
/sample (Status: 301)
/server-status (Status: 403)
/sitemap.xml (Status: 302)
/wp-admin (Status: 301)
/wp-content (Status: 301)
/wp-includes (Status: 301)
/~a (Status: 301)
===============================================================
2022/07/08 19:38:19 Finished
===============================================================
```

6. The website is made with WordPress, so run wp-scan on it. There's not much we can take advantage of. We find that the template being used is `twentyseventeen`.
```
root@ip-10-10-17-14:~# wpscan --url http://seasurfer.thm/
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

[+] URL: http://seasurfer.thm/ [10.10.235.8]
[+] Started: Fri Jul  8 19:52:13 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://seasurfer.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://seasurfer.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access

[+] WordPress readme found: http://seasurfer.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://seasurfer.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.9.3 identified (Latest, released on 2022-04-05).
 | Found By: Rss Generator (Passive Detection)
 |  - http://seasurfer.thm/feed/, <generator>https://wordpress.org/?v=5.9.3</generator>
 |  - http://seasurfer.thm/comments/feed/, <generator>https://wordpress.org/?v=5.9.3</generator>

[+] WordPress theme in use: twentyseventeen
 | Location: http://seasurfer.thm/wp-content/themes/twentyseventeen/
 | Last Updated: 2022-05-24T00:00:00.000Z
 | Readme: http://seasurfer.thm/wp-content/themes/twentyseventeen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://seasurfer.thm/wp-content/themes/twentyseventeen/style.css?ver=20201208
 | Style Name: Twenty Seventeen
 | Style URI: https://wordpress.org/themes/twentyseventeen/
 | Description: Twenty Seventeen brings your site to life with header video and immersive featured images. With a fo...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 2.9 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://seasurfer.thm/wp-content/themes/twentyseventeen/style.css?ver=20201208, Match: 'Version: 2.9'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] team-members
 | Location: http://seasurfer.thm/wp-content/plugins/team-members/
 | Last Updated: 2022-05-23T11:57:00.000Z
 | [!] The version is out of date, the latest version is 5.1.1
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Urls In 404 Page (Passive Detection)
 |
 | Version: 5.1.0 (50% confidence)
 | Found By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://seasurfer.thm/wp-content/plugins/team-members/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:23 <==========================================================================================================> (137 / 137) 100.00% Time: 00:00:23

[i] No Config Backups Found.

[!] No WPVulnDB API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 50 daily requests by registering at https://wpvulndb.com/users/sign_up

[+] Finished: Fri Jul  8 19:52:46 2022
[+] Requests Done: 183
[+] Cached Requests: 7
[+] Data Sent: 40.326 KB
[+] Data Received: 18.83 MB
[+] Memory used: 292.43 MB
[+] Elapsed time: 00:00:32
```

7. Looking through the website, we find some interesting information.
```
Maya Martins - Owner
Brandon Baker - Salesman
Kyle King - Sysadmin (a PHP code). We can assume this man fucked up somewhere

http://seasurfer.thm/new-website-is-up/
The website seems to have gotten hacked last year, and now it's using WordPress

http://seasurfer.thm/news/
A comment says that it can't access intrenal.seasurfer.thm.
```

8. The subdomain `intrenal` is misspelled, so fix it and add it to the `/etc/hosts` file like so: `10.10.235.8     internal.seasurfer.thm`. Now when we visit it we're presented with a portal where we can insert the customer name, payment method, an addition comment, and the price of different items.

9. Fill out the form with random information and hit `Create Receipt`. It redirects us to a pdf it rendered. Download the pdf and run exiftool on it to find that it was created with `wkhtmltopdf 0.12.5`.
```
root@ip-10-10-17-14:~# exiftool 08072022-zMz0CRWLJaAhvyhMVSQf.pdf
ExifTool Version Number         : 10.80
File Name                       : 08072022-zMz0CRWLJaAhvyhMVSQf.pdf
Directory                       : .
File Size                       : 52 kB
File Modification Date/Time     : 2022:07:08 20:00:51+01:00
File Access Date/Time           : 2022:07:08 20:00:51+01:00
File Inode Change Date/Time     : 2022:07:08 20:00:53+01:00
File Permissions                : rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.4
Linearized                      : No
Title                           : Receipt
Creator                         : wkhtmltopdf 0.12.5
Producer                        : Qt 4.8.7
Create Date                     : 2022:07:08 19:00:41Z
Page Count                      : 1
```
