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
