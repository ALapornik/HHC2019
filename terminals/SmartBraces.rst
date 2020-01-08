`Smart Braces <https://docker2019.kringlecon.com/?challenge=iptables>`_
=======================================================================

.. code-block:: none

    
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
    elfuuser@4a5f0c68d90a:~$ 
    
``nano /home/elfuuser/IOTteethBraces.md``

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