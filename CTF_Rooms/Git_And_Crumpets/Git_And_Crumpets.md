# Git and Crumpets


1. Run a port scan with nmap.
```
root@ip-10-10-35-21:~# sudo nmap -sS -A 10.10.164.248

Starting Nmap 7.60 ( https://nmap.org ) at 2022-07-13 20:01 BST
Nmap scan report for ip-10-10-164-248.eu-west-1.compute.internal (10.10.164.248)
Host is up (0.00054s latency).
Not shown: 997 filtered ports
PORT     STATE  SERVICE    VERSION
22/tcp   open   ssh        OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 d5:33:1f:04:50:a3:f8:9b:a5:d5:55:10:04:52:83:69 (RSA)
|_  256 4a:89:06:8b:1e:23:03:4a:7c:c4:92:6b:0f:84:3e:f8 (ECDSA)
80/tcp   open   http       nginx
|_http-server-header: nginx
| http-title: Hello, World
|_Requested resource was http://ip-10-10-164-248.eu-west-1.compute.internal/index.html
9090/tcp closed zeus-admin
MAC Address: 02:36:EF:45:A2:03 (Unknown)
Aggressive OS guesses: HP P2000 G3 NAS device (91%), Linux 3.13 (90%), Linux 3.8 (90%), Linux 2.6.32 (89%), Infomir MAG-250 set-top box (89%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (89%), Netgear RAIDiator 4.2.21 (Linux 2.6.37) (89%), Linux 2.6.32 - 3.13 (89%), Linux 3.3 (89%), Linux 3.7 (88%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

TRACEROUTE
HOP RTT     ADDRESS
1   0.54 ms ip-10-10-164-248.eu-west-1.compute.internal (10.10.164.248)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.47 seconds
```
