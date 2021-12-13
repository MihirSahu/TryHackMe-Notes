# Offensive is the Best Defense

- I know most if not all of this so the notes are going to be minimal

## Exercise
- Use nmap to find that 2 ports are open
>nmap -sT 10.10.136.173
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 00:36 EST
>Nmap scan report for 10.10.136.173
>Host is up (0.21s latency).
>Not shown: 998 closed tcp ports (conn-refused)
>PORT   STATE SERVICE
>22/tcp open  ssh
>80/tcp open  http
>
>Nmap done: 1 IP address (1 host up) scanned in 36.67 seconds
- The lowest port number is 22
- http
- Y
>sudo nmap -sS 10.10.136.173
>[sudo] password for kali: 
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 00:39 EST
>Nmap scan report for 10.10.136.173
>Host is up (0.21s latency).
>Not shown: 998 closed tcp ports (reset)
>PORT   STATE SERVICE
>22/tcp open  ssh
>80/tcp open  http
>
>Nmap done: 1 IP address (1 host up) scanned in 10.35 seconds
- Apache httpd 2.4.49
>nmap -sV 10.10.136.173
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 00:42 EST
>Nmap scan report for 10.10.136.173
>Host is up (0.21s latency).
>Not shown: 998 closed tcp ports (conn-refused)
>PORT   STATE SERVICE VERSION
>22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
>80/tcp open  http    Apache httpd 2.4.49
>Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
>
>Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
>Nmap done: 1 IP address (1 host up) scanned in 55.91 seconds
- CVE-2021-42013
- Use the hint given to get 20212
>sudo nmap -sT -p20000-21000 -T4 10.10.136.173                                                                                                                                                          1 ⨯
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 01:19 EST
>Nmap scan report for 10.10.136.173
>Host is up (0.21s latency).
>Not shown: 1000 closed tcp ports (conn-refused)
>PORT      STATE SERVICE
>20212/tcp open  unknown
>
>Nmap done: 1 IP address (1 host up) scanned in 18.82 seconds
- Add -sV to the command from the previous question to get telnetd
>sudo nmap -sT -p20000-21000 -T4 -sV 10.10.136.173
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 01:22 EST
>Nmap scan report for 10.10.136.173
>Host is up (0.21s latency).
>Not shown: 1000 closed tcp ports (conn-refused)
>PORT      STATE SERVICE VERSION
>20212/tcp open  telnet  Linux telnetd
>Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
>
>Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
>Nmap done: 1 IP address (1 host up) scanned in 14.40 seconds
