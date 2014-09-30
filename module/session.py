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
		
# Somewhere we must take care of the list and the htag features 
	
class Session(threading.Thread):

	#todo
	def __init__(self,timeRefresh=10,timeout=10):
		threading.Thread.__init__(self)	
		self.timeRefresh = timeRefresh
		self.timeout = timeout
	
	#todo
	def sessionOn(self):
		pass
	
	#todo
	def sessionOff(self):
		pass
		
	#todo
	def clearSession(self):
		pass
	
	#todo
	def saveSession(self,path):
		pass
		
	#todo	
	def restoreSession(self,path):
		pass
		





