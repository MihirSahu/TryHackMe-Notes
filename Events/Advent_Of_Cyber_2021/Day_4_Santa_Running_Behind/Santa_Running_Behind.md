# Santa's Running Behind

## What is Authentication?
- Authentication is the process of verifyign a user's identity
- Can be verified in a few ways
    1. A known ser of credentials to the server and user such as a username and password
    2. Token authentication (unique pieces of excrypted text)
    3. Biometric authentication (fingerprints, retina data, etc.)
- **Authentication is different from authorization**
- Authorization is what an authenticated user can or cannot access
## What is Fuzzing?
- Fuzzing is the automated testing of an element of a web application until the application gives avulnerability of valuable information
- We can use wordlists to test a web application's response to various info
### Fuzzing with Burpsuite
1. Set up firefox to work with burpsuite by either using the [FoxyProxy](https://getfoxyproxy.org/) extension or setting it up [manually](https://tryhackme.com/resources/blog/setting-up-burp)
2. After burpsuite is set up, navigate to the website you want to fuzz. It will hang, and the intercepted content will appear in the Proxy > Intercept tab on burpsuite
3. Click Forward until the website loads. Then enter a random username and password and click Login. Burpsuite will intercept this request and display it in the Intercept tab
>POST / HTTP/1.1
>Host: 10.10.182.139
>User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
>Accept-Language: en-US,en;q=0.5
>Accept-Encoding: gzip, deflate
>Content-Type: application/x-www-form-urlencoded
>Content-Length: 39
>Origin: http://10.10.182.139
>Connection: close
>Referer: http://10.10.182.139/
>Cookie: PHPSESSID=r5im8cnd1fbt6nbmpp52kuuld6
>Upgrade-Insecure-Requests: 1
>
>username=santa&password=hi&submit=Login
4. Now Right click and Send to Intruder. Then go to Intruder > Positions and select "Clear §". Since we already know what the username is, we only need to fuzz the password, so highlight the value of the password and click "Add §"
5. Go to the Payloads tab and add the payload in the Payload Options section. Then click Start Attack
6. A new window will pop up that displays the word from the wordlist, the response, and the response size. The responses of the wrong words will have the same sizes, while the correct word will have a different size from the rest
## Exersize
- Do exactly what we did in the example and we find that the password is "cookie" and the flag is "THM{SANTA_DELIVERS}"
