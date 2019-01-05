Title: Storing password in plain text, you’re doing it wrong
Date: 2013-03-06 16:41
Author: EmadMokhtar
Category: ASP.NET
Tags: security, dotNet ,Csharp

![Hacking for password]({static}/images/114166encryption.jpg)

If you’re software developer then there is big chance you’ll implement user login feature, and you must store the username and password in your system. Most of developers stored these precious information in database as plain text, yes we did include myself I was doing it wrong, and if you’re doing it please stop and read this article to know how to do it right and being awesome.

Username, Password, or Pin codes these are precious information, and if hacker or even internal employee stole the database he can do whatever he wants with your users information. So How to keep these information safe? The answer is hashing it.

Why I was not doing that? I was lazy and every time I googled/binged/searched about this, I found many complex How-To articles, but last week I finally found something simple and it’s the reason I’m writing this article.

# What is hashing?

Hashing is encoding string "message” to hash value and you can’t reproduce the original string “message” from hash value, so it’s one way cryptographic algorithm, [it’s different than encryption](http://stackoverflow.com/questions/326699/difference-between-hashing-a-password-and-encrypting-it) that it’s  two way cryptographic algorithm.

# How to Hash password?

As I mentioned above I found many articles about how-to hash password but most of them are very complex and I believe in work smart not hard, I found [`System.Web.Helpers`][1] Namespace that has  [`Crypto`][2] class that has many hashing helpers. I play with it and try to learn how to hash a password.

[1]: http://msdn.microsoft.com/en-us/library/system.web.helpers(v=vs.99).aspx
[2]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx

# Flow:

Now let’s understand the flow and then check how to implement it in code. First to save password in database you must hash it using one of hashing algorithm and store the hashes password into database.

![StoreHashedPassword]({static}/images/StoreHashedPassword.png)

Second to check the user password in login, you should hash the password user input and compare the two hashed passwords (user input & stored in database).

![RetreiveHashedPassword]({static}/images/RetreiveHashedPassword.png)

# Code:


I’ll show you how to hash user’s password and check the password he’ll enter when login to your system. Like I said above I’ll user [`System.Web.Helpers.Crypto`][3] class , this class has 2  methods [`HashPassword`][4] and [`VerifyHashedPassword`][5] we’ll use them*.* we’ll write the code in Unit Tests so no need for Console Application and wait for Command Prompt to run, you’ll just write your code test it and you’ll get results in test results quickly, so let’s get our hand dirty:

[3]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx
[4]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.hashpassword(vvs.99).aspx
[5]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.verifyhashedpassword(v=vs.99).aspx

## Hashing:

What you need to do is to pass the user input password to `HashPassword()` method and you’ll get the hashed password.

```csharp
plainPassword = "P@12345566";
hashedPassword = Crypto.HashPassword(plainPassword);
```
## Comparing:

We can verify the password by passing the hashed password and the plain password and `VerifyHashedPassword()` method will return true if it’s verified or false if it’s not.

```cshrap
Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword,plainPassword));
```

## Complete Code:

```charp
[Test]
public void test_hashing_password()
{
    string plainPassword;
    string hashedPassword;
    plainPassword = "P@12345566";
    hashedPassword = Crypto.HashPassword(plainPassword);
    Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword,plainPassword));
}
```

Note: I’m using [NUnit](http://www.nunit.org/) as my Unit Test Framework and [Resharper](http://www.jetbrains.com/resharper/) as my Test Runner.*

# Yet better Hashing:

Even after hashing passwords you aren’t safe from hacking and hackers, hackers can use [rainbow table](http://en.wikipedia.org/wiki/Rainbow_table) to attack your system. The good news is you can increase the security of your hashing by adding salt, let’s see how we can do this:

# Flow

Save the password looks like the same flow but this time we’ll use [`GenerateSalt`][6] method in [`System.Web.Helpers`][7] class to generate random salt that will be added to the password and store it to database with the hashed password.

[6]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto.generatesalt(v=vs.99).aspx
[7]: http://msdn.microsoft.com/en-us/library/system.web.helpers.crypto(v=vs.99).aspx

![YetBetterStoreHashingPassword]({static}/images/YetBetterStoreHashingPassword.png)

Retrieving and comparing user input password and the one stored in database is as before but you need to retrieve both the hashed password and salt from database, add salt to plain password, hash the produced string, then compare it with the hashed password that retrieved from database.

![YetBetterRetreivePassword]({static}/images/YetBetterRetreivePassword.png)

# Code:

## Hashing:

```csharp
plainPassword = "P@12345566";
salt = Crypto.GenerateSalt();
passwordSaltCombination = plainPassword + salt;
hashedPassword = Crypto.HashPassword(passwordSaltCombination);
```

## Comparing:

```charp
Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword, passwordSaltCombination));
```

## Complete Code:

```charp
[Test]
public void test_hasing_password_with_salt()
{
    string plainPassword;
    string hashedPassword;
    string salt;
    string passwordSaltCombination;
    plainPassword = "P@12345566";
    salt = Crypto.GenerateSalt();
    passwordSaltCombination = plainPassword + salt;
    hashedPassword = Crypto.HashPassword(passwordSaltCombination);
    Assert.AreEqual(true, Crypto.VerifyHashedPassword(hashedPassword, passwordSaltCombination));
}
```


As you can see it’s simple procedure so please use it and stop saving plain password in your database.

I encourage you to read Jeff Atwood’s article [You're Probably Storing Passwords Incorrectly](http://www.codinghorror.com/blog/2007/09/youre-probably-storing-passwords-incorrectly.html)
