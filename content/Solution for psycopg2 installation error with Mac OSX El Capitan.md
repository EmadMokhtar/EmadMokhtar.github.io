Title: Solution for psycopg2 installation error with Mac OSX El Capitan
Date: 2015-10-11 12:00
Category: Development
Tags: developement, macosx
Authors: Emad Mokhtar

# The Issue

If you tried to install to install psycopg2 package after upgrading to Mac OSX El Capitan and got an error like this:     
    
```
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), 
missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

![pip.log]({filename}/images/1444569163_full.png)

# The Soltuion:

Simplly install Command-Line Tools:

`sudo xcode-select --install`
