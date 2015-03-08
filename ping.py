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

Trigger_Ff=port.PE8
Echo_Ff=port.PE9
Trigger_Fr=port.PB4
Echo_Fr=port.PB3
Trigger_Fb=port.PC6
Echo_Fb=port.PC5
Trigger_Fl=port.PE10
Echo_Fl=port.PE11





gpio.init()
gpio.setcfg(Trigger_Ff,gpio.OUTPUT)
gpio.setcfg(Echo_Ff,gpio.INPUT)

gpio.setcfg(Trigger_Fr,gpio.OUTPUT)
gpio.setcfg(Echo_Fr,gpio.INPUT)

gpio.setcfg(Trigger_Fb,gpio.OUTPUT)
gpio.setcfg(Echo_Fb,gpio.INPUT)

gpio.setcfg(Trigger_Fl,gpio.OUTPUT)
gpio.setcfg(Echo_Fl,gpio.INPUT)


def front():
	gpio.output(Trigger_Ff,0) # Set Trigger LOW
	time.sleep(0.5)
	gpio.output(Trigger_Ff,1)
	time.sleep(0.00001) # 10uS pulse
	gpio.output(Trigger_Ff,0)
	start=time.time()
	while gpio.input(Echo_Ff)==0:
		start=time.time()
	while gpio.input(Echo_Ff)==1:
		stop=time.time()
	elapsed = stop-start
	distance_Ff = elapsed * 34000
	distance_Ff=distance_Ff/2
	distance_Ff=round(distance_Ff,0)
	return(distance_Ff)
	print(distance_Ff)



def right():
	gpio.output(Trigger_Fr,0) # Set Trigger LOW
	time.sleep(0.5)
	gpio.output(Trigger_Fr,1)
	time.sleep(0.00001) # 10uS pulse
	gpio.output(Trigger_Fr,0)
	start=time.time()
	while gpio.input(Echo_Fr)==0:
		start=time.time()
	while gpio.input(Echo_Fr)==1:
		stop=time.time()
	elapsed = stop-start
	distance_Fr = elapsed * 34000
	distance_Fr=distance_Fr/2
	distance_Fr=round(distance_Fr,0)
	return(distance_Fr)
	print(distance_Fr)


def back():
	gpio.output(Trigger_Fb,0) # Set Trigger LOW
	time.sleep(0.5)
	gpio.output(Trigger_Fb,1)
	time.sleep(0.00001) # 10uS pulse
	gpio.output(Trigger_Fb,0)
	start=time.time()
	while gpio.input(Echo_Fb)==0:
		start=time.time()
	while gpio.input(Echo_Fb)==1:
		stop=time.time()
	elapsed = stop-start
	distance_Fb = elapsed * 34000
	distance_Fb=distance_Fb/2
	distance_Fb=round(distance_Fb,0)
	return(distance_Fb)
	print(distance_Fb)

def left():
	gpio.output(Trigger_Fl,0) # Set Trigger LOW
	time.sleep(0.5)
	gpio.output(Trigger_Fl,1)
	time.sleep(0.00001) # 10uS pulse
	gpio.output(Trigger_Fl,0)
	start=time.time()
	while gpio.input(Echo_Fl)==0:
		start=time.time()
	while gpio.input(Echo_Fl)==1:
		stop=time.time()
	elapsed = stop-start
	distance_Fl = elapsed * 34000
	distance_Fl=distance_Fl/2
	distance_Fl=round(distance_Fl,0)
	return(distance_Fl)
	print(distance_Fl)



	







