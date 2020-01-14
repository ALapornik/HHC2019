6) Splunk
=========

Challenge
---------

Access `https:/splunk.elfu.org/ <https:/splunk.elfu.org/>`_ as elf with password elfsocks. What was the message for Kent that the adversary embedded in this attack? The SOC folks at that link will help you along! For hints on achieving this objective, please visit the Laboratory in Hermey Hall and talk with Prof. Banas.

Answer
------

Challenge Question Answer
^^^^^^^^^^^^^^^^^^^^^^^^^

What was the message for Kent that the adversary embedded in this attack?	

    Kent you are so unfair. And we were going to make you the king of the Winter Carnival.

Training Questions Answers
^^^^^^^^^^^^^^^^^^^^^^^^^^

1.	What is the short host name of Professor Banas' computer?		

    sweetums

2.	What is the name of the sensitive file that was likely accessed and copied by the attacker? Please provide the fully qualified location of the file. (Example: C:\\temp\\report.pdf)		

    C:\\Users\\cbanas\\Documents\\Naughty_and_Nice_2019_draft.txt

3.	What is the fully-qualified domain name(FQDN) of the command and control(C2) server? (Example: badguy.baddies.com)		

    144.202.46.214.vultr.com

4.	What document is involved with launching the malicious PowerShell code? Please provide just the filename. (Example: results.txt)		

    19th Century Holiday Cheer Assignment.docm

5.	How many unique email addresses were used to send Holiday Cheer essays to Professor Banas? Please provide the numeric value. (Example: 1)		

    21

6.	What was the password for the zip archive that contained the suspicious file?		

    123456789

7.	What email address did the suspicious file come from?		

    bradly.buttercups@eifu.org

Solution
--------

Logon to splunk using the following credentials:

Username: ``elf``   Password: ``********`` [1]_

Welcome message
^^^^^^^^^^^^^^^

    **The Search for Holiday Cheer Challenge**

    1. Your goal is to answer the Challenge Question. You will include the answer to this question in your HHC write-up!
    
    2. You do not need to answer the training questions. You may simply search through the Elf U SOC data to find the answer to the final question on your own.
    
    3. If you need some guidance, answer the training questions! Each one will help you get closer to the answering the Challenge Question.
    
    4. Characters in the SOC Secure Chat are there to help you. If you see a blinking red dot next to a character, click on them and read the chat history to learn what they have to teach you! And don't forget to scroll up in the chat history!
    
    5. To search the SOC data, just click the Search link in the navigation bar in the upper left hand corner of the page.
    
    6. This challenge is best enjoyed on a laptop or desktop computer with screen width of 1600 pixels or more.
    
    7. **WARNING** This is a defensive challenge. Do not attack this system, web application, or back-end APIs. Thank you!

Training Questions
^^^^^^^^^^^^^^^^^^

.. parsed-literal::
    **Kent**

    **Guest (me) :** Hi Kent :-)
    **Kent :** Hi yourself.
    **Guest (me) :** I ran into Professor Banas. He said you contacted him about his computer being hacked?
    **Kent :** Oh, well lots of analysts try to make it here in the ELF U SOC, but most of them crack under the pressure
    **Guest (me) :** Well, can I help?
    **Kent :** You can try. Go check out #ELFU SOC. Maybe someone there will have time to bring you up to speed. Here's a tip, click on those blinking red dots to the left column and read very carefully.
    **Guest (me) :** Thanks???


.. parsed-literal::
    **#ELFU SOC**

    **Cosmo Jingleberg :** Hey did you all see that beaconing detection from RITA?
    **Zippy Frostington :** Yep. And we have some system called '**sweetums**' here on campus communicating with the same weird IP
    **Alice Bluebird :** Gah... that's Professor Banas' system from over in the Polar Studies department
    **Guest (me) :** That's why I'm here, actually...Kent sent me to this channel to help with Prof. Banas' system
    **Alice Bluebird :** smh...I'll DM you

