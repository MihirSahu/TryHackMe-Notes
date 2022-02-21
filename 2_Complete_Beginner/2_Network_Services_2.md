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
