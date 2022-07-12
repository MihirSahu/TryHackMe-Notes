# Git Happens


1. Run a port scan with Rustscan.
```
root@ip-10-10-167-130:~# rustscan -r 1-65535 -a 10.10.224.8
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.\U0001f422

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 10.10.224.8:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2022-07-11 23:26 UTC
Initiating Ping Scan at 23:26
Scanning 10.10.224.8 [2 ports]
Completed Ping Scan at 23:26, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 23:26
Completed Parallel DNS resolution of 1 host. at 23:26, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 23:26
Scanning ip-10-10-224-8.eu-west-1.compute.internal (10.10.224.8) [1 port]
Discovered open port 80/tcp on 10.10.224.8
Completed Connect Scan at 23:26, 0.00s elapsed (1 total ports)
Nmap scan report for ip-10-10-224-8.eu-west-1.compute.internal (10.10.224.8)
Host is up, received syn-ack (0.00058s latency).
Scanned at 2022-07-11 23:26:27 UTC for 0s

PORT   STATE SERVICE REASON
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.18 seconds
```

2. Brute force subdirectories with Gobuster.
```
root@ip-10-10-167-130:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.224.8:80
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.224.8:80
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/12 00:28:25 Starting gobuster
===============================================================
/.git/HEAD (Status: 200)
/css (Status: 301)
/index.html (Status: 200)
===============================================================
2022/07/12 00:28:25 Finished
===============================================================
```

3. Make a folder and download all of the resources found with Gobuster into it. Use `wget -np -r http://10.10.224.8/` to download resursively.
```
root@ip-10-10-167-130:~/Downloads# wget http://10.10.224.8/
--2022-07-12 00:39:23--  http://10.10.224.8/
Connecting to 10.10.224.8:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6890 (6.7K) [text/html]
Saving to: \u2018index.html\u2019

index.html                                     100%[=================================================================================================>]   6.73K  --.-KB/s    in 0s

2022-07-12 00:39:23 (610 MB/s) - \u2018index.html\u2019 saved [6890/6890]

root@ip-10-10-167-130:~/Downloads# ls
index.html
root@ip-10-10-167-130:~/Downloads# mkdir css
root@ip-10-10-167-130:~/Downloads# cd css/
root@ip-10-10-167-130:~/Downloads/css# wget http://10.10.224.8/css/style.css
--2022-07-12 00:40:08--  http://10.10.224.8/css/style.css
Connecting to 10.10.224.8:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5603 (5.5K) [text/css]
Saving to: \u2018style.css\u2019

style.css                                      100%[=================================================================================================>]   5.47K  --.-KB/s    in 0s

2022-07-12 00:40:08 (514 MB/s) - \u2018style.css\u2019 saved [5603/5603]
```

4. Use `git log` to see previous commits.
```
root@ip-10-10-167-130:~/Downloads/website# git log
commit d0b3578a628889f38c0affb1b75457146a4678e5 (HEAD -> master, tag: v1.0)
Author: Adam Bertrand <hydragyrum@gmail.com>
Date:   Thu Jul 23 22:22:16 2020 +0000

    Update .gitlab-ci.yml

commit 77aab78e2624ec9400f9ed3f43a6f0c942eeb82d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Fri Jul 24 00:21:25 2020 +0200

    add gitlab-ci config to build docker file.

commit 2eb93ac3534155069a8ef59cb25b9c1971d5d199
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Fri Jul 24 00:08:38 2020 +0200

    setup dockerfile and setup defaults.

commit d6df4000639981d032f628af2b4d03b8eff31213
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:42:30 2020 +0200

    Make sure the css is standard-ish!

commit d954a99b96ff11c37a558a5d93ce52d0f3702a7d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:41:12 2020 +0200

    re-obfuscating the code to be really secure!

commit bc8054d9d95854d278359a432b6d97c27e24061d
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:37:32 2020 +0200

    Security says obfuscation isn't enough.

    They want me to use something called 'SHA-512'

commit e56eaa8e29b589976f33d76bc58a0c4dfb9315b1
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:25:52 2020 +0200

    Obfuscated the source code.

    Hopefully security will be happy!

commit 395e087334d613d5e423cdf8f7be27196a360459
Author: Hydragyrum <hydragyrum@gmail.com>
Date:   Thu Jul 23 23:17:43 2020 +0200

    Made the login page, boss!

commit 2f423697bf81fe5956684f66fb6fc6596a1903cc
Author: Adam Bertrand <hydragyrum@gmail.com>
Date:   Mon Jul 20 20:46:28 2020 +0000

    Initial commit
```

5. It looks like the third commit was made to obfuscate the source code, so to view the code before that we can use `git reset --hard HEAD~7`.

6. Now if we navigate to it we find a new file `dashboard.html`. It has a function `checkCookie()` that returns a boolean, which determines if you can login or not. We also see the deobfuscated function `login()` in `index.html`
```
<script>
  function checkCookie() {
    if (
      document.cookie.split(";").some((item) => item.includes("login=1"))
    ) {
      console.log('The cookie "login" has "1" for value');
    } else {
      window.location.href = "/index.html";
    }
  }
</script>
```
```
<script>
  function login() {
    let form = document.getElementById("login-form");
    console.log(form.elements);
    let username = form.elements["username"].value;
    let password = form.elements["password"].value;
    if (
      username === "admin" &&
      password === "Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!"
    ) {
      document.cookie = "login=1";
      window.location.href = "/dashboard.html";
    } else {
      document.getElementById("error").innerHTML =
        "INVALID USERNAME OR PASSWORD!";
    }
  }
</script>
```

7. The password is `Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!`.
