import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

import asyncio

# Initialize an event loop before importing Pyrogram to prevent RuntimeError on Python 3.11+
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client
from info import API_ID, API_HASH


async def main():
    """Generate session string for user bot"""

    phone_number = input('Enter phone number with country code prefix: ')

    user_bot = Client(
        name='User-bot',
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=phone_number,
        in_memory=True
    )

    async with user_bot:
        session_string = await user_bot.export_session_string()
        print(f"Following is your session string -\n\n{session_string}")


if __name__ == "__main__":
    asyncio.run(main())
