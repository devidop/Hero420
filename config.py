import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
API_ID = int(getenv("API_ID", "11799230"))
API_HASH = getenv("API_HASH", "7fa6c371601a46e953b8075e277f531f")
STRING_SESSION = getenv("STRING_SESSION", "BQA1iQxmHGB5ae0FepSwehhKD3Va_-F3G7iJhrw7-9MuV9LB9YsXBKSM1GbYbBVbFUH4Qle4s3x5A3IZVQjcOnTvWks_abwoKVfDZBpk5_Honoj-gxO3dj5EXws8uhj4K_L4qmZis2A-olLU_iw3ZAvcqrsh-iG_Qz00IytrxyQrUbP59Z9bM8epTytBHx-5DVajsCcuZ89m93Sy1twLIMgj-JjY4aWcNkWLS_vumPhP6K6CbejVyGEWmEzBusMel2QjArdQZVrixUFAbFldQYQKCZg9CIdQJgg_AVw0-yVpJk8pWz4FIfLodMcBavUePawXgQVJcMljuhjtZGLrX4MtAAAAATK-Xu0A")
BOT_NAME = getenv("BOT_NAME", "RoyalMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "Royalfeelings12bot")
BOT_TOKEN = getenv("BOT_TOKEN", "5457990326:AAG1ftbRI33rpShI3PH7ozLkX7Dz_5CzeOo")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "140"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5146304237 5557851887").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "royalkifeelings")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "royalkifeelings12")
OWNER_NAME = getenv("OWNER_NAME", "royal_boy_amit")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
