# Needles in Computer Stacks


## Yara
- YARA is a tool for matching patterns of interest in files
- Used to perform research on malware families and identify malware with similar patterns
- Yara rules - a way of telling yaya what characteristics to look for in a file
    - [Example](https://github.com/InQuest/awesome-yara)
```
rule rulename
  {
    meta:
      author = "tryhackme"
      description = "test rule"
      created = "11/12/2021 00:00"
    strings:
      $textstring = "text"
      $hexstring = {4D 5A}
    conditions:
      $textstring and $hexstring
  }
```
- Yara rule syntax
    - Strings
        - Specify the strings you want to match
        - Define strings like you define variables
            - `$textstring = "text"`
        - Can be text strings (which are strings found in the legible text portion of a file) or hex strings (raw sequences of bytes in a file)
            - Use double quotes for text strings and braces for hex strings
    - Conditions
        - Defines the conditions that the writer want to meet in order for the rule to hit on a file
        - Conditions are booleans, and use strings defined in the strings section as variables
        - Most common conditions are and, or, and not
    - Metadata
        - Adds metadata about the rule
        - Important when contributing to community
- Running yara
    - `yara [options] rule_file [target]`

## Exercise
1. or
2. -m
3. metadata
4. -n
5. 0
