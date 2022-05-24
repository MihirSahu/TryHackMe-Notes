# Burp Suite: Intruder


## What is Intruder?
- Intruder is a fuzzing tool that takes a request and uses it as a template to send more requests with slightly altered values automatically
- Can swap out username and password fields for values for a wordlist and brute force the login form
- Can fuzz for subdirectories, endpoints, or virtual hosts
- To access the full speed of Intruder, Burp Pro is required
- Intruder options
	- Positions allows us to select an Attack Type (we will cover these in an upcoming task), as well as configure where in the request template we wish to insert our payloads.
	- Payloads allows us to select values to insert into each of the positions we defined in the previous sub-tab. For example, we may choose to load items in from a wordlist to serve as payloads. How these get inserted into the template depends on the attack type we chose in the Positions tab. There are many payload types to choose from (anything from a simple wordlist to regexes based on responses from the server). The Payloads sub-tab also allows us to alter Intruder's behaviour with regards to payloads; for example, we can define pre-processing rules to apply to each payload (e.g. add a prefix or suffix, match and replace, or skip if the payload matches a defined regex).
	- Resource Pool is not particularly useful to us in Burp Community. It allows us to divide our resources between tasks. Burp Pro would allow us to run various types of automated tasks in the background, which is where we may wish to manually allocate our available memory and processing power between these automated tasks and Intruder. Without access to these automated tasks, there is little point in using this, so we won't devote much time to it.
	- As with most of the other Burp tools, Intruder allows us to configure attack behaviour in the Options sub-tab. The settings here apply primarily to how Burp handles results and how Burp handles the attack itself. For example, we can choose to flag requests that contain specified pieces of text or define how Burp responds to redirect (3xx) responses.

## Positions
- Positiont - tell Intruder where to insert payloads
- When a request is sent to Intruder, Burp will try to detect the most likely positions to insert a payload
- Payload sections are marked by `§`
- Positions can be Added, Cleared, or Auto (automatically generated)

## Attack Types
- Attack types can be modified in the Position sub-tab
- Sniper
- Battering ram
- Pitchfork
- Cluster bomb

## Sniper
- Most common atatck type
- Sniper accepts one set of payloads
	- A single file containing a wordlist or range of numbers
- Payload set - list of items to be inserted into requests
- Intruder will take each payload from the set and put it into the defined position
- Sniper is very good for single-position attacks (if we know one variable such as the username and want to find the password)

## Battering Ram
- Battering ram takes one set of payloads, but unlike Sniper, it puts the same payload in every position instead of each position in turn
- Ex. `username=burp&password=burp`

## Pitchfork
- Like multiple Snipers
- Uses one payload set per position (up to 20) and iterates through them all at once
- Iterates through each payload set simultaneously

## Cluster Bomb
- Combines multiple payload sets like Sniper, but iterates through each payload set individually, making sure that every possible combination of payloads is tested

## Payloads
- 4 sections
```
The Payload Sets section allows us to choose which position we want to configure a set for as well as what type of payload we would like to use.
When we use an attack type that only allows for a single payload set (i.e. Sniper or Battering Ram), the dropdown menu for "Payload Set" will only have one option, regardless of how many positions we have defined.
If we are using one of the attack types that use multiple payload sets (i.e. Pitchfork or Cluster Bomb), then there will be one item in the dropdown for each position.
Note: Multiple positions should be read from top to bottom, then left to right when being assigned numbers in the "Payload set" dropdown. For example, with two positions (username=§pentester§&password=§Expl01ted§), the first item in the payload set dropdown would refer to the username field, and the second would refer to the password field.
The second dropdown in this section allows us to select a "payload type". By default, this is a "Simple list" -- which, as the name suggests, lets us load in a wordlist to use. There are many other payload types available -- some common ones include: Recursive Grep, Numbers, and Username generator. It is well worth perusing this list to get a feel for the wide range of options available.
```
```
Payload Options differ depending on the payload type we select for the current payload set. For example, a "Simple List" payload type will give us a box to add and remove payloads to and from the set:
We can do this manually using the "Add" text box, paste lines in with "Paste", or "Load..." from a file. The "Remove" button removes the currently selected line only. The "Clear" button clears the entire list. Be warned: loading extremely large lists in here can cause Burp to crash!
By contrast, the options for a Numbers payload type allows us to change options such as the range of numbers used and the base that we are working with.
```
```
Payload Processing allows us to define rules to be applied to each payload in the set before being sent to the target. For example, we could capitalise every word or skip the payload if it matches a regex. You may not use this section particularly regularly, but you will definitely appreciate it when you do need it!
```
```
Finally, we have the Payload Encoding section. This section allows us to override the default URL encoding options that are applied automatically to allow for the safe transmission of our payload. Sometimes it can be beneficial to not URL encode these standard "unsafe" characters, which is where this section comes in. We can either adjust the list of characters to be encoded or outright uncheck the "URL-encode these characters" checkbox.
```
