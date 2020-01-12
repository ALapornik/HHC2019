3) Windows Log Analysis: Evaluate Attack Outcome
================================================

Challenge
---------
We're seeing attacks against the Elf U domain! Using `the event log data <https://downloads.elfu.org/Security.evtx.zip>`_, identify the user account that the attacker compromised using a password spray attack. Bushy Evergreen is hanging out in the train station and may be able to help you out.

Answer
------
supatree

Solution
--------

.. code-block:: powershell


    PS C:\Users\Administrator>  cd .\Downloads\DeepBlueCLI-master\DeepBlueCLI-master\
    #get into the DeepBlueCLI directory

    PS C:\Users\Administrator\Downloads\DeepBlueCLI-master\DeepBlueCLI-master> Get-ExecutionPolicy
    RemoteSigned
    #DeepBlueCLI gives an error message when you run it. The reason is that the Execution Policy is too strict. Hence, set it to Bypass
    PS C:\Users\Administrator\Downloads\DeepBlueCLI-master\DeepBlueCLI-master> Set-ExecutionPolicy Bypass

    Execution Policy Change
    The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose
    you to the security risks described in the about_Execution_Policies help topic at
    https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
    [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y

    #You can now run DeepBlueCLI
    PS C:\Users\Administrator\Downloads\DeepBlueCLI-master\DeepBlueCLI-master> .\DeepBlue.ps1 .\Security.evtx\Security.evtx

    #We found multiple Password Spray Attacks
    Date    : 11/19/2019 2:22:46 PM
    Log     : Security
    EventID : 4648
    Message : Distributed Account Explicit Credential Use (Password Spray Attack)
    Results : The use of multiple user account access attempts with explicit credentials is an indicator of a password
             spray attack.
              Target Usernames: ygoldentrifle esparklesleigh hevergreen Administrator sgreenbells cjinglebuns
              tcandybaubles bbrandyleaves bevergreen lstripyleaves gchocolatewine wopenslae ltrufflefig supatree
              mstripysleigh pbrandyberry civysparkles sscarletpie ftwinklestockings cstripyfluff gcandyfluff smullingfluff
             hcandysnaps mbrandybells twinterfig civypears ygreenpie ftinseltoes smary ttinselbubbles dsparkleleaves
              Accessing Username: -
              Accessing Host Name: -

    Command :
    Decoded :


    #At the end, we found the total numbers of accounts and logon failures
    Date    : 8/24/2019 3:00:20 AM
    Log     : Security
    EventID : 4672
    Message : High number of total logon failures for multiple accounts
    Results : Total accounts: 31
              Total logon failures: 2386

    Command :
    Decoded :

    #Password Spray attack repeat until a succesful logon is achieved.
    #Hence (Total failures + 1 (=success))/Total accounts = Total password spray attacks
    #(2386+1)/31=77 failed attempts
    #Hence, we need to look for an account with one less failure (a success)

    PS C:\Users\Administrator\Downloads\DeepBlueCLI-master\DeepBlueCLI-master> .\DeepBlue.ps1 .\Security.evtx\Security.evtx | Select-String -Pattern 'Total logon failures: 76'

    @{Date=08/24/2019 03:00:20; Log=Security; EventID=4672; Message=High number of logon failures for one account;
    Results=Username: supatree
    Total logon failures: 76; Command=; Decoded=}

Hence, the affected username is **supatree**.

Hint
----
**Bushy Evergreen:**
    
    Wow, that was much easier than I'd thought.
    Maybe I don't need a clunky GUI after all!
    Have you taken a look at the password spray attack artifacts?
    I'll bet that DeepBlueCLI tool is helpful.
    You can check it out on GitHub.
    It was written by that Eric Conrad.
    He lives in Maine - not too far from here!

.. hint:: 
    Deep Blue CLI on Github
    From: Bushy Evergreen
    `Github page for DeepBlueCLI <https://github.com/sans-blue-team/DeepBlueCLI>`_

.. hint:: 
    Deep Blue CLI Posting
    From: Bushy Evergreen
    `Eric Conrad on DeepBlueCLI <https://www.ericconrad.com/2016/09/deepbluecli-powershell-module-for-hunt.html>`_