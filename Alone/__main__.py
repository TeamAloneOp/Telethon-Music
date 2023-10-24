import asyncio
import telethon
import glob
from pathlib import Path
from Alone.utils import load_plugins
import logging
from Alone import Alone
from Alone import client, ASSISTANT_ID
from Alone.plugins.autoleave import leave_from_inactive_call


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Alone/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
async def start_bot():
     print("[INFO]: LOADING ASSISTANT DETAILS")
     botme = await client.get_me()
     botid = telethon.utils.get_peer_id(botme)
     print(f"[INFO]: ASSISTANT ID {botid}")
     await asyncio.create_task(leave_from_inactive_call())


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

print("[INFO]: SUCCESSFULLY STARTED BOT!")
print("[INFO]: VISIT @AloneXBots")

if __name__ == "__main__":
    Alone.run_until_disconnected()
