#!/usr/bin/env python



import os
import motor
import ping
import radar
import GPS




__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"


def forward():
	motor.forward(1)

def reverse():
	motor.reverse(1)

def right():
	motor.right(1)

def left():
	motor.left(1)

def stop():
	motor.stop(1)

options = {0: forward,
	   1: reverse,
	   2: right,
	   3: left,
	   4: stop,
}
while(1):
	try:
   		num=int(raw_input('Direction(0-4):'))
		options[num]()
		

	except ValueError:
    		print "Not a number"

