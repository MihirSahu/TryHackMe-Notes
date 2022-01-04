# Volume 1


1. Use cyberchef to decode `THM{ju57_d3c0d3_7h3_b453}`
2. Use exiftool `THM{3x1f_0r_3x17}`
3. Use steghide `THM{500n3r_0r_l473r_17_15_0ur_7urn}`
4. Highlight or check html `THM{wh173_fl46}`
5. Use an online qr code scanner to get `THM{qr_m4k3_l1f3_345y}`
6. Use `strings hello.hello | less` to find the flag `THM{345y_f1nd_345y_60}`
7. Use cyberchef with base58 `THM{17_h45_l3553r_l3773r5}`
8. Use a [ceaser cipher decoder](https://www.dcode.fr/caesar-cipher) to view all possible shifts to get `THM{hail_the_caesar}`
9. Inspect element to get `THM{4lw4y5_ch3ck_7h3_c0m3mn7}`
10. Open the file with a hex editor and replace the first 8 characters with the magic numbers for a png file: `89 50 4E 47`. `THM{y35_w3_c4n}`
11. Google it `THM{50c14l_4cc0un7_15_p4r7_0f_051n7}`
12. Use a brainfuck decoder `THM{0h_my_h34d}`
13. Use an [XOR decoder](https://md5decrypt.net/en/Xor/) with `44585d6b2368737c65252166234f20626d` as the key and `1010101010101010101010101010101010` as the value to get `54484d7b3378636c75353176335f30727d`. Convert this from hex to ascii to get `THM{3xclu51v3_0r}`
14. Use binarywalk `binwalk --extract hell.jpg` to get `THM{y0u_w4lk_m3_0u7}`
15. Use stegsolve and use the blue filters to find `THM{7h3r3_15_hop3_1n_7h3_d4rkn355}`
16. Use an online code scanner to find this line `https://soundcloud.com/user-86667759/thm-ctf-vol1`. The flag is `THM{SOUNDINGQR}`
17. Use the wayback machine on the internet archive on the data Jan 2, 2020 to find `THM{ch3ck_th3_h4ckb4ck}`
18. Use a Vigenere cipher to auto solve without the key to get `tryhackme{you_found_the_key}`. [Great resource to learn](https://www.boxentriq.com/code-breaking/vigenere-cipher)
19. Convert from [decimal to hex](https://www.rapidtables.com/convert/number/decimal-to-hex.html) to [ascii](https://gchq.github.io/CyberChef/) `THM{17_ju57_4n_0rd1n4ry_b4535}`
20. Open with wireshark, search for GET requests with `http.request.method == GET`and follow the http stream `THM{d0_n07_574lk_m3}`
