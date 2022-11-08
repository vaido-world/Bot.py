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
    
if sys.platform == "linux":
    if os.path.isfile("./data/pid"):
        with open('./data/pid', 'r') as file:
            oldpid = file.read()
        os.system('kill -9 ' + str(oldpid))
        
    pid = os.system('nohup python3 ./bot.py > bot.log 2>&1 &')
    with open('./data/pid', 'w') as file:
        file.write(str(pid))