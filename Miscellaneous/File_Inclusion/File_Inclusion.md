# File Inclusion


## Introduction
- Sometimes web applications are written to request access to files on a given system via parameters
- ![Graph](Images/URL.png)
- ![Graph](Images/graph.png)
    - The file name is the parameter sent to the web server
- File inclusion vulnerabilities occur in various programming languages that are poorly written and implemented
    - Main issue is that user input is not sanitized and the user controls them and can pass any input to the function

## Path Traversal
- Allows attacker to read operating system resources, such as local files
- Attacker can manipulate the URL to locate and access files or directories outside of the application's root directory
- This occurs when the user's input is passed into a function like file_get_contents in php without input validation/filtering
- ![Path Traversal 1](Images/path_traversal_1.png)
- Path traversal attack takes advantage of moving the directory a step up with the `../`
- ![Path Traversal 2](Images/path_traversal_2.png)
- Then instead of the original file the contents of the specified file are posted
- ![Path Traversal 3](Images/path_traversal_3.png)
- If the web server is running on windows, the attacker would need to provide windows paths
    - Ex. `http://webapp.thm/get.php?file=../../../../boot.ini` or `http://webapp.thm/get.php?file=../../../../windows/win.ini`
- ![Path Traversal 4](Images/path_traversal_4.png)

## Local File Inclusion (LFI)
- LFI attacks happen due to developers' lack of security awareness
- With PHP, functions such as `include`, `require`, `include_once`, and `require_once` contribute to vulnerable applications
- LFI can happen in any language
- Ex. The code uses a GET request via URL parameter `lang` to include the file on the page. There isn't any input validation. There isn't a directory specified in the `include` function, so we don't need path traversal
```
<?PHP 
	include($_GET["lang"]);
?>
```
- Ex. Because a directory is specified, we can bypass it with path traversal `http://webapp.thm/index.php?lang=../../../../etc/passwd`
```
<?PHP 
	include("languages/". $_GET['lang']); 
?>
```
