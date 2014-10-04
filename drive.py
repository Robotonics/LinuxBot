#!/usr/bin/env python

import os
import sys
import ping
import motor
import radar
import time

__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

def go (void):

	while(1):
		dist=ping.distance(1)
		if dist<10:
			motor.right(1)
		motor.forward(1)
			

