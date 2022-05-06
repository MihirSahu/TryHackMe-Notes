# Printer Hacking 101


- [Printer Hacking website](http://hacking-printers.net/wiki/index.php/Main_Page)
- [Printer Exploitation Toolkit](https://github.com/RUB-NDS/PRET)


## IPP Port
- Internet Printing Protocol (IPP) - specialized internet protocol for communication between client devices and printers
	- ALlows clients to submit one or more print jobs to the printer or print server and perform tasks such as querying the status of a printer, obtaining the status of print jobs, or canceling individual print jobs
	- When an IPP is open on the internet, it is possible for anyone to print to the printer or even transfer malicious data through it (using it as a middleman for attacks)
- In 2018 a hacker hacked 50,000 printers and asked people to subscript to PewDiePie
- A study showed that there are sill around 80,000 vulnerable printers open to the world, with most of them running the CUPS server
- An open IPP port can expose information such as printer name, location, model, firmware version, or even printer wifi SSID
- IPP uses port 631 by default

## Targeting and Exploitation
- Installation
```
git clone https://github.com/RUB-NDS/PRET && cd PRET
python2 -m pip install colorama pysnmP
```
- Run `python3 pret.py` to scan for printers
- Three options when exploiting a printer
	1. ps (postscript)
	2. pjl (printer job language)
	3. pcl (printer command language)
- Ex.
```
python pret.py {IP} pjl
python pret.py laserjet.lan ps
python pret.py /dev/usb/lp0 pcl
```
- After this you get a shell like output of commands that lets you interact with the printer
- [PRET cheat sheet](http://hacking-printers.net/wiki/index.php/Printer_Security_Testing_Cheat_Sheet)
- SSH access to the machine allows you to set up ssh tunneling, opening up all CUPS features and providing you an ability to use attached printers
	- The password can be brute forced
	- Ex. `ssh printer@10.10.94.204 -T -L 3631:localhost:631`
- Exercise
	1. How would a simple printer TCP DoS attack look as a one-line command?
		- `while true; do nc printer 9100; done`
	2. Review the cheat sheet provided in the task reading above. What attack are printers often vulnerable to which involves sending more and more information until a pre-allocated buffer size is surpassed?
		- Buffer overflow
	3. 

## Conclusion
- It's possible to get almost full server file access simply by exploiting the printer service running on it
