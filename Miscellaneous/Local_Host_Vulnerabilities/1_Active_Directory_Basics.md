# Active Directory Basics


## Introduction
- Active directory - the directory service for Windows Domain networks
	- A collection of machines and servers connected inside domains, which are a collective part of a bigger forest of domains
- Parts of active directory
	- Domain controllers
	- Forests, trees, domains
	- Users and groups
	- Trusts
	- Policies
	- Domain services
- Active directory is used because it allows for the control and monitoring of their user's computers through a single domain controller
	- Allows a single user to sign in to any computer on the active directory network and have access to his or her stored files and folders in the server, as well as the local storage on that machine
	- Any user can use any machine that the company owns

## Physical Active Directory
- Physical AD is the servers and machines on premise
- Domain controller - a windows server that has Active Directory Domain Services (AD DS) installed and has been promoted to a domain controller in the forest
	- The center of AD; they control the rest of the domain
- Roles of domain controller
	- Holds the AD DS store data
- AD DS Data Store - holds the databases and processes needed to store and manage directory information such as users, groups, and services
	- Contains the NTDS.dit - a database that contains all the information of an AD domain controller as well as password hashes for domain users
	- Stored by default in `%SystemRoot%\NTDS`
	- Accessible only by the domain controller
