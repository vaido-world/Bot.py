
#import tools.store_bot_token # Get bot token
#TOKEN = tools.store_bot_token.TOKEN

import os
user_directory = os.path.expanduser("~")
with open(user_directory + '/discord-bot-token.txt', 'r') as file:
    TOKEN = file.read()



import os
user_directory = os.path.expanduser("~")

print("3.Checking if bot token is valid.")
import discord
import platform
if platform.system() == 'Windows':
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
try:
    
    client = discord.Client(intents=discord.Intents.all())
    
    @client.event
    async def on_ready():
        await client.close()
        await client.session.close()
        exit(0)
        #await asyncio.get_event_loop().run(on_ready())
    client.run(TOKEN)
    print("Successful authentication")
    

except discord.errors.LoginFailure:
   print("The wrong credentials are passed.")
   os.remove(user_directory + '/discord-bot-token.txt')
   sys.exit()
   pass
   

#import time
#time.sleep(10)

from discord.ext.commands import *
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = Bot(command_prefix='$', intents=intents)


@bot.event
async def on_message(message):
    if message.author.bot: #if message's author is a bot, then ignore it.
        return


bot.run(TOKEN)