#!/usr/bin/env python

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA13.gpio import gpio
from pyA13.gpio import port

__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

ENA=port.PC0
IN1=port.PC1
IN2=port.PC2
IN3=port.PC3
IN4=port.PC4
ENB=port.PC5


gpio.init()
gpio.setcfg(ENA,gpio.OUTPUT)
gpio.setcfg(IN1,gpio.OUTPUT)
gpio.setcfg(IN2,gpio.OUTPUT)
gpio.setcfg(IN3,gpio.OUTPUT)
gpio.setcfg(IN4,gpio.OUTPUT)
gpio.setcfg(ENB,gpio.OUTPUT)

def forward(void):

	gpio.output(ENA, 1)
	gpio.output(ENB, 1)
	gpio.output(IN1, 1)
	gpio.output(IN2, 0)
	gpio.output(IN3, 0)
	gpio.output(IN4, 1)

def reverse(void):

	gpio.output(ENA, 1)
	gpio.output(ENB, 1)
	gpio.output(IN1, 0)
	gpio.output(IN2, 1)
	gpio.output(IN3, 1)
	gpio.output(IN4, 0)

def left(void):

	gpio.output(ENA, 1)
	gpio.output(ENB, 1)
	gpio.output(IN1, 1)
	gpio.output(IN2, 0)
	gpio.output(IN3, 1)
	gpio.output(IN4, 0)

def right(void):

	gpio.output(ENA, 1)
	gpio.output(ENB, 1)
	gpio.output(IN1, 0)
	gpio.output(IN2, 1)
	gpio.output(IN3, 0)
	gpio.output(IN4, 1)



