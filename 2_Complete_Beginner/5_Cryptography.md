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
- Establishing keys using asymmetric cryptography
