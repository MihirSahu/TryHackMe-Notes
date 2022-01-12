# Red Team Recon


## Introduction
- In a red team operation you start with minimal information and need to start gathering information about the target
- Reconnaissance (recon) - a preliminary observation of your target without alerting them of your activities
    - Can be passive or active

## Taxonomy of Reconnaissance
- Passive Recon
    - Can be carried out by watching passively
    - Relies on publicly available information that is collected and maintained by a third party
    - OSINT is used to collect information about the target and can be as simple as viewing a target's publicly available social media profile
    - Information we may collect
        - Domain names
        - IP address blocks
        - Email addresses
        - Employee names
        - Job posts
- Active Recon
    - Requires interacting with the target to provoke it in order to observer its response
    - Send requests and packets to observe if and how it responds
        - Ex. nmap scan
    - Has two parts
        - External recon - conducted outside that target's network and focuses on the externally facing assets from the internet
            - Ex. running nikto from outside the company network
        - Internal recon - conducted from within the company's network

## Built-in Tools
- whois
    - whois uses the WHOIS protocol
    - WHOIS - a request and response protocol
        - WHOIS server listens on TCP port 43 for incoming requests
        - Domain registrar is responsible for maintaining the WHOIS records for the domain name it's leasing
    - whois queries the WHOIS server to provide all saved records
    - whois can provide
```
Registrar WHOIS server
Registrar URL
Record creation date
Record update date
Registrant contact info and address (unless withheld for privacy)
Admin contact info and address (unless withheld for privacy)
Tech contact info and address (unless withheld for privacy)
```

- nslookup
    - Uses the default DNS server to get the A and AAAA records for the domain
- dig (domain information groper)
    - Provides query options and allows you to specify a different DNS server
- host
    - Alternative for querying DNS servers for DNS records
- traceroute
    - Traces the route taken by the packets from our system to the target host
    - Some routers don't respond to the packets sent by traceroute, and `*` is used to indicate it
- Exercise
    1. Use `whois thmredteam.com` to get `2021-09-24`
    2. Use `nslookup clinic.thmredteam.com` to get 2 ipv4 and 2 ipv6
