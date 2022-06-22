# Burp Suite: Other Modules


## Decoder
- Allows us to manipulate data
- Options
	- The box on the left is where we would paste or type text to be encoded or decoded. As with most other modules of Burp Suite, we can also send data here from other sections of the framework by right-clicking and choosing Send to Decoder.
	- We have the option to select between treating the input as text or hexadecimal byte values at the top of the list on the right.
	- Further down the list, we have dropdown menus to Encode, Decode or Hash the input.
	- Finally, we have the "Smart Decode" feature, which attempts to decode the input automatically.

### Encoding/Decoding
- Plain: Plaintext is what we have before performing any transformations.
- URL: URL encoding is used to make data safe to transfer in the URL of a web request. It involves exchanging characters for their ASCII character code in hexadecimal format, preceded by a percentage symbol (%). Url encoding is an extremely useful method to know for any kind of web application testing.
	- For example, let's encode the forward-slash character (/). The [ASCII character code](https://www.asciitable.com/) for a forward slash is 47. This is "2F" in hexadecimal, making the URL encoded forward-slash %2F. 
- HTML: Encoding text as HTML Entities involves replacing special characters with an ampersand (&) followed by either a hexadecimal number or a reference to the character being escaped, then a semicolon (;). For example, a quotation mark has its own reference: `&quot;`. When this is inserted into a webpage, it will be replaced by a double quotation mark ("). This encoding method allows special characters in the HTML language to be rendered safely in HTML pages and has the added bonus of being used to prevent attacks such as XSS (Cross-Site Scripting).
	- When we use the HTML option in Decoder, we can encode any character as its HTML escaped format or decode captured HTML entities. 
- Base64: Another widely used encoding method, base64 is used to encode any data in an ASCII-compatible format. It was designed to take binary data (e.g. images, media, programs) and encode it in a format that would be suitable to transfer over virtually any medium.
- ASCII Hex: This option converts data between ASCII representation and hexadecimal representation. For example, the word "ASCII" can be converted into the hexadecimal number "4153434949". Each letter in the original data is taken individually and converted from numeric ASCII representation into hexadecimal.
	- For example, the letter "A" in ASCII has a decimal character code of 65. In hexadecimal, this is 41. Similarly, the letter "S" can be converted to hexadecimal 53, and so on.
- Hex, Octal, and Binary: These encoding methods all apply only to numeric inputs. They convert between decimal, hexadecimal, octal (base eight) and binary.
- Gzip: Gzip provides a way to compress data. It is widely used to reduce the size of files and pages before they are sent to your browser. Smaller pages mean faster loading times, which is highly desirable for developers looking to increase their SEO score and avoid annoying their customers. Decoder allows us to manually encode and decode gzip data, although this can be hard to process as it is often not valid ASCII/Unicode.

### Hashing
- Use the `Hash` dropdown menu and choose the hashing algorithm

## Comparer
- 3 main parts
	- On the left, we have the items being compared. When we load data into Comparer, it will appear as rows in these tables -- we would then select two datasets to compare.
	- On the upper right, we have options for pasting data in from the clipboard (Paste), loading data from a file (Load), removing the current row (Remove) and clearing all datasets (Clear).
	- Finally, on the bottom right, we have the option to compare our datasets by either words or bytes. Don't worry about which of these buttons you select as this can be changed later on. These are the buttons we click when we are ready to compare the data we have selected.
- After loading data into comparer
	- The compared data takes up most of the window; this can be viewed in either text or hex format. The initial format is determined by whether we chose to compare by words or by bytes in the previous window, but this can be overwritten by using the buttons above the comparison boxes.
	- The key for comparisons is at the bottom left, showing which colours denote modified, deleted, and added data between the two datasets.
	- At the bottom right of the window is the "Sync views" checkbox. When selected, this means that both sets of data will sync formats -- i.e. if you change one of them into Hex view, the other will do the same to match.

## Sequencer
- Rarely gets used in CTFs but is useful in real world
- Allows us to measure the randomness of tokens - strings that are used to identify something and should be generated in a cryptographically secure manner. If not, we might be abe to predict the values of the upcoming tokens
	- Ex. Analyze randomness of a session cookie or a CSRF token
- 2 main methods
	- Live capture is the more common of the two methods -- this is the default sub-tab for Sequencer. Live capture allows us to pass a request to Sequencer, which we know will create a token for us to analyse. For example, we may wish to pass a POST request to a login endpoint into Sequencer, as we know that the server will respond by giving us a cookie. With the request passed in, we can tell Sequencer to start a live capture: it will then make the same request thousands of times automatically, storing the generated token samples for analysis. Once we have accumulated enough samples, we stop Sequencer and allow it to analyse the captured tokens.
	- Manual load allows us to load a list of pre-generated token samples straight into Sequencer for analysis. Using Manual Load means we don't have to make thousands of requests to our target (which is both loud and resource intensive), but it does mean that we need to obtain a large list of pre-generated tokens!

### Live Capture
1. Capture a request to `http://10.10.248.172/admin/login/` and send it to the Sequencer
2. The `Token Location Within Response` section will have the option to select between Cookie, Form field, and Custom location
3. Click `Start live capture`. Wait for a reasonable number of tokens to be captured
4. Pause and select `Analyze now`
