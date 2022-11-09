# Set the policy to prevent "Event loop is closed" error on Windows
# https://github.com/Rapptz/discord.py/issues/5209
import platform
import asyncio
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



# # Each function is a walkaround for "Event loop is Closed" Error.
# def set_event_loop_policy():
#     # Set the policy to prevent "Event loop is closed" error on Windows
#     # https://github.com/Rapptz/discord.py/issues/5209
#     import platform
#     import asyncio
#     if platform.system() == 'Windows':
#         asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())