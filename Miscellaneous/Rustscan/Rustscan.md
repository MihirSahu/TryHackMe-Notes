# Rustscan


## Fast
- Rustscan is fast
	- Low-level kernel networking
	- Written in a fast language (Rust)
	- Asynchronous scanning using asynchronous rather than multi-threading
- The bottleneck isn't in rustscan; it's in your computer, the network link between your computer and the target, and the target itself
- Deals with slowness due to adding features by
	- Manual testing on targets
	- Continuous integration that fails if the program is too slow
	- Benchmarking the program and graphing the results
	- Keeping all features outside of the scanning itself. Unless it is absolutely needed, RustScan will not run code before or during the scan -- only after.

## Extensible
- Rustscan scripting engine - allows scripting
	- Scripts run after scan has completed
	- Supports
		- Python
		- Shell
		- Perl
		- Any program which is a binary and is in $PATH
- Scripting engine can be altered using `--scripts`
	- None - don't run any scripts
	- Custom - run all scripts in the scripts folder
	- Default - runs Nmap scripts or whatever script is in the config file
- Python Custom Scripts
	- To execute custom scripts a file called `.rustscan_scripts.toml` needs to be created at `$HOME/.rustscan_scripts.toml`.
		```
		# Test/Example ScriptConfig file
		
		# Tags to filter on scripts. Only scripts containing all these tags will run.
		tags = ["core_approved", "example"]
		
		# If it's present then only those scripts will run which has a tag ports = "80". Not yet implemented.
		#
		# ex.:
		# ports = ["80"]
		# ports = ["80","81","8080"]
		ports = ["80"]
		
		# Only this developer(s) scripts to run. Not yet implemented.
		developer = ["example"]
		```
	- A python script will look like this
		```
		#!/usr/bin/python3
		#tags = ["core_approved", "example",]
		#developer = [ "example", "https://example.org" ]
		#trigger_port = "80"
		#call_format = "python3 {{script}} {{ip}} {{port}}"
		
		# Sriptfile parser stops at the first blank line with parsing.
		# This script will run itself as an argument with the system installed python interpreter, only scanning port 80.
		# Unused filed: ports_separator = ","
		
		import sys
		
		print('Python script ran with arguments', str(sys.argv))
		```
	- Tags - categories of scripts. We can choose to only run scripts that match these categories
		- Ex.
			- HTTP
			- SSH
			- Tomcat
		- `tags = ["core_approved", "example"]`
	- Trigger point - specify the port for which the script triggers
		- `ports = ["80"]`
	- Call format - uses templating to enclose variables in doubly curly braces
		- Supports three variables:
			- Script name
			- IP address
			- Ports
		- `#call_format = "python3 {{script}} {{ip}} {{port}}"`
	- Code - actual code comes after all the metadata
		- Script will receive arguments via `sys.argv` in the format specified in the `call_format` variable
	- [Example scripts](https://github.com/RustScan/RustScan/tree/master/fixtures/.rustscan_scripts)

## Adaptive
- Rustscan changes how it works to better suit its environment
- Adaptive learning features
	- Adaptive outbound SYN timing to optimise the speed of scanning
		- Learns how the target reacts
	- Custom top ports
		- Doesn't only scan the top 1000 ports by default
	- Operating system adaptation
		- Uses different configurations based on the OS being used
- All this information is stored in a configuration file
	- Can be used on other systems to automatically configure rustscan

## Scanning
- Multiple IP Scanning
	- `rustscan -a 127.0.0.1,0.0.0.0`
- RustScan can also scan hosts, like so:
	- `rustscan -a www.google.com, 127.0.0.1`
- RustScan supports CIDR:
	- `rustscan -a 192.168.0.0/30`
- Hosts file as input
	- `rustscan -a 'hosts.txt'`
- Individual Port Scanning
	- `rustscan -a 127.0.0.1 -p 53`
- You can input a comma-separated list of ports to scan:
	- `rustscan -a 127.0.0.1 -p 53,80,121,65535`
- To scan a range of ports:
	- `rustscan -a 127.0.0.1 --range 1-1000`
- RustScan, at the moment, runs Nmap by default.
	- `rustscan -a 127.0.0.1 -- -A -sC` runs `nmap -Pn -vvv -p $PORTS -A -sC 127.0.0.1`
Random Port Ordering
	- If you want to scan ports in a random order (which will help with not setting off firewalls) run RustScan like this:
	- `rustscan -a 127.0.0.1 --range 1-1000 --scan-order "Random"`
