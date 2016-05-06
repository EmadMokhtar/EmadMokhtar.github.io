Title: Getting Started with Microsoft Translator V2
Date: 2010-10-17 18:13
Author: admin
Category: .net, C#
Slug: getting-started-with-microsoft-translator-v2
Status: published

[![MSFT Translator
Logo](http://www.emadmokhtar.com/wp-content/uploads/2011/11/MSFT-Translator-Logo_thumb.jpg "MSFT Translator Logo")](http://www.emadmokhtar.com/wp-content/uploads/2011/11/MSFT-Translator-Logo.jpg)At
MIX10 conference Microsoft announced about V2 of its Translation API
“Microsoft Translator”.

I’ll use Microsoft Translator API to translate text from Arabic to
English, to show you it’s so simple and easy.

Before start coding, you need to get your AppID, so you can use the
API’s SOAP, HTTP, and AJAX functions, just go to this
[link](http://www.bing.com/developers/appids.aspx) and login using Live
ID if you have one, or great on if you don’t have it; After provide some
information about you and your application, the AppID will be created,
copy and save it, because we’ll use it later.

Add Microsoft Translator SOAP API to your project by right-click on
References folder and choose Add Service Reference,

[![add service
reference1](http://www.emadmokhtar.com/wp-content/uploads/2011/11/add-service-reference1_thumb.jpg "add service reference1")](http://www.emadmokhtar.com/wp-content/uploads/2011/11/add-service-reference1.jpg)

put this link <http://api.microsofttranslator.com/V2/Soap.svc> in
address filed and press Go,

[![add service
reference](http://www.emadmokhtar.com/wp-content/uploads/2011/11/add-service-reference_thumb.jpg "add service reference")](http://www.emadmokhtar.com/wp-content/uploads/2011/11/add-service-reference.jpg)

give it time and SoapService will appear in Services box, give name for
the Namespace, for example here I gave it “TranslatorSOAP”.

Now let’s code,

Here’s a C\# code snippet for translating Arabic text to English:

``` {.brush: .csharp; .highlight: .[11];}
using MicrosoftTranslatorCS.TranslatorSOAP;

namespace MicrosoftTranslatorCS
{
    class Program
    {
        static void Main(string[] args)
        {
            string appId = "Put Your AppID Here";
            LanguageServiceClient client = new LanguageServiceClient();
            string Translated = client.Translate(appId, "أهلا و سهلا", "ar", "en");
            Console.WriteLine(Translated); //Hello
            Console.ReadLine();

        }
    }
}
```

And here’s is a VB code snippet:

``` {.brush: .vb; .highlight: .[8];}
Imports MicrosoftTranslatorVB.TranslatorSOAP

Module Module1

    Sub Main()
        Dim appId As String = "Put Your AppID Here"
        Dim client As New LanguageServiceClient()
        Dim Translated As String = client.Translate(appId, "أهلا و سهلا", "ar", "en")
        Console.WriteLine(Translated) 'Hello
        Console.ReadLine()
    End Sub

End Module
```

The Translate method takes 4 parameters, and return the translated text.

``` {.brush: .csharp;}
Translate("AppID", "Source Text", "Source Language", "Translated Language")
```

Source files (C\# and VB):

<iframe style="background-color: #fcfcfc; width: 98px; height: 115px; padding: 0px;" title="Preview" src="http://cid-7d7052e2d56ee805.office.live.com/embedicon.aspx/MyBlogFolder/MicrosoftTranslatorVB.zip" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" width="320" height="240"></iframe><iframe style="background-color: #fcfcfc; width: 98px; height: 115px; padding: 0px;" title="Preview" src="http://cid-7d7052e2d56ee805.office.live.com/embedicon.aspx/MyBlogFolder/MicrosoftTranslatorCS.zip" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" width="320" height="240"></iframe>

 

<div
id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:bb488ea2-c0d2-4ea1-a080-a41b7bf7f836"
class="wlWriterEditableSmartContent"
style="margin: 0px; display: inline; float: none; padding: 0px;">

del.icio.us Tags:
[Microsoft](http://del.icio.us/popular/Microsoft),[Translation](http://del.icio.us/popular/Translation),[Translator](http://del.icio.us/popular/Translator)

</div>

 

<div
id="scid:0767317B-992E-4b12-91E0-4F059A8CECA8:3d4a8b3d-7960-40a0-b67c-68eb0ddc30b2"
class="wlWriterEditableSmartContent"
style="margin: 0px; display: inline; float: none; padding: 0px;">

Technorati Tags:
[Microsoft](http://technorati.com/tags/Microsoft),[Translation](http://technorati.com/tags/Translation),[Translator](http://technorati.com/tags/Translator)

</div>
