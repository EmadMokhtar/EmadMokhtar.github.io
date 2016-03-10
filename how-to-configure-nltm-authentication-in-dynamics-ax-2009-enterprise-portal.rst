How to configure NLTM authentication in Dynamics AX 2009 Enterprise Portal
##########################################################################
:date: 2011-11-24 13:44
:author: admin
:category: AX
:tags: AX, dynamicsAX, Enterpris, EP, Portal
:slug: how-to-configure-nltm-authentication-in-dynamics-ax-2009-enterprise-portal
:status: published

After installing Enterprise Portal you need to configure the way It’ll
authenticate the users, there’re 2 ways (NTLM or Kerberos), you’ll use
NTLM if the EP installed on the same machine where SQL Server/SSRS
installed, so here’s the way to configure it:

#. In SharePoint Central Administration and set IIS Authentication
   Settings to NLTM.\ |image0|
#. Go to Internet Information Services (IIS) Manager, go to Application
   Pool, locate EP’s Application Pool, and set the Identity to Business
   Proxy Account.\ |image1|
#. Then go to EP’s application node, on the right hand press on advance
   settings, and set Physical Path Credential to Application user (pass
   through authentication).\ |image2|
#. Locate authentication, go to windows authentication, and providers
   make sure NLTM is the first provider.\ |image3|

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/61-300x125.png
   :class: aligncenter size-medium wp-image-785
   :width: 300px
   :height: 125px
.. |image1| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/31-300x178.png
   :class: aligncenter size-medium wp-image-783
   :width: 300px
   :height: 178px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/31.png
.. |image2| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/51-300x175.png
   :class: aligncenter size-medium wp-image-784
   :width: 300px
   :height: 175px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/51.png
.. |image3| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/11/21-300x174.png
   :class: aligncenter size-medium wp-image-782
   :width: 300px
   :height: 174px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/11/21.png
