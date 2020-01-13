`Graylog <https://incident.elfu.org/?challenge=graylog>`_
=========================================================

Challenge
---------
The initial dialog with Pepper Minstix:

.. parsed-literal::
    **Pepper Minstix**
    Click on the All messages Link to access the Graylog search interface!
    Make sure you are searching in all messages!
    The Elf U Graylog server has an integrated incident response reporting system. 
    Just mouse-over the box in the lower-right corner.
    Login with the username elfustudent and password elfustudent.

The hints from our badge:

.. parsed-literal::
    **Graylog**
    From: Pepper Minstix
    `Graylog Docs <http://docs.graylog.org/en/3.1/pages/queries.html>`_

.. parsed-literal::
    **Event IDs and Sysmon**
    From: Pepper Minstix
    (Events and Sysmon)

Solution
--------
Question 1:
+++++++++++
Minty CandyCane reported some weird activity on his computer after he clicked on a link in Firefox for a cookie recipe and downloaded a file.

What is the full-path + filename of the first malicious file downloaded by Minty?

Answer:
"""""""
**C:\\Users\\minty\\Downloads\\cookie_recipe.exe**

Post-Answer Dialog: 
"""""""""""""""""""
We can find this searching for sysmon file creation event id **2** with a process named **firefox.exe** and not junk **.temp files**. We can use regular expressions to include or exclude patterns:
``TargetFilename:/.+\.pdf/``

Additional Notes:
"""""""""""""""""
Our query was:

``EventID:2 AND ProcessImage:/.+firefox.exe/ NOT TargetFilename:/.+\.temp/``

The file was accessed at **2019-11-19 05:28:33.000** which we can consider as the start of the attack. Any records before this time can be considered as out of scope for this investigation.

The machine to which the file was downloaded was **elfu-res-wks1**.

Question 2:
+++++++++++
The malicious file downloaded and executed by Minty gave the attacker remote access to his machine. What was the **ip:port** the malicious file connected to first?

Answer:
"""""""
**192.168.247.175:4444**

Post-Answer Dialog:
"""""""""""""""""""
We can pivot off the answer to our first question using the binary path as our **ProcessImage**.

Additional Notes:
"""""""""""""""""
We searched for records containing **cookie_recipe.exe** and containing a **DestinationIp**:
``cookie_recipe.exe AND _exists_:DestinationIp``

An alternative query based on the post-answer dialog might have been:
``ProcessImage:/.+cookie_recipe.exe/ AND _exists_:DestinationIp``

The destination hostname was **DEFANELF**. 

Question 3:
+++++++++++
What was the first command executed by the attacker?
(answer is a single word)

Answer:
"""""""
**whoami**

Post-Answer Dialog:
"""""""""""""""""""
Since all commands (sysmon event id 1) by the attacker are initially running through the **cookie_recipe.exe** binary, we can set its full-path as our **ParentProcessImage** to find child processes it creates sorting on timestamp.

Additional Notes:
"""""""""""""""""
Our query was:
``ParentProcessImage:/.+cookie_recipe.exe/``

The information that we were looking for was in the **CommandLine** field. The command was executed on the **elfu-res-wks1** host.

Question 4:
+++++++++++
What is the one-word service name the attacker used to escalate privileges?

Answer:
""""""" 
**webexservice**

Post-Answer Dialog:
"""""""""""""""""""
Continuing on using the **cookie_reciper.exe** binary as our **ParentProcessImage**, we should see some more commands later on related to a service.

Additional Notes:
"""""""""""""""""
We used the following query:
``ParentProcessImage:/.+cookie_recipe.exe/``

Our records were sorted according to the timestamp. This made it easy to look at the **CommandLine** field until we saw something involving a service.

We found some initial commands generally trying to determine what services were running on the machine. A bit later we saw a command trying to expoit the **webexservice**. The timestamp for this command was **2019-11-19 05:31:02.000**, just a few minutes after the initial file download. The command consisted of the following: ``C:\Windows\system32\cmd.exe /c "cmd.exe /c sc start webexservice a software-update 1 C:\Users\minty\Downloads\cookie_recipe2.exe "``. The command was executed on the **elfu-res-wks1** host.

Question 5:
+++++++++++
What is the file-path + filename of the binary ran by the attacker to dump credentials?

Answer:
"""""""
**C:\\cookie.exe**

Post-Answer Dialog:
"""""""""""""""""""
The attacker elevates privileges using the vulnerable **webexservice** to run a file called **cookie_recipe2.exe**. Let's use this binary path in our **ParentProcessImage** search.