.. parsed-literal::
    **Alice Bluebird**

    **Alice Bluebird :** hey hey...
    **Guest (me) :** Hiya Alice
    **Alice Bluebird :** I see you've met Kent
    **Guest (me) :** briefly. He seems...frustrated
    **Alice Bluebird :** Pretty accurate. He's been here a long time and he struts around like some sort of cyber-peacock
    **Alice Bluebird :** Some time (preferably over good eggnog) I'll tell you about his horrible opsec, too
    **Alice Bluebird :** Suffice to say we have adversaries poking fun at him during attacks. JML
    **Guest (me) :** JML?
    **Alice Bluebird :** jingle my life
    **Guest (me) :** LOL!
    **Alice Bluebird :** So Cosmo, Zippy, and I have a good handle on what went down with Professor B's system
    **Guest (me) :** ah, gotcha
    **Alice Bluebird :** But we can always use good analysts here in the SOC, so if you can figure it out, we'll put in a good word with the boss of the SOC.
    **Guest (me) :** Let's do this!
    **Alice Bluebird :** Okay. Your goal is to find the message for Kent that the adversary embedded in this attack.
    **Alice Bluebird :** If you think you have the chops for that, don't let me slow you down. Get searching and enter the Challenge Question answer when you've found it.
    **Alice Bluebird :** You'll need to know some things, though:
        1. We use Splunk, so click `here <https://splunk.elfu.org/en-US/app/SA-elfusoc/search>`_ or hit the Search link in the navigation up above to get started.
        2. I copied some raw files `here <http://elfu-soc.s3-website-us-east-1.amazonaws.com/>`_ or click the File Archive link in the navigation. (You'll find some references to the File Archive contents in Splunk)
        **You'll need to use both of these resources to answer the Challenge Question!**
    **Alice Bluebird :** Don't worry though, I can get you started down the right path with a few hints if you need 'em. All you have to do is answer the first training question. If you've read all the chat windows here, you already have the answer ;-)

**Training Question 1 Answer:** In #ELFU SOC we found out that **sweetums** was the name of Prof. Banas' system.

----

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : Training Question 1 Answered Correctly**
    **Guest (me) :** Boom, first one done.
    **Alice Bluebird :** Oh good, you read the #ELFU SOC chat :-)
    **Alice Bluebird :** I jest :-) Okay check out the next question. You'll need to actually search for the answer this time.
    **Alice Bluebird :** You may not know this, but Professor Banas is pretty close to the big guy.
    **Guest (me) :** Santa?
    **Alice Bluebird :** Yep. This is why we keep detailed logs from Professor B's machine
    **Guest (me) :** I didn't know Banas was inner-circle... But then again, why would I know that?
    **Alice Bluebird :** Well he is and the adversaries know it. They are always attacking him and the Elf U network trying to get to Santa.
    **Alice Bluebird :** Our very first worry was they may have found some of Santa's sensitive data.
    **Guest (me) :** Did they?
    **Alice Bluebird :** That's what you need to tell me!
    **Alice Bluebird :** I'll give you a tip. Sometimes simpler is better. If you have a word that you are really interested in, just start searching for it. Here is an example of searching for `the professor's username <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20cbanas&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`
    **Alice Bluebird :** It's not a very precise search technique, but it can provide context and get you started.
    **Guest (me) :** nods
    **Alice Bluebird :** Use that technique (with a different search term) to answer question 2.
    **Guest (me) :** I'm struggling with what to search for. Maybe I should search for "sweetums"
    **Alice Bluebird :** Well, I just told you who we were most worried about protecting. Maybe start with his name! Also, sweetums is a good thought, but this is a training exercise and pretty much all the data pertains to that one host already so just searching for that may not get you far.

**Training Question 2 Answer:** After viewing the linked query (``index=main cbanas``), we tried using ``index=main santa``. We found that the sensitive file path was: **C:\\Users\\cbanas\\Documents\\Naughty_and_Nice_2019_draft.txt**

.. image:: /images/splunk/tq2.PNG

----

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : Training Question 2 Answered Correctly**
    **Alice Bluebird :** Okay that was a good warmup. FYI, Here's `the search I'd have used for that last one <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20santa&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`_.
    **Alice Bluebird :** Why he had a draft copy of this year's naughty and nice list sitting on his PC, I'll never know.
    **Alice Bluebird :** Did you see the download of the scanning tool, too? That's interesting, but let's stay on task here.
    **Guest (me) :** That was pretty easy...
    **Alice Bluebird :** Well, you'll need to do a lot more than super-grep for Santa Claus to work in this SOC.
    **Guest (me) :** haha understood
    **Alice Bluebird :** You probably noticed right away that the attack used PowerShell. I need you to tell me the fully qualified domain name (FQDN) used for command and control.
    **Alice Bluebird :** Use Microsoft Sysmon data to answer this question. Here's some `background on Sysmon <https://www.splunk.com/en_us/blog/security/a-salacious-soliloquy-on-sysmon.html>`_ if you need it.
    **Alice Bluebird :** To search Sysmon data in our system, start by specifying the sourcetype using a search like `sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3DXmlWinEventLog%3AMicrosoft-Windows-Sysmon%2FOperational&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`_
    **Alice Bluebird :** In Sysmon, Event Code 3 represents network connections and you can narrow your search by adding the term 'powershell'. There is an implied boolean AND operator between any search terms that you add. Try to narrow your search to include these terms.
    **Alice Bluebird :** Your search should look something like this `sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational powershell EventCode=3 <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3DXmlWinEventLog%3AMicrosoft-Windows-Sysmon%2FOperational%20powershell%20EventCode%3D3&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`_
    **Alice Bluebird :** Look through the lists of **Interesting Fields** and **Selected Fields** in the left-hand column of the search window. You should find what you are looking for there.

