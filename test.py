#!/usr/bin/env python
# -*- coding: utf-8 -*
import session
import config



user1 = session.Session()
user1.connect(config.username,config.password)





user1.deconnect()









