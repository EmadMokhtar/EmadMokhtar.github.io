Coding For Fun: Get Now Playing from Last.FM
############################################
:date: 2010-10-25 07:15
:author: admin
:category: .net, C#
:slug: coding-for-fun-get-now-playing-from-last-fm
:status: published

|Last.fm\_Logo\_Red|

Let’s first know What is Last.FM?

    Last.fm is a music recommendation service. You use Last.fm by
    signing up and downloading The Scrobbler, which helps you discover
    more music based on the songs you play.

    What’s Scrobbling? A scrobble is a little note The Scrobbler sends
    to Last.fm to let us know what song you’re playing. Scrobbling helps
    us tell you what songs you play most often, which songs you like the
    most, how much you’ve played an artist over a certain amount of
    time, which of your friends have similar tastes… all kinds of stuff.
    By focusing on the music you already play we can help you discover
    more music.

    What you get? Scrobbles mean we can deliver personalized
    recommendations for every single Last.fm listener, every single day.
    We compare what you play to the scrobbles of millions of listeners
    around the world, meaning your recommendations are the result of
    more than 43 billion scrobbles and counting. There’s plenty more you
    can do with Last.fm too. By getting involved in our community you
    can tag tracks, join discussions, learn what’s hot and find new ways
    of uncovering the secrets of your listening history.

For myself I use it to let my friends know what I’m listening to:

|Last.fm3|

Yes I still using Winamp, and sometimes Zune software.

**What do you need to scrobbling to Last.FM:**

#. Last.FM account, get one from `here <http://www.last.fm/join>`__.
#. Download `Last.FM software <http://www.last.fm/download>`__, don’t
   worry it’ll detect all media player in your system and install the
   plug-in for them.

So for fun I use their API to get what I’m listening to, and this what
we will do later, but first we need to `apply for an API
account <http://www.last.fm/api/account>`__

|Last.fm1|

After getting your API key and secret, save them to use them in coding
later.

Last thing we need before coding, the C# Interface for Last.FM
`Last.FM# <http://code.google.com/p/lastfm-sharp/>`__, go to the link
and download “lastfm-sharp-0.1.10-bin.tar.gz” file and extract it, and
we’ll use “lastfm-sharp.dll” file in our project.

Now let’s code and have some fun |Winking smile| we need to “Add
Reference” to our project,

|google translation2|

browse to “lastfm-sharp.dll” file and add it to the project.

Here’s the code snippet for getting what “EmadMokhtar” last.fm user
listening to:

.. code:: brush:

    using System;
    using Lastfm.Services;

    namespace LastFMcurrentPlayingSongCS
    {
        class Program
        {
            static void Main(string[] args)
            {
                //Set the API KEY & SECRET
                string apiKEY = "Put your API Key here";
                string apiSECRET = "Put your Secert here";
                Session session = new Session(apiKEY, apiSECRET);

                //Set the user to EmadMokhtar (http://www.last.fm/user/emadmokhtar)
                var user = new User("EmadMokhtar", session);

                //Get the now play from Last.FM
                string nowPlaying = user.GetNowPlaying().ToString();

                // Display The now playing track info
                Console.WriteLine(nowPlaying);
                Console.ReadLine();
            }
        }
    }

and here’s a screenshot to what I was listening to:

|Last.fm2|

    Tip: If you’ll use Zune software, there’s no plugin for it, but
    don’t worry there’s a solution for it download
    `Zuse <http://zusefm.org/>`__.

Source Files:

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:f3178255-386d-4966-9559-cbaca04a5625"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

del.icio.us Tags:
`Last.fm <http://del.icio.us/popular/Last.fm>`__,\ `music <http://del.icio.us/popular/music>`__

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:3c2aba9e-d999-4f6f-8087-90c327d2153f"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

Technorati Tags:
`coding <http://technorati.com/tags/coding>`__,\ `codeforfun <http://technorati.com/tags/codeforfun>`__,\ `music <http://technorati.com/tags/music>`__

.. raw:: html

   </div>

.. |Last.fm\_Logo\_Red| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm_Logo_Red_thumb.jpg
   :width: 244px
   :height: 76px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm_Logo_Red_2.jpg
.. |Last.fm3| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm3_thumb.jpg
   :width: 754px
   :height: 768px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm3.jpg
.. |Last.fm1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm1_thumb.jpg
   :width: 644px
   :height: 124px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm1.jpg
.. |Winking smile| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/wlEmoticon-winkingsmile_2.png
   :class: wlEmoticon wlEmoticon-winkingsmile
.. |google translation2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation2_thumb.jpg
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation2.jpg
.. |Last.fm2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm2_thumb_2.jpg
   :width: 858px
   :height: 153px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/Last.fm2_2.jpg
