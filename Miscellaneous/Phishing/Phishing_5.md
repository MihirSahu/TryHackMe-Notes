# Phishing Emails 5


- Open the email with thunderbird
1. `06/10/2020 5:58`
2. `Mr. James Jackson`
3. `info@mutawamarine.com`
4. `info.mutawamarine@mail.com`
5. Open the source code and we see that there's nothing in `X-Originating-IP`. Look at the received section to find `192.119.71.157`
```
Received: from hwsrv-737338.hostwindsdns.com ([192.119.71.157]:51810 helo=mutawamarine.com)
	by sub.redacted.com with esmtp (Exim 4.80)
	(envelope-from <info@mutawamarine.com>)
	id 1jissD-0004g5-Ts
	for webmaster@redacted.org; Wed, 10 Jun 2020 01:02:04 -0400
```
6. Use [ipinfo](ipinfo.io) to find that the ip address belongs to `Hostwinds LLC`
7. Use [SPF Record checker](https://dmarcian.com/spf-survey/) on the Return-Path domain `mutawamarine.com` to find `v=spf1 include:spf.protection.outlook.com -all`
8. Use the [DMARC record checker](https://dmarcian.com/domain-checker/) on the Return-Path domain to find `v=DMARC1; p=quarantine; fo=1`
9. `SWT_#09674321____PDF__.CAB`
10. Save the attachment and use `sha256sum SWT_#09674321____PDF__.CAB` to find `2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f`
11. Use the hash to search for the file on virustotal and find `https://www.virustotal.com/gui/file/2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f/detection`, and the file size is `400.26 KB`
12. In the details tab we see that the actual extension is `rar`
