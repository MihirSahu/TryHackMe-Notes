# Cryptography


## Hashing
- Key terms
	- Plaintext - Data before encryption or hashing, often text but not always as it could be a photograph or other file instead.
	- Encoding - This is NOT a form of encryption, just a form of data representation like base64 or hexadecimal. Immediately reversible.
	- Hash - A hash is the output of a hash function. Hashing can also be used as a verb, "to hash", meaning to produce the hash value of some data.
	- Brute force - Attacking cryptography by trying every different password or every different key
	- Cryptanalysis - Attacking cryptography by finding a weakness in the underlying maths
- Hash functions
	- There is no key, and it's meant to be impossible to go back from the output to the input
	- A hash function takes input data of any size and creates a digest of the data of a fixed size
	- Good hashing functions will be fast to compute and slow to reverse
	- Any small change in the input data will cause a large change in output
	- The output of a hash function is normally raw bytes, which are then encoded, but decoding it won't give anything useful
- Hash collision
	- When two different inputs give the same output
	- Hash functions are designed to avoid this as best as they can
	- Due to the pidgeonhole principle, collisions are not avoidable because there are more inputs than outputs
- Uses for hashing
	- Two main purposes:
		1. Verify integrity of data
		2. Verifying passwords
	- Rainbow tables trade in processing for hard drive space, essentially a huge list of hash:plaintext
		- To defend against this, salting is used
		- When a hash is salted, you'll have to manually crack it
- Recognizing password hashes
	- No one software is too reliable for detecting a password hash
	- Use a combination of different tools
	- [Hash formats](https://hashcat.net/wiki/doku.php?id=example_hashes)
- Password cracking
	- Hashes are not encrypted, so they need to be cracked
	- Cracking on GPUs is better than cracking on CPUs because they have more cores
		- Some hashing algorithms are designed so that hashing on a GPU is about the same as hashing on a CPU, which helps it resist cracking
- Cracking on VMs
	- VM's don't ususally has access to host's graphics cards so it's better to use the host

## John The Ripper
- Basic syntax
	- `john [options] [path to file]`
- Automatic cracking - john can automatically detect the hash type but it can be unreliable
	- `john --wordlist=[path to wordlist] [path to file]`
- Identifying hashes - try to use multiple different programs to identify hashes
	- [Online identifier](https://hashes.com/en/tools/hash_identifier)
	- [hash-identifier](https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master)
- Format specific cracking
	- `john --format=[format] --wordlist=[path to wordlist] [path to file]`
- Cracking Windows authentication hashes
	- NTHash / NTLM
		- NThash is the hash format that modern Windows Operating System machines will store user and service passwords in. It's also commonly referred to as "NTLM" which references the previous version of Windows format for hashing passwords known as "LM", thus "NT/LM".
		- A little bit of history, the NT designation for Windows products originally meant "New Technology", and was used- starting with Windows NT, to denote products that were not built up from the MS-DOS Operating System. Eventually, the "NT" line became the standard Operating System type to be released by Microsoft and the name was dropped, but it still lives on in the names of some Microsoft technologies.
		- You can acquire NTHash/NTLM hashes by dumping the SAM database on a Windows machine, by using a tool like Mimikatz or from the Active Directory database: NTDS.dit. You may not have to crack the hash to continue privilege escalation- as you can often conduct a "pass the hash" attack instead, but sometimes hash cracking is a viable option if there is a weak password policy.
- Cracking Hashes from `/etc/shadow`
	- The /etc/shadow file is the file on Linux machines where password hashes are stored. It also stores other information, such as the date of last password change and password expiration information. It contains one entry per line for each user or user account of the system. This file is usually only accessible by the root user- so in order to get your hands on the hashes you must have sufficient privileges, but if you do- there is a chance that you will be able to crack some of the hashes.
	- John can be very particular about the formats it needs data in to be able to work with it, for this reason- in order to crack /etc/shadow passwords, you must combine it with the /etc/passwd file in order for John to understand the data it's being given. To do this, we use a tool built into the John suite of tools called unshadow. The basic syntax of unshadow is as follows:
		- `unshadow [path to passwrd] [path to shadow]`
	- Then the hash can be cracked manually
		- `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt`
- Single Crack Mode
	- A mode in which john uses only the information provided in the username, to try and work out possible passwords heuristically, by slightly changing the letters and numbers contained within the username
	- Word mangling
		```
		If we take the username: Markus
		Some possible passwords could be:
		
		Markus1, Markus2, Markus3 (etc.)
		MArkus, MARkus, MARKus (etc.)
		Markus!, Markus$, Markus* (etc.)
		```
	- GECOS
		- passwd and shadow files are separated into GECOS fields with `:`
	- Syntax
		- `john --single --format=[format] [path to file]`


## Encryption
- Key terms
	- Ciphertext - The result of encrypting a plaintext, encrypted data
	- Cipher - A method of encrypting or decrypting data. Modern ciphers are cryptographic, but there are many non cryptographic ciphers like Caesar.
	- Plaintext - Data before encryption, often text but not always. Could be a photograph or other file
	- Encryption - Transforming data into ciphertext, using a cipher.
	- Encoding - NOT a form of encryption, just a form of data representation like base64. Immediately reversible.
	- Key - Some information that is needed to correctly decrypt the ciphertext and obtain the plaintext.
	- Passphrase - Separate to the key, a passphrase is similar to a password and used to protect a key.
	- Asymmetric encryption - Uses different keys to encrypt and decrypt.
	- Symmetric encryption - Uses the same key to encrypt and decrypt
	- Brute force - Attacking cryptography by trying every different password or every different key
	- Cryptanalysis - Attacking cryptography by finding a weakness in the underlying maths
- Why is encryption important?
	- Cryptography is used to protect confidentialit, integrity and authenticity
	- Whenever sensitive user data needs to be stored, it should be encrypted
	- **Don't encrypt passwords unless you're using a password manager**
- Crucial Crypto Maths
	- The modulo operator is common in cryptography
- Types of encryption
	- Symmetric - uses the same key to encrypt and decrypt data
	- Asymmetric - uses a pair of keys, one to encrypt and one to decrypt
- RSA
	- Based on the mathematically difficult problem of working out the factors of a large number
	- Tools to break RSA in CTFs
		- [Resource 1](https://github.com/Ganapati/RsaCtfTool)
		- [Resource 2](https://github.com/ius/rsatool)
- Digital Signatures and Certificates
	- Digital certificates - prove the authencity of files
	- Certificates - certifies different parties using public key cryptography
	- A certificate authority (CA) holds certificates affiliated with different website domains
