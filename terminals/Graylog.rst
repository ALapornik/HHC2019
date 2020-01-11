`Graylog <https://incident.elfu.org/?challenge=graylog>`_
=========================================================

.. code-block:: none

    Click on the All messages Link to access the Graylog search interface!
    Make sure you are searching in all messages!
    The Elf U Graylog server has an integrated incident response reporting system. Just mouse-over the box in the lower-right corner.
    Login with the username elfustudent and password elfustudent.

Question 1:
-----------
Minty CandyCane reported some weird activity on his computer after he clicked on a link in Firefox for a cookie recipe and downloaded a file.

What is the full-path + filename of the first malicious file downloaded by Minty?
Answer: 
**C:\Users\minty\Downloads\cookie_recipe.exe**

Query: 
``EventID:2 AND ProcessImage:/.+\firefox.exe/ NOT TargetFilename:/.+\.temp/``

Post-Answer Dialog: 
We can find this searching for sysmon file creation event id 2 with a process named firefox.exe and not junk .temp files. We can use regular expressions to include or exclude patterns:
TargetFilename:/.+\.pdf/

The file was accessed at 2019-11-19 05:28:33.000
Question 2:
-----------
The malicious file downloaded and executed by Minty gave the attacker remote access to his machine. What was the ip:port the malicious file connected to first?

Answer:
**192.168.247.175:4444**

Query:
We searched for records containing "cookie_recipe.exe" and containing a DestinationIp
``cookie_recipe.exe AND DestinationIp:/.+/``

A better query might have been:
``ProcessImage:/.+cookie_recipe.exe/ AND DestinationIp:/.+/``

Post-Answer Dialog:
We can pivot off the answer to our first question using the binary path as our ProcessImage.

Question 3:
-----------
Question 3:
What was the first command executed by the attacker?
(answer is a single word)

Answer:
**whoami**

Query:
ParentProcessImage:/.+cookie_recipe.exe/

Post-Answer Dialog:
Since all commands (sysmon event id 1) by the attacker are initially running through the cookie_recipe.exe binary, we can set its full-path as our ParentProcessImage to find child processes it creates sorting on timestamp.

Question 4:
-----------
What is the one-word service name the attacker used to escalate privileges?

Answer: 
**webexservice**

Query:
ParentProcessImage:/.+cookie_recipe.exe/
Our records are sorted according to timestamp, so we look at later commands until we see something involving a service. The command used was:
C:\Windows\system32\cmd.exe /c "cmd.exe /c sc start webexservice a software-update 1 C:\Users\minty\Downloads\cookie_recipe2.exe "

Before this there were some commands passed to list services.

Post-Answer Dialog:
Continuing on using the cookie_reciper.exe binary as our ParentProcessImage, we should see some more commands later on related to a service.

Question 5:
-----------
What is the file-path + filename of the binary ran by the attacker to dump credentials?

Answer: C:\cookie.exe

Query:
ParentProcessImage:/.+cookie_recipe2.exe/

The attacker downloads mimikatz.exe and saves it as C:\cookie.exe

Post-Answer Dialog:
The attacker elevates privileges using the vulnerable webexservice to run a file called cookie_recipe2.exe. Let's use this binary path in our ParentProcessImage search.

Question 6:
-----------
The attacker pivoted to another workstation using credentials gained from Minty's computer. Which account name was used to pivot to another machine?

Windows Event Id 4624 is generated when a user network logon occurs successfully. We can also filter on the attacker's IP using SourceNetworkAddress.