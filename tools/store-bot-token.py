import os
user_directory = os.path.expanduser("~")

print("1.First time setup")
print("2.Checking if bot token already inserted.")
if os.path.exists(user_directory + '/discord-bot-token.txt'):
    print(" |Discord Bot Token already inserted.")
    print(" |" + user_directory + '/discord-bot-token.txt')
    with open(user_directory + '/discord-bot-token.txt', 'r') as file:
        TOKEN = file.read()
    print(" |Token found:" + "|" + TOKEN + "|")
    
if not os.path.exists(user_directory + '/discord-bot-token.txt'):
    TOKEN = input(" Please Insert Discord Developer Bot Token: ")
    with open(user_directory + '/discord-bot-token.txt', 'w') as file:
        file.write(TOKEN)
    
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
    client.run(TOKEN)
    print("Successful authentication")
    
    with open(user_directory + '/discord-bot-token.txt', 'w') as file:
        file.write(TOKEN)
except discord.errors.LoginFailure:
   print("The wrong credentials are passed.")
   os.remove(user_directory + '/discord-bot-token.txt')
   pass
   
   


print("finished")