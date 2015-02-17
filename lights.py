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

LEDR=port.PE6
LEDL=port.PC11
LEDIRR=port.PE7
LEDIRL=port.PC10

gpio.init()
gpio.setcfg(LEDR,gpio.OUTPUT)
gpio.setcfg(LEDL,gpio.OUTPUT)
gpio.setcfg(LEDIRR,gpio.OUTPUT)
gpio.setcfg(LEDIRL,gpio.OUTPUT)


def ledr_on():
	gpio.output(LEDR,1)

def ledl_on():
	gpio.output(LEDL,1)

def ledr_off():
	gpio.output(LEDR,0)

def ledl_off():
	gpio.output(LEDL,0)

def ledirr_on():
	gpio.output(LEDIRR,1)

def ledirl_on():
	gpio.output(LEDIRL,1)

def ledirr_off():
	gpio.output(LEDIRR,0)

def ledirl_off():
	gpio.output(LEDIRL,0)











