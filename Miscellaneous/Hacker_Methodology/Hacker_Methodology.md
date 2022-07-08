# Hacker Methodology


## Methodology Outline
1. Reconnaissance
2. Enumeration/Scanning
3. Gaining Access
4. Privilege Escalation
5. Covering Tracks
6. Reporting

## Reconnaissance
- Collect information about the target
- Single most important phase of a penetration test
- Mostly doesn't involve direct interaction with the target
- **Hackers use simple tools to conduct research**
- General resources
	- Google
	- Wikipedia
	- Social media
		- Twitter
		- Instagram
		- LinkedIn
	- PeopleFinder.com
	- who.is
	- sublist3r
	- hunter.io
	- wappalyzer

## Enumeration and Scanning Overview
- Interact with the target to attemt to find the attack surface and vulnerabilities related to the target
- Uses more advanced tools
- Tools
	- Nmap
	- Dirb
	- Dirbuster
	- enum4linux
	- Metasploit
	- Burp Suite

## Exploitation
- Exploit the vulnerabilites found in the previous stage
- This stage is only as good as the recon and enumeration pahses before it
- Tools
	- Metasploit
	- Burp Squite
	- Sql Map
	- Msfvenom
	- BeEF

## Privilege Escalation
- Escalate privileges to a higher user account
	- In Windows, this is usually `Administrator` or `System`
	- In Linux, this is usually `root`
- Can take many forms
	- Cracking password hashes found on the target
	- Finding a vulnerable service or version of a service which will allow you to escalate privilege THROUGH the service
	- Password spraying of previously discovered credentials (password re-use)
	- Using default credentials
	- Finding secret keys or SSH keys stored on a device which will allow pivoting to another machine
	- Running scripts or commands to enumerate system settings like 'ifconfig' to find network settings, or the command 'find / -perm -4000 -type f 2>/dev/null' to see if the user has access to any commands they can run as root

## Covering Tracks
- Always have explicit permission from the system owner regarding when the test is happening, how it's occuring, and the scope of targets in any penetration test
- Ethical hackers rarely need to cover their tracks, but they should carefull track and notate all of the tasks they have performed

## Reporting
- Often includes:
	- The Finding(s) or Vulnerabilities
	- The CRITICALITY of the Finding
	- A description or brief overview of how the finding was discovered
	- Remediation recommendations to resolve the finding
- Formats:
	- Vulnerability scan results (a simple listing of vulnerabilities)
	- Findings summary (list of the findings as outlined above)
	- Full formal report
