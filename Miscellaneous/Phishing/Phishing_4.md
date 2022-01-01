# Phishing Emails 4


## Introduction
- Ways to protect users from phishing
    - Email Security (SPF, DKIM, DMARC)
    - SPAM Filters (flags or blocks incoming emails based on reputation)
    - Email Labels (alert users that an incoming email is from an outside source)
    - Email Address/Domain/URL Blocking (based on reputation or explicit denylist)
    - Attachment Blocking (based on the extension of the attachment)
    - Attachment Sandboxing (detonating email attachments in a sandbox environment to detect malicious activity)
    - Security Awareness Training (internal phishing campaigns)
- Phishing is classified as **Technique ID 1598 (T1598)** and contains three sub-techniques

## SPF (Sender Policy Framework)
- Used to authenticate the sender of an email
- SPF record - a DNS TXT record containing a list of the IP addresses that are allowed to send email on behalf of your domain
- ![SPF](Images/SPF.png)
- Ex. `v=spf1 ip4:127.0.0.1 include:_spf.google.com -all`
    - v=spf1 -> This is the start of the SPF record
    - ip4:127.0.0.1 -> This specifies which IP (in this case version IP4 & not IP6) can send mail
    - include:_spf.google.com -> This specifies which domain can send mail
    - -all -> non-authorized emails will be rejected
- [SPF Record check](https://dmarcian.com/spf-survey/)
- [Resource 1](https://dmarcian.com/spf-syntax-table/), [Resource 2](https://dmarcian.com/what-is-the-difference-between-spf-all-and-all/)

## DKIM