Additional Notes:
"""""""""""""""""
We used the following query:
``ParentProcessImage:/.+cookie_recipe2.exe/``

In the **CommandLine** field we noticed a command at **2019-11-19 05:41:02.000** downloading **mimikatz.exe** and saving it as **C:\\cookie.exe**. A few minutes later at **2019-11-19 05:45:14.000** the attacker executed the **cookie.exe** file. The command was executed on the **elfu-res-wks1** host.

Question 6:
+++++++++++
The attacker pivoted to another workstation using credentials gained from Minty's computer. Which account name was used to pivot to another machine?

Answer:
"""""""
**alabaster**

Post-Answer Dialog:
"""""""""""""""""""
Windows Event Id **4624** is generated when a user network logon occurs successfully. We can also filter on the attacker's IP using **SourceNetworkAddress**.

Additional Notes:
"""""""""""""""""
We used the following query and looked at the **AccountName** field for the account:
``EventID:4624 AND SourceNetworkAddress:192.168.247.175``

The pivot was to the **elfu-res-wks2** host.

Question 7:
+++++++++++
What is the time ( HH:MM:SS ) the attacker makes a Remote Desktop connection to another machine?

Answer:
"""""""
**06:04:28**

Post-Answer Dialog:
"""""""""""""""""""
**LogonType 10** is used for successful network connections using the RDP client.

Additional Notes:
"""""""""""""""""
We used the following query although querying on just the **LogonType** would have been OK.
``LogonType:10 AND source:elfu-res-wks2``

The correct record was the one with an **AccountName** and **DestinationHostname**.

Question 8:
+++++++++++
The attacker navigates the file system of a third host using their Remote Desktop Connection to the second host. What is the **SourceHostName**,**DestinationHostname**,**LogonType** of this connection?
(submit in that order as csv)

Answer:
"""""""
**elfu-res-wks2,elfu-res-wks3,3**

Post-Answer Dialog:
"""""""""""""""""""
The attacker has GUI access to workstation 2 via RDP. They likely use this GUI connection to access the file system of of workstation 3 using explorer.exe via UNC file paths (which is why we don't see any cmd.exe or powershell.exe process creates). However, we still see the successful network authentication for this with event id **4624** and logon type **3**.

Additonal Notes:
""""""""""""""""
We used the following query, using **elf-res-wks2** as the source and looked for successful network connections: 
``SourceHostName:ELFU-RES-WKS2 AND EventID:4624``

The access occured at **2019-11-19 06:07:22.000**.

.. caution::
 The query is case-sensitive and the hostname must be in CAPITALS. We were initially unsuccessful with this question because we searched for **elfu-res-wks2** instead of **ELFU-RES-WKS2**.

Question 9:
+++++++++++
What is the full-path + filename of the secret research document after being transferred from the third host to the second host?

Answer:
"""""""
**C:\\Users\\alabaster\\Desktop\\super_secret_elfu_research.pdf**

Post-Answer Dialog:
"""""""""""""""""""
We can look for sysmon file creation event id of **2** with a source of workstation 2. We can also use regex to filter out overly common file paths using something like:
``AND NOT TargetFilename:/.+AppData.+/``

Additonal Notes:
""""""""""""""""
We performed a search using:
``source:elfu-res-wks2 AND EventID:2``

The first event after **2019-11-19 06:07:22.000** has a **TargetFilename** of **C:\\Users\\alabaster\\Desktop\\super_secret_elfu_research.pdf**. The timestamp for the event was **2019-11-19 06:07:51.000**.

Question 10:
++++++++++++
What is the IPv4 address (as found in logs) the secret research document was exfiltrated to?

Answer:
"""""""
**104.22.3.84**

Post-Answer Dialog:
"""""""""""""""""""
We can look for the original document in **CommandLine** using regex.

When we do that, we see a long a long PowerShell command using **Invoke-Webrequest** to a remote URL of **https://pastebin.com/post.php**.

We can pivot off of this information to look for a sysmon network connection id of **3** with a source of **elfu-res-wks2** and **DestinationHostname** of **pastebin.com**.

Additional Notes:
"""""""""""""""""
The first search term we used was:
``CommandLine:/.+secret.+/``

We found a command making use of **pastebin.com**. We pivoted off this imformation with the following search:
``DestinationHostname:pastebin.com``

.. note:: Dad complained that graylog seems too "gray". Added this to change that.


Hints
-----
Pepper Minstix provides the following hint in her dialog after solving the terminal challenge:

.. parsed-literal::
    **Pepper Minstix**
    That's it - hooray!
    Have you had any luck retrieving scraps of paper from the Elf U server?
    You might want to look into SQL injection techniques.
    You might want to look into SQL injection techniques.
    OWASP is always a good resource for web attacks.
    For blind SQLi, I've heard Sqlmap is a great tool.
    In certain circumstances though, you need custom tamper scripts to get things going!

The following hints were unlocked in our badge:

.. parsed-literal::
    **SQLMap Tamper Scripts**
    From: Pepper Minstix
    `Sqlmap Tamper Scripts <https://pen-testing.sans.org/blog/2017/10/13/sqlmap-tamper-scripts-for-the-win>`_

.. parsed-literal::
    **SQL Injection**
    From: Pepper Minstix
    `SQL Injection from OWASP <https://www.owasp.org/index.php/SQL_Injection>`_

