import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("Internal"):
   load_dotenv("Internal")

load_dotenv()
admins = {}
API_ID = int(getenv("API_ID", "11799230"))
API_HASH = getenv("API_HASH", "7fa6c371601a46e953b8075e277f531f")
STRING_SESSION = getenv("STRING_SESSION", "")
BOT_NAME = getenv("BOT_NAME", "Royal")
BOT_USERNAME = getenv("BOT_USERNAME", "Royalfeelings12bot")
BOT_TOKEN = getenv("BOT_TOKEN", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "royalkifeelings")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "royalkifeelings12")
OWNER_NAME = getenv("OWNER_NAME", "royal_boy_amit")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
