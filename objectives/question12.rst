12) Filter Out Poisoned Sources of Weather Data
===============================================
Challenge
---------
Difficulty: 4/5

Use the data supplied in the Zeek JSON logs to identify the IP addresses of attackers poisoning Santa's flight mapping software. Block the 100 offending sources of information to guide Santa's sleigh through the attack. Submit the Route ID ("RID") success value that you're given. For hints on achieving this objective, please visit the Sleigh Shop and talk with Wunorse Openslae.

Answer
------

1. Discovery
^^^^^^^^^^^^
To solve this challenge we had to analyse the supplied Zeek JSON logs and determine the IP addresses of approximately 100 sources performing the following classes of attacks:

* **SQLi** - the insertion of a SQL query via the input stream from the client to the application
* **XSS** - attacks where a malicious script is inserted into otherwise benign and trusted websites
* **LFI** - attacks that include files on the local server that is being attacked
* **Shell Shock** - attacks that exploit vulberabilities in the Bash shell

In addition we had to pivot on some of these sources to find additional sources.

The hints mention the use of the JQ tool to analyse the logs.

.. note::
    JQ is a lightweight and flexible command-line JSON processor that can be downloaded from the `https://github.com/stedolan/jq <https://github.com/stedolan/jq>`_ repository.

We had to enter all of these sources (approximately 100), as a string of comma separated IP addresses, into the firewall section of the supplied `Sleigh Route Finder API <https://srf.elfu.org>`_.

A secondary challenge was to find the username/password for the API.

The main difficulties with this challenge included the uncertainty behind exactly what to match in our queries, the various querks with the JQ tool, and the uncertainty about where to find the username/password.

Starting artefacts
""""""""""""""""""
* `Zeek JSON logs <https://downloads.elfu.org/http.log.gz>`_ 

2. Solving the challenge
^^^^^^^^^^^^^^^^^^^^^^^^

 