**Training Question 3 Answer:** Using the provided query (``index=main sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational powershell EventCode=3``), click on either: 
``DestinationHostname`` in Selected Fields or ``dest`` or ``dest_host`` in Interesting Fields to find the FDQN under Value: **144.202.46.214.vultr.com**

.. image:: /images/splunk/tq3.PNG

----

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : Training Question 3 Answered Correctly**
    **Alice Bluebird :** Well done.
    **Guest (me) :** Thanks
    **Alice Bluebird :** Let's investigate where all this PowerShell originated. You should start by running `this search <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3D%22WinEventLog%3AMicrosoft-Windows-Powershell%2FOperational%22&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`_ to view all the PowerShell logs on the system.
    **Guest (me) :** Searching now. What am I looking for?
    **Alice Bluebird :** We'd like to determine the process ID or process GUID associated with these PowerShell logs, but that information is not included in the events we have.
    **Guest (me) :** Ah, dead-end then?
    **Alice Bluebird :** Goodness no! We just need to pivot.
    **Guest (me) :** On what though?
    **Alice Bluebird :** We can pivot on...time.
    **Guest (me) :** whoa...
    **Alice Bluebird :** First off, flip the results of that last search so the oldest event is at the top of the list `by adding | reverse to the end <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3D%22WinEventLog%3AMicrosoft-Windows-Powershell%2FOperational%22%20%7C%20reverse&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=now&display.general.type=events&display.page.search.tab=events>`_
    **Guest (me) :** pipe reverse. That's handy.
    **Alice Bluebird :** Indeed. Okay, this is where we pivot...
    **Alice Bluebird :** Look at the **Time** column in your search results. If you click on the date/timestamp from that first event, you can specify a time window. Accept the default of +/- five seconds and click apply. Then remove the **sourcetype** search term and also remove the **'| reverse'** and re-run the search.
    **Guest (me) :** Well now I see lots of different types of events from that ten-second window.
    **Alice Bluebird :** Try to find a process ID of interest. Sysmon events are good for that. You should be able to find two different process IDs from Sysmon events in that time window...
    **Alice Bluebird :** You need to uncover what launched those processes. If Sysmon Event Code 1 results are not available, try looking for Windows Process Execution events (Event ID 4688). A search to get you started with 4688 logs is `sourcetype=WinEventLog EventCode=4688 <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3DWinEventLog%20EventCode%3D4688&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=&display.general.type=events&display.page.search.tab=events&display.events.fields=%5B>`_
    **Alice Bluebird :** Keep in mind that 4688 events record process IDs in hexadecimal, so you may need to do some conversion. Remember you should have a couple of process IDs that are interesting. Convert them to hex and search away in the 4688 events. Oh and at this point (when you are searching for 4688 events) go ahead and set your time window back to all time so you don't miss anything.
    **Guest (me) :** Uhh, this one is pretty difficult.
    **Alice Bluebird :** Yep, if the above is not clear, you may want to check out a KringleCon 2 talk by James Brodsky that covers this topic in detail.
    **Alice Bluebird :** You're looking for a "document" that appears to be involved with kicking off all this PowerShell.

