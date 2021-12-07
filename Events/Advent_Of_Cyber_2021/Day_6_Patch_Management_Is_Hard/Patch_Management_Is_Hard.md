# Patch Management is Hard

## Local File Inclusion Vulnerability
- Local file inclusion (LFI) vulerability is a web application vulnerability that allows the attacker to include and read local files on the server, which can contain keys, passwords, and other private data
- Occurs dure to a developer's lack of security awareness
    - Ex. If a developer includes files without proper input validation and doesn't filter/sanitize user input
- Found in various we applications
    - Ex. In php, these functions can cause the vulnerability
        - include
        - require
        - include_once
        - require_once
## Risk of LFI
- If a LFI is found, it's possible to read sensititive data and write to files
- One of the most significant risks is leaking sensitive data
- In some cases LFI can be chained to perform RCE on the server
## Identifying and Testing for LFI
- Attackers are interesed in HTTP parameters to manupulate input and inject attack payloads to see how the web application behaves
- Entry points - where to start looking for vulerabilities
    - It's important to use the web app and see how it works to find an entry point
    - Other entry points can be User-Agent, Cookies, session, and other HTTP headers
- HTTP query parameters are query strings attached to the URL that could be used to retrieve data or perform actions based on user input
- This code uses a GET request with the URL parameter 'file' to include a file on the page. This request can be mnade using `http://example.thm.labs/index.php?file=welcome.txt`, and is vulerable to LFI because it allows any user to access files in the directory
><?PHP 
>	include($_GET["file"]);
>?>
- Some Linux system files that contain sensitive information that we can test for:
>/etc/issue
>/etc/passwd
>/etc/shadow
>/etc/group
>/etc/hosts
>/etc/motd
>/etc/mysql/my.cnf
>/proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
>/proc/self/environ
>/proc/version
>/proc/cmdline
- A few techniques to use when testing:
    - A direct file inclusion, which starts with /etc/passwd
    - using `..` to get out the current directory, the number of `..` is varies depending on the web app directory. 
    - Bypassing filters using `....//`.
    - URL encoding techniques (such as double encoding)
- Ex. `http://example.thm.labs/page.php?file=/etc/passwd http://example.thm.labs/page.php?file=../../../../../../etc/passwd http://example.thm.labs/page.php?file=../../../../../../etc/passwd%00 http://example.thm.labs/page.php?file=....//....//....//....//etc/passwd http://example.thm.labs/page.php?file=%252e%252e%252fetc%252fpasswd`
