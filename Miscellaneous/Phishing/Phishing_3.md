# Phishing Emails 3


## What Information Should We Collect?
- Steps to analyze suspicious email
    1. Check the email header
        - Sender email address
        - Sender IP address
        - Reverse lookup of the sender IP address
        - Email subject line
        - Recipient email address (this information might be in the CC/BCC field)
        - Reply-to email address (if any)
        - Date/time
    2. Check the body and attachments
        - Any URL links (if an URL shortener service was used, then we'll need to obtain the real URL link)
        - The name of the attachment
        - The hash value of the attachment (hash type MD5 or SHA256, preferably the latter)

## Email Header Analysis
- View email header through email source code
- Some tools to help analyze
    - [Google MessageHeader](https://toolbox.googleapps.com/apps/messageheader/analyzeheader)
    - [Message Header Analyzer](https://mha.azurewebsites.net/)
    - [Mail Header Analysis](https://mailheader.org/)
- Message Transfer Agent (MTA) - software that transfers emails between sender and recipient
    - Mail User Agent (MUA)
- Analyze sender's IP address with [IPinfo](https://ipinfo.io/)
- Analyze website [URLscan](https://urlscan.io/)
- [Website reputation](https://talosintelligence.com/reputation)

## Email Body Analysis
- Check any links or attachments in the email
- Tools
    - [URL Extractor](https://www.convertcsv.com/url-extractor.htm)
    - Cyberchef
- Save the attachment, generate hash, then check hash with https://talosintelligence.com/reputation or virustotal

## Malware Sandbox
- We can upload files to online services and see what it does
- Tools
    - [Any Run](https://app.any.run/)
    - [Hybrid Analysis](https://www.hybrid-analysis.com/)
    - [Joe Security](https://www.joesecurity.org/)

## Phishtool
- https://www.phishtool.com/
- Classification code - categorizes phishing emails with code depending on value of the target

## Additional Tools
- https://mxtoolbox.com/
- https://phishtank.com/?
- https://www.spamhaus.org/
