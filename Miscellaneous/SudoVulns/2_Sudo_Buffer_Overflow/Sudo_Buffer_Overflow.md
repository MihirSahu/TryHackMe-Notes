# Sudo Buffer Overflow


- `CVE-2019-18634` affects versions of sudo earlier than 1.8.26
- One of the options that can be added to `/etc/sudoers` is `pwfeedback`
    - By default sudo doesn't show any output when you type in your password, but enabling `pwfeedback` displays asterisks when typing in the password
    - `pwfeedback` is purely for aesthetic
- This exploit doesn't need the any specific configuration in `/etc/sudoers` other than `pwfeedback` to be enabled
- While `pwfeedback` is enabled, it's possible to perform a buffer overflow attack on sudo
    - Give sudo so much data that it spille out of the storage space set and overwrites the content of the next buffer
- Proof of concept
    - `perl -e 'print(("A" x 100 . "\x{00}") x 50)' | sudo -S id`
    - This gives the error `Segmentation fault`, which we can exploit
- [Exploit from github](https://github.com/saleemrashid/sudo-cve-2019-18634)
