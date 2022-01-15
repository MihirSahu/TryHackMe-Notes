# Linux: Local Enumeration


## TTY
- A netcat reverse shell can be broken by simple mistakes
- To fix this we need to get a normal shell, a tty (text terminal)
- We also should get a tty because commands like su and sudo need a tty to run
- Simply running `/bin/bash` doesn't work easily, so just use an external program like python to upgrade the shell for you
    - `python3 -c 'import pty; pty.spawn("/bin/bash")'`
- [More information](http://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys)
- Exercise
    - Create tty with perl `perl -e 'exec "/bin/bash";'`

## SSH
- Always try to get ssh into target
- If you can find the target's `id_rsa` private key file in `.ssh/id_rsa` then download it to your system, change permissions with `chmod 600 id_rsa`, and connect by using `ssh -i id_rsa user@ip`
- If you can't find their `id_rsa` private key but you have write permissions in `.ssh`:
    1. Generate your own keys with `ssh-keygen`
    2. Go to your own `.ssh` folder and copy the contents of your public key file `id_rsa.pub` and then paste it into the `authorized_keys` file in the target `.ssh` folder
    3. Connect with `ssh -i id_rsa user@ip`
- Exercise
    1. `/home/user/.ssh/id_rsa`
    2. `nay`

## Basic Enumeration
- Basic enumeration is critical and can save a lot of time
1. `uname -a` to print out all information about system
2. Check `.bash_history` for user's actions and previous commands, `.bash_profile` and `.bashrc` for commands that run on startup or aliases
3. `sudo -V` to retrieve sudo's version
    - sudo is one of the most common targets in privilege escalation
    - sudo versions < 1.8.28 are vulnerable to CVE-2019-14287
4. `sudo -l` to check sudo rights
    - Some users may have the ability to run certain commands as root
- [GTFOBins](https://gtfobins.github.io/#+sudo)
- Exercise
    1. `uname -m`
    2. `~/.bash_history`
    3. `thm{clear_the_history}`

## Find Command and Interesting Files
- Most important options for find in enumeration are `-type` and `-name`
- Look out for interesting log and configuration files, as well as any backups that the system owner might be keeping
- [Important Extensions](https://lauraliparulo.altervista.org/most-common-linux-file-extensions/) to look out for
```
.a   : a static library ;
.au    : an audio file ;
.bin :    a) a binary image of a CD (usually a .cue file is also included); b) represents that the file is binary and is meant to be executed ;
.bz2 :    A file compressed using bzip2 ;
.c :    A C source file ;
.conf :  A configuration file. System-wide config files reside in /etc while any user-specific configuration will be somewhere in the user’s home directory ;
.cpp :  A C++ source file ;
.deb :  a Debian Package;
.diff :   A file containing instructions to apply a patch from a base version to another version of a single file or a project (such as the linux kernel);
.dsc:   a Debian Source information file ;
.ebuild : Bash script used to install programs through the portage system. Especially prevalent on Gentoo systems;
.el :  Emacs Lisp code file;
.elc :  Compiled Emacs Lisp code file;
.gif :    a graphical or image file;
.h :a C or C++ program language header file;
.html/.htm  :   an HTML file;
.iso :    A image (copy) of a CD-ROM or DVD in the ISO-9660 filesystem format;
.jpg :    a graphical or image file, such as a photo or artwork;
.ko :    The kernel module extension for the 2.6.x series kernel;
.la :    A file created by libtool to aide in using the library;
.lo :    The intermediate file of a library that is being compiled;
.lock :    A lock file that prevents the use of another file;
.log :    a system or program’s log file;
.m4 :    M4 macro code file;
.o :    1) The intermediate file of a program that is being compiled ; 2) The kernel module extension for a 2.4 series kernel ; 3)a program object file;
.pdf :    an electronic image of a document;
.php :     a PHP script;
.pid :    Some programs write their process ID into a file with this extention;
.pl :    a Perl script;
.png :    a graphical or image file;
.ps :    a PostScript file; formatted for printing;
.py :    a Python script;
.rpm :    an rpm package. See Distributions of Linux for a list of distributions that use rpms as a part of their package management system;
.s :    An assembly source code file;
.sh :    a shell script;
.so :     a Shared Object, which is a shared library. This is the equivalent form of a Windows DLL file;
.src  :    A source code file. Written in plain text, a source file must be compiled to be used;
.sfs :    Squashfs filesystem used in the SFS Technology;
.tar.bz2 , tbz2, tar.gz :     a compressed file per File Compression;
.tcl :    a TCL script;
.tgz :     a compressed file per File Compression. his may also denote a Slackware binary or source package;
.txt :    a plain ASCII text file;
.xbm :    an XWindows Bitmap image;
.xpm :     an image file;
.xcf.gz, xcf :  A GIMP image (native image format of the GIMP);
.xwd :    a screenshot or image of a window taken with xwd;
.zip :extension for files in ZIP format, a popular file compression format;
.wav :    an audio file.
```
- Exercise
    1. Use `find / -name *.bak 2> /dev/null` to find `/var/opt/passwords.bak`, which contains the password `THMSkidyPass`
    2. Use `find / -name *.conf 2> /dev/null | grep flag` to find `/etc/sysconf/flag.conf`, which contains `thm{conf_file}`

## SUID
- Set User ID (SUID) allows users to execute a file with the permissions of another user
- Files with SUID permissions can be run as root
- `find / -perm -u=s -type f 2>/dev/null` to find files with SUID set
- After finding any files with SUID set use GTFOBins to see if there's a way to abuse them
- Exercise
    1. Use `find / -perm -u=s -type f 2>/dev/null` to find `/bin/grep`
    2. Use GTFOBins to find that we can abuse grep with `grep '' <file>`
