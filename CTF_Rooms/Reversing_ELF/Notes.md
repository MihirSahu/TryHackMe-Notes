# Reversing ELF Writeup

## Notes
If bash gives an error when you try to execute the files it means that your machine doesn't have the right elf interpreter installed in your system. I solved this by using a kali VM
   https://stackoverflow.com/questions/27735915/linux-cannot-execute-binary-file
Using both gbd and r2 is useful in this
**Make sure you have gef for gdb installed**

## crackme1
1. Run the binary
        - flag{not_that_kind_of_elf}

## crackme2
1. Open binary with radare2 and you'll see the password
        - super_secret_password
2. Run binary with password as argument and receive flag
        - flag{if_i_submit_this_flag_then_i_will_get_points}

## crackme3
1. Open binary in radare2 and you'll see the weird string
2. Look closely and we see the line
        - 0x0804858f      83f840         cmp eax, 0x40               ; 64
3. We also see the string ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ
3. After analyzing the other functions we can conclude that something is manipulating the string, and if we try to decode it as base64 we get
        - f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5

## crackme4
1. Run the binary and we see that it takes one argument, the password
2. Open binary with gdb and "disas main"
3. We see that the main function checks and makes sure that there's exactly 1 argument, and if there is it calls the compare_pwd function
4. When we use "disas compare_pwd" we see that this function moves a lot of values around and calls the ```get_pwd``` function
5. Finally, when we "disas get_pwd" we see from the assembly structure that it's looping and manipulating a string
6. Now we run gdb on the target and run these commands:
        - break main
        - r <any string>
7. Now we go through the program with repeated 'si' or just enter until we finish the loop in the get_pwd function
        - You can just set a breakpoint at get_pwd, but for learning purposes we should go through the program and understand what it all means
8. After we finish the loop in the get_pwd function, we see that in the rdi register we have the string "```my_m0r3_secur3_pwd```"
9. We run the binary with this as the argument and we get "password OK"
