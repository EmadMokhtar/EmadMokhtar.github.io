Twitter OAuth using Twitterizer
###############################
:date: 2010-12-27 15:24
:author: admin
:category: .net, C#
:slug: twitter-oauth-using-twitterizer
:status: published

My friend `Mohamed Meligy <http://twitter.com/meligy>`__ wrote a great
`blog
post <http://gurustop.net/blog/2010/12/26/twitter-oauth-caching-oauth-tweetsharp-presentation-code-nuggets/>`__
about Twitter OAuth using
`TweetSharp <http://tweetsharp.codeplex.com/>`__, so I decide to share
my experience of dealing with Twitter OAuth using another .NET Twitter
API wrapper `Twitterizer <http://www.twitterizer.net/>`__ “The one used
by `MetroTwit <http://www.metrotwit.com/>`__ WPF Twitter Client”.

So let’s first explain the workflow of OAuth:

|OAuth-Workflow-diagram|

    First, every registered app in Twitter, has 2 keys **(Consumer key
    &  Consumer secret)**, you’ll use then to get the request token.

    Second, you’ll ask user to provide his/her credentials & grant
    access to your app, & you’ll have another key (Access Token).

    Third, then you’ll verify the request using the 3 keys **(Consumer
    key, Consumer secret, & Access Token)** plus **verifier**, if it a
    callback URL for Web Apps or Pin Code for Desktop Apps.

Let’s download `Twitterizer
Libraries <http://www.twitterizer.net/files/Twitterizer2-WithAddons-2.3.zip>`__
(I’m using version 2.3)  to start coding, so I’ll create a simple WPF
application just to authenticate then will using the credentials to
tweet from it, let’s start:

|wpfapp|

When user click on “Sign In” button, it’ll open a web browser to ask him
about Twitter account name & password, then if he/she want to grant
access to our application.

let’s examine this part’s code:

.. code:: brush:

    private static string _consumerKey = "ConsumerKey";
    private static string _consumerSecret = "ConsumerSecret";
    OAuthTokenResponse authTokenResponse = OAuthUtility.GetRequestToken(_consumerKey,
                                                        _consumerSecret,
                                                        "oob");

    private void btnAuth_Click(object sender, RoutedEventArgs e)
    {
        Process process = new Process();
        process.StartInfo.FileName = getDefaultBrowser();
        process.StartInfo.Arguments = "http://twitter.com/oauth/authorize?oauth_token=" + authTokenResponse.Token;
        process.Start();
    }
    private string getDefaultBrowser()
    {
        string browser = string.Empty;
        RegistryKey key = null;
        try
        {
    key = Registry.ClassesRoot.OpenSubKey(@"HTTP\shell\open\command", false);

    //trim off quotes
    browser = key.GetValue(null).ToString().ToLower().Replace("\"", "");
    if (!browser.EndsWith("exe"))
    {
        //get rid of everything after the ".exe"
        browser = browser.Substring(0, browser.LastIndexOf(".exe") + 4);
    }
        }
        finally
        {
    if (key != null) key.Close();
        }
        return browser;
    }

    First, we’ll initialize an object from OAuthTokenResponse with the
    Consumer key & Consumer secret & get the Request Token.

    Second, we’ll open the browser for the user to grant access to our
    application.

Note: I borrow \ `Ryan Fabley’s
method <http://ryanfarley.com/blog/archive/2004/05/16/649.aspx>`__\  to
detect the default browser.

Then user will have to put the Pin Code in our application in order to
get his Access Token & Access Secret.

let’s examine this part’s code:

.. code:: brush:

    private void btnVerify_Click(object sender, RoutedEventArgs e)
            {
                authTokenResponse = OAuthUtility.GetAccessToken("Consumer Key", "Consumer Secret", authTokenResponse.Token,
                                            txtPincode.Text);
            }

Now after the user grant access & verify our application we have 2 keys
**(Access token & Access Secret)** & they’ll be stored inside
OAuthTokenResponse object, so we can use them to update our Twitter
status or tweet.

Write a tweet, click on Tweet button & BOOM you’re tweeting from your
Twitter client, let’s examine the code of this button:

.. code:: brush:

    private void btnTweet_Click(object sender, RoutedEventArgs e)
            {

                OAuthTokens oAuthTokens = new OAuthTokens();

                oAuthTokens.ConsumerKey = _consumerKey;
                oAuthTokens.ConsumerSecret = _consumerSecret;
                oAuthTokens.AccessToken = authTokenResponse.Token;
                oAuthTokens.AccessTokenSecret = authTokenResponse.TokenSecret;

                TwitterStatus.Update(oAuthTokens, txtTweet.Text);
                txtTweet.Text = String.Empty;
            }

.. |OAuth-Workflow-diagram| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/OAuth-Workflow-diagram_thumb.png
   :width: 240px
   :height: 160px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/OAuth-Workflow-diagram_2.png
.. |wpfapp| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/wpfapp_thumb.jpg
   :width: 640px
   :height: 312px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/wpfapp.jpg
