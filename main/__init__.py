#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables (filled directly instead of config())
API_ID = 15663518
API_HASH = "d675b3e5ad6fcf248d6ddafc8c07c53b"
BOT_TOKEN = "8163129853:AAG3RimnlpjWdD9FHdXEM_gk_sL3T51rvrc"
SESSION = "BQDvAZ4AUPk2WgGR9V-R7k00wqR2d_4FKV3HCaZM_ZLF9OhfB0KM4KrKfWsDTtU4VDAiCfOobY5-8qLiuXYBIM1AV2C7SetUg4kImLOfzYkboxAWToS41hLSmrSzJhKAxf3jSIPx4WIZqFWabknxTV8gNelVjIeMlok_VyKf3X8AM5GkmiGDJGdH6ZbXSR5dVr9cZmv1utCyxjDm7Nuu21W21IbSK0eMSxgp0owkhSFSWbjN6CWBAoQiiaDuGapaWLMsKpuute4y3KlvUtxBbaMtn2mEKRHJjH0s2q-vL8JqtagT1h4CTsYPHTqVt3C5jyYDd1G4bchEXh_dfk8M_Yw90whECgAAAAGqNXUWAA"
FORCESUB = "srcbopbothain"
AUTH = 7150597398

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
