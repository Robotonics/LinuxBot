#!/usr/bin/env python



import os
import sys




__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"


class RingBuffer:
	def __init__(self, size):
		self.data= [None for i in xrange(size)]

	def append(self, x):
		self.data.pop(0)
		self.data.append(x)

	def get(self):
		return self.data



#def data():
	#buf=RingBuffer(4)
	#for i in xrange(10):
		#buf.append(i)
		#print buf.get()

