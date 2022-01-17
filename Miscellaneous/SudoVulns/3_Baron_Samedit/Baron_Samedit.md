# Baron Samedit


- `CVE-2021-3156` allows any user to escalate privileges to root even if sudo isn't misconfigured
- Affects any version from 1.8.2-1.8.31p2 to 1.9.0-1.9.5p1, it's been around for about 10 years
- The vulnerability is a buffer overflow, but affects the heap memory instead of the stack memory like `CVE-2019-18634`
- Check if system is vulnerable with `sudoedit -s '\' $(python3 -c 'print("A"*1000)')`
- [Exploit from github](https://github.com/blasty/CVE-2021-3156)