**Training Question 4 Answer:** Using the given query (``index=main sourcetype="WinEventLog:Microsoft-Windows-Powershell/Operational" | reverse``) and click on the first time value.

.. image:: /images/splunk/tq4a.PNG

Then, set the span to +/- 5 seconds.

.. image:: /images/splunk/tq4b.PNG

Edit the query to ``index=main``

Find the ``ProcessId`` field

.. image:: /images/splunk/tq4c.PNG

Set Time to AllTime

Search for the found PID (converted to hex)

Use the Queries: 

``index=main sourcetype=WinEventLog EventCode=4688 process_id=0x187c *doc*``

and

``index=main sourcetype=WinEventLog EventCode=4688 process_id=0x16e8 *doc*``

to find the document path.

The answer can be found in the ``Body`` and in ``Process_Command_Line`` as the last part of the path.

The answer is **19th Century Holiday Cheer Assignment.docm**

----

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : Training Question 4 Answered Correctly**
    **Alice Bluebird :** Good job. Malicious Word doc...
    **Guest (me) :** yeah...So you want me to find out where it came from?
    **Alice Bluebird :** Yes. You've heard of stoQ right?
    **Guest (me) :** umm....
    **Alice Bluebird :** Well, it's the coolest open source security tool you've probably never heard of.
    **Alice Bluebird :** It's an automation framework that we use to analyze all email messages at Elf U. Check out `the stoQ project home page <https://stoq.punchcyber.com/>`_. Oh and here are slides from a `talk on stoQ <https://www.sans.org/cyber-security-summit/archives/file/summit_archive_1492181136.pdf>`_ from the SANS DFIR Summit a few years back.
    **Guest (me) :** neat!
    **Alice Bluebird :** stoQ output is in JSON format, and we store that in our log management platform. It allows you to run `powerful searches like this one <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3Dstoq%20%7C%20table%20_time%20results%7B%7D.workers.smtp.to%20results%7B%7D.workers.smtp.from%20%20results%7B%7D.workers.smtp.subject%20results%7B%7D.workers.smtp.body%20%7C%20sort%20-%20_time&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=&display.general.type=statistics&display.page.search.tab=statistics&display.events.fields=%5B>`_. Check out those strange-looking field names like **results{}.workers.smtp.subject**. That's how JSON data looks in our search system, and stoQ events are made up of some fairly deeply nested JSON. Just keep that in mind.
    **Alice Bluebird :** Okay, time for you to play around with that search and answer the question. You should be aware that Professor Banas was very clear in his instructions to his students: All assignment submissions must be made via email and **must** have the subject 'Holiday Cheer Assignment Submission'. Remember email addresses are not case sensitive so don't double-count them!

**Training Question 5 Answer:** Edit the given query to search for the subject "Holiday Cheer Assignment". The answer is the number of results, and can be seen in brackets next to statistics. 

