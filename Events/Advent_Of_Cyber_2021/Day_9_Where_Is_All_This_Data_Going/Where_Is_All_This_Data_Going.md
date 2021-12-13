# Where Is All This Data Going?

 - I'm familiar with wireshark so I'm skipping over what I already know

## Filters
- The [Berkeley Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter) syntax is used for filtering
    - `ip.addr == 172.21.2.116`
    - `http contains` or `http contains google.com`
    - `tcp.port == 3389`
    - `http.request.method == GET`
- Prepend `not` to exclude with filters

## Exercise
- Use filter `http.request.method == GET` to find `login`
- Use filter `http.request.method == POST`, then Right click > Follow > TCP Stream to get `username=McSkidy&password=Christmas2021`. The answer is McSkidy:Christmas2021
- Same process as the previous to get `TryHackMe-UserAgent-THM{d8ab1be969825f2c5c937aec23d55bc9}`
- Use filter `dns.txt`, then Right click > Follow > UDP Stream to get `THM{dd63a80bf9fdd21aabbf70af7438c257}`
- Use filter `ftp` and find the password is `TryH@ckM3!`
- Same as previous, we find that the command is `STOR`
- Use filter `tcp.port == 21` - because ftp is usually on port 21 - and we see that the data is transferred between packets 1090 and 1094. Clear all filter, check the packets between those numbers, and we find that checking the tcp stream of packet 1091 gives us `AoC Flag: 123^-^321`
