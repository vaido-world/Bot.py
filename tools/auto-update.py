import os
current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory + "/../")

os.system("git remote update")

import subprocess
output = subprocess.check_output("git status", shell=True)
print(output)

if "Your branch is behind" in str(output):
    print("Found the sentence in the output")
    os.system("git reset --hard HEAD")
    os.system("git pull")