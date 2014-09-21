#!/usr/bin/env python

from subprocess import call
from time import sleep

while (1):

	call(["./HMC5883"])
	sleep(0.5)