#!/usr/bin/env python
# -*- coding: utf-8 -*

import botLib
import parser
import time
import sys

pyVersion = botLib.getPythonVersion()
if pyVersion == 2:
	import threading as threading
elif pyVersion == 3: 
	import threading
else :
	print("Python version not supported")
	sys.exit(0)
	
class Session(threading.Thread):

	#todo
	def __init__(self,timeRefresh=10,timeout=10):
		threading.Thread.__init__(self)	
		self.timeRefresh = timeRefresh
		self.timeout = timeout
	
	#todo
	def connect(self,username,password):
	
	
	#todo
	def deconnect(self):
	
	
	
	








