# Azure Sphere for PlatformIO
Azure Sphere SDK for PlatformIO

## is not ready yet ... do not install !!! ##

it's almost done... I have only one problem - Uploader - Microsoft use "TAP-Windows Provider V9" 

I install driver manually but I dont know how to config to work with the board 

and at this moment you need full ( 3Gb ) VS + Azure SDK installation...

If someone ( Microsoft, Avnet, Seed, Element14... ) help - full installation not need

## Microsoft ADD Accaunt

You need email at hotmail.com or ... or account at Microsoft

Example: **wizio[@]hotmail.com**

goto **Azure Portal** -> Azure Active Directory -> Users -> **New user**

Enter:

Name: Your Name ( does not matter )

User name: azure[@]wiziohotmail.onMicrosoft.com ( azure@ as your preferences, **wiziohotmail** as your email )

CREATE User

Select this user -> Directory role -> ADD -> **Global administrator**

That is all... Test: 

**azsphere login**

**azsphere dev show-attached** Show the details of the attached device

**azsphere dev recover** For device update

**azsphere prep-debug** Set up a device for local debugging

## Installation
( I need 150Mb "cloud" for compiler and tools )

Install VS Code + PlatformIO

PlatformIO - Home - Platforms - Advanced Installation

PASTE: https://github.com/Wiz-IO/platform-azure

PlatformIO - New Project

Name - search 'azure' - select Linux

Build, after this you will have template Project

OPEN: 'platformio.ini' and edit your settings

OPEN: 'src/app_manifest.json' and enter your 'Capabilities'

Build, Upload ... if uploader work - nice ...



IF YOU WANT HELP - CONNECT ME...


![Project](https://raw.githubusercontent.com/Wiz-IO/LIB/master/images/azure.png) 

![Project](https://raw.githubusercontent.com/Wiz-IO/LIB/master/images/azure-platformio.png) 
