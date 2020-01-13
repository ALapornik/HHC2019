4) Windows Log Analysis: Determine Attacker Technique
=====================================================

Challenge
---------
Difficulty: 2/5

Using these `normalized Sysmon logs <https://downloads.elfu.org/sysmon-data.json.zip>`_, identify the tool the attacker used to retrieve domain password hashes from the lsass.exe process. For hints on achieving this objective, please visit Hermey Hall and talk with SugarPlum Mary.

Answer
------
**ntdsutil**

Solution
--------
After unzipping the file and installing eql, we ran the following queries:

.. code-block:: bash

    # The attacker got the hashes 'from' lsass.exe, thus we looked for a parent_process_name=lsass.exe
    eql query -f sysmon-data.json "process where parent_process_name = 'lsass.exe'" | ./jq.exe
    {
      "command_line": "C:\\Windows\\system32\\cmd.exe",
      "event_type": "process",
      "logon_id": 999,
      "parent_process_name": "lsass.exe",
      "parent_process_path": "C:\\Windows\\System32\\lsass.exe",
      "pid": 3440,
      "ppid": 632,
      "process_name": "cmd.exe",
      "process_path": "C:\\Windows\\System32\\cmd.exe",
      "subtype": "create",
      "timestamp": 132186398356220000,
      "unique_pid": "{7431d376-dedb-5dd3-0000-001027be4f00}",
      "unique_ppid": "{7431d376-cd7f-5dd3-0000-001013920000}",
      "user": "NT AUTHORITY\\SYSTEM",
      "user_domain": "NT AUTHORITY",
      "user_name": "SYSTEM"
    }

    # The process_name above is cmd.exe, to see what this refers to we look for it in parent process name. To avoid a large output, we used '.process_name', to only get that field
    eql query -f sysmon-data.json "process where parent_process_name = 'cmd.exe'" | ./jq.exe '.process_name'
    # There was a lot of data in the output, see the summary below.
    # We get 2388 instances of net.exe, 3 instances of powershell.exe and 1 instance of ntdsutil.exe back
    # The hint clearly states that ntdsutil is an attack tool



Hint
----
**SugarPlum Mary:**

    Oh there they are! Now I can delete them. Thanks!
    Have you tried the Sysmon and EQL challenge?
    If you aren't familiar with Sysmon, Carlos Perez has some great info about it.
    Haven't heard of the Event Query Language?
    Check out some of `Ross Wolf <https://www.endgame.com/our-experts/ross-wolf>`_'s work on EQL or that blog post by Josh Wright in your badge.

.. hint:: 

    Sysmon
    
    From: SugarPlum Mary
    
    `Sysmon By Carlos Perez <https://www.darkoperator.com/blog/2014/8/8/sysinternals-sysmon>`_

.. hint:: 

    Event Query Language

    From: SugarPlum Mary
    
    `EQL Threat Hunting <https://pen-testing.sans.org/blog/2019/12/10/eql-threat-hunting/>`_
