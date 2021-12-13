# Santa's Bag of Toys

- Powershell Transcription Logs capture the input and output of windows powershell commands, allowing us to review what happened when
- Powershell Transcription can be enabled by Group Policy or be turned on from the Registry Editor
- Entering these into the command prompt will turn on Powershell Transcription
    >reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableTranscripting /t REG_DWORD /d 0x1 /f
    >reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v OutputDirectory /t REG_SZ /d C:/ /f
    >reg add HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShell\Transcription /v EnableInvocationHeader /t REG_DWORD /d 0x1 /f
- The Registry is a large database of operating system settings and configurations
    - Organized by hives, with each hive containing keys and corresponding values
    - Powershell Transcription Logging can be enabled for a certain user with `HKEY_CURRENT_USER` or system wide with `HKEY_LOCAL_MACHINE`
- Powershell doesn't have to be invoked through the .exe, it's actually a dll
- Shellbags are artifacts in the registry that store user preferences while viewing folders within windows explorer
    - These shellbags can be viewed with programs like [shellbags explorer](https://www.sans.org/tools/shellbags-explorer/)
    - Shellbag [article 1](https://shehackske.medium.com/windows-shellbags-part-1-9aae3cfaf17) [article 2](https://shehackske.medium.com/windows-shellbags-from-an-offline-hive-9465de1407ac)
    - If a directory is mentioned in shellbags, it must have been present on the system at some point in time
    - Shellbags located at `C:\Users\...\AppData\Local\Microsoft\Windows`. There should be a data file called `UsrClass.dat`
    - Shellbags can also be found on the registry at `Computer\HKEY_CLASSES_ROOT\LocalSettings\Software\Microsoft\Windows\Shell\`
        - ShellBag data contains 2 main registry keys, BagMRU and Bags
- Exercise
    - Microsoft Windows 11 Pro
    - grinchstolechristmas
    - `C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat`
    - certutil.exe
    - .github
    - bag_of_toys.zip
    - Grinchiest
    - operation-bag-of-toys
    - uharc-cmd-install.exe
    - Grinchmas
    - TheGrinchiestGrinchmasOfAll
    - 228
