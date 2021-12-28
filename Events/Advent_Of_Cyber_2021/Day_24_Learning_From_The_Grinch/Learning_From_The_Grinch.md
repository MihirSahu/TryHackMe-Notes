# Learning From the Grinch


## Post Exploitation
- Occurs after an attacker has gained access to a system
- Attacker will try to
    - Escalate their privileges - obtain access to sensitive information or critical funcionality that is only available to higher privileged users
    - Maintain persistencew within the target environment - will set up other mechanisms to maintain access ot the environment if their current access has been blocked or removed
- Post exploitation stage allows attackers to enumerate, identify, and exploit other components in the environment/network

## Authentication and Hashing
- Windows stores credentials in the Security Accounts Manager (SAM) database
- Most common types of hashes stored in SAM
    - LAN Manager (LM) - oldest form of password storage used by windows that are kept for legacy systems
        - Algorithm used has a limited character set as input, so it's possible to try all combinations
    - NT LAN Manager (NTLM) - modern algorithm
- Once a user logs on, the LSASS process stores the user's credentials in memory, so that they don't need to enter credentials constantly

## Dumping Password Hashes
- Since LSASS process has to interact with SAM database, it runs with more privileges than standard user
- Standard tool to retrieve password hashes from memory is [mimikatz](https://github.com/gentilkiwi/mimikatz)
- Mimikatz
    - `privilege::debug` to check if you have the necessary privileges
    - `sekurlsa::logonpasswords` to dump passwords

## Exercise
1. Use mimikatz to find `emily`
2. `8af326aa4850225b75c592d4ce19ccf5`
3. Use hashcat `hashcat -a 0 -m 1000 8af326aa4850225b75c592d4ce19ccf5 /usr/share/wordlists/rockyou.txt` to find `1234567890`
