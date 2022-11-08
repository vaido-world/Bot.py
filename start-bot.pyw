#!/usr/bin/env python3
#print("test")

#subprocess.run('cmd', shell=False, stdout=PIPE, creationflags=CREATE_NEW_CONSOLE).stdout.write("asd")




#import sys
#sys.stdout = open('stdout.txt', 'w')

import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE
#Popen('cmd', shell=False, creationflags=CREATE_NEW_CONSOLE) 
print("test1")


print("test2")


# cmd=['cmd']  
# 
# command_process = subprocess.Popen(
# cmd,
# shell='/bin/bash',
# stdin=subprocess.PIPE,
# stdout=subprocess.PIPE,
# stderr=subprocess.STDOUT,
# universal_newlines=True
# )
# 
# command_output = command_process.communicate()[0]
# 



#p = subprocess.Popen("cmd.exe", shell=True)
#os.waitpid(p.pid, 0)


#import os
#os.system('python ./bot.py')
input('Enter to exit from Python script...')

#print("test2")


# start the script directly with python ./bot.py
# redirect output to the newly ran cmd 
# cmd python ./bot.py
subprocess.run('python ./bot.py', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NEW_CONSOLE)

# Spawn a new command line window | or merge into current one
# Redirect stdout to the new command line
# Run python . bot.py in it.