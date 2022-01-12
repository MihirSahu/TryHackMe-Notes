# Juicy Details


## Reconnaissance
1. Look through `access.log` and we find `nmap,hydra,sqlmap,curl,feroxbuster`
2. The attacker brute forced with hydra, so the endpoint was `/rest/user/login`
3. The attacker used sqlmap to sql inject `/rest/products/search`
4. All the requests sent by sqlmap were sent to `/rest/products/search?q=`, so the query parameter is `q`
5. At the very end of `access.log` we see that ftp is being used to get files `/ftp`

## Stolen data
1. In `access.log` we see that the attacker uses `whoami` on users from the `product reviews` section
