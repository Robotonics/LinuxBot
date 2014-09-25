#!/usr/bin/env python

import os
import sys
import ping
from numpy import *
from array import *


__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

def scan (void):
	data = array('f',[ ])
	for i in range(5):
		distance=ping.distance(1)
		data.append(distance)
		result=sum(data)/len(data)
	print result

	