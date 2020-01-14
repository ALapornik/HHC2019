`Zeek JSON Analysis <https://docker2019.kringlecon.com/?challenge=jq&id=64e23b2a-9a30-4e76-b15e-5f97a639b57f>`_
===============================================================================================================

Challenge
---------
The initial dialog with Wunorse Openslae:

.. parsed-literal::
    **Wunorse Openslae**
    Wunorse Openslae here, just looking at some Zeek logs.
    I'm pretty sure one of these connections is a malicious C2 channel...
    Do you think you could take a look?
    I hear a lot of C2 channels have very long connection times.
    Please use jq to find the longest connection in this data set.
    We have to kick out any and all grinchy activity!

The hint from our badge:

.. parsed-literal::
    **Jq**
    From: Wunorse Openslae
    `Parsing Zeek JSON Logs with JQ <https://pen-testing.sans.org/blog/2019/12/03/parsing-zeek-json-logs-with-jq-2>`_

The banner page from the terminal challenge:

.. image:: /images/zeekjsonanalysis-banner.png

Solution
--------
**jq** is a lightweight and flexible command-line JSON processor which we used to solve his challenge.

We listed the contents of our folder to reveal a single file ``conn.log`` which we assumed to be the log file we needed to analyse.

We determined the keys by piping the first entry in **conn.log** into jq. The command we used was:

``head -1 conn.log | jq``

This produced the following output:

.. image:: /images/zeekjsonanalysis-determining-keys.png

We then ran the following command which sorts the entries by **duration** and returns the last entry (the longest).

``cat conn.log | jq -s 'sort_by(.duration) | reverse | .[0]'``

This produced the following output:

.. image:: /images/zeekjsonanalysis-longest-duration.png

Running ``runtoanswer`` and submiting the IP address corresponding to **id.resp_h** (13.107.21.200) produced the following output:

.. code-block::

    Loading, please wait......
    What is the destination IP address with the longes connection duration? 13.107.21.200
    Thank you for your analysis, you are spot-on.
    I would have been working on that until the early dawn.
    Now that you know the features of jq,
    You'll be able to answer other challenges too.
    -Wunorse Openslae
    Congratulations!


Hints
-----

Wunorse Openslae provides the following hint in his dialog after solving the terminal challenge:

.. parsed-literal::
    **Wunorse Openslae**
    That's got to be the one - thanks!
    Hey, you know what? We've got a crisis here.
    You see, Santa's flight route is planned by a complex set of machine learning algorithms which use available weather data.
    All the weather stations are reporting severe weather to Santa's Sleigh. I think someone might be forging intentionally false weather data!
    I'm so flummoxed I can't even remember how to login!
    Hmm... Maybe the Zeek http.log could help us.
    I worry about LFI, XSS, and SQLi in the Zeek log - oh my!
    And I'd be shocked if there weren't some shell stuff in there too.
    I'll bet if you pick through, you can find some naughty data from naughty hosts and block it in the firewall.
    If you find a log entry that definitely looks bad, try pivoting off other unusual attributes in that entry to find more bad IPs.
    The sleigh's machine learning device (SRF) needs most of the malicious IPs blocked in order to calculate a good route.
    Try not to block many legitimate weather station IPs as that could also cause route calculation failure.
    Remember, when looking at JSON data, jq is the tool for you!

The following hint was unlocked in our badge:

.. parsed-literal::
    **Finding Bad in Web Logs**
    From: Wunorse Openslae
    Do you see any `LFI <https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion>`_, `XSS <https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)>`_, `Shellshock <https://en.wikipedia.org/wiki/Shellshock_(software_bug)>`_, or `SQLi <https://www.owasp.org/index.php/SQL_Injection>`_?
    