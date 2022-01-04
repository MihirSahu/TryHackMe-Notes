# Volume 2


1. Enumerate with nmap
```
Starting Nmap 7.60 ( https://nmap.org ) at 2022-01-02 21:58 GMT
Nmap scan report for ip-10-10-7-155.eu-west-1.compute.internal (10.10.7.155)
Host is up (0.00067s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
| http-aspnet-debug: 
|_  status: DEBUG is enabled
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-enum: 
|   /login/: Login page
|   /robots.txt: Robots file
|_  /index/: Potentially interesting folder
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
MAC Address: 02:CD:1D:17:B1:B1 (Unknown)
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.13
OS details: Linux 3.13
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.67 ms ip-10-10-7-155.eu-west-1.compute.internal (10.10.7.155)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.01 seconds
```

2. Check robots.txt, convert from hex `45 61 73 74 65 72 20 31 3a 20 54 48 4d 7b 34 75 37 30 62 30 37 5f 72 30 6c 6c 5f 30 75 37 7d` to ascii to get `THM{4u70b07_r0ll_0u7}`. The file also denies robots from accessing a route that seems to be encoded in base64. Use cyberchef to decode it 4 times with base64 and we find `/DesKel_secret_base`. Navigate to it, view the source code to find the 2nd flag `THM{f4ll3n_b453}`
```
User-agent: * (I don't think this is entirely true, DesKel just wanna to play himself)
Disallow: /VlNCcElFSWdTQ0JKSUVZZ1dTQm5JR1VnYVNCQ0lGUWdTU0JFSUVrZ1p5QldJR2tnUWlCNklFa2dSaUJuSUdjZ1RTQjVJRUlnVHlCSklFY2dkeUJuSUZjZ1V5QkJJSG9nU1NCRklHOGdaeUJpSUVNZ1FpQnJJRWtnUlNCWklHY2dUeUJUSUVJZ2NDQkpJRVlnYXlCbklGY2dReUJDSUU4Z1NTQkhJSGNnUFElM0QlM0Q=


45 61 73 74 65 72 20 31 3a 20 54 48 4d 7b 34 75 37 30 62 30 37 5f 72 30 6c 6c 5f 30 75 37 7d
```

3. Check page source code. Scroll until you find the red button `<a href="/ready"><p style="text-align:center"><img src="button.gif"/></p></a>` Click on `/ready` to go to the source code page for `/ready`. Here we find the 9th flag, `THM{60nn4_60_f457}`. There's a `<meta>` tag here that leads to gone.php, so navigate there to get the 13th flag, `THM{1_c4n'7_b3l13v3_17}`

4. Keep scrolling through the home page source code and we find this. It's in base64, so convert it with cyberchef and use the magic stick button to render it and get the 14th flag, `THM{d1r3c7_3mb3d}`

6. Keep scrolling through source code until you come to `/game2`. Click on it to go to the source code for game2. We see that we need to click all 3 buttons at once, and if we don't then we get an error message. We see that a POST request is being used to send the data. Let's go to Inspect Element > Network and click on a button. A new request pops up, and if we double click on it and go to the Request tab we see that the body of the request is in the form `button1=button1&submit=submit`. Now that we know the structure we can use curl to "click" all three buttons together. Use `curl -d "button1=button1&submit=submit" -d "button2=button2&submit=submit" -d "button3=button3&submit=submit" http://10.10.242.21/game2/` this command to click all buttons, and curl will print the returned html to stdout. We find that the 16th flag is `THM{73mp3r_7h3_h7ml}`

7. Scroll through the source code and we see the `nyan` malfunction button. We see that clicking the button executes a function called `nyan()`. However, when we click it we see in Inspect Element > Console that there is no `nyan()` function, so clicking it does nothing. We see that there's a function called `catz()` that changes the content of the paragraph tag with the id `nyan` to a string. So we use Inspect Element to change the `onclick="nyan()"` into `onclick="catz()"`, and when we click the button we get the text printed out on the webpage. Now that we have what seems to be binary, we can convert to [hex](https://www.rapidtables.com/convert/number/binary-to-hex.html) and then to [ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html) to get `THM{j5_j5_k3p_d3c0d3}`
```
<script>
	function catz(){
        	document.getElementById("nyan").innerHTML = "100010101100001011100110111010001100101011100100010000000110001001101110011101000100000010101000100100001001101011110110110101000110101010111110110101000110101010111110110101100110011011100000101111101100100001100110110001100110000011001000011001101111101"
	}
</script>
```

