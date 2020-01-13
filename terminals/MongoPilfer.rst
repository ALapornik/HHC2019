`Mongo Pilfer <https://docker2019.kringlecon.com/?challenge=mongo&id=f1a2f647-4e3a-467f-b7bc-62c294fe6780>`_
============================================================================================================

Challenge
---------
The initial dialog with Holly Evergreen:

.. parsed-literal::
    **Holly Evergreen**
    Without access to the answer, none of our quizzes will get graded.
    Can we help get back in to find that solution?
    I tried lsof -i, but that tool doesn't seem to be installed.
    I think there's a tool like ps that'll help too. What are the flags I need?
    Either way, you'll need to know a teensy bit of Mongo once you're in.
    Pretty please find us the solution to the quiz!

The hint from our badge:

.. parsed-literal::
    **MongoDB**
    From: Holly Evergreen
    `MongoDB Documentation <https://docs.mongodb.com/manual/reference/command/listDatabases/#dbcmd.listDatabases>`_

The banner page from the terminal challenge:

.. image:: /images/mongopilfer-banner.png

Solution
--------
We used the following command to determine the port on which mongo was running:

``ps -AF``

We obtained the following output:

.. code-block::
    :emphasize-lines: 3

    UID        PID  PPID  C    SZ   RSS PSR STIME TTY          TIME CMD
    elf          1     0  0  4627  3572   9 19:36 pts/0    00:00:00 /bin/bash
    mongo        9     1  0 253905 62704  0 19:36 ?        00:00:01 /usr/bin/mongod --quiet --fork --port 12121 --bind_ip 127.0.0.1 --logpath=/tmp/mongo.log
    elf         48     1  0  8600  2880   0 19:40 pts/0    00:00:00 ps -AF

We connected to the MongoDB instance using the following command:

``mongo --port 12121``

We then ran the following command to list the databases:

``db.adminCommand( { listDatabases: 1 } )``

This produced the following output:

.. code-block::
    :emphasize-lines: 14

    {
        "databases" : [
            {
                "name" : "admin",
                "sizeOnDisk" : 32768,
                "empty" : false
            },
            {
                "name" : "config",
                "sizeOnDisk" : 12288,
                "empty" : false
            },
            {
                "name" : "elfu",
                "sizeOnDisk" : 294912,
                "empty" : false
            },
            {
                "name" : "local",
                "sizeOnDisk" : 65536,
                "empty" : false
            },
            {
                "name" : "test",
                "sizeOnDisk" : 32768,
                "empty" : false
            }
        ],
        "totalSize" : 438272,
        "ok" : 1
    }

The **elfu** database is probably the one we are interested in. We then run the following commands to determine the **collections** in the **elfu** database. 

.. note::
    Collections are analogous to tables in SQL databases.

``use elfu``

``db.runCommand( { listCollections: 1}``

We obtained the following output (truncated to show information of interest):

.. code-block::
    :emphasize-lines: 2

    {
        "name" : "solution",
        "type" : "collection",
        "options" : {
                    },
        "info" : {
                    "readOnly" : false,
                    "uuid" : UUID("67643830-b324-4995-8507-a7e21a65c7a5")
                    },
        "idIndex" : {
                        "v" : 2,
                        "key" : {
                                    "_id" : 1
                                },
                        "name" : "_id_",
                        "ns" : "elfu.solution"
                    }
    },

We then run the following command to return all documents in the **solution** collection.

``db.solution.find({})``

.. note::
    The above command corresponds to the following command in an SQL database:

    SELECT * FROM solution

We obtain the following output:

.. code-block::

    { "_id" : "You did good! Just run the command between the stars: ** db.loadServerScripts();displaySolution(); **" }

We then run the following command to solve the challenge:

``db.loadServerScripts();displaySolution();``

We get the following message:

.. code-block::

          .
       __/ __
            /
       /.'*'. 
        .o.'.
       .'.'*'.
      *'.*.'.o.
     .'.*.'.'.*.
    .o.'.*.'.*.'.
       [_____]
        ___/


  Congratulations!!


Hints
-----
Holly Evergreen provides the following hint in her dialog after solving the terminal challenge:

.. parsed-literal::
    **Holly Evergreen**
    Woohoo! Fantabulous! I'll be the coolest elf in class.
    On a completely unrelated note, digital rights management can bring a hacking elf down.
    That ElfScrow one can really be a hassle.
    It's a good thing Ron Bowes is giving a talk on reverse engineering!
    That guy knows how to rip a thing apart. It's like he breathes opcodes!

The following hint was unlocked in our badge:

.. parsed-literal::
    **Reverse Engineering**
    From: Holly Evergreen
    `Reversing Crypto the Easy Way <https://youtu.be/obJdpKDpFBA>`_
