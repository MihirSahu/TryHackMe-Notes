# Yara

- [Yara documentation](https://yara.readthedocs.io/en/stable/index.html)

## What is Yara?
- Yara can identify information based on binary and textal patterns
- Uses rules to label the patterns, which are used to determine if a file is malicious or not
- Malware use strings to store textual data, like crypto wallet addresses and ip addresses
- [Yara git repo](https://github.com/virustotal/yara)

## Yara Rules
- Rule is only as effective as your understanding of the patterns you want to search for
- `yara <rule file> <file, directory, or process id>`
- Each rule must have a name and a condition
```
rule examplerule {
        condition: true
}
```
- This checks to see if the file exists

## Expanding on Yara Rules
