Title: Storing password in plain text, you’re doing it wrong
Date: 2013-03-06 16:41
Author: admin
Category: .net, C#
Tags: #security #dotNet #Csharp
Slug: storing-password-in-plain-text-youre-doing-it-wrong
Status: published

![Hacking for password&lt;/p&gt;
&lt;p&gt;](http://www.emadmokhtar.com/wp-content/uploads/2013/03/114166encryption.jpg "Hacking for password</p>
<p>"){width="425" height="282"} If you’re software developer then there
is big chance you’ll implement user login feature, and you must store
the username and password in your system. Most of developers stored
these precious information in database as plain text, yes we did include
myself I was doing it wrong, and if you’re doing it please stop and read
this article to know how to do it right and being awesome.

Username, Password, or Pin codes these are precious information, and if
hacker or even internal employee stole the database he can do whatever
he wants with your users information. So How to keep these information
safe? The answer is hashing it.

Why I was not doing that? I was lazy and every time I
googled/binged/searched about this, I found many complex How-To
articles, but last week I finally found something simple and it’s the
reason I’m writing this article.

What is hashing?
================

Hashing is encoding string "message” to hash value and you can’t
reproduce the original string “message” from hash value, so it’s one way
cryptographic algorithm, [it’s different than
encryption](http://stackoverflow.com/questions/326699/difference-between-hashing-a-password-and-encrypting-it)
that it’s  two way cryptographic algorithm.

How to Hash password?
=====================

As I mentioned above I found many articles about how-to hash password
but most of them are very complex and I believe in work smart not hard,
I found
[System.Web.Helpers](http://msdn.microsoft.com/en-us/library/system.web.helpers(v=vs.99).aspx)
*Namespace* that has
[Crypto](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx)
*Class* that has many hashing helpers. I play with it and try to learn
how to hash a password.

Flow:
-----

Now let’s understand the flow and then check how to implement it in
code. First to save password in database you must hash it using one of
hashing algorithm and store the hashes password into database.

[![StoreHashedPassword](http://www.emadmokhtar.com/wp-content/uploads/2013/03/StoreHashedPassword_thumb.png "StoreHashedPassword"){width="640"
height="90"}](http://www.emadmokhtar.com/wp-content/uploads/2013/03/StoreHashedPassword.png)

Second to check the user password in login, you should hash the password
user input and compare the two hashed passwords (user input & stored in
database).

[![RetreiveHashedPassword](http://www.emadmokhtar.com/wp-content/uploads/2013/03/RetreiveHashedPassword_thumb.png "RetreiveHashedPassword"){width="640"
height="221"}](http://www.emadmokhtar.com/wp-content/uploads/2013/03/RetreiveHashedPassword.png)

Code:
-----

I’ll show you how to hash user’s password and check the password he’ll
enter when login to your system. Like I said above I’ll user
*[System.Web.Helpers.Crypto](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx)*
*Class*, this class has 2 m*ethods*
*[HashPassword](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.hashpassword(v=vs.99).aspx)*
and
[*VerifyHashedPassword*](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.verifyhashedpassword(v=vs.99).aspx)
we’ll use them*.* we’ll write the code in Unit Tests so no need for
Console Application and wait for Command Prompt to run, you’ll just
write your code test it and you’ll get results in test results quickly,
so let’s get our hand dirty:

### Hash:

What you need to do is to pass the user input password to
*HashPassword() Method* and you’ll get the hashed password.

<div class="csharpcode">

``` {.alt}
   1:   plainPassword = "P@12345566";
```

       2:   hashedPassword = Crypto.HashPassword(plainPassword);

</div>

<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
### Compare:

We can verify the password by passing the hashed password and the plain
password and *VerifyHashedPassword() Method* will return true if it’s
verified or false if it’s not.

<div class="csharpcode">

       1:  Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword,plainPassword));

</div>

<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
### Complete Code:

<div class="csharpcode">

``` {.alt}
   1:  [Test]
```

       2:  public void test_hashing_password()

``` {.alt}
   3:  {
```

       4:      string plainPassword;

``` {.alt}
   5:      string hashedPassword;
```

       6:  

``` {.alt}
   7:      plainPassword = "P@12345566";
```

       8:      hashedPassword = Crypto.HashPassword(plainPassword);

``` {.alt}
   9:  
```

      10:      Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword,plainPassword));

``` {.alt}
  11:  
```

      12:  }

