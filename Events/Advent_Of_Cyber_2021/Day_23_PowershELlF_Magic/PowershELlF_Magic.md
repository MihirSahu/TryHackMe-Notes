# PowershELlF Magic


- Powershell Logging - commands can be audited in the Windows Event Log
    - [Full Event Log View] is a useful alternative

## Exercise
1. We see this git repo `https://github.com/calebstewart/CVE-2021-1675`, if we visit it and look at the powershell commands we see `Invoke-Nightmare` is used to add a new user
2. The new user `adm1n` was created as a local administrator, and sends the password file to a remote server
3. The IP address is `10.10.148.96,4321`
4. `j3pn50vkw21hhurbqmxjlpmo9doiukyb`
5. `sdelete.exe`
6. Clear all filters and search for `password.txt` until you find the log for the deletion `11/11/2021 7:29:27 PM`
7. Use the key and the encrypted text to find the original text `Mission Control: letitsnowletitsnowletitsnow`
```
$key = (New-Object System.Text.ASCIIEncoding).GetBytes("j3pn50vkw21hhurbqmxjlpmo9doiukybpow")

$encrypted = "76492d1116743f0423413b16050a5345MgB8AEcAVwB1AFMATwB1ADgALwA0AGQAKwBSAEYAYQBHAE8ANgBHAG0AcQBnAHcAPQA9AHwAMwBlADAAYwBmADAAYQAzAGEANgBmADkAZQA0ADUAMABiADkANgA4ADcAZgA3ADAAMQA3ADAAOABiADkAZAA2ADgAOQA2ADAANQA3AGEAZAA4AGMANQBjADIAMAA4ADYAYQA0ADMAMABkADkAMwBiADUAYQBhADIANwA5AGMAYQA1ADYAYQAzAGEAYQA2ADUAMABjADAAMwAzADYANABlADYAOAA4ADQAYwAxAGMAYwAxADkANwBiADIANAAzADMAMAAzADgAYQA5ADYANAAzADEANAA2AGUAZgBkAGEAMAA3ADcANQAyADcAZgBlADMAZQA3ADUANwAyADkAZAAwAGUAOQA5ADQAOQA1AGQAYQBkADEANQAxADYANwA2AGIAYQBjADAAMQA0AGEAOQA3ADYAYgBkAGMAOAAxAGMAZgA2ADYAOABjADEAMABmADcAZgAyADcAZgBjADEAYgA3AGYAOAA3AGIANQAyAGUAMwA4ADgAYQAxADkANgA4ADMA"

echo $encrypted | ConvertTo-SecureString -key $key | ForEach-Object {[Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($_))}
```
