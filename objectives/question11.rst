`11) Open the Sleigh Shop Door <https://sleighworkshopdoor.elfu.org/>`_
=======================================================================

Challenge
---------

Visit **Shinny Upatree** in the **Student Union** and help solve their problem. What is written on the paper you retrieve for Shinny?

For hints on achieving this objective, please visit the *Student Union* and talk with *Kent Tinseltooth*.

Answer
------
**The Tooth Fairy**

Solution
--------

We used Google Chrome to solve this.

.. tip:: To open the Dev tools in Chrome either: Right click and choose ``inspect element``, click on ``options > More Tools > Developer Tools`` or press :kbd:`Ctrl` + :kbd:`Shift` + :kbd:`I`

.. warning:: The codes change everytime. DO NOT RELOAD while completing this challenge

.. note:: To submit the codes, click on the lock display, write them and click on unlock.


Lock 1
^^^^^^

.. image:: /images/objective11/lock1/locked.PNG

The clue refers to the console in the dev tools. Hence, open Dev tools and select the console tab. 

.. image:: /images/objective11/lock1/inspect.PNG

.. image:: /images/objective11/lock1/Console.PNG

When you scroll up (using the scroll wheel, for example) you see a code in the following form:

.. image:: /images/objective11/lock1/code.PNG



Lock 2
^^^^^^

.. image:: /images/objective11/lock2/locked.PNG

As suggested by the hints, when you click on print, you get a print preview which displays the code.

.. image:: /images/objective11/lock2/printpreview.PNG

Another way to get this is to look at the DOM tree (Inspect element)

.. image:: /images/objective11/lock2/alternative1.PNG

A nicer way to view this is to click on the display property (set to none). Removing the tick makes the code appear.

.. image:: /images/objective11/lock2/Alternative_nice_1.PNG


Lock 3
^^^^^^

.. image:: /images/objective11/lock3/locked.PNG

Open the Dev tools.

.. image:: /images/objective11/lock3/inspect.PNG

Click on Network

.. image:: /images/objective11/lock3/fetched.PNG

Look for the PNG file containing the code.

.. image:: /images/objective11/lock3/code.PNG

Lock 4
^^^^^^

.. image:: /images/objective11/lock4/locked.PNG

Open Dev Tools.

.. image:: /images/objective11/lock4/inspect.PNG

Click on Application

.. image:: /images/objective11/lock4/Application.PNG

Click on Local Storage. The code is found in the value field of the element found there.

.. image:: /images/objective11/lock4/code.PNG

Lock 5
^^^^^^

.. image:: /images/objective11/lock5/locked.PNG

We first tried the easiest suggested solution, hovering over the tab. This works for Edge but not for  

.. image:: /images/objective11/lock5/hover_nw.PNG

We then looked for the title element in the DOM tree

To do this, open Dev Tools

.. image:: /images/objective11/lock5/inspect.PNG

and scroll up to the title

.. image:: /images/objective11/lock5/domtitle.PNG

Although this method works, we also tried the Console method which appeared to be a bit cleaner

.. image:: /images/objective11/lock5/Console.PNG

Lock 6
^^^^^^

.. image:: /images/objective11/lock6/locked.PNG

Right click on the hologram and then click on inspect element. Change the perspective field to a (really) large value

.. image:: /images/objective11/lock6/perspective.PNG

The code is revealed on the hologram.

.. image:: /images/objective11/lock6/code.PNG

Lock 7
^^^^^^

.. image:: /images/objective11/lock7/locked.PNG

Right click on the text and click on inspect element. The code is found in the font property

.. image:: /images/objective11/lock7/code.PNG


Lock 8
^^^^^^

.. image:: /images/objective11/lock8/locked.PNG

Right click .eggs and inpect element

.. image:: /images/objective11/lock8/inspect.PNG

click on Event listeners. There is an event called spoil

.. image:: /images/objective11/lock8/spoil.PNG

start expanding this event, until you see ``='sad'``

.. image:: /images/objective11/lock8/code.PNG

``VERONICA`` is the code and doesn't change if you refresh.

Lock 9
^^^^^^

.. image:: /images/objective11/lock9/locked.PNG

Right click on the text, inspect element. We can see 5 chakra classes.

.. image:: /images/objective11/lock9/inactive_chakras.PNG

