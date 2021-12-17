# Sharing Without Caring

1. Use nmap to enumerate
```
$ sudo nmap --script=vuln -sS -A 10.10.119.239                                                                                                                                                           1 ⨯
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-13 16:51 EST
Pre-scan script results:
| broadcast-avahi-dos: 
|   Discovered hosts:
|     224.0.0.251
|   After NULL UDP avahi packet DoS (CVE-2011-1002).
|_  Hosts are all up (not vulnerable).
Nmap scan report for 10.10.119.239
Host is up (0.20s latency).
Not shown: 993 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
111/tcp  open  rpcbind       2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
2049/tcp open  mountd        1-3 (RPC #100005)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 4 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR

TRACEROUTE (using port 139/tcp)
HOP RTT       ADDRESS
1   87.47 ms  10.13.0.1
2   ... 3
4   196.83 ms 10.10.119.239

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 274.60 seconds
```
2. 7
- Network File System (NFS) is a protocol that allows the ability to transfer files between different computers and is available on many systems, including MS Windows and Linux
- Depending on whether we used -sV or -A on nmap, we can see any nfs services
3. 2049
- Once we know that NFS is running we can use the `showmount` tool to check which files are being shared
4. Use `showmount -e <ip>` to display shares
```
$ showmount -e 10.10.71.38                  
Export list for 10.10.71.38:
/share        (everyone)
/admin-files  (everyone)
/my-notes     (noone)
/confidential (everyone)
```
5. 4
6. 3
- Create a new folder and mount the /share share to the folder: `$ sudo mount 10.10.71.38:/share temp`
7. Open up 2680.txt and we see that it's a book titled Meditations
8. Use `umount temp` to unmount that /share share. Then try mounting the other shares and checking their contents. When we try the admin-files share we get `mount.nfs: access denied by server while mounting 10.10.71.38:/admin-files`. When we try /confidential, we see that there's an ssh folder inside with the private and public keys
9. Use `md5sum id_rsa`
```
$ md5sum id_rsa
3e2d315a38f377f304f5598dc2f044de  id_rsa
```
