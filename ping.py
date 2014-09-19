#!/usr/bin/env python

import os
import sys
import time

from pyA13.gpio import gpio
from pyA13.gpio import port

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

Trigger=port.PB2
Echo=port.PB3


gpio.init()
gpio.setcfg(Trigger,gpio.OUTPUT)
gpio.setcfg(Echo,gpio.INPUT)

gpio.output(Trigger,0) # Set Trigger LOW
time.sleep(0.5)

gpio.output(Trigger,1)
time.sleep(0.00001) # 10uS pulse
gpio.output(Trigger,0)
start=time.time()
while gpio.input(Echo)==0:
	start=time.time()
while gpio.input(Echo)==1:
	stop=time.time()

elapsed = stop-start
distance = elapsed * 34000
print "Distance : %.1f" % distance



	







