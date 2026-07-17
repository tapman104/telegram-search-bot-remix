import asyncio
import logging
import logging.config

# Initialize an event loop before importing Pyrogram to prevent RuntimeError on Python 3.11+
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from utils import Media
from info import SESSION, API_ID, API_HASH, BOT_TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        self.username = '@' + me.username
        print(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")

async def main():
    app = Bot()
    await app.start()
    try:
        await asyncio.Event().wait()
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
