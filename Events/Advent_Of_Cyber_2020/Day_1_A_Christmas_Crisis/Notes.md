# Day 1: A Christmas Crisis

## Notes
**Cookies**
- Http is a stateless protocol, so no the web server will have no way of knowing if pc has made request before
- To upgrade user experience (such as not asking the password to a website every time you visit it) cookies are used
- Cookies are stored on your pc and sent to the website whenever you access it to let it know who you are
- These cookies can be modified with your browser's developer tools
- Cookies can be used to escalate privileges if you have an Administrator's autorization cookie

## Writeup
1. The name of the cookie used for authentication is 'auth'
2. The auth cookie is encoded in hexadecimal
3. The cookie is decoded and stored in the json format, which is associated with javascript
4. To bypass the authentication:
- My auth cookie was encoded in hex: 7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a227468656f6e65227d
- If we decode it in cyberchef we get {"company":"The Best Festival Company", "username":"theone"}
- If we want santa's cookie, we simply change the username to "santa" and encode it again to get 7b22636f6d70616e79223a22546865204265737420466573746976616c20436f6d70616e79222c2022757365726e616d65223a2273616e7461227d
- Now we paste this into the cookie section in developer tools and refresh the page
5. Now we activate the assembly line and get this flag: THM{MjY0Yzg5NTJmY2Q1NzM1NjBmZWFhYmQy}
