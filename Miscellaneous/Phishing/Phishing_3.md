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
