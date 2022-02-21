# Nessus


- Nessus - a vulnerability scnner
    - Doesn't make assumptions when scanning, like assuming that a web app is running on port 80
    - Offers free and paid plans

## Installation
- Make an account for an activation code on the [website](https://www.tenable.com/products/nessus/nessus-essentials)
- Download the amd64 .deb file and install with dpkg `sudo dpkg -i <file>`
- Start it with `sudo systemctl start nessusd.service`
- Navigate to `https://localhost:8834/` and start configuring

## Navigation and Scans
- `New Scan` launches a new scan
- `Policies` allow the creation of custom templates
- `Plugin Rules` help change plugin properties
- Types of scans
    - `Host Discovery` discovers live hosts and open ports
    - `Basic Network Scan` is suitable for any host
    - `Credentialed Patch Audit` authenticates to hosts and enumerate missing updates
    - `Web Application Tests` scans web applications

## Scanning
- You can change things like
    - Schedule - time for the scan to run
    - Discovery - change the scan type (the range of the ports)
    - Advanced - also change the scan type
- Other stuff is pretty easy, just run nessus go brr
