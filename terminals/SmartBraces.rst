`Smart Braces <https://docker2019.kringlecon.com/?challenge=iptables>`_
=======================================================================

Challenge
---------
The initial dialog with Kent Tinseltooth:

The hint from our badge:

.. parsed-literal::
    **Iptables**
    From: Kent Tinseltooth
    `Iptables <https://upcloud.com/community/tutorials/configure-iptables-centos/>`_

The dialog when entering the terminal challenge:

.. parsed-literal::
    **Kent Tinseltooth**   
    Inner Voice: Kent. Kent. Wake up, Kent.
    Inner Voice: I'm talking to you, Kent.
    Kent TinselTooth: Who said that? I must be going insane.
    Kent TinselTooth: Am I?
    Inner Voice: That remains to be seen, Kent. But we are having a conversation.
    Inner Voice: This is Santa, Kent, and you've been a very naughty boy.
    Kent TinselTooth: Alright! Who is this?! Holly? Minty? Alabaster?
    Inner Voice: I am known by many names. I am the boss of the North Pole. Turn to me and be hired after graduation.
    Kent TinselTooth: Oh, sure.
    Inner Voice: Cut the candy, Kent, you've built an automated, machine-learning, sleigh device.
    Kent TinselTooth: How did you know that?
    Inner Voice: I'm Santa - I know everything.
    Kent TinselTooth: Oh. Kringle. *sigh*
    Inner Voice: That's right, Kent. Where is the sleigh device now?
    Kent TinselTooth: I can't tell you.
    Inner Voice: How would you like to intern for the rest of time?
    Kent TinselTooth: Please no, they're testing it at srf.elfu.org using default creds, but I don't know more. It's classified.
    Inner Voice: Very good Kent, that's all I needed to know.
    Kent TinselTooth: I thought you knew everything?
    Inner Voice: Nevermind that. I want you to think about what you've researched and studied. From now on, stop playing with your teeth, and floss more.
    *Inner Voice Goes Silent*

    Kent TinselTooth: Oh no, I sure hope that voice was Santa's.
    Kent TinselTooth: I suspect someone may have hacked into my IOT teeth braces.
    Kent TinselTooth: I must have forgotten to configure the firewall...
    Kent TinselTooth: Please review /home/elfuuser/IOTteethBraces.md and help me configure the firewall.
    Kent TinselTooth: Please hurry; having this ribbon cable on my teeth is uncomfortable.
    
Solution
--------
We displayed the contents of **IOTteethBraces.md** using the following command:

``cat /home/elfuuser/IOTteethBraces.md``

.. code-block::  none

    # ElfU Research Labs - Smart Braces
    ### A Lightweight Linux Device for Teeth Braces
    ### Imagined and Created by ElfU Student Kent TinselTooth
    This device is embedded into one's teeth braces for easy management and monitoring of dental status. It uses FTP and HTTP for management and monitoring purposes but also has SSH for remote access. Please $
    ## Proper Firewall configuration:
    The firewall used for this system is `iptables`. The following is an example of how to set a default policy with using `iptables`:
    ```
    sudo iptables -P FORWARD DROP
    ```
    The following is an example of allowing traffic from a specific IP and to a specific port:
    ```
    sudo iptables -A INPUT -p tcp --dport 25 -s 172.18.5.4 -j ACCEPT
    ```
    A proper configuration for the Smart Braces should be exactly:
    1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.
    2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPUT chains.
    3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH server (on port 22).
    4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.
    5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.
    6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.

Following these instructions, we typed the below commands into the terminal:

+---+------------------------------------------------------------------------------+
|   | ``sudo iptables -P INPUT DROP``                                              |
|   |                                                                              |
| 1 | ``sudo iptables -P FORWARD DROP``                                            |
|   |                                                                              |
|   | ``sudo iptables -P OUTPUT DROP``                                             |
+---+------------------------------------------------------------------------------+
|   | sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT  |
| 2 |                                                                              |
|   | sudo iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT |
+---+------------------------------------------------------------------------------+
| 3 | sudo iptables -A INPUT -p tcp --dport 22 -s 172.19.0.225 -j ACCEPT           |
+---+------------------------------------------------------------------------------+
|   | sudo iptables -A INPUT -p tcp --dport 21  -j ACCEPT                          |
| 4 |                                                                              |
|   | sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT                           |
+---+------------------------------------------------------------------------------+
| 5 | sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT                          |
+---+------------------------------------------------------------------------------+
| 6 | sudo iptables -A INPUT -i lo -j ACCEPT                                       |
+---+------------------------------------------------------------------------------+

Success! We got the following output:

.. code-block::

    Kent TinselTooth: Great, you hardened my IOT Smart Braces firewall!
    /usr/bin/inits: line 10:   642 Killed                  su elfuuser

Hints
-----
Kent Tinseltooth provides the following hint in his dialog after solving the terminal challenge:

.. parsed-literal::
    **Kent Tinseltooth**
    By the way, have you tried to get into the crate in the Student Union? It has an interesting set of locks.
    There are funny rhymes, references to perspective, and odd mentions of eggs!
    And if you think the stuff in your browser looks strange, you should see the page source...
    Special tools? No, I don't think you'll need any extra tooling for those locks.
    BUT - I'm pretty sure you'll need to use Chrome's developer tools for that one.
    Or sorry, you're a Firefox fan?
    Yeah, Safari's fine too - I just have an ineffible hunger for a physical Esc key.
    Edge? That's cool. Hm? No no, I was thinking of an unrelated thing.
    Curl fan? Right on! Just remember: the Windows one doesn't like double quotes.
    Old school, huh? Oh sure - I've got what you need right here...
    ...
    ...
    And I hear the Holiday Hack Trail game will give hints on the last screen if you complete it on Hard.

The following hints were unlocked in our badge:

.. parsed-literal::
    **Chrome Dev Tools**
    From: Kent Tinseltooth
    `Chrome Dev Tools <https://developers.google.com/web/tools/chrome-devtools>`_

.. parsed-literal::
    **Firefox Dev Tools**
    From: Kent Tinseltooth
    `Firefox Dev Tools <https://developer.mozilla.org/en-US/docs/Tools>`_

.. parsed-literal::
    **Safari Dev Tools**
    From: Kent Tinseltooth
    `Safari Dev Tools <https://developer.apple.com/safari/tools/>`_

.. parsed-literal::
    **Edge Dev Tools**
    From: Kent Tinseltooth
    `Edge Dev Tools <https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console>`_

.. parsed-literal::
    **Curl Dev Tools**
    From: Kent Tinseltooth
    `Curl Dev Tools <https://curl.haxx.se/docs/manpage.html>`_

.. parsed-literal::
    **Lynx Dev Tools**
    From: Kent Tinseltooth
    `Lynx Dev Tools <https://xkcd.com/325/>`_
    