find the active attribute (click on ``:hov``)

.. image:: /images/objective11/lock9/active.PNG

click on the tick box next to ``:active``, repeat for all chackras

.. image:: /images/objective11/lock9/all_active.PNG

The code appears around the text with red letters

.. image:: /images/objective11/lock9/code.PNG

.. tip:: You can see the hidden text instantaneously by clicking on it.


Lock 10
^^^^^^^

.. image:: /images/objective11/lock10/locked.PNG

Right click on the cover, Inspect element

.. image:: /images/objective11/lock10/cover_found.PNG

select the cover element, right click and delete/hide it

.. image:: /images/objective11/lock10/cover_off.PNG

You can see the code ``KD29XJ37`` on the edge of the circuit board.

However, when you try to input the code, the button doesn't work.
Instead, an error (``missing macaroni``) is shown in the console

.. image:: /images/objective11/lock10/1macaroni/macaronierror.PNG

Searching in the DOM tree reveals an element called ``component macaroni``

.. image:: /images/objective11/lock10/1macaroni/componentfound.PNG

When you drag it down to lock 10, a macaroni appears.

.. image:: /images/objective11/lock10/1macaroni/result.PNG

Repeat the process until you have all components (you'll get a ``missing cotton swab`` error followed by a ``missing gnome`` error)

.. image:: /images/objective11/lock10/2swab/swaberror.PNG

.. image:: /images/objective11/lock10/2swab/componentfound.PNG

.. image:: /images/objective11/lock10/2swab/result.PNG

.. tip:: You can find the images in the sources tab. Curiously, the cotton swab is named qtip


.. image:: /images/objective11/lock10/3gnome/gnomeerror.PNG

.. image:: /images/objective11/lock10/3gnome/componentfound.PNG

.. image:: /images/objective11/lock10/3gnome/result.PNG

Result
^^^^^^

Once all codes are found and all locks are unlocked, you are redirected to the following result page:

.. image:: /images/objective11/result.PNG

In the console, the page challenges you to solve it faster

.. image:: /images/objective11/result_console.PNG

We couldn't resist a nice chalenge and eventually got a time of 172.35s

.. image:: /images/objective11/The_Quickness.PNG

This time the challenge was much harder

.. image:: /images/objective11/CHALLENGE2.PNG

Hint
----

.. note:: Solve the `Smart Braces </terminals/SmartBraces>`_ terminal to get this hint


**Kent Tinseltooth**

    Oh thank you! It's so nice to be back in my own head again. Er, alone.

    By the way, have you tried to get into the crate in the Student Union? It has an interesting set of locks.

    There are funny rhymes, references to perspective, and odd mentions of eggs!

    And if you think the stuff in your browser looks strange, you should see the page source...

    Special tools? No, I don't think you'll need any extra tooling for those locks.

    BUT - I'm pretty sure you'll need to use *Chrome's developer tools* for that one.

    Or sorry, you're a *Firefox* fan?

    Yeah, *Safari*'s fine too - I just have an ineffible hunger for a physical Esc key.

    *Edge*? That's cool. Hm? No no, I was thinking of an unrelated thing.

    *Curl* fan? Right on! Just remember: the Windows one doesn't like double quotes.

    Old school, huh? Oh sure - I've got what you need right here...

.. hint::
    **Chrome Dev Tools**

    *From: Kent Tinseltooth*

    `Chrome Dev Tools <https://developers.google.com/web/tools/chrome-devtools>`_

.. hint::
    **Firefox Dev Tools**

    *From: Kent Tinseltooth*

    `Firefox Dev Tools <https://developer.mozilla.org/en-US/docs/Tools>`_

.. hint:: 
    **Safari Dev Tools**

    *From: Kent Tinseltooth*

    `Safari Dev Tools <https://developer.apple.com/safari/tools/>`_

.. hint::
    **Edge Dev Tools**

    *From: Kent Tinseltooth*

    `Edge Dev Tools <https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console>`_

.. hint::
    **Curl Dev Tools**

    *From: Kent Tinseltooth*

    `Curl Dev Tools <https://curl.haxx.se/docs/manpage.html>`_

.. hint:: 
    **Lynx Dev Tools**

    *From: Kent Tinseltooth*
    
    `Lynx Dev Tools <https://xkcd.com/325/>`_
    