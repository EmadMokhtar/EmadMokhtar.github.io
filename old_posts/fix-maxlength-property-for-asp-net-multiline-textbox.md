Title: Fix MaxLength property for ASP.NET Multiline Textbox
Date: 2012-11-12 10:54
Author: admin
Category: asp.net, webdev
Tags: aspnet, webforms
Slug: fix-maxlength-property-for-asp-net-multiline-textbox
Status: published

If you try to change the TextMode property of ASP.NET TextBox control to
Multiline and set the MaxLength property it’ll not work and user can
insert as much characters as he/she want. WHY? Because when you put
TextBox in your WebForm it’ll be rendered to HTML *&lt;input&gt;* tag
but when you set the TextMode to multiline it’ll be rendered to
*&lt;textarea&gt;* tag, and MaxLength attribute is in *&lt;input&gt;*
but it’s not for *&lt;textarea&gt;*.

So dude How can I solve this issue?

From my opinion it’s better to solve this by using JavaScript function
than using RegularExpressionValidator, so let’s write the JavaScript
function and call it in onKeyPress TextBox client event.

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:246112b8-c17a-4cb5-92ce-8f31e8e69d6f"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

JavaScript function

</div>

<div style="background: #ddd; overflow: auto">

1.  <span style="color:#f1f2f3">        </span><span
    style="color:#93c763">function</span><span style="color:#f1f2f3">
    textboxMultilineMaxNumber(txt, maxLen) {</span>
2.   
3.  <span style="color:#f1f2f3">            </span><span
    style="color:#93c763">if</span><span style="color:#f1f2f3">
    (txt.value.length &gt; (maxLen -</span><span
    style="color:#ffcd22">1</span><span
    style="color:#f1f2f3">))</span><span
    style="color:#93c763">return</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">false</span><span
    style="color:#f1f2f3">;</span>
4.  <span style="color:#f1f2f3">            </span><span
    style="color:#93c763">else</span><span style="color:#f1f2f3">
    {</span>
5.  <span style="color:#f1f2f3">                </span><span
    style="color:#93c763">return</span><span
    style="color:#f1f2f3"></span><span
    style="color:#93c763">true</span><span
    style="color:#f1f2f3">;</span>
6.  <span style="color:#f1f2f3">            }</span>
7.  <span style="color:#f1f2f3">        }</span>

</div>

</div>

</div>

<div
id="scid:9ce6104f-a9aa-4a17-a79f-3a39532ebf7c:a74685d0-fe1e-4754-9188-7572abf305bd"
class="wlWriterEditableSmartContent"
style="padding-bottom: 0px; margin: 0px; padding-left: 0px; padding-right: 0px; display: inline; float: none; padding-top: 0px">

<div
style="border: #000080 1px solid; color: #000; font-family: 'Courier New', Courier, Monospace; font-size: 10pt">

<div
style="background: #000080; color: #fff; font-family: Verdana, Tahoma, Arial, sans-serif; font-weight: bold; padding: 2px 5px">

MultiLine TextBox

</div>

<div style="background: #ddd; overflow: auto">

1.  <span style="color:#f1f2f3">&lt;</span><span
    style="color:#93c763">asp</span><span
    style="background:#293134;color:#e0e2e4">:</span><span
    style="color:#93c763">TextBox</span><span
    style="color:#f1f2f3"></span><span
    style="background:#293134;color:#e0e2e4">ID=</span><span
    style="color:#ec7600">"TextBox1"</span><span
    style="color:#f1f2f3"></span><span
    style="background:#293134;color:#e0e2e4">runat=</span><span
    style="color:#ec7600">"server"</span><span
    style="color:#f1f2f3"></span><span
    style="background:#293134;color:#e0e2e4">TextMode=</span><span
    style="color:#ec7600">"MultiLine"</span><span
    style="color:#f1f2f3"></span>
2.      <span style="color:#f1f2f3"></span><span
    style="background:#293134;color:#e0e2e4">onkeypress=</span><span
    style="color:#ec7600">"return
    textboxMultilineMaxNumber(this,15);"</span><span
    style="color:#f1f2f3">&gt;</span>
3.      <span style="color:#f1f2f3">&lt;/</span><span
    style="color:#93c763">asp</span><span
    style="background:#293134;color:#e0e2e4">:</span><span
    style="color:#93c763">TextBox</span><span
    style="color:#f1f2f3">&gt;</span>

</div>

</div>

</div>

As you can see in line number 2 I pass TextBox and MaxLength, this will
make the max number of characters user can input in the MultiLine
TextBox is 15.
