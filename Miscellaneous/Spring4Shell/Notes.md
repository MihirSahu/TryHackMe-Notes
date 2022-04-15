# Spring4Shell: CVE-2022-22965


## Introduction
- March 2022, two RCE vulns in the Java Spring Framework were made public
	- One affects a component called `Spring CLoud Functions`
	- Another affects a component in `Spring Core`, which is the heard of the framework

## Vulnerability Background
- Overview
	- Originally released as a 0-day on Twitter
	- Identified as a bypass of the patch for CVE-2010-1622, a vuln that allowed attackers to obtain remote command execution by abusing the way that Spring handles data sent in HTTP requests
		- Allows attackers to upload a webshell to the server
- How does it work?
	- Spring MVC (model view controller) is a part of the framework that makes it easy to develop web apps following the MVC design pattern
	- Automatically instantiates and populates an object of a specified class when a request is made based on the parameters sent to the endpoint
		- This could be abused to overwrite important attributes of the parent class, resulting in RCE
	- The majority of exploits for Spring4Shell operate by forcing the application to write a malicious `.jsp` file to the webserver
		- Then the webshell can be executed to gain RCE
- Limitations
	- Conditions in which the vuln can be exploted are limited
- Upgrade the framework to remediate

## Exploitation
- Use this [proof of concept exploit](https://github.com/BobTheShoplifter/Spring4Shell-POC)
