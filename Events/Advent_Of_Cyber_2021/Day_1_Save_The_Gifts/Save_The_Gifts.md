# Save the Gifts!

## What is an IDOR vulnerability?
- IDOR stands for Insecure Direct Object Reference and is a type of access control vulnerability
- Access control vulnerability when an attacker can gain access to information or actions not intended for them
- Can occur when a web server receives user-supplied input to retrieve objects, and the server doesn't valiate whether the user should have access to it
## How to find and exploit IDOR vulnerabilities?
- IDOR vulnerabilities rely on user supplied data, which can be found in three places:
1. Query Component - passed in the url when making a request to a website
    - Ex. `https://website.thm/profile?id=23`
    - Protocol: https://
    - Domain: website.thm
    - Page: /profile
    - Query Component: id=23
    - By changing the query component, we could potentially view other users data
2. Post Variables - Examining the forms of a website can reveal fields that could be vulnerable
><form method="POST" action="/update-password">
>    <input type="hidden" name"user_id" value="123">
>    <div>New Password:</div>
>    <div><input type="password" name="new_password"></div>
>    <div><input type="submit" value="Change Password">
></form>
    - User's id is being passed to the webserver in a hidden field, changing the value may change the password of another user's account
3. Cookies
    - Used to remember your session
    - Usually, a session id - consisting of a long string of random text - will be sent to the webserver, which then retrieves your user information
    - Sometimes user information may be stored in the cookie itself, and tampering with the cookie may display another user's information
## Exercise
1. The Boss!
2. Build Manager
3. Mischief Manager
4. THM{AOC_IDOR_2B34BHI3}
