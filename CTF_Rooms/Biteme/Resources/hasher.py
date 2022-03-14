import hashlib

flag = False

with open("/usr/share/wordlists/rockyou.txt", "r") as file:
    for lines in file:
        line = lines.strip()
        hash = hashlib.md5(line.encode("utf-8")).hexdigest()
        if (hash)[-3:] == '001':
            print(line, hash)
            break

