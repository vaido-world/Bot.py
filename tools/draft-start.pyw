#print("test")

#subprocess.run('cmd', shell=False, stdout=PIPE, creationflags=CREATE_NEW_CONSOLE).stdout.write("asd")

import sys

### Good debug
#import sys
#sys.stdout=open("test.txt","w")
#sys.stderr=open("test2.txt","w")


#sys.stdout = sys.stderr


import time



#import sys
#sys.stdout = open('stdout.txt', 'w')

import subprocess
from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE, STDOUT 

process = subprocess.Popen('cmd.exe /k ', shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
process.stdin.write("dir\n")
o,e=process.communicate()
print o
process.stdin.close()

for line in p.stdout:
    print("O=:", line)


#time.sleep(2.5)
#Popen('cmd', shell=False, stdout=PIPE, stderr=STDOUT, stdin=PIPE, creationflags=CREATE_NEW_CONSOLE) 
#time.sleep(2.5)
#input('Enter to exit from Python script...')
# python start-bot.pyw 
#tests = input('Enter to exit from Python script...')

print("test1")

print("test2")
#Popen('cmd', shell=False, creationflags=CREATE_NEW_CONSOLE) 


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




#print("test2")


# start the script directly with python ./bot.py
# redirect output to the newly ran cmd 
# cmd python ./bot.py
#subprocess.Popen('cmd', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NEW_CONSOLE)

# Spawn a new command line window | or merge into current one
# Redirect stdout to the new command line
# Run python . bot.py in it.
# Spawn command prompt only if it does not exist


# python start-bot.pyw launches the script not as pyw, but as .py