The query we used was ``index=main sourcetype=stoq  results{}.workers.smtp.subject="Holiday Cheer Assignment Submission" | table _time results{}.workers.smtp.to results{}.workers.smtp.from  results{}.workers.smtp.subject results{}.workers.smtp.body | sort - _time``

.. image:: /images/splunk/tq5.PNG

In this case, there are **21** results.

----

.. parsed-literal::
    **Alice Bluebird**

    **TrainingBOT : Training Question 5 Answered Correctly**
    **Alice Bluebird :** Nice, you are getting the hang of this.
    **Guest (me) :** It's fun!
    **Alice Bluebird :** The attacker used MITRE ATT&CK Technique 1193 in their attack on Professor Banas.
    **Guest (me) :** mmmmm hmmmm
    **Alice Bluebird :** This one should be easy for you. Just use what you already know about the suspicious file name you identified, and about the type of visibility that stoQ gives you...

**Training Question 6 Answer:** Although the same query can be used, It's easy to search for the password. Just use the following query:
``index=main sourcetype=stoq  results{}.workers.smtp.body="*password*" | table  results{}.workers.smtp.body | sort - _time``

.. image:: /images/splunk/tq6.PNG

The password is **123456789** as seen in the message.

----

.. parsed-literal::
    **Alice Bluebird**

    **TrainingBOT : Training Question 6 Answered Correctly**
    **Alice Bluebird :** Good.
    **Guest (me) :** Can stoQ deal with password-protected zip attachments like that one?
    **Alice Bluebird :** It can! It tries a list of common passwords, and the attacker chose one that was on the list.
    **Guest (me) :** Sweet
    **Alice Bluebird :** Here's another easy one for you...

**Training Question 7 Answer:** For this question, just edit the previous query to output the ``from`` field. The email **bradly.buttercups@eifu.org** is found. Notice that the domain is eifu.org, not elfu.org

.. image:: /images/splunk/tq7.PNG

Challenge Question
^^^^^^^^^^^^^^^^^^

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : Training Question 7 Answered Correctly**
    **Alice Bluebird :** Well, now you are ready to find the message that the attacker embedded for our friend Kent.
    **Alice Bluebird :** Kent missed it, which is not surprising, but Zippy noticed a funny (yet terrifying) message in the properties of the malicious document.
    **Guest (me) :** Hmmm. I was going to start looking through the macros.
    **Alice Bluebird :** Look, I was not about to put the actual malicious executable content into this training exercise.
    **Guest (me) :** Oh, understood. I will dig for properties.
    **Alice Bluebird :** Remember I provided you with a `File Archive <http://elfu-soc.s3-website-us-east-1.amazonaws.com/>`_. stoQ puts metadata into the log management platform, but it stores the raw artifacts in their entirety in the archive. Use the stoQ events in the search platform to guide your search through the File Archive.
    **Alice Bluebird :** `Start with this stoQ event <https://splunk.elfu.org/en-US/app/SA-elfusoc/search?q=search%20index%3Dmain%20sourcetype%3Dstoq%20%20%22results%7B%7D.workers.smtp.from%22%3D%22bradly%20buttercups%20%3Cbradly.buttercups%40eifu.org%3E%22&display.page.search.mode=smart&dispatch.sample_ratio=1&earliest=0&latest=&display.general.type=events&display.page.search.tab=events&display.events.fields=%5B>`_
    **Alice Bluebird :** Look in the 'results' array. Each element contains the name of the file that stoQ extracted in the 'results->payload_meta->extra_data->filename' field. And when you find one of interest, use the associated 'results->archivers->filedir->path' field to guide you through the File Archive.
    **Guest (me) :** Uhhh okay. But that JSON event is a beast. So many 'results'!
    **Alice Bluebird :** Yeah but you can use it to your advantage with the Splunk spath command. Add this to the end of that last search I provided.
        | eval results = spath(_raw, "results{}") 
        | mvexpand results
        | eval path=spath(results, "archivers.filedir.path"), filename=spath(results, "payload_meta.extra_data.filename"), fullpath=path."/".filename 
        | search fullpath!="" 
        | table filename,fullpath
    **Alice Bluebird :** Last thing for you today: Did you know that modern Word documents are (at their **core**) nothing more than a bunch of .xml files?
    **Guest (me) :** haha! I'm on it.

