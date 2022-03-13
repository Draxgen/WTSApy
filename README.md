# WTSApy - Windows Task Scheduler Alternative for Python

Schedule all your tasks in Windows using only Python.

WTSApy is a script that launches other scripts. It is meant to omit using the Windows Task Scheduler, because adding a Python script to it and configuring the task for it is tedious and annoying and also [potentially buggy](https://answers.microsoft.com/en-us/windows/forum/all/task-scheduler-cannot-run-files-at-system-startup/6a8617bc-be73-4719-9cf3-9c17e1cb295b). Instead all you have to do is add a shortcut to WTSApy's main script in the Startup folder. The main script will take care of the rest by dynamically launching other scripts.

Currently supported launching modes: 
- Windows Startup

Launching modes to be added: 
- Windows Shutdow
- Application Starting
- Time intervals
- Specific time (13:30 for instance)