</div>

<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
*Note: I’m using [NUnit](http://www.nunit.org/) as my Unit Test
Framework and [Resharper](http://www.jetbrains.com/resharper/) as my
Test Runner.*

Yet better Hashing:
===================

Even after hashing passwords you aren’t safe from hacking and hackers,
hackers can use [rainbow
table](http://en.wikipedia.org/wiki/Rainbow_table) to attack your
system. The good news is you can increase the security of your hashing
by adding salt, let’s see how we can do this:

Flow
----

Save the password looks like the same flow but this time we’ll use
[*GenerateSalt*](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.generatesalt(v=vs.99).aspx)
*Method* in
[*System.Web.Helpers*](http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx)
*Class* to generate random salt that will be added to the password and
store it to database with the hashed password.

[![YetBetterStoreHashingPassword](http://www.emadmokhtar.com/wp-content/uploads/2013/03/YetBetterStoreHashingPassword_thumb.png "YetBetterStoreHashingPassword"){width="640"
height="164"}](http://www.emadmokhtar.com/wp-content/uploads/2013/03/YetBetterStoreHashingPassword.png)

Retrieving and comparing user input password and the one stored in
database is as before but you need to retrieve both the hashed password
and salt from database, add salt to plain password, hash the produced
string, then compare it with the hashed password that retrieved from
database.

[![YetBetterRetreivePassword](http://www.emadmokhtar.com/wp-content/uploads/2013/03/YetBetterRetreivePassword_thumb.png "YetBetterRetreivePassword"){width="640"
height="285"}](http://www.emadmokhtar.com/wp-content/uploads/2013/03/YetBetterRetreivePassword.png)

Code:
-----

### Hash:

<div class="csharpcode">

``` {.alt}
   1:  plainPassword = "P@12345566";
```

       2:  salt = Crypto.GenerateSalt();

``` {.alt}
   3:  passwordSaltCombination = plainPassword + salt;
```

       4:  hashedPassword = Crypto.HashPassword(passwordSaltCombination);

</div>

<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
### Compare:

<div class="csharpcode">

       1:  Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword, passwordSaltCombination));

</div>

<style type="text/css"><!--.csharpcode, .csharpcode pre<br />
{<br />
    font-size: small;<br />
    color: black;<br />
    font-family: consolas, "Courier New", courier, monospace;<br />
    background-color: #ffffff;<br />
    /*white-space: pre;*/<br />
}<br />
.csharpcode pre { margin: 0em; }<br />
.csharpcode .rem { color: #008000; }<br />
.csharpcode .kwrd { color: #0000ff; }<br />
.csharpcode .str { color: #006080; }<br />
.csharpcode .op { color: #0000c0; }<br />
.csharpcode .preproc { color: #cc6633; }<br />
.csharpcode .asp { background-color: #ffff00; }<br />
.csharpcode .html { color: #800000; }<br />
.csharpcode .attr { color: #ff0000; }<br />
.csharpcode .alt<br />
{<br />
    background-color: #f4f4f4;<br />
    width: 100%;<br />
    margin: 0em;<br />
}<br />
.csharpcode .lnum { color: #606060; }<br />
--></style>
### Complete Code:

<div class="csharpcode">

       1:  [Test]

       2:  public void test_hasing_password_with_salt()

       3:  {

       4:      string plainPassword;

       5:      string hashedPassword;

       6:      string salt;

       7:      string passwordSaltCombination;

       8:  

       9:      plainPassword = "P@12345566";

      10:      salt = Crypto.GenerateSalt();

      11:      passwordSaltCombination = plainPassword + salt;

      12:      hashedPassword = Crypto.HashPassword(passwordSaltCombination);

      13:  

      14:      Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword, passwordSaltCombination));

      15:  

      16:  }

</div>

As you can see it’s simple procedure so please use it and stop saving
plain password in your database.

I encourage you to read Jeff Atwood’s article [You're Probably Storing
Passwords
Incorrectly](http://www.codinghorror.com/blog/2007/09/youre-probably-storing-passwords-incorrectly.html).
