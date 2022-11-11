import tools.windows_tweak
from discord.ext.commands import *


def main():

    import discord

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = Bot(command_prefix='$', intents=intents)
    try:
        bot.run(token="MTAzNDg0Mjk1NzQxMDQ4ND78M0NQ.GjjeVF.7SDjDt35dkcowQn7865dxQQXYgSOlQqnbZONOH12w0")
    except discord.errors.LoginFailure:
       print("The wrong credentials are passed.")
       pass




def handle_keyboard_interrupt():
    def signal_handler(signal, frame):
        import os
        os._exit(2)
        
    import signal
    signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    #handle_keyboard_interrupt()
    main()