# IDOR

## What is an IDOR?
- IDOR stands for Insecure Direct Object Reference and is a type of access control vulnerability
- Access control vulnerability when an attacker can gain access to information or actions not intended for them
- Can occur when a web server receives user-supplied input to retrieve objects, and the server doesn't valiate whether the user should have access to it
## An IDOR Example
- The online store email looks vulnerable because it has a directory that looks like a kind of user id `https://onlinestore.thm/order/1234/invoice`
- Go to it, change the `1234` to `1000`, and we get THM{IDOR-VULN-FOUND}
## Finding IDORs in Encoded IDs
- When passing data from page to page by post data, query strings, or cookies, web devs will take the raw data and encode it
- Encoding data changes binary data to ascii string; the most common encoding technique on the web is base4
- If you suspect an IDOR, you can decode the data, change a value like user id, and then encode it and resubmit it
## Hashed IDs
- IDs can also be hashed, but they can follow a predictable pattern , like being a hashed version of the integer value
- Hashes can be cracked using software like hashcat or john the ripper, or web services like [crackstation](phttps://crackstation.net/) can be used to find matches
- A common algorithm for hashing IDs is md5
## Unpredictable IDs
- If the id cannot be detected using the other methods, a good way of IDOR detection is creating two accounts and swapping the ID numbers between them
## A Practical IDOR Example
1. Go to the website `https://10-10-105-54.p.thmlabs.com/`, navigate to the Customer section and sign up, and then go to the Your Account section
2. Use inspect element and go to the Network tab, reload, and find the api in the form `/api/v1/customer?id={user_id}`
3. Go to `https://10-10-105-54.p.thmlabs.com/api/v1/customer?id=1` to get the username with id of 1 `adam84` 
4. Go to `https://10-10-105-54.p.thmlabs.com/api/v1/customer?id=3` to get the email with id of 3 `j@fakemail.thm`
