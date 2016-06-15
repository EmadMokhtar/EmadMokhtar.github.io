Title: Enable ASP.NET 32-bit application on 64-bit environment
Date: 2011-03-11 10:47
Author: EmadMokhtar
Category: ASP.NET
Slug: enable-asp-net-32-bit-application-on-64-bit-environment
Status: published

If you’re deploying 32-bit ASP.NET application on 64-bit environment,
you can enable 32-bit in IIS, you have 2 ways to do it by:

1.  Set Application Pool Defaults.
2.  Change specific Application Pool Advanced Settings.

![IIS Manager]({filename}/images/32bitasp_1.jpg)

Here is the setting you need to change either in number 1 or 2:

![Application Pool settings]({filename}/images/32bitasp1.jpg)
