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
- .dat files can contain shellbags, or artifacts in the registry that store user preferences while viewing folders within windows explorer
- Exercise
    - Microsoft Windows 11 Pro
    - grinchstolechristmas
    - `C:\Users\santa\AppData\Local\Microsoft\Windows\UsrClass.dat`
    - certutil.exe
