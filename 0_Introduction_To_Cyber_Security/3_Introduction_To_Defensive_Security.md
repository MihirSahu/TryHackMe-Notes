# Introduction to Defensive Security


## Security Operations
- Team that monitors a company's network 24 hours a day
```
Find vulnerabilities on the network: A vulnerability is a weakness that an attacker can exploit to carry out things beyond their permission level. A vulnerability might be discovered in any device’s software (operating system and programs) on the network, such as a server or a computer. For instance, the SOC might discover a set of MS Windows computers that must be patched against a specific published vulnerability. Strictly speaking, vulnerabilities are not necessarily the SOC’s responsibility; however, unfixed vulnerabilities affect the security level of the entire company.

Detect unauthorized activity: Consider the case where an attacker discovered the username and password of one of the employees and used it to log in to the company system. It is crucial to detect this kind of unauthorized activity quickly before it causes any damage. Many clues can help us detect this, such as geographic location.

Discover policy violations: A security policy is a set of rules and procedures created to help protect a company against security threats and ensure compliance. What is considered a violation would vary from one company to another; examples include downloading pirated media files and sending confidential company files insecurely.

Detect intrusions: Intrusions refer to system and network intrusions. One example scenario would be an attacker successfully exploiting our web application. Another example scenario would be a user visiting a malicious site and getting their computer infected.

Support with the incident response: An incident can be an observation, a policy violation, an intrusion attempt, or something more damaging such as a major breach. Responding correctly to a severe incident is not an easy task. The SOC can support the incident response team handle the situation.
```

- Elements of Security Operations
	- Data Sources
		```
		Server logs: There are many types of servers on a network, such as a mail server, web server, and domain controller on MS Windows networks. Logs contain information about various activities, such as successful and failed login attempts, among many others. There is a trove of information that can be found in the server logs.
		DNS activity: DNS stands for Domain Name System, and it is the protocol responsible for converting a domain name, such as tryhackme.com, to an IP address, such as 10.3.13.37, among other domain name related queries. One analogy of the DNS query is asking, “How can I reach TryHackMe?” and someone replying with the postal address. In practice, if someone tries to browse tryhackme.com, the DNS server has to resolve it and can log the DNS query to monitoring. The SOC can gather information about domain names that internal systems are trying to communicate with by merely inspecting DNS queries.
		Firewall logs: A firewall is a device that controls network packets entering and leaving the network mainly by letting them through or blocking them. Consequently, firewall logs can reveal much information about what packets passed or tried to pass through the firewall.
		DHCP logs: DHCP stands for Dynamic Host Configuration Protocol, and it is responsible for assigning an IP address to the systems that try to connect to a network. One analogy of the DHCP request would be when you enter a fancy restaurant, and the waiter welcomes you and guides you to an empty table. Know that DHCP has automatically provided your device with the network settings whenever you can join a network without manual configuration. By inspecting DHCP transactions, we can learn about the devices that joined the network.
		```
	- SOC Services
		- Reactive
			```
			Monitor security posture: This is the primary role of the SOC, and it includes monitoring the network and computers for security alerts and notifications and responding to them as the need dictates.
			Vulnerability management: This refers to finding vulnerabilities in the company systems and patching (fixing) them. The SOC can assist with this task but not necessarily execute it.
			Malware analysis: The SOC might recover malicious programs that reached the network. The SOC can do basic analysis by executing it in a controlled environment. However, more advanced analysis requires sending it to a dedicated team.
			Intrusion detection: An intrusion detection system (IDS) is used to detect and log intrusions and suspicious packets. The SOC’s job is to maintain such a system, monitor its alerts, and go through its logs as the need dictates.
			Reporting: It is essential to report incidents and alarms. Reporting is necessary to ensure a smooth workflow and to support compliance requirements.
			```
		- Proactive
			```
			Network security monitoring (NSM): This focuses on monitoring the network data and analyzing the traffic to detect signs of intrusions.
			Threat hunting: With threat hunting, the SOC assumes an intrusion has already taken place and begins its hunt to see if they can confirm this assumption.
			Threat Intelligence: Threat intelligence focuses on learning about potential adversaries and their tactics and techniques to improve the company’s defences. The purpose would be to establish a threat-informed defence.
			```

## Intro to Digital Forensics
- Forensics - application of science to investigate crimes
- Digital media
	- CDs
	- DVDs
	- USB
	- External storage
```
How should the police collect digital evidence, such as smartphones and laptops? What are the procedures to follow if the computer and smartphone are running?
How to transfer the digital evidence? Are there certain best practices to follow when moving computers, for instance?
How to analyze the collected digital evidence? Personal device storage ranges between tens of gigabytes to several terabytes; how can this be analyzed.
```
- Two types of investigations
	- Public sector - carried out by government and law enforcement agencies
	- Private sector - carried out by corporate bodies by assigning a private investigator
- When arriving at a scene
```
Acquire the evidence: Collect the digital devices such as laptops, storage devices, and digital cameras. (Note that laptops and computers require special handling if they are turned on; however, this is outside the scope of this room.)
Establish a chain of custody: Fill out the related form appropriately (Sample form). The purpose is to ensure that only the authorized investigators had access to the evidence and no one could have tampered with it.
Place the evidence in a secure container: You want to ensure that the evidence does not get damaged. In the case of smartphones, you want to ensure that they cannot access the network, so they don’t get wiped remotely.
Transport the evidence to your digital forensics lab.
```
- When at a lab
```

Retrieve the digital evidence from the secure container.
Create a forensic copy of the evidence: The forensic copy requires advanced software to avoid modifying the original data.
Return the digital evidence to the secure container: You will be working on the copy. If you damage the copy, you can always create a new one.
Start processing the copy on your forensics workstation.
```
- Digital forensics includes
```
Proper search authority: Investigators cannot commence without the proper legal authority.
Chain of custody: This is necessary to keep track of who was holding the evidence at any time.
Validation with mathematics: Using a special kind of mathematical function, called a hash function, we can confirm that a file has not been modified.
Use of validated tools: The tools used in digital forensics should be validated to ensure that they work correctly. For example, if you are creating an image of a disk, you want to ensure that the forensic image is identical to the data on the disk.
Repeatability: The findings of digital forensics can be reproduced as long as the proper skills and tools are available.
Reporting: The digital forensics investigation is concluded with a report that shows the evidence related to the case that was discovered.
```
