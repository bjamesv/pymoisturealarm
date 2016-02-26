# pyMoistureAlarm

A simple pair of Python programs to monitor moisture & alert when a target threshold is exceeded.

## Overview

One program _sensor_ is run from a networked embedded device with moisture sensor.

The other program (_server_) is run on a networked computer with audio output, to alert the room's occupants when the moisture threshold has been exceeded.

## Sample Output
    $ python2 listener.py 
    serving at port 8000
    192.168.1.1 - - [25/Feb/2016 22:34:47] "GET /V:2175" 200 -
    192.168.1.1 - - [25/Feb/2016 22:34:53] "GET /V:2207" 200 -
    192.168.1.1 - - [25/Feb/2016 22:34:59] "GET /V:2207" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:05] "GET /V:2175" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:11] "GET /V:2223" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:17] "GET /V:2207" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:23] "GET /V:2215" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:29] "GET /V:2215" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:35] "GET /V:2207" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:41] "GET /V:2175" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:47] "GET /V:2175" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:53] "GET /V:2223" 200 -
    192.168.1.1 - - [25/Feb/2016 22:35:59] "GET /V:2175" 200 -

Copyright (C) 2016 Brandon J. Van Vaerenbergh
