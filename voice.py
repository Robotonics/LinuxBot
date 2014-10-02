#!/usr/bin/env python

import os
import sys


import subprocess

def say_name(void):

	text1 = '"My Name is LinuxBot."'
	subprocess.call('espeak '+text1, shell=True)
	return text1

def say_hello(void):

	text2 = '"Hello."'
	subprocess.call('espeak '+text2, shell=True)
	return text2

def say_goodbye(void):

	text3 = '"Good Bye!'
	subprocess.call('espeak '+text3, shell=True)
	return text3

def ask_name(void):

	text4 = '"What is your name?"'
	subprocess.call('espeak '+text4, shell=True)
	return text4
