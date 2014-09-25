#!/usr/bin/env python

import MotorControl
import ping
from subprocess import call
from time import sleep
from numpy import *
import Gnuplot, Gnuplot.funcutils

g = Gnuplot.Gnuplot(debug=1)
g.title('A simple example')
while (1):
	x=call(["./HMC5883"])
	y=ping.distance(1)
	g.splot ([x,y])

