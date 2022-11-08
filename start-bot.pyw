#!/usr/bin/env python3

# .pyw is a Windows-only thing, used to indicate that a script needs to be run using PYTHONW.EXE 
# instead of PYTHON.EXE in order to prevent a DOS console from popping up to display the output. 
# https://docs.python.org/3/whatsnew/2.2.html

import datetime
with open('./data/start-bot.log', 'a') as logfile:
    logfile.write(str(datetime.datetime.now()) + "\n")

import sys
sys.stdout=open("./data/start-bot.log","a")
sys.stderr=open("./data/start-bot.log","a")

import os
if sys.platform == "win32":
    os.system('python ./bot.py && pause')

