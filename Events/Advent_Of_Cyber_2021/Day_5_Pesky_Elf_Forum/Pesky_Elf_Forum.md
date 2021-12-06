# Pesky Elf Forum

## What is an XSS Vulnerability?
- Cross site scripting (XSS) is an injection attack where javascript is injected into a website with the intention of being executed by other users
- If you can get js to run on a victim's computer, you can:
    - Steal their cookies and take over their session
    - Run a keylogger
    - Redirect to different websites
## Types of XSS Vulnerabilities
- Dom
    - DOM stands for Document Object Model
    - Represents the page so that programs can change the structure, style, and content
    - DOM based XSS is when javascript execution happends directly in the browser without any new pages being loaded or data being submitted to the backend
    - Execution occurs when the website javascript code acts on input or user interaction
- Reflected
    - Occurs when user-supplied data in an HTTP request is included in the webpage source without any validation
    - Ex. `https://website.thm/login?error=Username%20Is%20Incorrect`
- Stored
    - Payload is stored on the webapplication (Ex. database) and then runs when others visit the website
    - Has the potential to effect multiple people
    - Ex. If a visitor of a blog comments an XSS payload and is not properly sanitized, then every person that visits the page could be vulnerable
- Blind
    - Similar to stored, but you can't see the payload working or be able to test it
## Exercise
1. Log in with username "McSkidy" and password "password", go to settings, and change your password to anything you want
2. Notice that the url has a reflected vulnerability, and we can change the password to an account by navigating to `/settings?new_password=password`
3. Now test if the comment box allows html code to be executed by posting `hello <u>world</u>`. Because the word "world" was underlined, it means that html code can be executed through the comments box, and our comment will load whenever any user visits the website
4. Now we can create the payload `<script>fetch('settings?new_password=pass123')</script>` and post it. Whenever a logged in user visits the website, their password will automatically be changed to pass123. This is now a stored vulnerability
5. Assume that the grinch has visited the website and their password has been changed. Log in with "grinch" and "pass123", go to settings, and disable the "Christmas to Buttmas" option
6. The flag is `THM{NO_MORE_BUTTMAS}`
