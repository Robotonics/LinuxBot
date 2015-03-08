#!/usr/bin/env python

import os
import sys
import numpy as np
from numpy import *
import array

if not os.getegid() == 0:
    sys.exit('Script must be run as root')



__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"


sonar=[0,0,0,0,0]


def new(x):

	global sonar
	sonar=np.append(sonar,x)
	if (np.size(sonar)>5):
		sonar=np.delete(sonar,0)

def fresh():
	global sonar
	print(sonar[4])



	
