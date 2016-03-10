Getting Started with Google Translation
#######################################
:date: 2010-10-31 09:08
:author: admin
:category: .net, C#
:slug: getting-started-with-google-translation
:status: published

|google translation3|

Google provide a powerful translation web service, and there’s some time
you wish you can use it inside your application, so it’s possible, and
we’ll do it now.

We’re going to use “\ `Google API for .NET
Framework <http://code.google.com/p/google-api-for-dotnet/>`__\ ” to use
Google translate services, first we need to download the `Google
Translation
API <http://code.google.com/p/google-api-for-dotnet/downloads/detail?name=GoogleTranslateAPI_0.3.1.zip>`__
unzip it, we going to add “GoogleTranslateAPI.dll” file into our project
later.

The best of Google Translation it’s not require AppID like Microsoft
Translator, so no need to go and claim any API ID.

Now let’s get our hand dirty with some code:

First fire Microsoft Visual Studio, create new project, then Add
Reference to it,

|google translation2|

Then browse to where you unzipped “GoogleTranslateAPI\_0.3.1.zip” and
add “GoogleTranslationAPI.dll”

|google translation1|

Let’s add some code to the project:

Here’s C# code snippet:

.. code:: brush:

    using Google.API.Translate;

    namespace GoogleTanslationCS
    {
        class Program
        {
            static void Main(string[] args)
            {
                TranslateClient client = new TranslateClient("www.emadmokhtar.com");
                string tranlsated = client.Translate("???? ? ????", "ar", "en");
                Console.WriteLine(tranlsated); //Welcome
                Console.ReadLine();
            }
        }
    }

Here’s VB code snippet:

.. code:: brush:

    Imports Google.API.Translate

    Module Module1

        Sub Main()
            Dim client As New TranslateClient("www.emadmokhtar.com")
            Dim translated As String = client.Translate("???? ? ????", "ar", "en")
            Console.WriteLine(translated) 'Welcome
            Console.ReadLine()
        End Sub

    End Module

as you can see translate method take 3 parameters (source text, source
language, target language) and returns the translated text.

Source Files (C# & VB):

 

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:93a74d0f-b3d3-4e03-972d-2ce6cf60e5dd"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

Technorati Tags:
`google <http://technorati.com/tags/google>`__,\ `translation <http://technorati.com/tags/translation>`__,\ `translate <http://technorati.com/tags/translate>`__

.. raw:: html

   </div>

 

.. raw:: html

   <div
   id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:c2b99004-5e35-48f4-8ed8-f6b473afd8f5"
   class="wlWriterEditableSmartContent"
   style="margin: 0px; display: inline; float: none; padding: 0px;">

del.icio.us Tags:
`google <http://del.icio.us/popular/google>`__,\ `translation <http://del.icio.us/popular/translation>`__,\ `translate <http://del.icio.us/popular/translate>`__

.. raw:: html

   </div>

.. |google translation3| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation3_thumb_1.jpg
   :width: 244px
   :height: 78px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation3_1.jpg
.. |google translation2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation2_thumb.jpg
   :width: 244px
   :height: 88px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation2.jpg
.. |google translation1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation1_thumb.jpg
   :width: 555px
   :height: 484px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/google-translation1.jpg
