# Introduction To Cyber Security


## Introduction To Defensive Security
- Offensive security focuses on breaking into systems
	- Exploitin bugs, abusing insecure setups, taking advantage of unenforced access control policies
- Red teams and penetration testers specalize in offensive security
- Defensive security focuses on preventing intrusions from occuring and detecting intrusions when they occur and responding properly
- Some tasks related to defensive security:
```
User cyber security awareness: Training users about cyber security helps protect against various attacks that target their systems.
Documenting and managing assets: We need to know the types of systems and devices that we have to manage and protect properly.
Updating and patching systems: Ensuring that computers, servers, and network devices are correctly updated and patched against any known vulnerability (weakness).
Setting up preventative security devices: firewall and intrusion prevention systems (IPS) are critical components of preventative security. Firewalls control what network traffic can go inside and what can leave the system or network. IPS blocks any network traffic that matches present rules and attack signatures.
Setting up logging and monitoring devices: Without proper logging and monitoring of the network, it won’t be possible to detect malicious activities and intrusions. If a new unauthorized device appears on our network, we should be able to know.
```
### Areas of Defensive Security
- Security Operations Center (SOC)
	- A team of cyber security professions that monitors the network and its systems to detect malicious cyber security events
	- Main areas of interest:
	```
	Vulnerabilities: Whenever a system vulnerability (weakness) is discovered, it is essential to fix it by installing a proper update or patch. When a fix is not available, the necessary measures should be taken to prevent an attacker from exploiting it. Although remediating vulnerabilities is of vital interest to a SOC, it is not necessarily assigned to them.
	Policy violations: We can think of a security policy as a set of rules required for the protection of the network and systems. For example, it might be a policy violation if users start uploading confidential company data to an online storage service.
	Unauthorized activity: Consider the case where a user’s login name and password are stolen, and the attacker uses them to log into the network. A SOC needs to detect such an event and block it as soon as possible before further damage is done.
	Network intrusions: No matter how good your security is, there is always a chance for an intrusion. An intrusion can occur when a user clicks on a malicious link or when an attacker exploits a public server. Either way, when an intrusion occurs, we must detect it as soon as possible to prevent further damage.
	```
	- Threat Intelligence
		- Intelligence - information you gather about actual and potential enemies
		- Threat - any action that can disrupt or adversly affect a system
		- Different companies have different adversaries
		- Learning about adversaries will allow us to prepare a response strategy
- Digital Forensics and Incident Response (DFIR)
	- Digital Forensics - application of science to investigate crimes and establish facts
		- Analyze evidence of an attack and its perpetrators
		- Focuses on different areas such as:
		```
		File System: Analyzing a digital forensics image (low-level copy) of a system’s storage reveals much information, such as installed programs, created files, partially overwritten files, and deleted files.
		System memory: If the attacker is running their malicious program in memory without saving it to the disk, taking a forensic image (low-level copy) of the system memory is the best way to analyze its contents and learn about the attack.
		System logs: Each client and server computer maintains different log files about what is happening. Log files provide plenty of information about what happened on a system. Some traces will be left even if the attacker tries to clear their traces.
		Network logs: Logs of the network packets that have traversed a network would help answer more questions about whether an attack is occurring and what it entails.
		```
	- Incident Response
		- Incident - a data breach or cyber attack
		- Specifies methodology that should be followed to handle an incident
		- Goal is to reduce damage and recover in the shortest time possible
		- Four major phases
		```
		Preparation: This requires a team trained and ready to handle incidents. Ideally, various measures are put in place to prevent incidents from happening in the first place.
		Detection and Analysis: The team has the necessary resources to detect any incident; moreover, it is essential to further analyze any detected incident to learn about its severity.
		Containment, Eradication, and Recovery: Once an incident is detected, it is crucial to stop it from affecting other systems, eliminate it, and recover the affected systems. For instance, when we notice that a system is infected with a computer virus, we would like to stop (contain) the virus from spreading to other systems, clean (eradicate) the virus, and ensure proper system recovery.
		Post-Incident Activity: After successful recovery, a report is produced, and the learned lesson is shared to prevent similar future incidents.
		```
	- Malware Analysis
		- Malicious software
		- Many types of malware:
		```
		Virus is a piece of code (part of a program) that attaches itself to a program. It is designed to spread from one computer to another; moreover, it works by altering, overwriting, and deleting files once it infects a computer. The result ranges from the computer becoming slow to unusable.
		Trojan Horse is a program that shows one desirable function but hides a malicious function underneath. For example, a victim might download a video player from a shady website that gives the attacker complete control over their system.
		Ransomware is a malicious program that encrypts the user’s files. Encryption makes the files unreadable without knowing the encryption password. The attacker offers the user the encryption password if the user is willing to pay a “ransom.”
		```
		- Methods used to analyze malware:
		```
		Static analysis works by inspecting the malicious program without running it. Usually, this requires solid knowledge of assembly language (processor’s instruction set, i.e., computer’s fundamental instructions).
		Dynamic analysis works by running the malware in a controlled environment and monitoring its activities. It lets you observe how the malware behaves when running.
		```

## Careers in Cyber
- [TryHackMe Room](https://tryhackme.com/room/careersincyber)
