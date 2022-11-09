from discord.ext.commands import *


def main():
    try:
        import discord

        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        bot = Bot(command_prefix='$', intents=intents)

        bot.run(token="MTAzNDg0Mjk1NzQxMDQ4ND78M0NQ.GjjeVF.7SDjDt35dkcowQn7865dxQQXYgSOlQqnbZONOH12w0")

    except discord.errors.LoginFailure:
       import os
       print("The wrong credentials are passed.")
       os._exit(1)
       pass

# Each function is a walkaround for "Event loop is Closed" Error.
def set_event_loop_policy():
    # Set the policy to prevent "Event loop is closed" error on Windows
    # https://github.com/Rapptz/discord.py/issues/5209
    import platform
    import asyncio
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def handle_keyboard_interrupt():
    def signal_handler(signal, frame):
        import os
        os._exit(2)
        
    import signal
    signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    set_event_loop_policy()
    #handle_keyboard_interrupt()
    main()