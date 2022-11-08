#!/usr/bin/env python3

print("test")



from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE
#

pipe = Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)    

while True:         
    line = pipe.stdout.readline()
    if line:            
        print line
    if not line:
        break

#Popen('cmd', shell=False, creationflags=CREATE_NEW_CONSOLE)
print("test")

#
#input('Enter to exit from Python script...')

#process = subprocess.Popen(cmd, shell=True, text=True, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
#process.wait()
#stderr = process.stderr.read()
#print(stderr, end="")
input('Enter to exit from Python script...')

