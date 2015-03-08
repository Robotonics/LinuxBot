#!/usr/bin/env python

import os
import sys
import ping
from pylab import arange, plt
import drawnow as drawn
import numpy as np

__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

plt.ion() 			# enable interactivity
fig=plt.figure()		# make a figure

def makeFig():
	plt.scatter(x,y)

x=list()
y=list()

for i in arange(1000):
	temp_y=np.random.random()
	x.append(i)
	y.append(temp_y)
	i+=1
	drawn(makeFig)
		

