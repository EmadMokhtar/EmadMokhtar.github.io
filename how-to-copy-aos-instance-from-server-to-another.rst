How to copy AOS instance from server to another
###############################################
:date: 2011-12-10 18:18
:author: admin
:category: AX
:tags: AX, AX2009, dynamicsAX, DYNAX, MSDYNAX
:slug: how-to-copy-aos-instance-from-server-to-another
:status: published

|image0|

These are the steps to take a copy from AOS instance from server to
another:

#. Take copy of Dynamics AX database. (optional)
#. Install AOS, Application Files, .NET Business Connector, and Client.
#. Install Updates like Service Pack 1.
#. Stop Application Object Server service “Dynamics AX Object Server
   5.0$01-{Instance name}”.
#. Copy “\ *{Driver Letter}*:\\Program Files\\Microsoft Dynamics
   AX\\50\\Application\\Appl\ ” from original to “\ *{Driver
   Letter}*:\\Program Files\\Microsoft Dynamics
   AX\\50\\Application\\Appl\ ”  in destination server.
#. Start Application Object Server service “Dynamics AX Object Server
   5.0$01-{Instance name}”.
#. Open Client to check everything is working smoothly.

 

Notes:

#. Any customization made on the original AOS will transferred to
   destination server

.. |image0| image:: http://www.emadmokhtar.com/wp-content/uploads/2011/12/AOSCopying-300x82.png
   :class: aligncenter size-medium wp-image-813
   :width: 300px
   :height: 82px
   :target: http://www.emadmokhtar.com/wp-content/uploads/2011/12/AOSCopying.png
