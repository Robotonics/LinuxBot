#!/usr/bin/env python

import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from collections import deque
import random
import ping


if not os.getegid() == 0:
    sys.exit('Script must be run as root')


__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

MAX_X=100   	# Width of graph
MAX_Y=1000 	# Height of graph 
sonar=0

# initialise line to horizontal line on 0

line=deque([0,0]*MAX_X,maxlen=MAX_X)



def update(fn, l2d):
	# simulate data[from serial within +-5 of last datapoint
	sonar=ping.distance_Ff()
	dy=sonar
	# add new point to deque
	line.append(line[MAX_X-1]+dy)
	# set the l2d to the new line coords
	# args are ([x-coords],[y-coords])
	l2d.set_data(range(-MAX_X/2,MAX_X/2), line)

fig=plt.figure()

# make the axes revolve around [0,0] at the centre
# instead of the x-axis being 0 to +100, make it -50 to +50
# ditto for y-axis -512 to +512

a=plt.axes(xlim=(-(MAX_X/2),MAX_X/2),ylim=(-(MAX_Y/2),MAX_Y/2))
l1,=a.plot([], [])
ani=anim.FuncAnimation(fig,update,fargs=(l1,),interval=50)


plt.show()