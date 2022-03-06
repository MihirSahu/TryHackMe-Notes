# Common Attacke


- Common techniques used by attackers to target people online

## Social Engineering
- When a human rather than a computer is the target
    - Also referred to as `People Hacking`
```
Whilst the example linked above is relatively straightforward, social engineering attacks can become very complex and often result in an attacker gaining significant control over a target's life — both online and offline. Social engineering attacks are often multi-layered and escalate due to the snowball effect. For example, an attacker may start off by obtaining a small amount of publicly available information from a victim's social media presence, which they could then use to get more information from, say, your phone or broadband provider. The information obtained from the second stage could then be used to gain more useful information, then escalate step-by-step to something like the victim's bank account.
```
- [Resource 1](https://youtu.be/fHhNWAKw0bY?t=100), [Resource 2](https://youtu.be/PWVN3Rq4gzw)
- Many different types of social engineering
    - Calling phone company and taking possession of your account
    - Drop USB in public and wait for someone to plug it in
    - Leave a "charging cable" plugged into a socket in a public place
- Staying safe from social engineering attacks
    - Many times it won't be you who the attacker is talking to but rather someone who can give them what they need without your consent
    1. Always set up multiple forms of authentication
    2. Never plug in external media into a computer that you care about or that is connected to other devices
    3. Always insist on proof of identify when a stranger calls or messages you claiming to work for a company whose services you use

## Phishing
- Skipping most of this because I already did the Phishing module
```
Delete unknown or untrusted emails without opening them. If you can see anything suspicious in the email, also report it as spam to your email provider, or forward it to your IT Security department if you received the email at work.
Never open attachments from untrusted emails — this includes any attachments from a legitimate contact that you were not expecting.
Do not click on embedded links in emails or messages. Where possible, navigate to the real website in your web browser and access the content that way. If you absolutely must click on the link, ensure that the domain name is correct and that the link points to where you think it does.
Always make sure that your device and antivirus software are up-to-date.
Avoid making your personal information (e.g. email address and phone number) public if possible. If you must publish personal details publicly, create a "burner" email address (a temporary address made for one purpose, then destroyed soon afterwards) for the occasion, then destroy it as soon as it is no longer required.
```

## Malware and Ransomware
- Ransomware - infects as many systems as possible, encrypting data and holding it to ransom
- Exploits known vulnerabilities in commonly installed software, infects many systems, and then makes data inaccessible by encrypting it with a key known to the attacker
- Ex. [Wannacry](https://www.malwarebytes.com/wannacry)
- Many delivery methods use social engineering or phishing
- Staying safe
```
Always accept updates and patches when offered — especially in important software like operating systems. Updates often contain fixes to security flaws, so it is important to get these in place as soon as possible.
Never click on suspicious links, especially in emails. Try not to open file attachments if possible. If a message looks suspicious, delete it, or forward it to the appropriate team if using your work account.
Always be on the lookout for people trying to get you to download or run files — especially over email or instant messaging.
Never plug unknown media devices (e.g. USB devices) into important computers. If you find a device in public, do not plug it into your work laptop!
Always back up important data — this will be discussed in more detail later in the room and can be crucial in recovering from a ransomware attack.
Make sure that your antivirus software is always up-to-date and activated.
```
```
Note: If you or your business get infected with ransomware, do not pay the ransom. Instead, call your local authorities immediately, and try to contain the infection by disabling your router or otherwise physically preventing the infected device from connecting to anything else. Do not power the infected device off, as this can sometimes destroy any potential opportunities to decrypt the data without paying.
```

## Passwords and Authentication
- What makes a strong password?
```
Advice on what constitutes a strong password has changed over time. In the past, people were advised to choose complex passwords that were easy to remember, for example:

@Ed1nburgh#1988-2000!

The password above is a collection of lowercase and uppercase characters, including symbols and numeric digits. It is over eight characters long (making it almost impossible to attack by brute-force with our current level of technology) and is created using knowledge that is unlikely to be held by anyone other than the owner of the password. Importantly, it also doesn't conform to normal patterns  (using unusual symbols, exchanging only some characters of l33t speak, and containing a date range as opposed to a single date), making it harder to guess. For all intents and purposes, this is a traditionally strong password. That said, the personal connection means that this password could potentially still be made weaker through social engineering or in-depth information gathering on a target.

Current best practices lean more towards length than complexity. For example:

Vim is _obviously_, indisputably the best text editor in existence!

By using a passphrase rather than a traditional password, the password is significantly longer whilst still retaining some of the more complex elements — despite not looking quite so obfuscated. This has the advantage of being easier to remember whilst still being incredibly difficult to brute-force.

Ideally, however, you should use long, completely random passwords. For example:

w41=V1)S7KIJGPN,dII>cHEh>FRVQsj3M^]CB

These take millions of years to crack and are objectively the most secure option available. The drawback is usability; however, this is largely mitigated by using a password manager, which will be discussed in the next task.
```
- What makes a weak password?
```
People often go for simple passwords that mean something to them, often following one of a few "simple" patterns. For example, a commonly used pattern is a name/location, followed by a year, followed by an exclamation mark. For example:

Gareth2012!


This is enough to satisfy most password complexity requirements (lowercase and uppercase characters, over eight characters, contains numerical digits and a symbol); however, it is trivial to guess if an attacker knows that you have a son called Gareth who was born in 2012. This kind of password is inherently extremely insecure.

In short, any password that could easily be guessed by someone who knows you relatively well (this includes an attacker looking at your social media) is a bad idea!

Equally, short passwords (especially those that don't contain any non-alphanumeric characters) are weak against brute-force attacks. We will look at this in more depth later in the task.

Of equal importance to password strength is password reuse. You can have the strongest password in the world, but if you use it across numerous accounts and it gets leaked, an attacker can simply use the same strong password on all affected accounts. Equally, if you find out that your password has been exposed, you will have a lot of work to do changing all of your account passwords!
```
- Exposed passwords
```
When you sign up for an online account, the provider must store a copy of your password in order to validate it the next time you sign in; but this poses a huge problem: how can the passwords be stored securely?
Storing the passwords as plain text (e.g. the same way you submit them) isn't an option as every password will instantly be leaked if the database is ever hacked.
Encrypting the passwords is an improvement, but not by much. If the passwords are stored encrypted, then they can also be decrypted — an attacker simply has to obtain the key, and they can turn every encrypted password back into plaintext. Encrypting passwords was part of what made the 2013 Adobe breach so serious.
The industry-standard password storage method is referred to as password hashing. Password hashing (or simply "hashing") involves using complicated mathematical algorithms to take any input and turn it into a unique, fixed-length output in a way that is impossible to reverse. This means that when you sign up, your password will be hashed and stored in the database in a way that stops everyone (including server administrators) from being able to read it!
When you try to sign in, the same algorithm is applied to the password that you supply: if the stored hash matches the hash of the password you are trying to log in with (remembering that the same input will always create the same unique output), then you are considered to have successfully authenticated.
Ideally, every service would hash user passwords with a secure algorithm. Even if the entire database were leaked, the attackers would still need to waste valuable time and computational power attempting to brute-force the (otherwise useless) hashes to find the plaintext passwords. This is why it is so important that passwords are long and preferably of a decent level of complexity: the longer the password and the larger the number of potential characters involved, the more power it takes to effectively guess the password input used to generate a hash.
```
```
So, what happens if a service gets hacked and their database containing user account information gets leaked? As a best-case scenario, the service has used a secure hashing algorithm, and you have a strong password — in this case, your password is safe, but your email address or username may still be leaked publicly (so expect some spam emails).Decorative image of a broken chain

As a worst-case scenario, your plaintext password is either immediately available, or is easy for an attacker to find. If this happens then both your username and password are known to the attacker, allowing them to take over your account or perform "credential stuffing" attacks — using your stolen username and password pair against other services to see if you reused them elsewhere. These leaked databases containing credentials frequently appear on the dark web, which leads us to our final point in this section: data exposure notification services.

The largest and most well-known data exposure checker is called "Have I Been Pwned?". It exists as a free online service that scours data dumps and catalogues all of the information found, allowing users to enter their email addresses to see if they have been included in any breaches. Have I Been Pwned also allows you to add yourself to a notification list, meaning that you will receive an email notifying you if your email address appears in any data breaches.

Whilst not a perfect defence, notification services give you a vital early warning to change your passwords (hopefully) before you get hacked.
```
```
An attacker has a few options when it comes to attacking passwords and authentication systems. Some attacks are entirely local (i.e. working entirely on a device owned by the attacker without interacting with the target service at all), others are remote attacks involving the original server.

Local attacks require a stolen copy of the credentials in question. The attacker will take a file full of stolen usernames/emails and hashed passwords, then use software to effectively try to guess the input that created the hash either using randomly generated sequences of characters (slower but more thorough) or by using a pre-generated wordlist of possible passwords (faster but much more likely to miss things). Hybrid types are also very widely used; these are when an attacker takes an existing wordlist and mutates it to add new characters, symbols, or random elements. Local password attacks will be demonstrated in the interactive element for this task.

Remote attacks tend to be one of two categories; they either involve attempting to brute-force known usernames by sending requests to the server and seeing what it responds with, or they use known username and password pairs from previous breaches to see if they are valid on the target site — this is the aforementioned credential stuffing.
```

## Multi-Factor Authentication and Password Managers
- Multi-Factor Authentication (MFA) - describe any authentication process where more than one step is needed to sign in
    - Time-based One Time Password - once you enter your password, a code is sent to your phone that expires after some time
    - Always activate multi factor when available, which will make the attacker need one more factor if they want to get into your accounts
    - SMS based TOTP is the most common, but it's not the most secure because texts can be rerouted
    - Authenticator app - apps that generate TOTP codes for you
- Password manager - provide a safe space to store passwords
    - Stored in encrypted storage either locally or online
    - Can be accessed using a master password or biometric data

## Public Network Safety
- Many public spaces have wifi, and this can be dangerous
- Public wifi gives an attacker ideal opportunities to attack other users' devices, intercept information, and record traffic
- The attacker can set up a network of their own and monitor the traffic of everyone who connects (man in the middle)
    - This can happen if you're not using HTTPS, but is less likely if the website uses TLS
- Being Connected to any network makes your device visible to others on the network
- The solutions
    - Ideal solution is to not connect to untrusted networks
    - VPN - encrypt all traffic leaving and entering your machine
        - Free VPNs tend to not provide the best security and often harvest your data
- Website Connection Security
    - Websites can use an encrypted connection with HTTPS and TLS
    - When accessing a website without HTTPS, *never* enter any credentials or sensitive information

## Backups
- Backups - the most important defensive measure you can take to protect your data
- The Golden 3,2,1 Rule
    1. `You should always keep at least three up-to-date copies of your data; this can include the original copy, but all copies must be maintained.`
    2. `Backups should be stored on at least two different storage mediums; for example: a cloud backup and a USB device. This can include a hard drive on your PC.`
    3. `One (or more) backups should be stored "off-site". Cloud services such as Google Drive are ideal for personal use in this regard.`
- The frequency of backups taken is equally important

## Updates and Patches
- Updates are essential for adding new features, fixing bugs, etc.
- Patches - special updates that contain fixes for vulnerabilities
```
Eternal Blue is believed to have been discovered by the United States National Security Agency (the NSA) and was leaked to the general public in April 2017. The vulnerability affects an integral part of the Windows operating system and gives a remote attacker complete control over the target at the highest level of privileges. You can see this for yourself in the "Blue" room on TryHackMe.

Microsoft quickly released a patch (the infamous MS17-010) which was designed to remove the vulnerable component in the software; however, many administrators simply chose not to download it for one reason or another.

Why is this important? Eternal Blue was the transmission vector that the Wannacry ransomware (discussed in task 4) used to spread and infect new devices! Eternal Blue gave full access to a target remotely, making it a perfect vulnerability to exploit with a self-replicating virus. Despite a patch having been made available months before the appearance of Wannacry, the ransomware was still able to attack millions of unpatched systems, with devastating effects.
```
- End of Life (EOL) - All software eventually loses support from its maintainers and stops receiving updates
```
Most antivirus software packages receive very frequent updates; this is because they largely work using a local database of known exploit signatures, which must be kept up-to-date.

In other words: when new malware is discovered, it gets sent around antivirus vendors who generate a "signature" that identifies this particular piece of malicious software. These signatures are then distributed to every device on the planet that uses the antivirus software, ensuring that your installed antivirus solution is kept up-to-date on all the latest (known) malware.

If antivirus software is not allowed to update it will still be able to catch some malware through other methods. However, the local signature database will quickly become outdated, resulting in malicious software potentially falling through the gaps. In short: if the antivirus wants to update, let it!
```
