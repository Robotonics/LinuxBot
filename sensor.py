#!/usr/bin/env python





import ping




__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"


front=0
rear=0
left=0
right=0


	



def read_all():

	front=ping.distance_Ff()
	rear=ping.distance_Fb()
	left=ping.distance_Fl()
	right=ping.distance_Fr()
	return front,left,right,rear

	print(front,left,right,rear)
	