# Wifi Hacking 101


## Intro to WPA
- Terms
    - SSID - The network "name" that you see when you try and connect
    - ESSID - An SSID that *may* apply to multiple access points, eg a company office, normally forming a bigger network. For Aircrack they normally refer to the network you're attacking.
    - BSSID - An access point MAC (hardware) address
    - WPA2-PSK - Wifi networks that you connect to by providing a password that's the same for everyone
    - WPA2-EAP - Wifi networks that you authenticate to by providing a username and password, which is sent to a RADIUS server.
    - RADIUS - A server for authenticating clients, not just for wifi.
- WPA authentication uses the 4 way handshake
    - Allows the client and the AP to prove they know the key, without telling each other
- WPA and WPA2 use the same authentication method, so the attacks on both are the same
- The keys for WPA are derived from the ESSID and the password for the network
    - ESSID acts as a salt, making dictionary attacks more difficult
        - For a given password, the key will still vary for each access point
- Exercise
    1. WPA can be brute forced
    2. Brute forcing doesn't work against WPA2-EPA because they require a username and a password
    3. `psk` is an abbreviation for password or passphrase
    4. The minimum length of a WPA2 personal password is 8

## Capturing Packets to Attack
- Aircrack-ng suite consists of:
    - aircrack-ng
    - airdecap-ng
    - airmon-ng
    - aireplay-ng
    - airodump-ng
    - airtun-ng
    - packetforge-ng
    - airbase-ng
    - airdecloak-ng
    - airolib-ng
    - airserv-ng
    - buddy-ng
    - ivstools
    - easside-ng
    - tkiptun-ng
    - wesside-ng
- A network adapter with monitor mode is necessary for this
- Exercise
    1. Enable monitor mode with `airmon-ng start wlan0`
    - [Documentation for monitor mode](https://www.aircrack-ng.org/~~V:/doku.php?id=airmon-ng)
    2. `wlan0mon`
    3. `airmon-ng check kill` to kill other processes using the adapter
    4. `airodump-ng` is designed to capture packets
    5. Use the `--bssid` flag to set bssid
    6. Use the `--channel` flag to set channel
    7. Use `-w` to write output to a file

## Let's Get Cracking
- Assuming we used airodump to capture the packets and write them to a file, we can now use aircrack-ng to crack the password
- Exercise
    1. Use `-b` to specify a bssid
    2. Use `-w` to specify a wordlist
    3. If you want to use hashcat to crack the password instead - which is useful if we want to use GPU acceleration - use `-j` to create a hashcat capture file
    4. Use `aircrack-ng NinjaJc01-01.cap -w /usr/share/wordlists/rockyou.txt` to get the password `greeneggsandham`
    5. The GPU is going to be faster at cracking than the CPU
