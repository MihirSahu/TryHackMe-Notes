# What's the Worst that Could Happen?

- Malware analysis

## Initial Analysis
- Run the `file` command
    - Determines the file's type, regardless of the file extension
- `strings` command extracts the strings from a file
    - Can give pointers to the different functions called inside the file, IP addresses, domain names, URLs, etc.

## Virustotal
- Upload files or hashes to virustotal to see more information
- If you don't want to upload the file, calculate the md5 with the `md5sum` command and search by hash instead
- Once the file is analyzed make sure to check all the tabs, including detection, details, relations, behavior, and community

## Exercise
1. X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
2. EICAR virus test files
3. Hash is `44d88612fea8a8f36de82e1278abb02f`, search virustotal and check Details tab. `2005-10-17 22:03:48`
4. Virus:DOS/EICAR_Test_File
5. ducklin.htm or ducklin-html.htm
6. 128
