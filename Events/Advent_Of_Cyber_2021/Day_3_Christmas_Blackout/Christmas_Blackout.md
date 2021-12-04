# Christmas Blackout

## Content Discovery
- Content - the assets and innerworkings of the application we're testing
    - Can be files, folders, or pathways that weren't intended to be accessed by the general public
- Web servers are designed to server files and folders that are in it, unless configured otherwise
- Content discovery lets use find:
    - Configuration files
    - Passwords and secrets
    - Backups
    - Content management systems
    - Administrator dashboards or portals
- Tools such as dirbuster and gobuster allow us to find content
    - Ex. `dirb http://santascookies.thm`
    - Your ability to discover content is only as good as your wordlist. A good resource for wordlists is [SecLists](https://github.com/danielmiessler/SecLists)
## Default Credentials
- Web apps and services often come with default credentials - devs leave them so you can quickly get started with the platform
- Not everyone changes the default credentials
- SecList has a [wordlist](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials) for default credentials
- Sometimes default credentials are stored in configuration files or in public documentation
## Exercise
1. Use dirb to enumerate the website `dirb http://10.10.85.104` and we find the admin/ page
>root@ip-10-10-33-198:~# dirb http://10.10.85.104
>
>-----------------
>DIRB v2.22    
>By The Dark Raver
>-----------------
>
>START_TIME: Fri Dec  3 18:30:14 2021
>URL_BASE: http://10.10.85.104/
>WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
>
>-----------------
>
>GENERATED WORDS: 4612                                                          
>
>---- Scanning URL: http://10.10.85.104/ ----
>==> DIRECTORY: http://10.10.85.104/admin/                                                                                                                                               
>==> DIRECTORY: http://10.10.85.104/assets/                                                                                                                                              
>+ http://10.10.85.104/index.html (CODE:200|SIZE:5061)                                                                                                                                   
>==> DIRECTORY: http://10.10.85.104/javascript/                                                                                                                                          
>+ http://10.10.85.104/server-status (CODE:403|SIZE:277)                                                                                                                                 
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/admin/ ----
>==> DIRECTORY: http://10.10.85.104/admin/assets/                                                                                                                                        
>+ http://10.10.85.104/admin/index.html (CODE:200|SIZE:2251)                                                                                                                             
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/assets/ ----
>==> DIRECTORY: http://10.10.85.104/assets/css/                                                                                                                                          
>==> DIRECTORY: http://10.10.85.104/assets/fonts/                                                                                                                                        
>==> DIRECTORY: http://10.10.85.104/assets/img/                                                                                                                                          
>==> DIRECTORY: http://10.10.85.104/assets/js/                                                                                                                                           
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/javascript/ ----
>==> DIRECTORY: http://10.10.85.104/javascript/jquery/                                                                                                                                   
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/admin/assets/ ----
>==> DIRECTORY: http://10.10.85.104/admin/assets/css/                                                                                                                                    
>==> DIRECTORY: http://10.10.85.104/admin/assets/js/                                                                                                                                     
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/assets/css/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/assets/fonts/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/assets/img/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/assets/js/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/javascript/jquery/ ----
>+ http://10.10.85.104/javascript/jquery/jquery (CODE:200|SIZE:271809)                                                                                                                   
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/admin/assets/css/ ----
>                                                                                                                                                                                        
>---- Entering directory: http://10.10.85.104/admin/assets/js/ ----
>                                                                                                                                                                                        
>-----------------
>END_TIME: Fri Dec  3 18:30:42 2021
>DOWNLOADED: 55344 - FOUND: 4
2. Try some of the default usernames and passwords and we find that 'administrator' is the username and password
3. The flag is THM{ADM1N_AC3SS} 
