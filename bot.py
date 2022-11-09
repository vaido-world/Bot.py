# pip install -U discord.py
# https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py

import os
import discord
from discord.ext import commands

print("Welcome to bot.py Discord Bot")

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

def check_bot_token():
    if not os.getenv('DISCORD_TOKEN'):
        TOKEN = input("Please Insert Discord Developer Bot Token: ")
        os.environ["DISCORD_TOKEN"] = TOKEN
        
    if not os.getenv('DISCORD_TOKEN'):
        import subprocess
        if os.name == 'posix':  # if is in linux
            exp = 'export DISCORD_TOKEN=' + '\"' + TOKEN + '\"'
        if os.name == 'nt':  # if is in windows
            exp = 'setx DISCORD_TOKEN' + " " + '\"' + TOKEN + '\"'
        subprocess.Popen(exp, shell=True).wait()
        print("Bot Token saved as System Environment Variable.")
        
    if os.getenv('DISCORD_TOKEN'):
        print("Found Bot Token stored in the user wide Environment Variable.")
        
        

def main():
    check_bot_token()
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix='?', description=description, intents=intents)
    bot.run(os.getenv('DISCORD_TOKEN'))
    import sys
    if sys.platform == "linux":
        print("Check if token is valid then fork the process,get the pid and exit ")
        #if pid = os.fork():
        #    sys.exit()
if __name__ == "__main__":
    main()

#input('Press <ENTER> to continue')