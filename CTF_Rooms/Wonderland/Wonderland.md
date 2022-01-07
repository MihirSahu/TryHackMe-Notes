# Wonderland



1. Enumerate with nmap
```
root@ip-10-10-15-9:~# sudo nmap -sS -A -script=vuln 10.10.149.16

Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-05 04:23 GMT
Nmap scan report for ip-10-10-149-16.eu-west-1.compute.internal (10.10.149.16)
Host is up (0.00047s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /r/: Potentially interesting folder
|_  /img/: Potentially interesting folder
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
MAC Address: 02:49:6E:A7:5C:17 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=1/5%OT=22%CT=1%CU=40034%PV=Y%DS=1%DC=D%G=Y%M=02496E%TM
OS:=61D51F7D%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10A%TI=Z%CI=Z%TS=A)
OS:SEQ(SP=105%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M2301ST11NW7%O2=M230
OS:1ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11NW7%O5=M2301ST11NW7%O6=M2301ST11)W
OS:IN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F
OS:507%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)
OS:T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%
OS:S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(
OS:R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0
OS:%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.47 ms ip-10-10-149-16.eu-west-1.compute.internal (10.10.149.16)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 547.47 seconds
```

2. We see tht a web server is running on port 80, so run gobuster with the big wordlist
```
root@ip-10-10-15-9:~/Downloads/Wonderland# gobuster dir -w /usr/share/wordlists/dirb/big.txt -u http://10.10.149.16/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.149.16/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/big.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/01/05 05:09:22 Starting gobuster
===============================================================
/img (Status: 301)
/poem (Status: 301)
/r (Status: 301)
===============================================================
2022/01/05 05:09:24 Finished
===============================================================
```

3. Let's visit the webpage. All it says is `Follow the White Rabbit`, and contains a picture of the white rabbit from the novel

4. Visit each of the routes found with gobuster and check the source code and the Network and Cookies tabs in Inspect Element. Nothing seems to be hidden in the source code, and nothing special is seen in Network or Cookies. Now take a look at the actual contents of the directories. `/poem` contains a poem called `The Jabberwocky`. A quick search reveals that it's a nonsense poem that was included in the novel `Through the Looking-Glass`. This doesn't seem to help us at the moment, so let's go to the next route. `/img` contains 3 images: `alice_door.jpg`, `alice_door.png`, and `white_rabbit_1.jpg`. Note: from the source code of the index page we see that `white_rabbit_1.jpg` was the picture used to show the white rabbit. Download all of these images and analyze the metadata with exiftool `exiftool <image>`. Nothing seems out of place. Now try using steghide `steghide extract -sf <image>` on them to see if there's any files hidden inside. The 2 `alice_door` images don't seem to have anything, but `white_rabbit_1.jpg` is not password protected and contains `hint.txt`, which contains the text `follow the r a b b i t`. This doesn't mean anything to us at the moment. Lastly, we can use stegsolve to try to analyze the pictures, but we find nothing. Moving on to `/r`, we find is `Keep Going. "Would you tell me, please, which way I ought to go from here?"`. This doesn't tell us much but from the it's probably not a coincidence that the route starts with an `r`, just like the work `rabbit`. Additionally, the hint told us to follow the `r a b b i t`. Could it be referring to the URL, and specifically the route `/r`? There can't be any spaces in URLs, so we can try using `/r_a_b_b_i_t`, but it doesn't work. We can also try using `/`. So if we try `/r/a`, we find that we're directed to another page. As we keep going through the letters in `rabbit`, `/r/a/b/b/i/t` we are presented with quotes from the novel. Make sure to view the source code and inspect element to see if there are any clues hidden. When we get to the `t`, we find that we're instructed to `Open the door and enter wonderland`. Looking through the source code for this page we find a hidden paragraph `<p style="display: none;">alice:HowDothTheLittleCrocodileImproveHisShiningTail</p>` that look like some kind of username and password combination. We know from the nmap scan that ssh is open, and using `ssh alice@<ip address>` with the password successfuly logs us into the machine as alice
```
Open the door and enter wonderland

"Oh, you're sure to do that," said the Cat, "if you only walk long enough."

Alice felt that this could not be denied, so she tried another question. "What sort of people live about here?"

"In that direction,"" the Cat said, waving its right paw round, "lives a Hatter: and in that direction," waving the other paw, "lives a March Hare. Visit either you like: they're both mad."
```

5. 
