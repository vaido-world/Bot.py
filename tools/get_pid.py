import os
print(os.system('nohup python3 ./bot.py > bot.log 2>&1 & echo $! &'))