7. Let's take a break from the source code. Let's use gobuster on the website. There's a lot to unpack here, so let's visit all the directories. Most of the directories are just pictures or files that we've already explored. The only ones that seem interesting are `/cgi-bin/`, `/login`, and `/small`. Navigating to `/small` gives us our 19th flag, `THM{700_5m4ll_3yy}`, and `/cgi-bin/` gives us a 403, which means we're not allowed to access it. Let's run gobuster on it to see if anything pops up. Nothing shows up, so let's try the `/login` page. Check the source code and we find the 3rd flag `THM{y0u_c4n'7_533_m3}`.
```
$ gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://10.10.247.181/       
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.247.181/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/01/02 23:48:39 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 285]
/.htaccess            (Status: 403) [Size: 290]
/.htpasswd            (Status: 403) [Size: 290]
/button               (Status: 200) [Size: 39148]
/cat                  (Status: 200) [Size: 62048]
/cgi-bin/             (Status: 403) [Size: 289]  
/index                (Status: 200) [Size: 94328]
/index.php            (Status: 200) [Size: 94328]
/iphone               (Status: 200) [Size: 19867]
/login                (Status: 301) [Size: 314] [--> http://10.10.247.181/login/]
/robots               (Status: 200) [Size: 430]                                  
/robots.txt           (Status: 200) [Size: 430]                                  
/server-status        (Status: 403) [Size: 294]                                  
/small                (Status: 200) [Size: 689]                                  
/static               (Status: 200) [Size: 253890]                               
/who                  (Status: 200) [Size: 3847428]                              
                                                                                 
===============================================================
2022/01/02 23:50:11 Finished
===============================================================
```

8. We try the credentials found at the end of the home page on the login page, but they don't work. It looks like they want us to post the username and password `Hey! I got the easter 20 for you. I leave the credential for you to POST (username:DesKel, password:heIsDumb). Please, I beg you. Don't let him know.`. Let's use the same strategy we used in step 6 and use Inspect Element to analyze how the POST request is structured and then emulate it with curl. Just for this, we use the username `hi` and password `hi`. From the Network > Request tab we see that the body is `username=hi&password=hi&submit=submit`.

9. Jumping back to the iphone picture on the home page, we see that we need to have an iphone with IOS 13.1.12 and safari 13 to view the message. Maybe it detects our model and version through the user-agent? We find the user-agent for [safari and ios online](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) (or look at the hint) and then craft our request with curl `curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1" http://10.10.32.134/`. The response is printed to stdout, and we find `You are Rich! Subscribe to THM server ^^ now. Oh btw, Easter 8: THM{h3y_r1ch3r_wh3r3_15_my_k1dn3y}`

10. Now let's take a look at the tryhackme subscription voucher. If we visit the link, we get `only people came from tryhackme are allowed to claim the voucher.`. How can we make it seem that we're coming from tryhackme? The referer header allows the website to identify which page we're visiting from. So we create the curl command `curl --referer "tryhackme.com" http://10.10.32.134/free_sub/` to make it seem like we're coming from tryhackme and we get `Nah, there are no voucher here, I'm too poor to buy a new one XD. But i got an egg for you. Easter 10: THM{50rry_dud3}`

11. Let's look at the form with 4 different menu items and a button. One of the hints told us to look at the response header, so maybe this is it? Navigate to Inspect Element > Network and click the button. Double click on the POST request and look at the response headers, and we find `Busted: Hey, you found me, take this Easter 6: THM{l37'5_p4r7y_h4rd}`

12. Let's try Game 1 now. After trying a few letters, we see that two digits are used to represent each character. We can brute force every character to see if it matches the number in the hints `hints: 51 89 77 93 126 14 93 10 `

## Easter Eggs
1. `THM{4u70b07_r0ll_0u7}`
2. `THM{f4ll3n_b453}`
3. `THM{y0u_c4n'7_533_m3}`
6. `THM{l37'5_p4r7y_h4rd}`
8. `THM{h3y_r1ch3r_wh3r3_15_my_k1dn3y}`
9. `THM{60nn4_60_f457}`
10. `THM{50rry_dud3}`
13. `THM{1_c4n'7_b3l13v3_17}`
14. `THM{d1r3c7_3mb3d}`
16. `THM{73mp3r_7h3_h7ml}`
17. `THM{j5_j5_k3p_d3c0d3}`
19. `THM{700_5m4ll_3yy}`
