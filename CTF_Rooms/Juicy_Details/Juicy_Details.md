# Juicy Details


## Reconnaissance
1. Look through `access.log` and we find `nmap,hydra,sqlmap,curl,feroxbuster`
2. The attacker brute forced with hydra, so the endpoint was `/rest/user/login`
3. The attacker used sqlmap to sql inject `/rest/products/search`
4. All the requests sent by sqlmap were sent to `/rest/products/search?q=`, so the query parameter is `q`
5. At the very end of `access.log` we see that ftp is being used to get files `/ftp`

## Stolen data
1. In `access.log` we see that the attacker uses `whoami` on users from the `product reviews` section
2. In `access.log` we see that the attacker brute forced with hydra, so if we look at where hydra was stopped being used we find the answer to be `Yay, 11/Apr/2021:09:16:32 +0000`
3. In `access.log` we see that after the attacker gets information from the sql injection, they retrieve the `email, password` with curl
```
::ffff:192.168.10.5 - - [11/Apr/2021:09:32:51 +0000] "GET /rest/products/search?q=qwert%27))%20UNION%20SELECT%20id,%20email,%20password,%20%274%27,%20%275%27,%20%276%27,%20%277%27,%20%278%27,%20%279%27%20FROM%20Users-- HTTP/1.1" 200 3742 "-" "curl/7.74.0"
```
4. In `access.log` after enumerating with feroxbuster the attacker downloads the file `coupons_2013.md.bak, www-data.bak`
```
::ffff:192.168.10.5 - - [11/Apr/2021:09:34:40 +0000] "GET /ftp/www-data.bak HTTP/1.1" 403 300 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
::ffff:192.168.10.5 - - [11/Apr/2021:09:34:43 +0000] "GET /ftp/coupons_2013.md.bak HTTP/1.1" 403 78965 "-" ""Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
```
5. We see from `access.log` that ftp was used to download the previous files, and if we look at `vsftpd.log` we see that the `anonymous` account was used to login to ftp. The answer is `ftp, anonymous`
6. In `auth.log` we see that ssh is being used to login as `www-data`. The answer is `ssh, www-data`
