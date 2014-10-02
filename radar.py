#!/usr/bin/env python

import os
import glob
import sys
import ranger
from scipy import *
import io

__author__ = "David Cotterill-Drew"
__copyright__ = "Copyright 2014, RoboTonics"
__credits__ = ["David Cotterill-Drew"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "roboshopz@gmail.com"

def search (void):

	while(1):
		ranger.scan(1)
		
