import os
import platform
import sys

print()
print("Released into Public Domain. No rights reserved. ")
print("General purpose bot written in Python for Discord. ")
print()
print("0. Welcome to the Bot.py Discord Bot")
current_script_directory = os.path.dirname(os.path.abspath(__file__))

print("1. Getting Discord Bot Token")
try:
    with open(current_script_directory + '/data/discord_bot_token.txt', 'r') as file:
        TOKEN = file.read()
except FileNotFoundError:
    print("   Please insert Bot Token.")
    TOKEN = input("Bot Token: ")
    with open(current_script_directory + '/data/discord_bot_token.txt', 'w') as file:
        file.write(TOKEN)
        
print("2. Overseeing platform specific tweaks")
if platform.system() == 'Windows':
    print("  Applying tweak for Windows Operating System.")
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if platform.system() == 'Linux':    
    print("Checking if bot process is already running.")
    if os.path.exists('./data/pid.txt'):
        print("Previous bot PID was found.")
        with open('./data/pid.txt', 'r') as file:
            pid = file.read().strip()
        print("Previous PID: " + pid )
        print("Previous PID running?:" + str(os.path.isdir('/proc/' + pid)))
        if os.path.isdir('/proc/' + pid):
            print("Bot process is already running.")
            print("Please shut it down before running a new one.")
            sys.exit(0)

    
from discord.ext.commands import *
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = Bot(command_prefix='$', intents=intents)


# https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    
    # Show Bot Presence status.
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="you."))
    
    if platform.system() == 'Linux':
        print("Starting a new background process")
        if os.path.exists('./data/pid.txt'):
            print("Previous bot PID was found.")
            with open('./data/pid.txt', 'r') as file:
                pid = file.read().strip()
            print("Previous PID: " + pid )
            print("Previous PID running?:" + str(os.path.isdir('/proc/' + pid)))
            if not os.path.isdir('/proc/' + pid):
                print("Starting the bot as a background process.")
                os.system('nohup python3 ./bot.py > bot.log 2>&1 & echo $! > ./data/pid.txt &')
                os._exit(0)

           # if not os.path.isdir('/proc/{}'.format(pid)):
           
           #     pass
               # 
        #else:
        #    #os.system('nohup python3 ./bot.py > bot.log 2>&1 & echo $! > ./data/pid.txt &')
        #    
        #    with open('./data/pid.txt', 'r') as file:
        #        pid = file.read()
        #    await bot.close()
        
        








try:
    print("3. Starting to run the Bot.py")
    
    bot.run(TOKEN)
        

    print("4. End of Successful Run of the bot.")
    # Linux:
    # Check if pid is not running
    # Remove the pid as it is not running anymore.
    # os.remove(current_script_directory + '/data/linux_discord_bot_pid.txt')
    
except discord.errors.LoginFailure:
    print("The wrong credentials are passed.")
    print("Probably incorect Bot Token.")
    os.remove(current_script_directory + '/data/discord_bot_token.txt')