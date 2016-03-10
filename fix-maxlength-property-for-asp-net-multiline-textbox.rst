Fix MaxLength property for ASP.NET Multiline Textbox
####################################################
:date: 2012-11-12 10:54
:author: admin
:category: asp.net, webdev
:tags: aspnet, webforms
:slug: fix-maxlength-property-for-asp-net-multiline-textbox
:status: published

If you try to change the TextMode property of ASP.NET TextBox control to
Multiline and set the MaxLength property it’ll not work and user can
insert as much characters as he/she want. WHY? Because when you put
TextBox in your WebForm it’ll be rendered to HTML *<input>* tag but when
you set the TextMode to multiline it’ll be rendered to *<textarea>* tag,
and MaxLength attribute is in *<input>* but it’s not for *<textarea>*.

So dude How can I solve this issue?

From my opinion it’s better to solve this by using JavaScript function
than using RegularExpressionValidator, so let’s write the JavaScript
function and call it in onKeyPress TextBox client event.

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:246112b8-c17a-4cb5-92ce-8f31e8e69d6f"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

JavaScript function

.. raw:: html

   </div>

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#.         function textboxMultilineMaxNumber(txt, maxLen) {
#.  
#.             if (txt.value.length > (maxLen -1))returnfalse;
#.             else {
#.                 returntrue;
#.             }
#.         }

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div
   id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:a74685d0-fe1e-4754-9188-7572abf305bd"
   class="wlWriterEditableSmartContent"
   style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

.. raw:: html

   <div
   style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

.. raw:: html

   <div
   style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

MultiLine TextBox

.. raw:: html

   </div>

.. raw:: html

   <div style="background: #ddd; overflow: auto">

#. <asp:TextBoxID="TextBox1"runat="server"TextMode="MultiLine"
#.     onkeypress="return textboxMultilineMaxNumber(this,15);">
#.     </asp:TextBox>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

As you can see in line number 2 I pass TextBox and MaxLength, this will
make the max number of characters user can input in the MultiLine
TextBox is 15.
