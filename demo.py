#!/usr/bin/env python

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
import MotorControl

__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

while True:

	MotorControl.right(1)
	sleep(0.9)
	MotorControl.left(1)
	sleep(0.9)
	MotorControl.forward(1)
	sleep(0.9)
	MotorControl.reverse(1)
	sleep(0.9)
