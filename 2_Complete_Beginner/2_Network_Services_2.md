# Network Services 2
- This was supposed to be included in Network Exploitation Basics notes but that was a normal text file and I wanted to use markdown :(

## Understanding NFS
- Network File System - allows a system to share directories and files with others over a network
- Programs can access files on remote systems like as if they were local files
- How does NFS work?
    1. Client will request to mount a directory from a remote host on a local directory (just like it mounts a physical device)
        - The mount service will connect to the relevant mount daemon using RPC
    2. The server checks if the user has permission to mount whatever directory has been specified. Then it returns a file handle which uniquely identifies each file and directory on the server
    3. If someone wants to access a file using NFS, an RPC call is placed to NFSD (NFS daemon) on the server
        - Takes parameters like:
            - File handle
            - Name of file
            - User ID
            - Group ID

## Enumerating NFS
- Enumeration - process which establishes an active connection to the target hosts to discover potential attack vectors in the system
- nfs-common is needed to interact with any NFS share
    - Contains programs like lockd, statd, showmount, nfsstat, gssd, idmapd
- View NFS shares with `showmount -e [IP]`
- Mounting NFS shares
    - Your client's system needs a directory to mount all the content shared by the host server
    - `sudo mount -t nfs <IP>:<share> <directory to mount to> -nolock`

## Exploiting NFS
- If you have a low privilege shell on any machine that has an NFS share, it's possible to escalate privileges
- root_squash is a feature that's enabled by default on NFS that prevents anyone connecting to the NFS share from having root access to the NFS volume
    - If it's turned off then SUID bit files can be created
- Steps
```
    NFS Access ->
        Gain Low Privilege Shell ->
            Upload Bash Executable to the NFS share ->
                Set SUID Permissions Through NFS Due To Misconfigured Root Squash ->
                    Login through SSH ->
                        Execute SUID Bit Bash Executable ->
                            ROOT ACCESS
```

## SMTP
- SMTP - Simple mail transfer protocol
	- Handles the sending of emails
	- Functions
		- Verifies who is sending emails through SMTP server
		- Sends the outgoing mail
		- If the outgoing mail can't be delivered it sends the message back to the sender
- POP/IMAP handle the retrieving of emails
	- POP - Post office protocol
		- Downloads the inbox from the mail server to the client
	- IMAP - Internet message access protocol
		- Synchronizes the current inbox and downloads anything new
- Steps
```
1. The mail user agent, which is either your email client or an external program. connects to the SMTP server of your domain, e.g. smtp.google.com. This initiates the SMTP handshake. This connection works over the SMTP port- which is usually 25. Once these connections have been made and validated, the SMTP session starts.

2. The process of sending mail can now begin. The client first submits the sender, and recipient's email address- the body of the email and any attachments, to the server.

3. The SMTP server then checks whether the domain name of the recipient and the sender is the same.

4. The SMTP server of the sender will make a connection to the recipient's SMTP server before relaying the email. If the recipient's server can't be accessed, or is not available- the Email gets put into an SMTP queue.

5. Then, the recipient's SMTP server will verify the incoming email. It does this by checking if the domain and user name have been recognised. The server will then forward the email to the POP or IMAP server, as shown in the diagram above.

6. The E-Mail will then show up in the recipient's inbox.
```

## Enumerating SMTP
- Enumerating server details
	- Poorly configured mail servers can provide an initial foothold into a network
	- First, fingerprint the server to make targeting as precise as possible
		- Use metasploit's `smtp_version` module
- Enumerating users from smtp
	- SMTP service has two internal commands that allow enumeration of users
		- VRFY - confirms names of valid users
		- EXPN - reveals actual addresses of user aliases and lists of email
	- We can use metasploit's `smtp_enum` module for this
	- Can also use [smtp-user-enum](https://pentestmonkey.net/tools/user-enumeration/smtp-user-enum)
- We should look for a user account name and the type of SMTP server and OS running

## MySQL
- MySQL isa a RDBMS based on SQL
- Uses the client server model, communicate with MySQL protocol
- Server handles creating, editing, and accessing data
- Stages
	1. MySQL creates a database for storing and manipulating data, defining the relationship of each table
	2. Clients make requests by making specific statements in SQL
	3. The server will respond to the client with whatever information has been requests

## Enumerating MySQL
- MySQL is likely not going to be the first point of call when getting initial information about the server
- Typically, you will have gained some initial credentials from enumerating other services that you can then use to enumerate and exploit the MySQL service
- You will need to have MySQL installed on your system
- Metasploit's built in module `mysql_sql` or nmap scripts like `mysql-enum` can be used
- Connect to mysql server with `mysql -h <ip address> -u <username> -p`

## Exploiting MySQL
- `mysql_schemadump` module dumps databases
- `mysql_hashdump` module dumps password hashes

## Further Learning
- [Resource 1](https://web.mit.edu/rhel-doc/4/RH-DOCS/rhel-sg-en-4/ch-exploits.html)
- [Resource 2](https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/)
