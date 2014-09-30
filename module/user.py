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


class User:		
	
	#todo
	def connect(self,username,password):
		pass
	
	#todo
	def deconnect(self):
		pass
	
	#todo
	def getFollowers(self):
		pass
	
	#todo
	def getFollowing(self):
		pass
	
	#todo
	def addFollowing(self,following):
		pass
	
	#todo
	def delFollowing(self,following):
		pass
	
	#todo
	# Location, birth, little description ...
	def getInfoAcount(self):
		pass
	

