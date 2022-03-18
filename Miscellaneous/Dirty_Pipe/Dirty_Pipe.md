# Dirty Pipe


## Introduction and Deploy
- March 2022, Dirty Pipe was disclosed, named because of its similarity to Dirty Cow vulnerability
- Allows for file overwrites at the kernel level, which can be leveraged to escalate privileges
- [Disclosure](https://dirtypipe.cm4all.com/)

## Exploit Background
- Page - smallest unit of memory controlled by the CPU
	- Used when reading and writing files from the disk
	- Page cache - part of the kernel that manages pages
- When a process tries to open a file, the kernel loads it into pages which are then made available in two ways
	1. Pages can be copied into the user-space memory
	2. Pages can be kept in kernel-space but made accessibly via system calls (special functions to interact with the kernel)
- Pipes `|` allow data to be passed between two processes
	- Have two ends; one for reading and one for writing
	- Pipes take standard output of a process and write it into a pipe, where it can be read by the standard input of the next program in the chain
- Linux kernel provides a system call `splice()`, which speeds up the process of pushing the contents of a file into a pipe
	- The optimization is achieved by moving references to the pages storing the file contents instead of moving the entirety of the data
	- In other words, `splice()` allows us to point a pipe at a page which is already loaded into memory, containing a section of a file originally opened by a process requesting read-only access
		- 0_0
	- By splicing a page into the pipe then writing our own arbitrary data to the pipe, we can overwrite the contents of the page
- Usually when you write to a pipe after splicing a file, no changes actually happen on the disk - changes are made to the page buffer in memory but nothing is altered in the file itself, so how to force the kernel to write the contents of the relevant pages back to the disk?
- Two commits on the Linux kernel:
	- A bug was introduced in Linux Kernel v4.9 (2016) which allowed pipes to be created with arbitrary flags. None of the flags available at the time were in any way dangerous, so this wasn't an issue, until...
	- Linux Kernel v5.8 (2020) added a new flag — PIPE_BUF_FLAG_CAN_MERGE. In simple terms, this flag tells the kernel that the changes written to the page pointed to by the pipe should be written directly back to the file that the page comes from.
- To summarise: we have a flag that allows us to tell the kernel to write the page back to the disk as data comes into it, we have a bug that allows us to specify arbitrary flags for a pipe, and we have a system call that inadvertently allows us to point pipes at page buffers which were opened as read-only. What could possibly go wrong?
- Put simply, the exploit first opens a target file with the read-only flag set — in order to do this, we must choose a file that we have permission to read. The exploit then prepares a pipe in a special way, forcing the addition of the PIPE_BUF_FLAG_CAN_MERGE flag. Next, it uses splice() to make the pipe point at the desired section of the target file. Finally, it writes whatever arbitrary data that the user has specified into the pipe, thereby overwriting the page buffer and — by merit of PIPE_BUF_FLAG_CAN_MERGE — overwriting the file on the disk.
- In short, it means that, with the right code, we can arbitrarily overwrite any file on the system, provided we can open it for reading. In other words: if our user has read access over the file (regardless of other permissions or mutability) then we can also write to it. Interestingly, this also applies to read-only file systems, or otherwise protected files which the kernel would usually stop us from writing to; by exploiting the kernel vulnerability and circumventing the "usual" write methods, we also bypass these protections.

## A Weaponised PoC
- The proof of concept included in the [Disclosure](https://dirtypipe.cm4all.com/) allows us to specify the file we want to overwrite, the offset we want to overwrite at, and the content we want to insert
- The exploit only works on a file that the user has read access
- We want to find a file that we have read access to and will allow us to escalate privileges. An obvious file is `/etc/passwd`
- Exploit
	1. Create a new password hash `openssl passwd -6 --salt <salt> <password>`
	2. Create a template in this format `USERNAME:HASH:0:0::/root:/bin/bash`, it should look something like this `muiri:$6$THM$eRD0Ur0SZuwDLSwf9Lb2vyC2T6/PtQUA/B0Ssm6/jsiBtpSvc6QLjhFF0XNM8odgfkxMnC4oczGuvEomrVRfz0:0:0::/root:/bin/bash`
	3. Because we're overwriting the file, we need to add a new line to the end to avoid corrupting the entry
	```
	'muiri:$6$THM$eRD0Ur0SZuwDLSwf9Lb2vyC2T6/PtQUA/B0Ssm6/jsiBtpSvc6QLjhFF0XNM8odgfkxMnC4oczGuvEomrVRfz0:0:0::/root:/bin/bash
	'
	```
	4. Now we need to find the offset (where in the file the exploit should begin writing at). The exploit doesn't let us append to a file, so we need to pick an account(s) (depending on how large our template is) and overwrite it. We want to overwrite an account that seems little-used. In this `/etc/passwd` file, we want to overwrite the `games` user, so find the offset with `grep -b "games" /etc/passwd`
	5. Backup the `/etc/passwd` file
	5. Compile and run the exploit
	```
	./exploit /etc/passwd 189 'USERNAME:HASH:0:0::/root:/bin/bash
	> '
	```
	6. Because overwriting `/etc/passwd` could have caused issues on the server, restore the file from the backup after you're done with the exploit
- Note: The exploit .cast file can be viewed with asciinema

## A Second Exploit
- Another exploit called `dirtypipez.c` overwrites binary files instead of something like `/etc/passwd` and then executes it with the permissions of a privileged user
- Normally SUID programs lose their SUID bit when you try to write to them, but it doesn't happen with Dirty Pipe
- All you have to do is compile it and run it while specifying the SUID binary you want to target: `./exploit /bin/su`
