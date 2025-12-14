The Exo Planet Clock Program. Replicating a Clock for the planet "Ork"! A mystical planet where its inhabitants experience time in either a 36 or 72 Hour formats...

Program Information:

There are 3 available/working program functions:

1.) orkTime(total seconds, format) - Gives a User the Clock-Time on the Planet Ork in either 36 Hour / 72 Hour Formats (e.g. - 11:112:31 PM)
2.) getData72HrFormat(time) - Gives a User the Inputted Time in a 72-Hour Format for Ork
3.) convert2Seconds(time) - Gives the User the total amound of seconds from an inputted time (e.g. 11Hrs, 47Min, 22Sec = 389,320 Seconds)
4.) timeElapsed(time1, time2) - Under Construction...
5.) Duration(time) - Under Construction...

How to Use:

The Procedure to initialize the groundwork is to call Python and then import all modules from the exo_main file...
>>> python
>>> from exo_main import *

Next, call the function you wish to use...

*Using orkTime()*
orkTime is called as -- orktime(total seconds, format) [e.g. - orkTime(64321, 36)]
The output will be the Clock-Time Displayed on Ork in either a 36/72 Hour Format

*using getData72HrFormat()*
This function is called as -- getData72HrFormat(time) [e.g. - getData72HrFormat('12:47 PM')]
The output will be the conversion of Earth Time to Ork Time Displayed to User