Using the provided query:

    index=main sourcetype=stoq  "results{}.workers.smtp.from"="bradly buttercups <bradly.buttercups@eifu.org>" | eval results = spath(_raw, "results{}") 
    | mvexpand results
    | eval path=spath(results, "archivers.filedir.path"), filename=spath(results, "payload_meta.extra_data.filename"), fullpath=path."/".filename 
    | search filename="core.xml"
    | table filename,fullpath

We can find the address of core.xml in the archive

.. image:: /images/splunk/challenge-search.PNG


Find the file in the archive, download and open it in notepad

.. image:: /images/splunk/Archive.PNG


Content:

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Holiday Cheer Assignment</dc:title><dc:subject>19th Century Cheer</dc:subject><dc:creator>Bradly Buttercups</dc:creator><cp:keywords></cp:keywords><dc:description>Kent you are so unfair. And we were going to make you the king of the Winter Carnival.</dc:description><cp:lastModifiedBy>Tim Edwards</cp:lastModifiedBy><cp:revision>4</cp:revision><dcterms:created xsi:type="dcterms:W3CDTF">2019-11-19T14:54:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2019-11-19T17:50:00Z</dcterms:modified><cp:category></cp:category></cp:coreProperties>

**Challenge Question Answer:** **Kent you are so unfair. And we were going to make you the king of the Winter Carnival.**

Additional Content
^^^^^^^^^^^^^^^^^^

After the Main Challenge is solved, some more messages appear

.. parsed-literal::
    **Alice Bluebird**

    **Training BOT : CHALLENGE QUESTION Answered Correctly**
    **Alice Bluebird :** Oh nice job on the challenge question!
    **Guest (me) :** Thx! And thanks for all the help :-)
    **Alice Bluebird :** No worries. Steep learning curve around here.
    **Alice Bluebird :** I'll put in a good word for you with the boss of the SOC.
    **Alice Bluebird :** and feel free to poke around more. There's fun stuff in the data that I did not guide you to.
    **Guest (me) :** Oh cool I may do that...but do you think it's getting too weird around here?
    **Alice Bluebird :** Absolutely

.. parsed-literal::
    **Kent**

    **Guest (me) :** Oh man that's pretty embarrassing, eh?
    **Kent :** Oh you again?
    **Guest (me) :** lulz...
        Kent you are so unfair. And we were going to make you the king of the Winter Carnival.
    **Kent :** You'll rue the day.
    **Guest (me) :** Who talks like that?

Message:

    Congratulations!
    You found the message from the attacker. Be sure to record it somewhere safe for your writeup! Oh, and feel free to poke around here as long as you'd like!


Hint
----

**Professor Banas:**
    Hi, I'm Dr. Banas, professor of Cheerology at Elf University.
    This term, I'm teaching "HOL 404: The Search for Holiday Cheer in Popular Culture," and I've had quite a shock!
    I was at home enjoying a nice cup of Gløgg when I had a call from Kent, one of my students who interns at the Elf U SOC.
    Kent said that my computer has been hacking other computers on campus and that I needed to fix it ASAP!
    If I don't, he will have to report the incident to the boss of the SOC.
    Apparently, I can find out more information from this website https://splunk.elfu.org/ with the username: elf / Password: elfsocks.
    I don't know anything about computer security. Can you please help me?

.. note:: 

    No hint is given by Prof Banas. However, Alice Bluebird guides you through the challenge once you log on.


.. rubric:: Footnotes

.. [1] elfsocks
