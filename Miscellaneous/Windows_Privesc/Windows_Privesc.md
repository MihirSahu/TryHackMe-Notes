# Windows Privesc


## Intro
- During a penetration test or CTF, getting into the system is easy, but escalating priveleges is tricky
- Account types
    - Administrator (local): This is the user with the most privileges.
    - Standard (local): These users can access the computer but can only perform limited tasks. Typically these users can not make permanent or essential changes to the system. 
    - Guest: This account gives access to the system but is not defined as a user. 
    - Standard (domain): Active Directory allows organizations to manage user accounts. A standard domain account may have local administrator privileges. 
    - Administrator (domain): Could be considered as the most privileged user. It can edit, create, and delete other users throughout the organization's domain. 
- The "SYSTEM" account is used by windows services to perform tasks, and is not an actual account
- Typical privilege escalation
    1. Enumerate the current user's privileges and the resources it can access
    2. If the AV allows it, run an automated enumeration script like winPEAS or PowerUp.ps1
    3. If the initial enumeration and scripts don't uncover an obvious strategy, try a different approach, like going over a [checklist](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md#firewall)

## Information Gathering
- Conduct thorough enumeration
- Using automated scripts will help, but know how to do it manually as well
- User Enumeration
    - Listing all users present on the system and looking at how they are configured can provide interesting info
    - Current user’s privileges: `whoami /priv`
    - List users: `net users`
    - List details of a user: `net user username (e.g. net user Administrator)`
    - Other users logged in simultaneously: `qwinsta` (the query session command can be used the same way) 
    - User groups defined on the system: `net localgroup`
    - List members of a specific group: `net localgroup groupname` (e.g. net localgroup Administrators)
- Collecting System Information
    - `systeminfo` will return overview of system
    - `systeminfo | findstr /B /C:"OS Name" /C:"OS Version"` returns summary
    - The computer name can also show what the system is used for or who the user is
    - `hostname`
