5) Network Log Analysis: Determine Compromised System
=====================================================

Challenge
---------
Difficulty: 2/5

The attacks don't stop! Can you help identify the IP address of the malware-infected system using these `Zeek logs <https://downloads.elfu.org/elfu-zeeklogs.zip>`_? For hints on achieving this objective, please visit the Laboratory and talk with Sparkle Redberry.

Answer
------
**192.168.134.130**

Solution
--------
After Downloading and Extracting the file, we noticed that it contained a folder ``elfu-zeeklogs``.
We opened this folder and noticed that it contained 890 log files and a folder ``ELFU``
We then opened  ELFU:

.. image:: /images/ELFU.PNG

There is a file named ``index.html`` as well as some other files and folders.

The ELFU folder contains the tabs that can be accesed from the index

.. image:: /images/ELFU2.PNG

Open the index.html file in a browser.

.. image:: /images/INDEX.PNG

Click on ELFU

.. image:: /images/MENU.PNG

Click on Beacons

.. image:: /images/Beacons.PNG

The first row has the highest score, so it's the most likely to be a beacon.
The Source field of the first row contains the IP of the affected system.

Hint
----

**Sparkle Redberry:**

    You got it - three cheers for cheer!
    For objective 5, have you taken a look at our Zeek logs?
    Something's gone wrong. But I hear someone named Rita can help us.
    Can you and she figure out what happened?

.. hint:: 

    RITA
    
    From: Sparkle Redberry
    
    `RITA's homepage <https://www.activecountermeasures.com/free-tools/rita/>`_

